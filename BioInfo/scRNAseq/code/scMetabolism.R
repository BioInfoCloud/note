

library(scMetabolism)
library(ggplot2)
library(rsvd)

load("sce.Rdata")
countexp.Seurat<-sc.metabolism.Seurat(obj = subcell_sce, 
                                      method = "AUCell", 
                                      imputation = F, ncores = 2, 
                                      metabolism.type = "KEGG")
ls()


rownames(countexp.Seurat@assays[["METABOLISM"]][["score"]])[1:6]

DimPlot.metabolism(obj = countexp.Seurat, 
                   pathway = "Pentose phosphate pathway", 
                   dimention.reduction.type = "umap", 
                   dimention.reduction.run = F, size = 1)
DimPlot.metabolism(obj = countexp.Seurat, 
                   pathway = "Citrate cycle (TCA cycle)", 
                   dimention.reduction.type = "tsne", 
                   dimention.reduction.run = F, size = 1)


input.pathway<-rownames(countexp.Seurat@assays[["METABOLISM"]][["score"]])[1:6]
DotPlot.metabolism(obj = countexp.Seurat, pathway = input.pathway, 
                   phenotype = "seurat_clusters", norm = "y")

