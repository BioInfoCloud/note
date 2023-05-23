ScAnno 是一个针对单细胞 RNA 测序数据集的自动注释工具，主要基于单细胞簇水平，使用联合反卷积策略和 Logit模型。作者明确创建了完整的人类参考图谱(来自人类细胞景观的30种细胞类型，覆盖50多个人类组织)和小鼠参考图谱(来自小鼠细胞图谱的26种细胞类型，覆盖近50个小鼠组织)以支持这种新方法(scAnno)。ScAnno 通过将共表达基因与种子基因作为核心结合，提供了在特定细胞类型中获得高表达和特异性基因的可能性，作为细胞类型特异性基因(标记基因)。重要的是，scAnno 可以在没有先验信息的情况下，基于细胞类型参考表达谱准确鉴定细胞类型特异性基因。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202305180957977.png)

## 1.包的安装

```R
#install.packages("devtools")  
devtools::install_github("liuhong-jia/scAnno") 
```

## 2.准备输入数据

```R
library(scAnno)

#Import human single cell reference profile.
data(hcl.sc)

#Import protein coding gene(19814 genes) to filter reference expression profile.
data(gene.anno)

#Import TCGA bulk data in pan-cancer.
data(tcga.data.u)

#A liver tissue data set to be annotated.
data(GSE136103)
```

## 3.单细胞注释

```R
# Seurat object, which need to be annotated.
obj.seu <- GSE136103

#Seurat object of reference gene expression profile.
ref.obj <- hcl.sc

#Reference gene expression profile.
ref.expr <- GetAssayData(ref.obj, slot = 'data') %>% as.data.frame

#Cell type information of reference profile, corresponding to the above `ref.expr`.
ref.anno <- Idents(ref.obj) %>% as.character
```

## 4.运行 scAnno 来注释细胞

```r
results = scAnno(query = obj.seu,
	ref.expr = ref.expr,
	ref.anno = ref.anno,
	save.markers = "markers",
	cluster.col = "seurat_clusters",
	factor.size = 0.1,
	pvalue.cut = 0.01,
	seed.num = 10,
	redo.markers = FALSE,
	gene.anno = gene.anno,
	permut.num = 100,
	permut.p = 0.01,
	show.plot = TRUE,
	verbose = TRUE,
	tcga.data.u = tcga.data.u
	)
```

## 5.可视化

```R
DimPlot(results$query, group.by = "seurat_clusters", label = TRUE, label.size = 6) | DimPlot(results$query, group.by = 'scAnno', label = TRUE , label.size = 6)
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202305181507974.png)

## 6.引用

参考：https://github.com/liuhong-jia/scAnno

Hongjia Liu and others, scAnno: a deconvolution strategy-based automatic cell type annotation tool for single-cell RNA-sequencing data sets, Briefings in Bioinformatics, 2023;, bbad179, https://doi.org/10.1093/bib/bbad179