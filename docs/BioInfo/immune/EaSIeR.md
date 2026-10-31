---
title: EaSIeR
---

# EaSIeR

## 1.EaSIeR包介绍及安装

恶性肿瘤细胞可通过多种方式干扰肿瘤微环境的免疫细胞以减弱对肿瘤细胞的杀伤作用并诱导免疫细胞免疫耐受。而肿瘤微环境固有的复杂性，多细胞的动态特性，对获取免疫反应生物标志物和预测免疫治疗效果提出了巨大挑战。因此，作者期望使用 bulk RNA-seq数据与不同的先验知识来源（肿瘤浸润细胞，细胞内信号传导，TFs活性,细胞间通讯强弱）相结合，以得出基于系统的肿瘤微环境特征，量化免疫细胞组成以及细胞内和细胞间的通讯。作者通过将多任务学习应用于这些特征，预测免疫反应的不同特征，并基于可解释的Biomarker推导出癌症类型特异性模型。并将该模型应用于来自接受 PD-1/PD-L1 抑制剂治疗的癌症患者的独立 RNA-seq 数据，以证明EaSIeR 的方法可以准确预测治疗结果。

EaSIeR 存储在Biocondoctor， 可以使用BiocManager 下载安装。

## 2.EaSIeR 示例数据

IMvigor210CoreBiologies包，文献PMCID: PMC6028240，数据包含RNA-seq 数据（Count和 TPM）、肿瘤突变负荷 (TMB) 信息和 192 名患者对 ICB 治疗的反应结果。CR, complete response; PD, progressive disease; PR, partial response; SD, stable disease。其中（完全缓解 (CR) 的 25 名：R；疾病进展 (PD) 的 167 名：NR）

官方指导手册：[TGF-b attenuates tumor response to PD-L1 blockade by contributing to exclusion of T cells (gene.com)](http://research-pub.gene.com/IMvigor210CoreBiologies/)

指导手册中IMvigor210CoreBiologies包下载地址失效，可以从我[百度网盘下载](https://pan.baidu.com/s/1eFxcfSmQccrd3y5rHSnikA?)

下载后参照官方指导手册安装。

查看数据：

获取基因表达数据

## 3. 计算免疫反应的Hallmarks

作者利用TPM数据计算下列免疫特征的评分：溶细胞活性 (CYT) (Rooney et al. 2015)、Roh 免疫评分 (Roh_IS) (Roh et al. 2017)、趋化因子特征 (chemokines) (Messina et al. . 2012) , Davoli 免疫特征 (Davoli_IS) (Davoli et al. 2017) , IFNy 特征 (IFNy) (McClanahan 2017) , 扩展免疫特征 (Ayers_expIS) (McClanahan 2017) , T 细胞炎症特征 (Tcell_inflamed) (McClanahan 2017 ) )、免疫抵抗程序（RIR：resF_down、resF_up、resF）(Jerby-Arnon et al. 2018)和三级淋巴结构特征 (TLS) (Cabrita et al. 2020)。

Immunophenoscore是根据与MHC分子、免疫调节剂、效应细胞和抑制细胞有关的基因来计算的。IMPRES是通过免疫检查点基因对的表达的逻辑比较得到的。Roh免疫评分（Roh_IS）是由一组参与与肿瘤排斥有关的免疫激活的基因定义的。趋化因子标签（Chemokine）是基于一组与炎症和免疫有关的基因，它能够预测宿主的免疫反应和肿瘤局部淋巴结构的形成。Davoli免疫特征（Davoli_IS）来自于细胞毒性CD8+T细胞和NK细胞标记物的表达。IFN-γ签名包括能够区分黑色素瘤中的应答者和非应答者的基因。免疫扩展标签（Ayes_expIS）是通过搜索与IFN-γ标签基因高度相关的基因产生的；这个新的集合包括所有免疫相关的基因。T细胞炎症微环境标签（T cell_inflamed）是基于IFN-γ和T细胞相关炎症基因在预测对PD-1阻断反应方面的联合潜力。TIDE是在免疫逃逸特征的基础上开发的，如T细胞功能紊乱或排斥。MSI状态是通过MSI相关基因对的逻辑比较确定的。TLS特征是由有TLS的肿瘤中差异表达的基因得出。压抑的免疫抵抗是通过结合一套与T细胞排斥、治疗后和功能抵抗相关的基因签名来定义的。

## 4.对TME的特征进行定量

这里是通过quanTIseq方法。该方法通过反卷积算法量化Bulk RNAseq数据中的10种免疫细胞的比例（B cells；Classically-activated (M1) macrophages；Alternatively-activated (M2) macrophages；Monocytes；Neutrophils；Natural killer (NK) cells；Non-regulatory (helper) CD4^+^ T cells；Cytotoxic CD8^+^ T cells；Regulatory CD4^+^ T (Treg) cells；Myeloid dendritic cells；Other uncharacterized cells)。

后续通路算法通过应用PROGENy（Holland、Szalai 和 Saez-Rodriguez 2020；Schubert 等人 2018）方法对来自 RNA-seq 的数据进行计数，可以推断出 14 条信号通路的活性。`pathway_activities` 是一个`data.frame` ，包含每个样本的14条通路的评分。

后续再使用DoRothEA进行转录因子分析，输入参数是TPM ,转录因子总共包含118个。

使用源于肿瘤特异性细胞间通讯网络，在接下来的算法中量化了867个配受体对的关联强度。这个部分参考数据是 存储在easierData的intercell_networks和group_lrpairs。intercell_networks里面包含约18种癌症类型的细胞间网络数据和group_lrpairs含56个类型含多个配受体对的list。

后续则根据上一步的配受体对分析的结果，量化细胞间的关联强度。

`cancer_type`的设置取决于`intercell_networks`中有没有这一肿瘤类型。下面是可能`cancer_type`在这个部分可以设定的参数，具体每一种类型需要各自领域的同学去尝试`names(intercell_networks)`。

## 5.预测患者的免疫反应

在前述的定量分析的基础上,predict_immune_response函数根据前期的计算值，初步计算出预测值。

具体如何评估这个`predictions` 的准确性，作者在后续的说明文档中进一步给出评估：如果已知病人的免疫治疗效果，那么可以判断`predictions` 的准确性，而如果未知免疫治疗效果，则预测的结果无从判断。

## 6.评估EaSIeR的预测

assess_immune_response 这部分的函数 主要就是ROC曲线评估免疫治疗反应，这部分的Gold standard 使用的是compute_scores_immune_response函数计算的结果。TMB 状态和免疫治疗反应关联强度还是要高于其他评分的，部分量化指标比如TFs和LRpairs的AUC都>0.7 ，总体上还是不错的。

在无免疫治疗数据情况下，可以省略函数 assess_immune_response 中的参数 patient_response 来为每个患者分配免疫反应可能性的分数。

## 7.获得免疫反应评分

这部分的函数要求提供对免疫治疗反应的结局的数据。
