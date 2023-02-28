## 一.原理

参考文献：https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9010342/

单细胞 RNA 测序可区分异质组织背景下的细胞类型、状态和谱系。然而，目前的单细胞数据无法直接将具有特定表型的细胞簇联系起来。 Scissor是一种从与给定表型相关的单细胞数据中识别细胞亚群的方法。Scissor 通过首先量化每个单细胞和每个批量样本之间的相似性来整合表型相关的大量表达数据和单细胞数据。然后，它使用样本表型优化相关矩阵的回归模型，以识别相关亚群。

Scissor的工作流程如图1所示。将m和n分别表示为单元编号和大样本编号。剪式输入的三个数据源是具有m个细胞的单细胞表达矩阵、具有n个样本的批量分析数据和感兴趣的样本表型Y（如图1a）。Y注释每个大样本，可以是连续因变量、二元组指示向量或临床生存数据。Scissor首先对单个单元格和批量表达式数据使用分位数归一化，以消除潜在的批处理效应。之后，为每对细胞和批量样本计算皮尔逊相关矩阵S=(s~ij~)~n×m~，以量化单细胞数据和批量数据之间的相似性，其中s~ij~是标准化单细胞和批量数据中样本i和细胞j共同基因的相关性。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302232208694.png)

Scissor优化了相关矩阵S与样本表型Y的回归模型（图1b）。设*β*表示单元上的系数向量，l(*β*)表示适当选择的对数似然函数。l(*β*)的公式取决于输入表型Y，即连续因变量的线性回归、二分变量的逻辑回归（分类）和临床生存数据的Cox回归。由于单独的细胞亚群可以驱动感兴趣的表型，我们对模型施加稀疏惩罚（*l*~1~-norm），以选择对给定表型重要的高置信度细胞。此外，基于网络的惩罚迫使网络中紧密连接的节点（细胞）具有更相似的系数，使得表型与细胞的关联结果更一致和可解释。受此启发，我们使用Seurat中计算的共享最近邻图作为细胞-细胞相似性网络*G*，并将相应的图正则化应用于回归模型。总体而言，Scissor 被制定为以下网络正则化稀疏回归模型:

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211659156.png)

其中 L 是对称归一化拉普拉斯矩阵，定义为:

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211700640.png)

其中A＝(a~ij~)~m×m~是G的二进制或加权邻接矩阵。如果单元i和j在G中连接，则a~ij~等于1或范围为0到1的值，否则a~ij~＝0。D=(d~ij~)~m×m~是G的度矩阵，其中<img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211705177.png" style="zoom:50%;" />，并且对于i≠j时*d~i,j~* = 0。调整参数λ控制惩罚的整体强度，λ平衡平滑度和稀疏度的正则化量。

通过上述优化模型求解的β的非零系数用于选择与感兴趣表型相关的细胞亚群（图1c）。根据β的符号，我们用Scissor+细胞和Scissor-细胞表示选择的细胞，它们分别与感兴趣的表型正相关和负相关。系数为零的单元表示为背景单元。此外，为了控制single-cell和bulk数据之间的错误关联，我们设计了可靠性显著性测试，以确定所选数据是否适合我们的表型与细胞关联（图1d）。最后，Scissor选择的细胞将通过几个下游分析进一步研究，如差异表达基因分析、功能富集分析和基序分析，以揭示所选细胞亚群的潜在生物学机制（图1e）。

对数似然函数l(*β*)的公式取决于表型Y的类型。Scissor可以做到：（1）连续因变量的线性回归；（2）二分变量分类；（3） 临床生存数据的Cox回归。具体而言，将 *S~i~* = (*s~i1~*,*s~i2~*,⋯,*s~im~*)^T^ 表示为样本 i 在所有 m 个单元格中的相关系数。如果 Y=(y~1~,y~2~,⋯,y~n~)^T^ 是连续变量，则使用线性回归对数似然函数：

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211734785.png)

如果 Y 是二元组指标向量，例如 yi ∈{0,1}，则使用逻辑回归对数似然函数：

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211735615.png)

对于受独立审查的事件间结果，考虑Cox回归。设T~i~为非负事件时间，C~i~为审查时间。将<img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211738988.png" style="zoom:50%;" />表示为观察到的事件时间或删失时间，δ~i~ = I(T~i~ ≤ C~i~)作为事件指示器，其中I(.)是指示器函数。使用以下对数似然函数：

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211739182.png)

其中 <img src="https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302211741799.png" style="zoom:67%;" />表示在时间T^^^~i~时的风险集。

## 二.案例

### 1.准备单细胞数据

```R
devtools::install_github('sunduanchen/Scissor')#安装包
library(Scissor)
location <- "https://xialab.s3-us-west-2.amazonaws.com/Duanchen/Scissor_data/"
load(url(paste0(location, 'scRNA-seq.RData')))
ls()
head(sc_dataset)[,1:3]
```

```R
MedBioInfoCloud: head(sc_dataset)[,1:3]
              AAACCTGAGACTACAA_15 AAACCTGAGACTTGAA_20 AAACCTGAGCGCCTTG_15
RP11-34P13.3                    0                   0                   0
FAM138A                         0                   0                   0
OR4F5                           0                   0                   0
RP11-34P13.7                    0                   0                   0
RP11-34P13.8                    0                   0                   0
RP11-34P13.14                   0                   0                   0
```

在这个 LUAD scRNA-seq 数据中，每一行代表一个基因，每一列代表一个癌细胞。共有33694个基因和4102个癌症细胞。对于Scissor中使用的scRNA-seq数据，优选包含预处理数据和构建网络的Seurat对象。我们使用Seurat包中的函数来预处理这些数据并构建细胞-细胞相似性网络。在这个包中，我们将Seurat分析管道打包为以下函数：

```R
sc_dataset <- Seurat_preprocessing(sc_dataset, verbose = F)
```

```R
MedBioInfoCloud: class(sc_dataset)
[1] "Seurat"
attr(,"package")
[1] "SeuratObject"
MedBioInfoCloud: names(sc_dataset)
[1] "RNA"     "RNA_nn"  "RNA_snn" "pca"     "tsne"    "umap" 
```

它包含所需的预处理矩阵和构建的细胞间相似性网络，以及其他有用的降维结果，例如 PCA、t-SNE 和 UMAP。

用户可以在此函数中调整预处理参数以实现不同的目标，并将其他相关的 Seurat 函数应用于 sc_dataset。例如，我们可以使用 UMAP 坐标可视化这 4,102 个细胞：

```R
DimPlot(sc_dataset, reduction = 'umap', label = T, label.size = 7)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302221046179.png)

此外，用户还可以使用自己的 Seurat 分析管道（需要归一化数据和构建的网络）或其他工具预处理的 scRNA-seq 数据集来提供 Seurat 对象。可参考去哦前面单细胞的文章。

### 2.将 Scissor 与Cox回归一起应用

#### 2.1准备RNAseq数据和表型

我们加载预处理的 LUAD 大量表达矩阵和从癌症基因组图谱 (TCGA) 下载的相应生存数据。

```R
load(url(paste0(location, 'TCGA_LUAD_exp1.RData')))
load(url(paste0(location, 'TCGA_LUAD_survival.RData')))
head(bulk_dataset)[,1:4]
head(bulk_survival)
```

```R
MedBioInfoCloud: head(bulk_dataset)[,1:4]
         TCGA-05-4249 TCGA-05-4250 TCGA-05-4382 TCGA-05-4384
TSPAN6      57.523977   66.4940573    30.905120    35.104344
TNMD         0.000000    0.1748819     0.000000     0.000000
DPM1        98.838134  135.2046911    84.362971    89.105535
SCYL3       16.233391    6.0050820     6.226792    16.930497
C1orf112     5.139334    7.4082268     4.778406     4.139623
FGR         20.750354   24.0549654    48.509972    35.823591
MedBioInfoCloud: head(bulk_survival)
  TCGA_patient_barcode OS_time Status
1         TCGA-05-4249    1158      0
2         TCGA-05-4250     121      1
3         TCGA-05-4382     607      0
4         TCGA-05-4384     426      0
5         TCGA-05-4389    1369      0
6         TCGA-05-4390    1126      0
```

数据共有56716个基因和471个样本。用户不需要保留单细胞样本和批量样本之间的共同基因，这可以在 Scissor 中自动实现。此外，所有这些样本都有临床结果。

临床生存表型需要两列矩阵，其中列名为“时间”和“状态”。第一列包含样本ID（观察值），其顺序应与表达矩阵中的列相同。

```R
all(colnames(bulk_dataset) == bulk_survival$TCGA_patient_barcode)
```

```R
phenotype <- bulk_survival[,2:3]
colnames(phenotype) <- c("time", "status")
head(phenotype)
```

#### 2.2.执行 Scissor 以选择信息细胞

鉴于上述输入，我们可以使用 Scissor 来选择与表型相关的细胞亚群，该亚群由 Cox 回归模型（family = 'cox'）拟合：

```R
infos1 <- Scissor(bulk_dataset, sc_dataset, phenotype, alpha = 0.05, 
                 family = "cox", Save_file = 'Scissor_LUAD_survival.RData')
```

```R
[1] "|**************************************************|"
[1] "Performing quality-check for the correlations"
[1] "The five-number summary of correlations:"
        0%        25%        50%        75%       100% 
0.01319134 0.19658357 0.23945759 0.29808510 0.83727807 
[1] "|**************************************************|"
[1] "Perform cox regression on the given clinical outcomes:"
[1] "alpha = 0.05"
[1] "Scissor identified 201 Scissor+ cells and 4 Scissor- cells."
[1] "The percentage of selected cell is: 4.998%"
[1] "|**************************************************|"
```

如打印消息所示，Scissor首先输出单细胞样本和大样本之间相关性的五个数字摘要。我们发现所有的相关性都是正的，并且这些值不接近0。在实际应用中，如果使用的数据集的中值相关性太低（<0.01），Scissor将发出警告信息，这可能会导致不可靠的表型与细胞的关联。

Scissor 总共识别出 201 个与较差生存相关的 Scissor+ 细胞和 4 个与良好生存相关的 Scissor- 细胞，这些细胞保存在 infos1 中：

```R
MedBioInfoCloud: names(infos1)
[1] "para"        "Coefs"       "Scissor_pos" "Scissor_neg"
MedBioInfoCloud: length(infos1$Scissor_pos)
[1] 201
MedBioInfoCloud: infos1$Scissor_pos[1:4]
[1] "AAAGTAGAGGAGCGAG_19" "AACCATGCATCTCCCA_19" "AACCGCGAGCTGCGAA_20" "AACTCAGTCCGCGGTA_19"
MedBioInfoCloud: length(infos1$Scissor_neg)
[1] 4
MedBioInfoCloud: infos1$Scissor_neg
[1] "ACGCCAGTCCTCCTAG_20" "ACGGGCTAGTGGCACA_20" "CCGGTAGGTACCCAAT_15" "GACGCGTAGTGGTCCC_20"
```

这些选定的cell占总数 4,102 个cell的 5%。我们可以通过在 Seurat 对象 sc_dataset 中添加一个新的注释来可视化Scissor选择的单元格：

```R
Scissor_select <- rep(0, ncol(sc_dataset))
names(Scissor_select) <- colnames(sc_dataset)
Scissor_select[infos1$Scissor_pos] <- 1
Scissor_select[infos1$Scissor_neg] <- 2
sc_dataset <- AddMetaData(sc_dataset, metadata = Scissor_select, 
                          col.name = "scissor")
DimPlot(sc_dataset, reduction = 'umap', group.by = 'scissor', 
        cols = c('grey','indianred1','royalblue'), 
        pt.size = 1.2, order = c(2,1))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302221114295.png)

其中1代表Scissor+细胞，2代表Scissor-细胞。 最后，我们可以使用以下方法访问参数和使用的模型：

```R
MedBioInfoCloud: infos1$para
$alpha
[1] 0.05

$lambda
[1] 0.04229243

$family
[1] "cox"
```

在上述实现中，我们将参数α设置为0.05（α=0.05）。参数α平衡L1-norm和基于网络的惩罚的效果。较大的α倾向于强调L1-norm以鼓励稀疏性，使得Scissor比使用较小α的结果选择更少的细胞。在应用程序中，Scissor可以自动将回归输入保存到RData（`save_file='Scissor_LUAD_survive.RData`）中，方便用户调整不同的α。我们可以将Load_file设置为“`Scissor_LUAD_survive.RData`”，并使用默认的α序列（alpha=NULL）运行Scissor：

```R
infos2 <- Scissor(bulk_dataset, sc_dataset, phenotype, alpha = NULL, cutoff = 0.03, 
                 family = "cox", Load_file = 'Scissor_LUAD_survival.RData')
```

```R
[1] "alpha = 0.005"
[1] "Scissor identified 887 Scissor+ cells and 28 Scissor- cells."
[1] "The percentage of selected cell is: 22.306%"

[1] "alpha = 0.01"
[1] "Scissor identified 573 Scissor+ cells and 20 Scissor- cells."
[1] "The percentage of selected cell is: 14.456%"

[1] "alpha = 0.05"
[1] "Scissor identified 201 Scissor+ cells and 4 Scissor- cells."
[1] "The percentage of selected cell is: 4.998%"

[1] "alpha = 0.1"
[1] "Scissor identified 139 Scissor+ cells and 5 Scissor- cells."
[1] "The percentage of selected cell is: 3.510%"

[1] "alpha = 0.2"
[1] "Scissor identified 78 Scissor+ cells and 5 Scissor- cells."
[1] "The percentage of selected cell is: 2.023%"
[1] "|**************************************************|"
```

在上述实现中，我们设置了一个新的百分比截止值（截止值=0.03），当所选细胞的总百分比小于3%时，它停止了α搜索。相应的α等于0.2，选择了78个Scissor+细胞和5个Scissor-细胞。为了避免在实际应用中任意选择alpha，我们建议根据所选细胞在总细胞中的百分比来搜索alpha。截止值的默认值为0.2，即Scissor选择的细胞的数量不应超过单个细胞数据中总单元格的20%。此外，用户可以设置自定义的α序列和百分比截止值，以实现不同的目标。例如，我们可以将Scissor运行为：

```R
infos3 <- Scissor(bulk_dataset, sc_dataset, phenotype, alpha = seq(1,10,2)/1000, cutoff = 0.2,
                 family = "cox", Load_file = 'Scissor_LUAD_survival.RData')
```

```R
[1] "alpha = 0.001"
[1] "Scissor identified 1663 Scissor+ cells and 1870 Scissor- cells."
[1] "The percentage of selected cell is: 86.129%"

[1] "alpha = 0.003"
[1] "Scissor identified 1264 Scissor+ cells and 37 Scissor- cells."
[1] "The percentage of selected cell is: 31.716%"

[1] "alpha = 0.005"
[1] "Scissor identified 887 Scissor+ cells and 28 Scissor- cells."
[1] "The percentage of selected cell is: 22.306%"

[1] "alpha = 0.007"
[1] "Scissor identified 729 Scissor+ cells and 24 Scissor- cells."
[1] "The percentage of selected cell is: 18.357%"
[1] "|**************************************************|"
```

### 4.将 Scissor 与逻辑回归一起应用

在另一个例子中，我们使用TCGA-LUAD提供的其他表型特征来指导相同4102个癌症细胞内细胞亚群的识别。这里我们重点关注TP53，它是人类恶性肿瘤中最常见的突变抑癌基因之一。

#### 4.1准备RNAseq数据和表型

```R
load(url(paste0(location, 'TCGA_LUAD_exp2.RData')))
load(url(paste0(location, 'TCGA_LUAD_TP53_mutation.RData')))
```

样本498个；其中255个检测到TP53突变体，其余为野生型：

```R
MedBioInfoCloud: table(TP53_mutation)
TP53_mutation
  0   1 
243 255 
```

#### 4.2执行Scissor 选择信息细胞

给定TP53突变体=1和野生型=0的上述二元变量，我们使用Scissor中的`family = 'binomial'`来选择表型相关的细胞亚群：

```R
phenotype <- TP53_mutation
tag <- c('wild-type', 'TP53 mutant')
infos4 <- Scissor(bulk_dataset, sc_dataset, phenotype, tag = tag, alpha = 0.5, 
                  family = "binomial", Save_file = "Scissor_LUAD_TP53_mutation.RData")
```

```R
[1] "|**************************************************|"
[1] "Performing quality-check for the correlations"
[1] "The five-number summary of correlations:"
        0%        25%        50%        75%       100% 
0.01308976 0.19502200 0.23725380 0.29589213 0.83830571 
[1] "|**************************************************|"
[1] "Current phenotype contains 243 wild-type and 255 TP53 mutant samples."
[1] "Perform logistic regression on the given phenotypes:"
[1] "alpha = 0.5"
[1] "Scissor identified 173 Scissor+ cells and 160 Scissor- cells."
[1] "The percentage of selected cell is: 8.118%"
[1] "|**************************************************|"
```

注意，参数标签用于双重检查表型编码。表型中不同的0-1编码可能导致相反的解释。有关更多详细信息，请参阅下一节Scissor结果解释。类似地，我们可以设置α加载`"Load_file="Scissor_LUAD_TP53_mutation.RData"`重新运行：

```R
infos5 <- Scissor(bulk_dataset, sc_dataset, phenotype, tag = tag, alpha = 0.2, 
                 family = "binomial", Load_file = "Scissor_LUAD_TP53_mutation.RData")
```

```R
[1] "alpha = 0.2"
[1] "Scissor identified 414 Scissor+ cells and 320 Scissor- cells."
[1] "The percentage of selected cell is: 17.894%"
[1] "|**************************************************|"
```

Scissor 总共识别出 414 个与 TP53 突变体相关的 Scissor+ 细胞和 318 个与野生型相关的 Scissor- 细胞。我们可以使用 UMAP 技术可视化这些选定的细胞：

```R
Scissor_select <- rep(0, ncol(sc_dataset))
names(Scissor_select) <- colnames(sc_dataset)
Scissor_select[infos5$Scissor_pos] <- 1
Scissor_select[infos5$Scissor_neg] <- 2
sc_dataset <- AddMetaData(sc_dataset, metadata = Scissor_select, col.name = "scissor")
DimPlot(sc_dataset, reduction = 'umap', group.by = 'scissor', 
        cols = c('grey','indianred1','royalblue'), pt.size = 1.2, order = c(2,1))
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202302221238660.png)

其中1代表Scissor+细胞，2代表Scissor-细胞。

### 5.可靠性显著性试验

为了确定推断出的表型与细胞的相关性是否可靠，我们使用功能`reliability.test`进行可靠性显著性检验。可靠性显著性测试的动机是：如果所选的单细胞和bulk数据不适合表型与细胞的关联，则相关性信息较少，且与表型标签不太相关。因此，相应的预测性能将是差的，并且不能与随机置换的标签显著区分。在本教程中，我们将测试上述应用程序中识别的关联作为示例，以演示如何运行`reliability.test`。

```R
load('Scissor_LUAD_survival.RData')
```

我们使用10倍交叉验证（nfold＝10），并将置换时间设置为10（n＝10）以节省一些时间。在实际应用中，可靠性显著性测试对于较大的排列时间（默认n=100）来说可能是耗时的。

```R
numbers <- length(infos1$Scissor_pos) + length(infos1$Scissor_neg)
result1 <- reliability.test(X, Y, network, alpha = 0.05, 
                            family = "cox", cell_num = numbers, n = 10, nfold = 10)
```

```R
[1] "|**************************************************|"
[1] "Perform cross-validation on X with true label"
Finished!
[1] "|**************************************************|"
[1] "Perform cross-validation on X with permutated label"
Finished!
[1] "Test statistic = 0.628"
[1] "Reliability significance test p = 0.000"
```

我们可以看到，`reliability.test`打印检验统计和检验p值。该p值小于0.05，表明这些关联是可靠的。输出结果1还包含使用真实标签和置换标签计算的评估测量值：

在我们的研究中，评价度量是线性回归的均方误差（MSE）、分类的ROC曲线下面积（AUC）和Cox回归的一致性指数（c-index）。使用真实标签计算的平均评价测量值用作测试统计量。

同样，我们可以测试与 TP53 突变体或野生型相关的 Scissor 选择细胞。

```R
load('Scissor_LUAD_TP53_mutation.RData')
numbers <- length(infos5$Scissor_pos) + length(infos5$Scissor_neg)
result2 <- reliability.test(X, Y, network, alpha = 0.2, family = "binomial", cell_num = numbers, n = 10, nfold = 10)
```

```R
## [1] "|**************************************************|"
## [1] "Perform cross-validation on X with true label"
## Finished!
## [1] "|**************************************************|"
## [1] "Perform cross-validation on X with permutated label"
## Finished!
## [1] "Test statistic = 0.790"
## [1] "Reliability significance test p = 0.000"
```

### 6.细胞水平评估

最后，我们可以使用函数evaluate.cell为每个Scissor选择的细胞获取一些支持信息。以LUAD癌症细胞存活应用程序为例，我们通过运行以下代码评估205 Scissor选择的细胞：

```R
evaluate_summary <- evaluate.cell('Scissor_LUAD_survival.RData', infos1, FDR = 0.05, bootstrap_n = 100)
```

evaluate.cell函数包含两种策略来评估每个Scissor选择的细胞。第一种策略侧重于具有所有bulk样本的每个选定细胞的相关值及其对应的p值，包括输出data.frame变量中的前四列：

```R
evaluate_summary[1:5,1:4]
```

```R
MedBioInfoCloud: evaluate_summary[1:5,1:4]
                    Mean correlation Correlation > 0 Correlation < 0 Significant Correlation
AAAGTAGAGGAGCGAG_19        0.3056072            100%              0%                    100%
AACCATGCATCTCCCA_19        0.1974518            100%              0%                    100%
AACCGCGAGCTGCGAA_20        0.3569129            100%              0%                    100%
AACTCAGTCCGCGGTA_19        0.3628618            100%              0%                    100%
AACTCCCAGCGCCTTG_19        0.2835872            100%              0%                    100%
```

我们可以看到，`evaluate.cell`函数报告了一个细胞与所有bulk样本的平均相关性（列mean correlation）和正/负相关性（列correlation>0和correlation<0）的百分比，这与我们提出的一般解释标准（表1）中的条件相对应。在该应用中，所有Scissor选择的细胞与相关表型更相似：

```R
all(evaluate_summary$`Mean correlation` & as.numeric(gsub('%','',evaluate_summary$`Correlation > 0`)) > 50)
```

evaluate.cell函数还检查从每个选定细胞的标准相关p值导出的FDR。它输出每个选定细胞的显著相关性百分比（FDR<0.05，显著相关性列）。

```R
MedBioInfoCloud: evaluate_summary[1:5,5:10]
                    Coefficient      Beta 0%    Beta 25%    Beta 50%   Beta 75%  Beta 100%
AAAGTAGAGGAGCGAG_19 0.009203078 0.0006535843 0.006349622 0.009940265 0.01499857 0.02747730
AACCATGCATCTCCCA_19 0.003779788 0.0001131087 0.003247118 0.006729676 0.01058692 0.02185486
AACCGCGAGCTGCGAA_20 0.005839546 0.0001044831 0.003500107 0.007839735 0.01359622 0.02852694
AACTCAGTCCGCGGTA_19 0.004415840 0.0005875274 0.003877294 0.008254801 0.01476508 0.03463764
AACTCCCAGCGCCTTG_19 0.014565920 0.0003173535 0.010897044 0.018264455 0.02771921 0.04282416
```

通过使用bootstrap重采样，`evaluate.cell`函数输出五个数字摘要以显示每个Scissor选择的细胞的系数范围，其中包括最小值（Beta列0%），下四分位数（Beta列25%）），中值（Beta列50%），上四分位数（Beta列75%）和最大值（Beta列100%）。
