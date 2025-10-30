


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


cellchat <- createCellChat(object = exp, meta = meta2, group.by = "cell_type")




cellchat <- addMeta(cellchat, meta = meta2)
cellchat <- setIdent(cellchat, ident.use = "cell_type") # set "cell_type" as default cell identity
levels(cellchat@idents) # show factor levels of the cell_type

groupSize <- as.numeric(table(cellchat@idents)) # number of cells in each cell group


CellChatDB <- CellChatDB.human # use CellChatDB.mouse if running on mouse data
showDatabaseCategory(CellChatDB)

CellChatDB_mouse <- CellChatDB.mouse 
showDatabaseCategory(CellChatDB_mouse)

dplyr::glimpse(CellChatDB$interaction)

# use Secreted Signaling
CellChatDB.use <- subsetDB(CellChatDB, search = "Secreted Signaling") 
# use all CellChatDB for cell-cell communication analysis
# CellChatDB.use <- CellChatDB # simply use the default CellChatDB

# set the used database in the object
cellchat@DB <- CellChatDB.use

# subset the expression data of signaling genes for saving computation cost
cellchat <- subsetData(cellchat) 
# future::plan("multiprocess", workers = 4) # do parallel
cellchat <- identifyOverExpressedGenes(cellchat)
cellchat <- identifyOverExpressedInteractions(cellchat)
cellchat <- projectData(cellchat, PPI.human)

cellchat <- computeCommunProb(cellchat, raw.use = TRUE)
# 如果某些细胞组中只有少数细胞，则过滤掉细胞间通信
cellchat <- filterCommunication(cellchat, min.cells = 10)

df.net <- subsetCommunication(cellchat)
df.net <- subsetCommunication(cellchat, 
                              sources.use = c(1,2), 
                              targets.use = c(4,5))

df.net <- subsetCommunication(cellchat, signaling = c("CXCL", "ANGPTL"))

cellchat <- computeCommunProbPathway(cellchat)

cellchat <- aggregateNet(cellchat)


groupSize <- as.numeric(table(cellchat@idents))
# par(mfrow = c(1,2), xpd=TRUE)
netVisual_circle(cellchat@net$count, vertex.weight = groupSize, 
                 weight.scale = T, label.edge= F, 
                 title.name = "Number of interactions")
netVisual_circle(cellchat@net$weight, 
                 vertex.weight = groupSize, 
                 weight.scale = T, label.edge= F, 
                 title.name = "Interaction weights/strength")


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


# 
# group.cellType <- c(rep("Epithelial_cells", 3642),rep("Chondrocytes", 143), 
#                     rep("Endothelial_cells", 141),rep("NK_cell", 26)) 
group.cellType <- c("Epithelial_cells","Chondrocytes", "Endothelial_cells",
                    "Tissue_stem_cells","NK_cell") 
names(group.cellType) <- levels(cellchat@idents)
netVisual_chord_cell(cellchat, signaling = pathways.show,
                     group = group.cellType, 
                     title.name = paste0(pathways.show, " signaling network"))

netAnalysis_contribution(cellchat, signaling = pathways.show)

pairLR.ANGPTL <- extractEnrichedLR(cellchat, 
                                    signaling = pathways.show, 
                                    geneLR.return = FALSE)
LR.show <- pairLR.ANGPTL [1,] # show one ligand-receptor pair
# Hierarchy plot
vertex.receiver = seq(1,4) # a numeric vector
netVisual_individual(cellchat, 
                     signaling = pathways.show,  
                     pairLR.use = LR.show, vertex.receiver = vertex.receiver)

netVisual_individual(cellchat, 
                     signaling = pathways.show, 
                     pairLR.use = LR.show, layout = "circle")
netVisual_individual(cellchat, signaling = pathways.show, 
                     pairLR.use = LR.show, layout = "chord")


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


# show all the significant interactions (L-R pairs) from some cell groups (defined by 'sources.use') to other cell groups (defined by 'targets.use')
netVisual_bubble(cellchat, sources.use = 4, 
                 targets.use = c(1:5), 
                 remove.isolate = FALSE)
#> Comparing communications on a single object
netVisual_chord_gene(cellchat, sources.use = 4, 
                     targets.use = c(1:5), 
                     lab.cex = 0.5,legend.pos.y = 30)

netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), 
                     targets.use = 2, legend.pos.x = 15)

netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), targets.use = c(5:11), 
                     signaling = c("CCL","CXCL"),legend.pos.x = 8)

netVisual_chord_gene(cellchat, sources.use = c(1,2,3,4), 
                     targets.use = c(1:5), 
                     small.gap =3,
                     slot.name = "netP", legend.pos.x = 1)

plotGeneExpression(cellchat, signaling = "ANGPTL")
plotGeneExpression(cellchat, signaling = "ANGPTL", 
                   enriched.only = FALSE)

# Compute the network centrality scores
cellchat <- netAnalysis_computeCentrality(cellchat, slot.name = "netP") # the slot 'netP' means the inferred intercellular communication network of signaling pathways
# Visualize the computed centrality scores using heatmap, allowing ready identification of major signaling roles of cell groups
netAnalysis_signalingRole_network(cellchat, signaling = pathways.show, width = 8, height = 2.5, font.size = 10)

gg1 <- netAnalysis_signalingRole_scatter(cellchat)
#> Signaling role analysis on the aggregated cell-cell communication network from all signaling pathways
# Signaling role analysis on the cell-cell communication networks of interest
gg2 <- netAnalysis_signalingRole_scatter(cellchat, signaling = c("CXCL", "CXC"))
#> Signaling role analysis on the cell-cell communication network from user's input
gg1 + gg2

ht1 <- netAnalysis_signalingRole_heatmap(cellchat, pattern = "outgoing")
ht2 <- netAnalysis_signalingRole_heatmap(cellchat, pattern = "incoming")
ht1 + ht2
library(NMF)
library(ggalluvial)

selectK(cellchat, pattern = "outgoing")


nPatterns = 2
cellchat <- identifyCommunicationPatterns(cellchat, 
                                          pattern = "outgoing", 
                                          k = nPatterns)
netAnalysis_river(cellchat, pattern = "outgoing")

netAnalysis_dot(cellchat, pattern = "outgoing")

selectK(cellchat, pattern = "incoming")

nPatterns = 2
cellchat <- identifyCommunicationPatterns(cellchat, 
                                          pattern = "incoming", 
                                          k = nPatterns)

netAnalysis_river(cellchat, pattern = "incoming")
netAnalysis_dot(cellchat, pattern = "incoming")

cellchat <- computeNetSimilarity(cellchat, type = "functional")
cellchat <- netEmbedding(cellchat, type = "functional")
#> Manifold learning of the signaling networks for a single dataset
cellchat <- netClustering(cellchat, type = "functional")
#> Classification learning of the signaling networks for a single dataset
# Visualization in 2D-space
netVisual_embedding(cellchat, type = "functional", label.size = 3.5)

netVisual_embeddingZoomIn(cellchat, type = "structural", nCol = 2)




