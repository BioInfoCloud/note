```
Choi, JH., Lee, BS., Jang, J.Y. et al. Single-cell transcriptome profiling of the stepwise progression of head and neck cancer. Nat Commun 14, 1055 (2023). https://doi.org/10.1038/s41467-023-36691-x
```

头颈部鳞状细胞癌 (HNSCC) 是第六大最常见的癌症类型，包括口腔癌、咽癌和喉癌。头颈部鳞癌诊治水平稳步提高；然而，晚期 HNSCC 的 5 年生存率仍然不利，约为 50-60%。以前，大规模基因组分析研究，如癌症基因组图谱 (TCGA)，已经证明了 HNSCC 的分子异质性，为 HNSCC 进展的病理生物学提供了新的见解。然而，对大块组织的研究在区分肿瘤微环境细胞（如免疫细胞和基质细胞）对癌症进展的影响方面非常有限。单细胞RNA-seq（scRNA-seq）技术的最新进展使得有可能克服这些限制，区分单细胞水平上基因表达的变化，并为肿瘤组织中不同细胞类型之间的相互作用提供新的见解。

HNSCC 经历了从正常组织 (NL) 到癌前白斑 (LP) 的逐步进展，然后是原发性癌症 (CA)，最终是淋巴结 (LN) 中的转移性肿瘤。LP 以不同的速度发展为恶性肿瘤；因此，人们努力根据 LP 进展率来预测癌前病变的恶性进展。然而，LP 恶性转化的分子机制仍不清楚。此外，HNSCC 的发展涉及多种病因，包括接触酒精或烟草以及人乳头瘤病毒 (HPV) 感染。特别是，HPV 感染在 HNSCC 进展中起着关键作用，与 HPV 阴性患者相比，HPV 阳性患者的预后更佳。基因组分析还表明，先天性和获得性抗病毒免疫反应在 HPV 阳性患者中受到抑制。

在这项研究中，我们对非肿瘤周围的NL、LP、CA和LN组织进行scRNA-seq谱分析，以描绘单细胞水平的改变和细胞间相互作用，这有助于HNSCC从非肿瘤性病变逐步发展为转移性肿瘤。考虑到HPV的机械和临床影响，我们根据HPV感染状态仔细分析单细胞转录物。我们证明了HNSCC进展过程中细胞组成的逐步变化，识别了恶性细胞、间质细胞和免疫细胞的细胞簇。我们的结果揭示了肿瘤细胞与其微环境之间的细胞间相互作用，为HNSCC提供了关键的机制和临床见解。

## 结果1：HNSCC 逐步进展的 scRNA-seq 分析

从23例HNSCC患者中获得scRNA-seq谱，包括NL的组织类型（n = 9） ，LP（n = 4） ，CA（n = 20） 和LN（n = 4） （图1a和补充表1）。共有54239个细胞聚集成16个簇，根据已知细胞类型标记基因的差异表达将其分为9种细胞类型，包括上皮细胞、成纤维细胞、内皮细胞、肌细胞、免疫NK/T细胞、B/浆细胞、巨噬细胞、树突状细胞和肥大细胞（图1b和补充图1a）。细胞簇与组织类型、HPV感染状态和患者样本有关（图1c）。HPV阳性患者的LP组织不可用；因此，他们被排除在分析之外。当根据HPV感染状态评估细胞组成时，与HPV阴性肿瘤相比，HPV阳性肿瘤中的成纤维细胞比例较低（11.49%对1.02%），但NK/T细胞（48.50%对25.05%）和B/浆细胞比例较高（22.79%对13.87%）（图1d和补充图1b）。这一发现与先前的研究一致，表明HPV阳性肿瘤中免疫细胞的功能改变。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303151731554.png)

## 结果2：LP 组织中 TP63 和 ATP1B3 的 DNA 拷贝数依赖性失调

接下来，我们使用infreCNV方法推断了重复性DNA拷贝数畸变（CNAs），并进行了改进，排除了共表达功能基因簇和非重复性畸变的影响。CA和LN组织的上皮细胞表现出深刻的CNA，但没有表现出其他基质细胞（补充图2a）。与之前的研究12、13一致，HPV阴性肿瘤显示出比HPV阳性肿瘤更高的DNA拷贝增益（每个细胞中具有CNA的基因的平均数量=245.2对111.7，P < 3.0×10–16，图2a）。在LP组织中，我们观察到80个上皮细胞含有类似于恶性细胞的CNA，我们将其命名为原位癌（CIS）细胞。比较HPV阴性患者的NL和LP组织之间的CNA，CIS细胞在1q、3q、8q、20p和22q处显示出显著的DNA拷贝增加，在3p、10p和10q处显示了丢失，证实了先前的发现14（图2b）。CIS细胞开始表达TNF-α/NF-kB、凋亡、P53、雌激素反应、缺氧、PI3K/AKT/mTOR和糖酵解相关基因，并且在恶性细胞中进一步加重（图2c）。基因水平分析显示，与上皮细胞相比，CIS表达了已知的肿瘤标记基因[例如，CXCL1、EFNA1、TM4SF1、ELF3和角蛋白细胞骨架基因（即，KRT19、KRT13、KRT18和KRT8）]，表明其恶性特征15、16、17（倍差>1，置换学生t检验P < 0.0001，图2d）。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303151732048.png)

此前，CNA依赖性转录调控障碍被认为在癌症进展中起驱动作用。考虑到这一点，我们鉴定了CNA依赖性基因，这些基因在不同组织类型（n = 8，排列学生t检验P < 0.001，折叠差>1，补充图2b，参见补充方法）。染色体3q上的TP63和ATP1B3在HPV阴性的CIS细胞中表现出最显著的CNA依赖性转录调控（图2e）。我们可以在HPV阴性TCGA-HNSCC数据中验证这一结果，表明CNAs与TP63转录水平之间存在显著相关性（r = 0.19，P = 2.5×10^-3^）和ATP1B3（r = 0.37，P = 2.0×10^–9^）（图2f）。这些基因的致癌活性已在各种癌症类型中显示，这可以通过执行siRNA-介导的敲除实验进行验证。用靶向TP63（siTP63）或ATP1B3（siATP1B3）的siRNA治疗显著抑制了HNSCC细胞的促肿瘤功能，包括细胞活力、肿瘤球形成、迁移和侵袭（图2g，h，I和补充图3）。这些结果一致支持癌前LP病变中TP63和ATP1B3的CNA依赖性表达在HNSCC的进展中起关键作用。

## 结果3：恶性细胞簇 CC1 具有侵袭性表型

接下来，我们将CA和LN组织中的上皮细胞指定为恶性细胞（n = 5,113)。为了评估转录异质性，将恶性细胞分为六个簇（CC0至CC5，图3a，顶部，见补充方法）。我们观察到，每对匹配的原发性和转移性肿瘤（CA和LN）聚集在一起，如前所示21（图3a，底部）。此外，我们观察到，转移肿瘤的恶性细胞簇的细胞组成与配对的原发性肿瘤的细胞组成非常相似，表明在分级聚类分析中，每对原发性和转移性肿瘤都聚集在一起（图3b）。这一结果表明，原发性肿瘤的转录多样性在转移性肿瘤中是保守的。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303151735801.png)

接下来，我们进行去卷积分析，以评估TCGA-HNSCC（n = 500，补充方法）。与scRNA-seq数据不同，反褶积分析表明，恶性细胞是最丰富的细胞类型（79.17%），其次是成纤维细胞（10.07%）（补充图4a）。在恶性细胞中，CC0和CC1是最丰富的恶性细胞簇（图3c）。在GSE41613（n = 97），GSE42743（n = 74）和GSE65858（n = 270），证明了我们结果的鲁棒性（补充图4b）。有趣的是，我们发现根据HPV感染状态，恶性细胞簇被紧密定位（图3d，顶部）。CC0和CC4细胞主要是HPV阳性肿瘤，而其他簇是HPV阴性肿瘤（图3d，底部）。这一发现表明，我们的恶性细胞簇具有与HPV感染相关的不同转录组程序。此外，肿瘤消退（如口咽和口腔）已被证明与HPV感染状态有关；然而，我们无法观察到恶性细胞簇和肿瘤消退之间的显著关联（图3e）。

我们还评估了我们的恶性细胞簇是否可以在独立的scRNA-seq数据集中找到。使用最近模板预测（NTP）分析对恶性细胞进行亚型可以分别在GSE103322（77.16%）和GSE164690（99.10%）中重新识别我们的恶性细胞簇（补充图5）；然而，我们的细胞亚型并没有涵盖恶性细胞的所有异质性，这可能是由于采样的患者数量较少。这可能支持我们的恶性细胞簇代表HNSCC中的大多数恶性细胞类型。此外，我们检查了HNSCC先前的单细胞恶性细胞程序在每个恶性细胞群中的表达。CC0表达缺氧和上皮分化相关基因，而CC1表达部分上皮间质转化（p-EMT）相关基因（图3f）。有人建议p-EMT定位于癌相关成纤维细胞（CAFs）的前沿，并通过CAFs和恶性细胞之间的旁分泌相互作用促进，导致HNSCC的侵袭性进展。支持这一点，我们可以证明，与CC1低水平组相比，CC1高水平组（大于CC1的70%）的总体生存率（OS；危险比[HR] = 1.38，P = 0.02）和无复发生存率（RFS；HR = 1.69，P = 0.006），尽管其他恶性细胞簇没有（图3g，顶部）。这一发现可以使用GSE41613（OS，HR）的独立数据集进行验证 = 2.30磅 = 0.003）和GSE42743（OS，HR = 第2.16页 = 0.016）（图3g，底部）。多变量分析还揭示了CC1与HNSCC预后不良的相关性（GSE41613，OS，HR = 2.68，P = 0.001; GSE42743，操作系统，小时 = 2.33，P = 0.011，补充表2）。总之，我们认为CC1的丰度与获得侵袭性表型的HPV阴性肿瘤样特征的表达有关。

接下来，我们确定了可能代表每个聚类的差异表达基因（Wilcoxon秩和检验P < 0.001，折叠差>1，补充图6）。我们发现CC1显著表达LGALS7B（图3h），这可以通过在CC1高样本（即C04、C30、C51、C26、C07、C06、C31和C15）中显示LGALS7B的表达来验证，但在CC1低样本（C38和C09）中没有（图3i和补充图7）。半乳糖凝集素-7在多种癌症类型中具有促癌作用，包括HNSCC25,26,27，因此，CC1的侵袭性特征可能与p-EMT和LGALS7B的表达有关。

## 结果4：恶性细胞中成纤维细胞来源的COL1A1表达与CD44相互作用

成纤维细胞是反褶积分析中第二常见的细胞类型（参见补充图4a）。我们可以在每种细胞类型的上皮/恶性细胞（n = 17，例如KRT6A）和成纤维细胞（n = 41，例如，POSTN）（补充图8），这可以通过伪时间轨迹分析28（图4a）更清楚地证明。有趣的是，我们观察到LP的伪时间更接近CA或LN，而不是NL，这可能表明癌前LP成纤维细胞已经获得了CAF样特征（图4b）。为了进一步阐明成纤维细胞转录改变对癌症进展的影响，我们分析了成纤维细胞和恶性细胞之间的配体受体（LR）相互作用（有关详细信息，请参阅补充方法）。我们旨在鉴定恶性细胞和成纤维细胞之间相互依赖的LR对，它们在恶性细胞中表现出受体表达，但其相应的配体仅在成纤维细胞中表达，而在恶性细胞内不表达。我们可以鉴定七对LR，它们显示配体在成纤维细胞中的相互依赖和逐步表达（即COL1A1、COL1A2、COL6A3、THBS1、THBS2、TNC和LAMA4），以及它们在恶性细胞中的相应推定受体（即CD44、ITGB1、SDC4、CD47和ITGA6，图4c）。值得注意的是，COL1A1-CD44配体-受体对显示出最显著和最相互依赖的表达（图4d，顶部），这可以通过Puram的scRNA-seq数据进行验证（图4d，底部）。此外，COL1A1表达与成纤维细胞的假时间最显著相关（r = 0.57，P < 2.2 × 10^−16^，补充图9a）。我们可以成功地证明成纤维细胞中COL1A1和上皮细胞中CD44的相关表达（r = 0.43，P = 7.47 × 10^−3^，图4e和补充图9b）。然而，成纤维细胞中CD44的表达与COL1A1的表达无关（补充图9c）。这些结果表明CD44-COL1A1相互作用发生在成纤维细胞和恶性细胞之间，但不是以自分泌的方式发生。免疫组织化学分析还表明，在表达CD44的恶性细胞附近的成纤维细胞中，COL1A1表达显著（图4f和补充图9d）。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303151740105.png)

此外，我们通过对COL1A1（siCOL1A1）和CD44（siCD44）进行siRNA介导的敲除实验来评估COL1A1-CD44相互作用的功能。选择了两个表达CD44的HNSCC细胞系（MSKQLL1和SCCQLL1，补充图10a）和表达COL1A1的CAF（CAF48）（补充图10b）。我们观察到，用胶原（I型）治疗诱导了肿瘤细胞的侵袭，并被siCD44转染所消除（图4g）。此外，MSKQLL1和CAF48的共培养增强了肿瘤细胞的迁移，但不影响siCD44转染的MSKQLL2细胞与CAF48或MSKQL1细胞与siCOL1A1转染的CAF48细胞的共培养（图4h）。总之，我们认为成纤维细胞中的COL1A1和CD44上皮/恶性细胞相互依赖，促进肿瘤进展。

## 结果5：表达 CXCL8 的 CAF 会加重 HNSCC 的进展

来自肿瘤组织（CA和LN）的CAF进一步分层为五个簇（CF0至CF4），揭示了它们的代表性标记基因（图5a和补充图11a）。当在Puram的研究21中将CAF簇与之前的CAF进行比较时，CF0和CF4与表达其标记基因的Puram亚型CAF1相似（例如，CTHRC1、COL1A1、COL3A1、POSTN和MFAP2，图5b）。然而，CF4与CF0不同，显示出更高的增殖活性（补充图11b）。CF2和CF3与Puram的CAF2和肌成纤维细胞相似，表达CXCL12和NDUFA4L2等标记基因。有趣的是，我们发现了一种CAF亚型CF1，表达CXCL8（IL-8编码基因）。在二维扩散图嵌入分析29中，CF1显示出不同于其他CAF簇的独特表达模式（图5c，左侧）。伪时间投影分析还显示CF1是最后的轨迹，这意味着CF1是进展最快的成纤维细胞（图5c，右）。此外，我们证明，在TCGA-HNSCC的独立数据集中，CF1的丰度与CXCL8的表达水平显著相关（r = 0.38，P = 2.72 × 10−18）、GSE41613（r = 0.74，P = 3.41 × 10−18），GSE42743（r = 0.62，P = 3.54 × 10−9）和GSE65858（r = 0.68，P = 9.58 × 10−38，图5d）。当我们根据HPV感染状况比较CAF亚型的比例时，大多数CF1细胞在HPV阴性肿瘤中观察到，但在HPV阳性肿瘤中观察不到（P = 1.33 × 10−7，补充图11c，左侧）。TCGA数据还显示，HPV阴性肿瘤中CF1细胞（10.15%）比HPV阳性肿瘤（5.04%）更丰富（P = 5.26 × 10−7，补充图11c，右侧）。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303151743247.png)

接下来，我们评估了CF1和CC1的丰度是否相互关联，因为CF1和CC1的丰度都具有攻击性特征。正如预期的，CC1和CF1丰度在汇总的HNSCC数据中显著相关（r = 0.41，P = 1.11 × 10−38，图5e），暗示CF1和CC1可能相互作用。事实上，galectin-7（在CC1中表达）可促进各种癌症类型的转移，包括HNSCC30。IL-8（在CF1中表达）由促进肿瘤进展的多种细胞类型产生31、32。为了评估这一假设，我们证明galectin-7处理显著诱导了各种CAF细胞（CAF30、CAF57、CAF58和CAF70）以及HNSCC细胞（SCCQLL1和SNU1066）中CXCL8的表达（图5f）。相比之下，IL-8处理没有在HNSCC细胞中诱导galectin-7。（补充图12）。这些结果表明galectin-7激活恶性细胞（CC1）和成纤维细胞（CF1）以表达IL-8，促进HNSCC的侵袭性进展。

## 结果6：Treg 细胞中的 LAIR2 表达与 HNSCC 进展相关

在免疫细胞中，NK/T细胞是scRNA-seq数据中最常见的细胞类型。染色体畸变的细胞被重新分配为未确定的细胞类型，并在以下分析中排除（见“方法”）。然后，将NK/T细胞簇进一步分层为六个亚簇；幼稚T细胞、CD8+CCL5+、CD4+FOXP3+（调节性T细胞，Treg）、CD4+CD154+（滤泡辅助性T细胞）、循环T细胞和NK细胞（图6a，顶部）。显示较高增殖活性的T细胞簇被指定为循环T细胞，显示CD8编码基因（即CD8A和CD8B）的表达高于CD4，如前所述33（图6a，底部和补充图13a）。在HNSCC进展过程中，循环T细胞和CD4+T细胞的比例增加，而幼稚T细胞和CD8+T细胞比例减少，无论其HPV感染状态如何（图6b）。伪时间轨迹分析证明了T细胞根据组织类型的逐步转变（图6c）。值得注意的是，LP中的Tregs表现出两个伪时间分布峰值，表明癌前病变中T细胞状态的改变。特别是，我们观察到LP中Tregs中白细胞相关免疫球蛋白样受体2（LAIR2，CD306）的显著表达（置换学生t检验P = 2.50 × 10^−9^，fold difference=2.32，图6d和补充图13b）。尽管LAIR2的功能在很大程度上是未知的，但LAIR2被认为是激活促炎过程的可溶性胶原受体34。因此，成纤维细胞中COL1A1的表达可能激活Tregs中LAIR2介导的下游信号传导。为了支持这一点，我们观察到成纤维细胞中COL1A1表达水平较弱，但与LAIR2表达水平显著相关（r = 0.48，P = 2.48 × 10−3）和Tregs的丰度（r = 0.38，P = 2.60 × 10^−2^，图6e）。此外，我们证明胶原处理显著诱导小鼠Tregs中FOXP3的表达（图6f和方法）。此外，通过进行荧光活化细胞分选（FACS）分析，我们证实胶原处理增加了HNSCC患者PBMC中获得的FOXP3+CD25+Treg和LAIR2+FOXP3+CD 25+Treg的数量（图6g，h和补充图13c，和“方法”）。总之，我们认为来自成纤维细胞的胶原与Tregs相互作用，诱导LAIR2和FOXP3表达，并为肿瘤进展提供有利的微环境。

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202303151746464.png)

## 数据集：

The raw and processed data generated in this study have been deposited in the database under accession code [GSE181919](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE181919). The processed single-cell datasets and bulk transcriptome profiles of HNSCC used in the study are obtained from: Puram(https://www.nature.com/articles/s41467-023-36691-x#ref-CR21) (scRNA-seq, [GSE103322](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE103322)), Kurten(https://www.nature.com/articles/s41467-023-36691-x#ref-CR42) (scRNA-seq, [GSE164690](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE164690)), Lohavanichbutr(https://www.nature.com/articles/s41467-023-36691-x#ref-CR22) (Microarray, [GSE41613](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE41613) and [GSE42743](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE42743)), Wichmann 23 (Microarray, [GSE65858](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE65858)), and TCGA-HNSCC (RNA-Seq, https://portal.gdc.cancer.gov/). [Source data](https://www.nature.com/articles/s41467-023-36691-x#Sec22) are provided with this paper.

标记基因和分析方法看[这里](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-023-36691-x/MediaObjects/41467_2023_36691_MOESM1_ESM.pdf)。

Cell typing was performed by manually examining the expression levels of the canonical marker genes for malignant cells (KRT14, KRT17, KRT6A, KRT5, KRT19, KRT8, KRT16, KRT18, KRT6B, KRT15, KRT6C, KRTCAP3, EPCAM, SFN), fibroblasts (FAP, PDPN, COL1A2, DCN, COL3A1, COL6A1), myocytes (ACTA1, ACTN2, MYL2, MYH2), T cells (CD2, CD3D, CD3E, CD3G), B/Plasma cells (SLAMF7, CD79A, BLNK, FCRL5), macrophages (CD14, CD163, CD68, FCGR2A, CSF1R), dendritic cells (CD40, CD80, CD83, CCR7), mast cells (CMA1, MS4A2, TPSAB1, TPSB2) and endothelial cells (PECAM1, VWF, ENG). Deconvolution of the bulk RNA-Seq data s was performed using “MuSiC” R package.