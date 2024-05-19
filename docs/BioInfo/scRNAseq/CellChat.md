## 1.CellChat对象的数据输入、处理及初始化

CellChat 要求将细胞的基因表达数据作为输入，并通过将基因表达与信号配体、受体与其同因子之间的相互作用的先验知识相结合来对细胞-细胞通信的概率进行模拟。在推断细胞间通信网络后，CellChat 为进一步的数据探索、分析和可视化提供了功能。

### **(1) 加载数据**

CellChat 需要两个输入：一个是细胞的基因表达数据，另一个是用户分配的细胞标签（即基于标签的模式）或单细胞数据的低维表示（即无标签模式）。对于后者，CellChat 通过根据低维空间或伪时间轨迹空间中的细胞距离构建共享的邻近图自动对细胞进行分组。

**对于基因表达数据矩阵**，要求基因为行名，细胞为列名。需要将标准化数据作为 CellChat 分析的输入。如果用户提供count数据，我们提供一个函数normalizeData来计算文库大小，然后进行log转换。**对于分组信息**，需要使用带有行名的数据作为CellChat 的输入:

```R
library(Seurat)
library(CellChat) 
load("GSE130001/sce_opt_anno_GSE130001.Rdata")
exp  <- as.data.frame( sce2@assays$RNA@data)
dim(exp)
exp = normalizeData(exp)
head(exp)[,1:4]

meta1 = sce2@meta.data
meta2 =  data.frame(Cell = rownames(sce2@meta.data), 
                    cell_type = sce2@active.ident ) 

table(meta2$cell_type)
```

### (2) 创建CellChat 对象

```R
cellchat <- createCellChat(object = exp, meta = meta2, group.by = "cell_type")
```

**可以从数据矩阵、Seurat 或 SingleCellExperiment**对象创建新的 CellChat 对象。如果输入是**Seurat 或 SingleCellExperiment**对象，则默认情况下将使用对象中的meta data，用户必须提供该数据来定义细胞分组。例如，group.by=Seurat 对象中默认的细胞标识。

如果在创建cellchat对象时未添加细胞meta信息，用户也可以稍后添加该信息，并使用setIdent设置该对象默认的细胞标识。

```R
cellchat <- addMeta(cellchat, meta = meta2)
cellchat <- setIdent(cellchat, ident.use = "cell_type") # set "cell_type" as default cell identity
levels(cellchat@idents) # show factor levels of the cell_type
```

```R
# number of cells in each cell group
groupSize <- as.numeric(table(cellchat@idents)) 
```

### (3) 设置受体配体数据库

 CellChatDB数据库是一个手动整理的文献支持的配体受体在人和小鼠中的交互数据库。小鼠中的CellChatDB包含2021个经验证的分子相互作用，包括60%的自分泌/旁分泌信号相互作用、21%的细胞外基质（ECM）受体相互作用和19%的细胞-细胞接触相互作用。人的CellChatDB包含1，939个经验证的分子相互作用，包括61.8%的自分泌/旁分泌信号相互作用、21.7%的细胞外基质（ECM）受体相互作用和16.5%的细胞-细胞接触相互作用。

```R
CellChatDB <- CellChatDB.human # use CellChatDB.mouse if running on mouse data
showDatabaseCategory(CellChatDB)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303130956549.png)

```R
CellChatDB_mouse <- CellChatDB.mouse 
showDatabaseCategory(CellChatDB_mouse)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303130958563.png)

```R
dplyr::glimpse(CellChatDB$interaction)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303130959302.png)

通过包含感兴趣的交互来子集CellChatDB数据库。

```R
CellChatDB.use <- subsetDB(CellChatDB, search = "Secreted Signaling") # use Secreted Signaling
# use all CellChatDB for cell-cell communication analysis
# CellChatDB.use <- CellChatDB # simply use the default CellChatDB

# set the used database in the object
cellchat@DB <- CellChatDB.use
```

### (4) 预处理用于细胞通信分析的表达数据

为了推断细胞状态特异的通信，我们识别一个细胞组中过度表达的配体或受体，然后识别过度表达的配体受体相互作用，是否过表达。我们还提供将基因表达数据投影到蛋白质-蛋白质相互作用 （PPI） 网络上的功能。具体来说，投影过程根据高度可信的实验验证的蛋白质-蛋白质网络中定义的基因表达值来平滑基因的表达值。此功能在分析具有浅测序深度的单细胞数据时很有用，因为投影可减少信号基因的dropput效应，特别是对于配体/受体的可能的零表达。人们可能担心这种投影过程可能引入的人为因素，但是，这几乎可以忽略不计。用户还可以通过在函数computeCommunProb()中设置raw.use = TRUE跳过此步骤。

```R
# subset the expression data of signaling genes for saving computation cost
cellchat <- subsetData(cellchat) 
# future::plan("multiprocess", workers = 4) # do parallel
cellchat <- identifyOverExpressedGenes(cellchat)
cellchat <- identifyOverExpressedInteractions(cellchat)
cellchat <- projectData(cellchat, PPI.human)
```

## 2. 细胞通信网络的推断

CellChat 通过分配具有概率值的每个相互作用并进行排列检验，来推断具有生物学意义的细胞-细胞通信。CellChat通过将基因表达与先前已知的信号配体、受体及其同因子之间的相互作用知识相结合，利用大量作用规律，对细胞-细胞通信的概率进行模拟。

推断的配体受体对的数量显然取决于**计算每个细胞组平均基因表达的方法**。默认情况下，CellChat 使用一种统计学上强大的均值方法，称为"trimean"，与其他方法相比，它产生的相互作用更少。然而，我们发现 CellChat 在预测更强的交互方面表现良好，这非常有助于缩小交互范围，以便进一步进行实验验证。在computeCommunProb中，我们提供了一个选项，用于使用其他方法，如5%和10%截断均值，来计算平均基因表达。值得注意的是，"trimean"大约是25%的截断平均值，这意味着如果一组表达细胞的百分比低于25%，则平均基因表达为零。要使用 10% 截断的平均值，用户可以设置`type = "truncatedMean"`和对`trim = 0.1`。

在分析未分类的单细胞转录组时，假设丰富的细胞群倾向于发送比稀有细胞群更强的信号，CellChat 还可以在概率计算中考虑每个细胞组中细胞比例的影响。用户可以设置`population.size = TRUE`。

### (1)计算通信概率并推断cellchat网络

```R
cellchat <- computeCommunProb(cellchat, raw.use = TRUE)
# 如果某些细胞组中只有少数细胞，则过滤掉细胞间通信
cellchat <- filterCommunication(cellchat, min.cells = 10)
```

### (2) 提取推断的cellchat网络作为数据框架

提供一个函数`subsetCommunication`，以轻松访问推断感兴趣的细胞-细胞通信。例如:

- xxxxxxxxxx # T Cells (CD3D, CD3E, CD8A), # B cells (CD19, CD79A, MS4A1 [CD20]), # Plasma cells (IGHG1, MZB1, SDC1, CD79A), # Monocytes and macrophages (CD68, CD163, CD14),# NK Cells (FGFBP2, FCG3RA, CX3CR1),  # Photoreceptor cells (RCVRN), # Fibroblasts (FGF7, MME), # Endothelial cells (PECAM1, VWF). # epi or tumor (EPCAM, KRT19, PROM1, ALDH1A1, CD24).#   immune (CD45+,PTPRC), epithelial/cancer (EpCAM+,EPCAM), # stromal (CD10+,MME,fibo or CD31+,PECAM1,endo) R
- `df.net <- subsetCommunication(cellchat, sources.use = c(1,2), targets.use = c(4,5))`将推断的细胞-细胞通信从细胞组1和2发送到细胞组4和5。
- `df.net <- subsetCommunication(cellchat, signaling = c("CXCL", "ANGPTL"))`通过向CXCL和ANGPTL发出信号来调节推断的细胞通信。

```R
df.net <- subsetCommunication(cellchat)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131536394.png)

```R
df.net <- subsetCommunication(cellchat)
df.net <- subsetCommunication(cellchat, 
                              sources.use = c(1,2), 
                              targets.use = c(4,5))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131637056.png)

```R
df.net <- subsetCommunication(cellchat, signaling = c("CXCL", "ANGPTL"))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131640515.png)

### (3) 在信号通路级别推断细胞-细胞通信

CellChat 通过总结与每个信号通路相关的所有配体-受体相互作用的通信概率，来计算信号通路级别上的通信概率。

NB：每个配体受体对和每个信号通路的推断细胞间通信网络分别存储在插槽"net"和"netP"中。

```R
cellchat <- computeCommunProbPathway(cellchat)
```

### (4) 计算整合的细胞通信网络

我们可以通过计算链接数或汇总通信概率来计算整合的细胞通信网络。用户还可以通过设置sources.use和targets.use。

```R
cellchat <- aggregateNet(cellchat)
```

还可以可视化整合的细胞通信网络。例如，使用圆图显示任意两个细胞组之间的相互作用次数或总交互强度（比重）。

```R
netVisual_circle(cellchat@net$count, vertex.weight = groupSize, 
                 weight.scale = T, label.edge= F, 
                 title.name = "Number of interactions")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131651117.png)

```R
netVisual_circle(cellchat@net$weight, 
                 vertex.weight = groupSize, 
                 weight.scale = T, label.edge= F, 
                 title.name = "Interaction weights/strength")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131650588.png)

由于细胞通信网络复杂，可以检查每个细胞组发送的信号。通过控制参数`edge.weight.max`，以便可以比较不同网络之间的边缘权重。

```R
mat <- cellchat@net$weight
par(mfrow = c(3,2), xpd=TRUE)
rm(i)
for (i in 1:nrow(mat)) {
  mat2 <- matrix(0, nrow = nrow(mat), ncol = ncol(mat), dimnames = dimnames(mat))
  mat2[i, ] <- mat[i, ]
  netVisual_circle(mat2, vertex.weight = groupSize, 
                   weight.scale = T, edge.weight.max = max(mat), 
                   title.name = rownames(mat)[i])
}

```

## 3. 细胞通信网络的可视化

在推断细胞通信网络后，CellChat 为进一步的数据探索、分析和可视化提供了各种功能。

它提供了几种可视化细胞通信网络的方法，包括分层图、圆图、和弦图和气泡图。
它提供了一个易于使用的工具，用于提取和可视化推断网络的高阶信息。例如，它允许对细胞群的主要信号输入和输出以及这些群和信号如何协调功能进行现成预测。
它可以通过结合通讯网络分析、模式识别和多重学习方法，使用综合方法对推断出的细胞-细胞通信网络进行定量表征和比较。

### (1) 使用层次结构图、圆图或和弦图可视化每个信号通路

**层次结构图：**用户应定义vertex.receiver，这是一个数字矢量，将细胞群的索引作为层次图左侧的目标。此分层图由两个部分组成：左部分显示自分泌和旁分泌向某些感兴趣的细胞组（即定义的）发出信号，右部分显示自分泌和旁分泌向数据集中剩余的细胞组发出信号。因此，层级图提供了一种信息性和直观的方式来可视化自分泌和旁分泌信号之间的细胞群之间的感兴趣通信。例如，在研究成纤维细胞和免疫细胞之间的细胞-细胞通信时，用户可以定义为所有成纤维细胞组。

**和弦图：**CellChat 提供两种功能netVisual_chord_cell和netVisual_chord_gene，并可视化具有不同目的和不同级别的细胞通信。netVisual_chord_cell用于可视化不同细胞群之间的细胞-细胞通信（和弦图中的每个部分是细胞组），netVisual_chord_gene用于可视化由多个配体受体或信号通路调节的细胞-细胞通信（和弦图中的每个部分都是配体、受体或信号通路）。

边缘颜色/权重、节点颜色/大小/形状的解释：在所有可视化图中，边缘颜色与发送者源一致，边缘权重与交互强度成正比。较厚的边缘线表示信号更强。在层次结构图和圆图中，圆的大小与每个细胞组中的细胞数量成正比。在层次图中，实心和开放的圆分别代表源和目标。在和弦图中，内条颜色表示从相应的外条接收信号的目标。内条大小与目标接收的信号强度成正比。这种内条有助于解释复杂的和弦图。请注意，有一些内条没有与任何一些细胞组链接，请忽略它，因为这是一个本包尚未解决的问题。

不同层次的细胞通信可视化：可以使用netVisual_aggregate可视化信号通路的推断通信网络，并使用netVisual_individual可视化与该信号通路相关的单个L-R对的推断通信网络。

在这里，我们以输入一个信号通路为例。所有显示重要通信的信号通路均可通过cellchat@netP$pathways获取。

```R
pathways.show <- c("ANGPTL") 
# Hierarchy plot
# Here we define `vertex.receive` so that the left portion of the hierarchy plot shows signaling to fibroblast and the right portion shows signaling to immune cells 
vertex.receiver = seq(1,5) # a numeric vector. 
netVisual_aggregate(cellchat, signaling = pathways.show,
                    vertex.receiver = vertex.receiver)

par(mfrow=c(1,1))
netVisual_aggregate(cellchat, 
                    signaling = pathways.show, layout = "circle")

netVisual_aggregate(cellchat, signaling = pathways.show, layout = "chord")
netVisual_heatmap(cellchat, signaling = pathways.show, color.heatmap = "Reds")
```



对于和弦图，CellChat 具有独立函数netVisual_chord_cell，通过调整circlize包中的不同参数来灵活可视化信号网络。例如，我们可以定义一个group命名的字符矢量，以创建多组和弦图，将细胞群集分组到不同的细胞类型。

```R
group.cellType <- c("Epithelial_cells","Chondrocytes", "Endothelial_cells",
                    "Tissue_stem_cells","NK_cell") 
names(group.cellType) <- levels(cellchat@idents)
netVisual_chord_cell(cellchat, signaling = pathways.show,
                     group = group.cellType, 
                     title.name = paste0(pathways.show, " signaling network"))
```

计算每个配体受体对整体信号通路的贡献，并可视化由单个配体受体对调节的细胞通信。

```R
netAnalysis_contribution(cellchat, signaling = pathways.show)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131728194.png)

还可以可视化由单个配体受体对调节的细胞-细胞通信。提供一个函数extractEnrichedLR来提取给定信号通路的所有重要相互作用（L-R对）和相关信号基因。

```R
pairLR.ANGPTL <- extractEnrichedLR(cellchat, 
                                    signaling = pathways.show, 
                                    geneLR.return = FALSE)
LR.show <- pairLR.ANGPTL [1,] # show one ligand-receptor pair
# Hierarchy plot
vertex.receiver = seq(1,4) # a numeric vector
netVisual_individual(cellchat, 
                     signaling = pathways.show,  
                     pairLR.use = LR.show, vertex.receiver = vertex.receiver)
```

### (2) 自动保存所有推断网络的模块以进行快速探索

在实际使用中，用户可以使用‘for … loop’自动保存所有推断网络快速探索使用。netVisual，netVisual支持svg、png和pdf格式的输出。

```R
pathways.show.all <- cellchat@netP$pathways
# check the order of cell identity to set suitable vertex.receiver
levels(cellchat@idents)
vertex.receiver = seq(1,4)
for (i in 1:length(pathways.show.all)) {
  # Visualize communication network associated with both signaling pathway and individual L-R pairs
  netVisual(cellchat, signaling = pathways.show.all[i], 
            vertex.receiver = vertex.receiver, layout = "circle")
  # Compute and visualize the contribution of each ligand-receptor pair to the overall signaling pathway
  gg <- netAnalysis_contribution(cellchat, 
                                 signaling = pathways.show.all[i])
  ggsave(filename=paste0(pathways.show.all[i], "_L-R_contribution.pdf"), 
         plot=gg, width = 3, height = 2, units = 'in', dpi = 300)
}
```

### (3) 可视化由多个配体受体或信号通路调节的细胞通信

可以使用netVisual_bubble显示从某些细胞组到其他细胞组的所有重要相互作用（L-R对）。

```R
netVisual_bubble(cellchat, sources.use = 4, 
                 targets.use = c(1:5), 
                 remove.isolate = FALSE)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131937376.png)

类似于气泡图，cellchat提供了绘制和弦图的功能`netVisual_chord_gene`

- 显示从某些细胞组到其他细胞组的所有相互作用（L-R对或信号通路）。两个特殊情况：一个显示从一个细胞组发送的所有交互，另一个显示一个细胞组接收的所有交互。

- 显示用户输入的交互或用户定义的某些信号通路

  ```R
  netVisual_chord_gene(cellchat, sources.use = 4, 
                       targets.use = c(1:5), 
                       lab.cex = 0.5,legend.pos.y = 30)
  ```

  

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131942639.png)

```R
netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), 
                     targets.use = 2, legend.pos.x = 15)
```

![image-20230313194502451](C:/Users/chens/AppData/Roaming/Typora/typora-user-images/image-20230313194502451.png)

```R
netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), targets.use = c(5:11), 
                     signaling = c("CCL","CXCL"),legend.pos.x = 8)
```

```R
netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), targets.use = c(5:11), slot.name = "netP", legend.pos.x = 10)
```

```R
netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), 
                     targets.use = c(1:5), 
                     small.gap =3,
                     slot.name = "netP", legend.pos.x = 1)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131952172.png)

NB：在生成图时，请忽略注释，例如 “Note: The first link end is drawn out of sector ‘MIF’。如果基因名称重叠，您可以通过调整small.gap值来调整参数。

### **(4) 使用小提琴/点图绘制信号基因表达分布**

可以利用Seurat 包装的函数plotGeneExpression绘制与L-R对或信号通路相关的信号基因的基因表达分布图。

```R
plotGeneExpression(cellchat, signaling = "ANGPTL")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303131955452.png)

默认情况下，用户可以通过`plotGeneExpression`只显示与推断的重要通信相关的信号基因的表达。

```R
plotGeneExpression(cellchat, signaling = "ANGPTL", 
                   enriched.only = FALSE)
```

或者，可以使用extractEnrichedLR提取与推断的L-R对或信号通路相关的信号基因，然后使用Seurat包绘制基因表达图。

## 4. 细胞通信网络系统分析

为了便于对复杂的细胞间通信网络进行解释，CellChat 通过从图形理论、模式识别和多重学习中抽象的方法对网络进行量化。

- 它可以使用网络分析的集中度措施确定给定信号网络中的主要信号源和目标以及调节者和影响者
- 它可以通过利用模式识别方法预测特定细胞类型的关键传入和传出信号，以及不同细胞类型之间的协调响应。
- 它可以通过定义相似度测量方法和从功能和拓扑角度进行多重学习来分组信号通路。
- 它可以通过对多个网络的联合多重学习来描绘保存上下文特定的信号通路。

### (1) 识别细胞组的信号角色（例如，占主导地位的发送器、接收器）以及主要贡献信号

CellChat 允许通过计算每个细胞组的多个网络中心测量，随时识别细胞间通信网络中**占主导地位的发送者、接收者、调解者和影响者**。具体来说，我们在加权导向网络中采用了措施，包括**度外、度内、介于两者之间流动和信息集中度**，分别识别细胞间通信的主要发送者、接收者、调解者和影响者。在以权重为计算通信概率的加权定向网络中，将外向度计算为来自细胞组的传出信号的通信概率之和，并计算为传入信号对单元组通信概率的总和的度内，可用于分别识别信号网络的主要单元件发送器和接收器。有关信息中心之间流动的定义。

#### 计算和可视化网络中心分数

```R
# Compute the network centrality scores
cellchat <- netAnalysis_computeCentrality(cellchat, slot.name = "netP") # the slot 'netP' means the inferred intercellular communication network of signaling pathways
# Visualize the computed centrality scores using heatmap, allowing ready identification of major signaling roles of cell groups
netAnalysis_signalingRole_network(cellchat, signaling = pathways.show, width = 8, height = 2.5, font.size = 10)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132002955.png)

#### 在 2D 空间中可视化占主导地位的发送器（源）和接收器（目标）

我们还提供了另一种直观方法，使用散点图在 2D 空间中可视化占主导地位的发射器（源）和接收器（目标）。

```R
gg1 <- netAnalysis_signalingRole_scatter(cellchat)
#> Signaling role analysis on the aggregated cell-cell communication network from all signaling pathways
# Signaling role analysis on the cell-cell communication networks of interest
gg2 <- netAnalysis_signalingRole_scatter(cellchat, signaling = c("CXCL", "ANGPTL"))
#> Signaling role analysis on the cell-cell communication network from user's input
gg1 + gg2
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132005099.png)

#### 识别对某些细胞组的传出或传入信号贡献最大的信号

我们还可以回答以下问题：哪些信号对某些细胞组的传出或传入信号贡献最大。

```R
ht1 <- netAnalysis_signalingRole_heatmap(cellchat, pattern = "outgoing")
ht2 <- netAnalysis_signalingRole_heatmap(cellchat, pattern = "incoming")
ht1 + ht2
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132008388.png)

#### 确定全局通信模式，探索多个细胞类型和信号通路如何协调在一起

除了探索单个通路的详细通信外，一个重要问题是多个细胞组和信号通路如何协调功能。CellChat 采用模式识别方法识别全局通信模式。随着模式数量的增加，可能会有多余的模式，因此很难解释通信模式。我们选择了五种模式作为默认模式。一般来说，它具有生物学意义，模式数量要大于2。此外，我们还提供了一个函数selectK来推断模式的数量，该数基于 NMF R 包中已实施的两个指标Cophenetic和Silhouette。这两个指标都根据共识矩阵的分层聚类来衡量特定数量模式的稳定性。对于一系列模式，适当的模式数量是Cophenetic 和 Silhouette值开始突然下降的模式。

**识别和可视化分泌细胞的传出通信模式**

传出模式揭示了发送者细胞（即作为信号源的细胞）如何相互协调，以及它们如何与某些信号通路协调以驱动通信。

为了直观地显示潜在模式与细胞群和配体受体对或信号通路的关联，我们使用了河流（冲积）图。我们首先将每行 W 和 H 的每列标准化为 [0，1]，然后在 W 和 H 中设置为零，如果它们小于 0.5。这种阈值允许发现与每个推断模式相关的最丰富的细胞组和信号通路，即每个细胞组或信号通路仅与一个推断模式相关联。这些阈值矩阵 W 和 H 用作创建冲积图的输入。

为了将细胞群与其丰富的信号通路直接联系起来，如果 W 和 H 中的元素少于  1/R（R 是潜在模式数），则我们将它们中的元素设置为零。通过使用不太严格的阈值，可以获得与每个细胞组相关的更丰富的信号通路。我们使用每个细胞组对通过乘以 W 乘以 H 计算的每个信号通路的贡献分数，构建了一个点图，其中点大小与贡献分数成正比，以显示细胞组与其丰富信号通路之间的关联。用户还可以降低参数cutoff，以显示每个细胞组关联的更丰富的信号通路。

通信模式分析所需的包

```R
library(NMF)
library(ggalluvial)
```

在这里，我们运行selectK推断模式的数量。

```R
selectK(cellchat, pattern = "outgoing")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132015469.png)

当传出模式数为 2 时，Cophenetic 和Silhouette值都开始突然下降。

```R
nPatterns = 2
cellchat <- identifyCommunicationPatterns(cellchat, 
                                          pattern = "outgoing", 
                                          k = nPatterns)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132016890.png)

```R
netAnalysis_river(cellchat, pattern = "outgoing")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132017979.png)

```R
netAnalysis_dot(cellchat, pattern = "outgoing")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132019512.png)

**识别和可视化目标细胞的传入通信模式**

**传入模式**显示目标细胞（即信号接收器中的细胞）如何相互协调，以及它们如何与某些信号通路协调以响应传入的信号。

```
selectK(cellchat, pattern = "incoming")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132023432.png)

当传入模式的数量为 2 时，Cophenetic 值开始下降。

```R
nPatterns = 2
cellchat <- identifyCommunicationPatterns(cellchat, 
                                          pattern = "incoming", 
                                          k = nPatterns)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132025373.png)

```R
netAnalysis_river(cellchat, pattern = "incoming")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132027571.png)

```R
netAnalysis_dot(cellchat, pattern = "incoming")
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303132028974.png)

### (2) 信号网络的多重和分类学习分析

此外，CellChat 能够量化所有重要信号通路之间的相似性，然后根据其CellChat 网络的相似性对其进行分组。分组可以基于功能或结构相似性进行。

功能相似性：功能相似度高表示主要发送器和接收器相似，可解释为两个信号通路或两个配体受体对具有相似的作用。功能相似性分析要求两个数据集之间的细胞群组成相同。

结构相似性：结构相似性用于比较其信号网络结构，而不考虑发送器和接收器的相似性。

**根据信号组的功能相似性识别信号组**

```R
cellchat <- computeNetSimilarity(cellchat, type = "functional")
cellchat <- netEmbedding(cellchat, type = "functional")
#> Manifold learning of the signaling networks for a single dataset
cellchat <- netClustering(cellchat, type = "functional")
#> Classification learning of the signaling networks for a single dataset
# Visualization in 2D-space
netVisual_embedding(cellchat, type = "functional", label.size = 3.5)
```

**基于结构相似性识别信号组**

```R
cellchat <- computeNetSimilarity(cellchat, type = "structural")
cellchat <- netEmbedding(cellchat, type = "structural")
#> Manifold learning of the signaling networks for a single dataset
cellchat <- netClustering(cellchat, type = "structural")
#> Classification learning of the signaling networks for a single dataset
# Visualization in 2D-space
netVisual_embedding(cellchat, type = "structural", label.size = 3.5)
```

```R
netVisual_embeddingZoomIn(cellchat, type = "structural", nCol = 2)
```

