
```r

library(clusterProfiler)
library(org.Hs.eg.db)
library(org.Mm.eg.db)
library(AnnotationDbi)
load("F:/BioInfoStudy/data/genesets/mouse_H_v5p2.rdata")
load("F:/BioInfoStudy/data/genesets/human_H_v5p2.rdata")
hsa_ent <- c()
for(x in names(Hs.H)){
  hsa_ent <- c(hsa_ent,Hs.H[[x]])
}
hsa_ent <- unique(hsa_ent)
length(hsa_ent)

hsa_ent2symb <- bitr(hsa_ent,
                     fromType = "ENTREZID",
                     toType = "SYMBOL",
                     OrgDb = org.Hs.eg.db)
dim(hsa_ent2symb)

diff_ent <- setdiff(hsa_ent,hsa_ent2symb$ENTREZID)

ent2symb <- toTable(org.Hs.egSYMBOL)
ent2symb[match(diff_ent,ent2symb$gene_id),]

AnnotationDbi::select(org.Hs.eg.db,
                      keys=diff_ent,columns=c("SYMBOL"),
                      keytype="ENTREZID" )
mget(diff_ent,
     org.Hs.egSYMBOL,
     ifnotfound=NA)
```
通过多种转换方式，发现人的ENTREZID有3个无法找到对应的SYMBOL，NCBI上检索了一下，也没找到这3个基因。
```r
> diff_ent
[1] "285464" "11217"  "80761"
```
再看看小鼠的。
```r
mus_ent <- c()
for(x in names(Mm.H)){
  mus_ent <- c(mus_ent,Mm.H[[x]])
}
mus_ent <- unique(mus_ent)
length(mus_ent)

mus_ent2symb <- bitr(mus_ent,
                     fromType = "ENTREZID",
                     toType = "SYMBOL",
                     OrgDb = org.Mm.eg.db)
dim(mus_ent2symb)

diff_ent <- setdiff(mus_ent,mus_ent2symb$ENTREZID)

ent2symb <- toTable(org.Hs.egSYMBOL)
ent2symb[match(diff_ent,ent2symb$gene_id),]

AnnotationDbi::select(org.Hs.eg.db,
                      keys=diff_ent,columns=c("SYMBOL"),
                      keytype="ENTREZID" )

#org.Mm.egMAPCOUNTS
mget(diff_ent,
     org.Mm.egSYMBOL,
     ifnotfound=NA)
```
居然有15个没有找到对应的symbol。
```r
> diff_ent
 [1] "675165"    "100038993" "100861969" "100043385" "100504735" "105245585" "546061"   
 [8] "625758"    "668131"    "665343"    "667941"    "11641"     "100039053" "100043918"
[15] "100043921"
```
```r
####------------------------------
conversion_BtHsaAndMusGenes <- function(genes,species){
  human <- biomaRt::useMart(biomart = "ENSEMBL_MART_ENSEMBL",
                            dataset = "hsapiens_gene_ensembl")
  mouse <- biomaRt::useMart(biomart = "ENSEMBL_MART_ENSEMBL",
                            dataset = "mmusculus_gene_ensembl")
  if(species == "human"){
    gt <- biomaRt::getLDS(attributes = c("hgnc_symbol"),
                          filters = "hgnc_symbol",
                          values = genes,
                          mart = human,
                          attributesL = c("mgi_symbol"),
                          martL = mouse,uniqueRows = T)
  }else if(species == "mouse"){
    gt <- biomaRt::getLDS(attributes = c("mgi_symbol"),
                          filters = "mgi_symbol",
                          values = genes , mart = mouse,
                          attributesL = c("hgnc_symbol"),
                          martL = human, uniqueRows=T)
  }else{stop("Wrong species information")}

  return(gt)
}

load(file = "K:/BioInfoFiles/基因组相关文件/human/gencode.v35_human_hsaGeneInfo.Rdata")
head(hsaGeneInfo)[1:3,]
# > head(hsaGeneInfo)
# ensembl   symbol      gene_type geneLength
# 1 ENSG00000000003   TSPAN6 protein_coding       4536
# 2 ENSG00000000005     TNMD protein_coding       1476
# 3 ENSG00000000419     DPM1 protein_coding       1207

load(file = "K:/BioInfoFiles/基因组相关文件/mouse/gencode.vM27/gencode.vM27_mouse_musGeneInfo.Rdata")
head(musGeneInfo)
# > head(musGeneInfo)[1:4,]
# ensembl symbol      gene_type geneLength
# 1 ENSMUSG00000000001  Gnai3 protein_coding       3262
# 2 ENSMUSG00000000003   Pbsn protein_coding        902
# 3 ENSMUSG00000000028  Cdc45 protein_coding       3506
# 4 ENSMUSG00000000031    H19         lncRNA       2460

###把小鼠基因转换为人的同源基因
m2h <- conversion_BtHsaAndMusGenes(genes = musGeneInfo$symbol,species = "mouse")

head(m2h)
# > head( m2h)[1:2,]
# MGI.symbol HGNC.symbol
# 1    mt-Atp6     MT-ATP6
# 2     mt-Co2      MT-CO2
dim(m2h)
# > dim(m2h)
# [1] 23075     2
###把人基因转换为小鼠的同源基因
h2m <- conversion_BtHsaAndMusGenes(genes = hsaGeneInfo$symbol,species = "human")
h2m[1:2,]
# > h2m[1:2,]
# HGNC.symbol MGI.symbol
# 1      MT-CO2     mt-Co2
# 2      MT-CO1     mt-Co1
dim(h2m)
# > dim(h2m)
# [1] 22714     2

##有重复的
length(unique(m2h$HGNC.symbol))
length(unique(m2h$MGI.symbol))
# > length(unique(m2h$HGNC.symbol))
# [1] 18411
# > length(unique(m2h$MGI.symbol))
# [1] 19308



hsa_ent_info <- h2m[match(hsa_ent,hsa_ent2symb$ENTREZID),c("HGNC.symbol", "MGI.symbol")]
hsa_ent_info <- merge(h2m,hsa_ent2symb,by.x = "HGNC.symbol",by.y = "SYMBOL")

head(hsa_ent_info)
head(h2m)
length(hsa_ent)
dim(hsa_ent_info)
hsa_ent_info <- na.omit(hsa_ent_info)
dim(hsa_ent_info)

mus_ent_info <- m2h[match(mus_ent,mus_ent2symb$ENTREZID),]
mus_ent_info <- merge(m2h,mus_ent2symb,by.x = "MGI.symbol",by.y = "SYMBOL")
length(mus_ent)
dim(mus_ent_info)
mus_ent_info <- na.omit(mus_ent_info)
dim(mus_ent_info)


statgeneinfo <- data.frame()
identical(names(Hs.H),names(Mm.H))
#gs <- names(Mm.H)[1]
for(gs in names(Mm.H)){
  total_pre_hsa <- length(Hs.H[[gs]])
  total_pre_mus <- length(Mm.H[[gs]])
  hsa_symbol <- bitr(Hs.H[[gs]],
                     fromType = "ENTREZID",
                     toType = "SYMBOL",
                     OrgDb = org.Hs.eg.db)[,2] %>% na.omit()
  total_after_hsa <- length(hsa_symbol)
  mus_symbol <- bitr(Mm.H[[gs]],
                     fromType = "ENTREZID",
                     toType = "SYMBOL",
                     OrgDb = org.Mm.eg.db)[,2] %>% na.omit()
  total_after_mus <- length(mus_symbol)

  hsa_mus_con_g <- intersect(hsa_symbol,m2h[match(mus_symbol,mus_ent2symb$SYMBOL),2])
  hsa_mus_con_len <- length(hsa_mus_con_g)
  has_uniq <- total_pre_hsa - hsa_mus_con_len
  mus_uniq <- total_pre_mus - hsa_mus_con_len
  hsa_na <- total_pre_hsa - total_after_hsa
  mus_na <- total_pre_mus - total_after_mus

  info <- data.frame(dataset = gs,
                     total_pre_hsa = total_pre_hsa,
                     total_pre_mus = total_pre_mus,
                     total_after_hsa = total_after_hsa,
                     total_after_mus = total_after_mus,
                     hsa_mus_con_len = hsa_mus_con_len,
                     has_uniq = has_uniq,
                     mus_uniq = mus_uniq,
                     hsa_na = hsa_na,
                     mus_na = mus_na)
  statgeneinfo <- rbind(statgeneinfo,info)
}

```
