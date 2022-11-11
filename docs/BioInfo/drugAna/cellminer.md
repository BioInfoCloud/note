

> 作者：DoubleHelix
>
> 微信公众号：生物信息云

**CellMiner数据库，主要是通过国家癌症研究所癌症研究中心(NCI)所列出的60种癌细胞为基础而建立的。该数据库最初发表于2009年，后于2012年在Cancer Research杂志上进行了更新，题目为“CellMiner: a web-based suite of genomic and pharmacologic tools to explore transcript and drug patterns in the NCI-60 cell line set”。大家后期在使用该数据库记得应用相关文献。**

数据库地址：[CellMiner - Analysis Tools | Genomics and Pharmacology Facility (nih.gov)](https://discover.nci.nih.gov/cellminer/)

## 1.数据下载





## 2.读入药物数据

```R

library(readxl)
rt1 <- read_excel(path = "DTP_NCI60_ZSCORE.xls", skip = 7)
```

