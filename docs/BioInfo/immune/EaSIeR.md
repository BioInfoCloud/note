

## 1.EaSIeR包介绍及安装

恶性肿瘤细胞可通过多种方式干扰肿瘤微环境的免疫细胞以减弱对肿瘤细胞的杀伤作用并诱导免疫细胞免疫耐受。而肿瘤微环境固有的复杂性，多细胞的动态特性，对获取免疫反应生物标志物和预测免疫治疗效果提出了巨大挑战。因此，作者期望使用 bulk RNA-seq数据与不同的先验知识来源（肿瘤浸润细胞，细胞内信号传导，TFs活性,细胞间通讯强弱）相结合，以得出基于系统的肿瘤微环境特征，量化免疫细胞组成以及细胞内和细胞间的通讯。作者通过将多任务学习应用于这些特征，预测免疫反应的不同特征，并基于可解释的Biomarker推导出癌症类型特异性模型。并将该模型应用于来自接受 PD-1/PD-L1 抑制剂治疗的癌症患者的独立 RNA-seq 数据，以证明EaSIeR 的方法可以准确预测治疗结果。

EaSIeR 存储在Biocondoctor， 可以使用BiocManager 下载安装。

```R
BiocManager::install("easier")
# 安装依赖项
BiocManager::install("easier", dependencies = TRUE)
# 下载开发版本
BiocManager::install("olapuentesantana/easier")
# 加载R包
library("easier")
```

## 2.EaSIeR 示例数据

IMvigor210CoreBiologies包，文献PMCID: PMC6028240，数据包含RNA-seq 数据（Count和 TPM）、肿瘤突变负荷 (TMB) 信息和 192 名患者对 ICB 治疗的反应结果。CR, complete response; PD, progressive disease; PR, partial response; SD, stable disease。其中（完全缓解 (CR) 的 25 名：R；疾病进展 (PD) 的 167 名：NR）

官方指导手册：[TGF-b attenuates tumor response to PD-L1 blockade by contributing to exclusion of T cells (gene.com)](http://research-pub.gene.com/IMvigor210CoreBiologies/)

指导手册中IMvigor210CoreBiologies包下载地址失效，可以从我[百度网盘下载](https://pan.baidu.com/s/1eFxcfSmQccrd3y5rHSnikA? )

下载后参照官方指导手册安装。

查看数据：

```R
library(IMvigor210CoreBiologies)
data(cds)
head(counts(cds))
head(fData(cds))
head(pData(cds))

dataset_mariathasan <- get_Mariathasan2018_PDL1_treatment()
dataset_mariathasan

#获取PD-1治疗反应信息
# patient_ICBresponse <- dataset_mariathasan@colData@listData[["BOR"]]
# names(patient_ICBresponse) <- dataset_mariathasan@colData@listData[["pat_id"]]
library(SummarizedExperiment)
#获取PD-1治疗反应信息
patient_ICBresponse <- colData(dataset_mariathasan)[["BOR"]]
names(patient_ICBresponse) <- colData(dataset_mariathasan)[["pat_id"]]

table(meta[colData(dataset_mariathasan)[["pat_id"]],1])


# 获取肿瘤突变负荷信息
TMB <- colData(dataset_mariathasan)[["TMB"]]
names(TMB) <- colData(dataset_mariathasan)[["pat_id"]]

# 获取肿瘤类型
cancer_type <- metadata(dataset_mariathasan)[["cancertype"]]

```

获取基因表达数据

```R
# 获取基因表达矩阵（counts 和tpm）
RNA_counts <- assays(dataset_mariathasan)[["counts"]]
RNA_tpm <- assays(dataset_mariathasan)[["tpm"]]
```

```R
# 随机抽样30例，设定随机数
set.seed(2019)
pat_subset <- sample(names(patient_ICBresponse), size = 30)
patient_ICBresponse <- patient_ICBresponse[pat_subset]
TMB <- TMB[pat_subset]
RNA_counts <- RNA_counts[, pat_subset]
RNA_tpm <- RNA_tpm[, pat_subset]
```

```R
# 考虑到部分基因有多个对应关系，需要进一步处理（保留作者给定的gene symbol）
genes_info <- easier:::reannotate_genes(cur_genes = rownames(RNA_tpm))

## 去除不支持的基因symbol
non_na <- !is.na(genes_info$new_names)
RNA_tpm <- RNA_tpm[non_na, ]
genes_info <- genes_info[non_na, ]

## 去除 entries that are withdrawn
RNA_tpm <- RNA_tpm[-which(genes_info$new_names == "entry withdrawn"), ]
genes_info <- genes_info[-which(genes_info$new_names == "entry withdrawn"), ]
## 找出重复基因
newnames_dup <- unique(genes_info$new_names[duplicated(genes_info$new_names)])
newnames_dup_ind <- do.call(c, lapply(newnames_dup, function(X) which(genes_info$new_names == X)))
newnames_dup <- genes_info$new_names[newnames_dup_ind]

## 检索重复基因的数据
tmp <- RNA_tpm[genes_info$old_names[genes_info$new_names %in% newnames_dup],]

## 删除重复基因的数据
RNA_tpm <- RNA_tpm[-which(rownames(RNA_tpm) %in% rownames(tmp)),]

## 整合重复基因的数据
dup_genes <- genes_info$new_names[which(genes_info$new_names %in% newnames_dup)]
names(dup_genes) <- rownames(tmp)
if (anyDuplicated(newnames_dup)){
  tmp2 <- stats::aggregate(tmp, by = list(dup_genes), FUN = "mean")
  rownames(tmp2) <- tmp2$Group.1
  tmp2$Group.1 <- NULL
  # 整理归纳到一个表达矩阵
  RNA_tpm <- rbind(RNA_tpm, tmp2)
}


```

## 3. 计算免疫反应的Hallmarks

作者利用TPM数据计算下列免疫特征的评分：溶细胞活性 (CYT) (Rooney et al. 2015)、Roh 免疫评分 (Roh_IS) (Roh et al. 2017)、趋化因子特征 (chemokines) (Messina et al. . 2012) , Davoli 免疫特征 (Davoli_IS) (Davoli et al. 2017) , IFNy 特征 (IFNy) (McClanahan 2017) , 扩展免疫特征 (Ayers_expIS) (McClanahan 2017) , T 细胞炎症特征 (Tcell_inflamed) (McClanahan 2017 ) )、免疫抵抗程序（RIR：resF_down、resF_up、resF）(Jerby-Arnon et al. 2018)和三级淋巴结构特征 (TLS) (Cabrita et al. 2020)。

Immunophenoscore是根据与MHC分子、免疫调节剂、效应细胞和抑制细胞有关的基因来计算的。IMPRES是通过免疫检查点基因对的表达的逻辑比较得到的。Roh免疫评分（Roh_IS）是由一组参与与肿瘤排斥有关的免疫激活的基因定义的。趋化因子标签（Chemokine）是基于一组与炎症和免疫有关的基因，它能够预测宿主的免疫反应和肿瘤局部淋巴结构的形成。Davoli免疫特征（Davoli_IS）来自于细胞毒性CD8+T细胞和NK细胞标记物的表达。IFN-γ签名包括能够区分黑色素瘤中的应答者和非应答者的基因。免疫扩展标签（Ayes_expIS）是通过搜索与IFN-γ标签基因高度相关的基因产生的；这个新的集合包括所有免疫相关的基因。T细胞炎症微环境标签（T cell_inflamed）是基于IFN-γ和T细胞相关炎症基因在预测对PD-1阻断反应方面的联合潜力。TIDE是在免疫逃逸特征的基础上开发的，如T细胞功能紊乱或排斥。MSI状态是通过MSI相关基因对的逻辑比较确定的。TLS特征是由有TLS的肿瘤中差异表达的基因得出。压抑的免疫抵抗是通过结合一套与T细胞排斥、治疗后和功能抵抗相关的基因签名来定义的。

```R
hallmarks_of_immune_response <- c("CYT", "Roh_IS", "chemokines", "Davoli_IS", "IFNy", "Ayers_expIS", "Tcell_inflamed", "RIR", "TLS")
immune_response_scores <- compute_scores_immune_response(RNA_tpm = RNA_tpm, 
                                                         selected_scores = hallmarks_of_immune_response)

head(immune_response_scores) 

```

## 4.对TME的特征进行定量

这里是通过quanTIseq方法。该方法通过反卷积算法量化Bulk RNAseq数据中的10种免疫细胞的比例（B cells；Classically-activated (M1) macrophages；Alternatively-activated (M2) macrophages；Monocytes；Neutrophils；Natural killer (NK) cells；Non-regulatory (helper) CD4^+^ T cells；Cytotoxic CD8^+^ T cells；Regulatory CD4^+^ T (Treg) cells；Myeloid dendritic cells；Other uncharacterized cells)。

```R
#quanTIseq
cell_fractions <- compute_cell_fractions(RNA_tpm = RNA_tpm)
```

后续通路算法通过应用PROGENy（Holland、Szalai 和 Saez-Rodriguez 2020；Schubert 等人 2018）方法对来自 RNA-seq 的数据进行计数，可以推断出 14 条信号通路的活性。`pathway_activities` 是一个`data.frame` ，包含每个样本的14条通路的评分。

```R
# 考虑到部分通路相关基因可能被纳入计算免疫反应评分，
# 因此参数remove_sig_genes_immune_response  设置为True， 去除这部分重复基因进行计算，
# 初次使用可以尝试使用效果。
pathway_activities <- compute_pathway_activity(RNA_counts = RNA_counts,
                                               remove_sig_genes_immune_response = TRUE)
```

后续再使用DoRothEA进行转录因子分析，输入参数是TPM ,转录因子总共包含118个。

```R
##====转录因子分析
tf_activities <- compute_TF_activity(RNA_tpm = RNA_tpm)
```

使用源于肿瘤特异性细胞间通讯网络，在接下来的算法中量化了867个配受体对的关联强度。这个部分参考数据是 存储在easierData的intercell_networks和group_lrpairs。intercell_networks里面包含约18种癌症类型的细胞间网络数据和group_lrpairs含56个类型含多个配受体对的list。

```R
#> lrpair_weights 是个data.frame
lrpair_weights <- compute_LR_pairs(RNA_tpm = RNA_tpm,
                                  cancer_type = "pancan")
#> LR signature genes found in data set: 629/644 (97.7%)
#> Ligand-Receptor pair weights computed 
head(lrpair_weights)[,1:5]
```

后续则根据上一步的配受体对分析的结果，量化细胞间的关联强度。

```R
ccpair_scores <- compute_CC_pairs(lrpairs = lrpair_weights, 
                                   cancer_type = "pancan")
head(ccpair_scores) 
```

`cancer_type`的设置取决于`intercell_networks`中有没有这一肿瘤类型。下面是可能`cancer_type`在这个部分可以设定的参数，具体每一种类型需要各自领域的同学去尝试`names(intercell_networks)`。

## 5.预测患者的免疫反应

在前述的定量分析的基础上,predict_immune_response函数根据前期的计算值，初步计算出预测值。

```R
# 这个部分 cancer_type需要特别指定，需要注意的是，前面cancer_type 默认值都是 'pancan'  == ‘泛癌’
# 但在这个部分 'pancan' 却不能作为其中一个参数，而需要特别指定'BRCA'（膀胱癌样本）
predictions <- predict_immune_response(pathways = pathway_activities,
                                       immunecells = cell_fractions,
                                       tfs = tf_activities,
                                       lrpairs = lrpair_weights,
                                       ccpairs = ccpair_scores,
                                       cancer_type = cancer_type, 
                                       verbose = TRUE)
predict_immune_response
```

具体如何评估这个`predictions` 的准确性，作者在后续的说明文档中进一步给出评估：如果已知病人的免疫治疗效果，那么可以判断`predictions` 的准确性，而如果未知免疫治疗效果，则预测的结果无从判断。

## 6.评估EaSIeR的预测

assess_immune_response 这部分的函数 主要就是ROC曲线评估免疫治疗反应，这部分的Gold standard 使用的是compute_scores_immune_response函数计算的结果。TMB 状态和免疫治疗反应关联强度还是要高于其他评分的，部分量化指标比如TFs和LRpairs的AUC都>0.7 ，总体上还是不错的。

```R
output_eval_with_resp <- assess_immune_response(predictions_immune_response = predictions,
                                                patient_response = patient_ICBresponse,
                                                RNA_tpm = RNA_tpm,
                                                TMB_values = TMB,
                                                easier_with_TMB = "weighted_average",
                                                weight_penalty = 0.5)
```

```R
# inspect output
output_eval_with_resp[[1]]
output_eval_with_resp[[2]]
output_eval_with_resp[[3]]
```

在无免疫治疗数据情况下，可以省略函数 assess_immune_response 中的参数 patient_response 来为每个患者分配免疫反应可能性的分数。

```R
output_eval_no_resp <- assess_immune_response(predictions_immune_response = predictions,
                                              TMB_values = TMB,
                                              easier_with_TMB = "weighted_average",
                                              weight_penalty = 0.5)
```

```R
output_eval_no_resp[[1]]
output_eval_no_resp[[2]]
```

## 7.获得免疫反应评分

这部分的函数要求提供对免疫治疗反应的结局的数据。

```R
#获得免疫反应评分
output_biomarkers <- explore_biomarkers(pathways = pathway_activities,
                                        immunecells = cell_fractions,
                                        tfs = tf_activities,
                                        lrpairs = lrpair_weights,
                                        ccpairs = ccpair_scores,
                                        cancer_type = 'BLCA',
                                        patient_response = patient_ICBresponse)
# 输出图片
output_biomarkers[[1]]
output_biomarkers[[2]]
output_biomarkers[[3]]
output_biomarkers[[4]]
output_biomarkers[[5]]
output_biomarkers[[6]]
```

