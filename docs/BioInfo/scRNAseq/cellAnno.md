## 1.细胞类型的marker基因

单细胞人工注释依赖于marker gene的调查，简单来说，就是收集各种细胞类型的标志物，根据标志物在不同细胞亚群中的表达来判断细胞类型。细胞标志物的收集可以来源于文献或者数据库。

下面这些是一些来自文献的标志物信息

### 1.1 文献

**文献：**Acquired cancer resistance to combination immunotherapy from transcriptional loss of class I HLA

<img src="https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210141625398.png" style="zoom: 67%;" />

再比如2018年发表于science杂志的文章就是自己根据文献进行整理的：Single-cell transcriptomes from human kidneys reveal the cellular identity of renal tumors.

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210141653204.png)

再如：人肾脏组织主要细胞类型marker基因列表（data from CellMarker）

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210151755415.png)

### 1.2 数据库

[panglaodb](https://panglaodb.se/index.html)： https://panglaodb.se/index.html

[CellMarker ](http://xteam.xbio.top/CellMarker/index.jsp)：http://xteam.xbio.top/CellMarker/index.jsp

## 2.人工注释案例

我们继续以我们前面的文章保存的数据为例：

```R
library(SingleR)
library(Seurat)
setwd("H:/MedBioInfoCloud/analysis/scRNAseq/BLCA/GSE130001/")
load('data/sce.output.merge.GSE130001.Rdata')
```

我们从CellMarker 数据库中查看膀胱组织中的标志物信息：

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210151952372.png)

可视化这些基因在不同亚群中的表达：

```R
genes_to_check <- c("ALDH1",
                    "CD133", "OCT4",
                    "CD133",
                    "CD24", "CD44", "CD47",
                    "CD44v6","EMA",
                    "SOX2",
                    "CD34",
                    "EMA",
                    "N-cadherin",
                    "UGP85",
                    "CD44", "CK20", "CK5")
library(stringr) 
library(ggplot2)
genes_to_check = unique(intersect(rownames(sce),genes_to_check))
genes_to_check
P13 <- DotPlot(sce, features = genes_to_check,
                         assay='RNA'  )  + coord_flip()
P14 <- VlnPlot(object = sce, features =genes_to_check,log =T )
P15 <- FeaturePlot(object = sce, features=genes_to_check )
ggsave(filename = "data/mk.pdf",P13/P14/P15,height = 15,width = 10)
```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210152008394.png)

上次singleR注释的结果：

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210140044729.png)



根据标志物的表达情况，首先，可以很确定的是第8个细胞亚群为Endothelial cell。因为Endothelial cell的标志物是CD34，但是这个正常的膀胱组织细胞类型，这个也很正常，取的肿瘤组织（CD45-），含有个别正常细胞正常。其他的大部分类群都是Bladder Cancer 细胞。但是上次使用singleR注释时，第12个亚群是NK细胞，查看一下CD45的表达。

```R
MedBioInfoCloud: DotPlot(sce, features = "CD45",
+         assay='RNA'  )
Error in FetchData.Seurat(object = object, vars = features, cells = cells) : 
  None of the requested variables were found: CD45
```

CD45在数据质控的时候已经被过滤掉了【本身样本CD45阴性】，作者文章也说有了，有CD45阴性的免疫细胞。所以我个人觉得可以将12这个细胞类群删除，用于后续的分析。

这里我们就暂且按照注释的细胞重新命名一下就行了：

```R
###直接修改类群的值
sce3 <- sce
new.cluster.ids <- c(rep("Bladder Cancer",8),"Endothelial cell",rep("Bladder Cancer",4))

names(new.cluster.ids) <- levels(sce3)
sce3 <- RenameIdents(sce3, new.cluster.ids)

DimPlot(sce3, reduction = "tsne", label = TRUE, pt.size = 0.5) + NoLegend()

```

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210152117061.png)

相对来说，该数据集中是流式筛选后测序的数据，所以这里的注释还是可靠的，后续的分析可以结合SingleR包注释的结果和人工审核的结果一起判断，用于后续的分析，这里可以只选择上皮细胞进行后续的分析，因为这个类群是很确定的癌细胞。下面这个图是来自一篇使用了该数据集的一篇生信文章【[PMID：35769986](https://www.ncbi.nlm.nih.gov/pubmed/35769986)】中的结果图，作者使用的是SingleR包注释，也的确有NK细胞，但它的过滤条件和我这里教程的不一样，作者还融合了其他数据集。但整体上来说，自己注释的方法就是这么一个流程。

![](https://raw.githubusercontent.com/BioInfoCloud/ImageGo/main/202210152119255.png)



## 3.总结

总之，人工注释依赖于自己的知识背景和marker基因的收集。实际上我做的大量肿瘤单细胞数据分析项目里面，需要有一些背景知识哦！比如背诵如下所示各个细胞亚群高表达量基因的列表：

```R
# T Cells (CD3D, CD3E, CD8A), 
# B cells (CD19, CD79A, MS4A1 [CD20]), 
# Plasma cells (IGHG1, MZB1, SDC1, CD79A), 
# Monocytes and macrophages (CD68, CD163, CD14),
# NK Cells (FGFBP2, FCG3RA, CX3CR1),  
# Photoreceptor cells (RCVRN), 
# Fibroblasts (FGF7, MME), 
# Endothelial cells (PECAM1, VWF). 
# epi or tumor (EPCAM, KRT19, PROM1, ALDH1A1, CD24).
#   immune (CD45+,PTPRC), epithelial/cancer (EpCAM+,EPCAM), 
# stromal (CD10+,MME,fibo or CD31+,PECAM1,endo) 
```