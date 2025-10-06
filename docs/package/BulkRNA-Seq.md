## Bulk RNA-Seq基础分析

### 差异表达分析

data为表达数据，行为基因名称，列为样本名称，group是一个数据框，只有一列为group的值，其值是二分类的字符串标签（如：Tumor，Normal），行名为样本名称，其顺序与data的列名一致。comparison是一个由group中的二分类标签值用-链接，如"Tumor-Normal"，表示Tumor组与Normal进行差异表达分析。method是DESeq2, edgeR和 limma中的一种，RNAseq数据建议使用DESeq2或edgeR，芯片数据使用limma。filter是否过滤低表达的基因，默认为FALSE。**注意：该函数值适合count数据**。

```R
DEG <- geneDEAnalysis(data, group, comparison,method = "DESeq2",filter = TRUE)
```

**标准化后的芯片数据可用arrayDataDEA_limma函数**：

 group是一个长度和data列数一样的向量，其中每一个元素值应该对应样本的分组，且唯一值只有2种，comparison同上。

```R
comparison = "Liver_Metastasis-Primary" # 必须在函数外定义
DEG = arrayDataDEA_limma(data = Liver_M_vs_Primary,
                         group = rep(c("Liver_Metastasis","Primary"),
                                     times = c(length(LiverID),length(PrimaryID))),
                         comparison = comparison
                         )
```

筛选差异表达基因的函数`selectDEG `。

```R
selectDEG(DEAR, cutFC = 1, pMethod = "FDR", cutP = 0.05)
```

- `DEAR`：为数据框（data.frame）类型，需传入差异表达分析结果数据，且必须包含两列关键信息 —— 一列是由 `pMethod` 指定的统计检验指标列（如 "FDR"、"pAdj" 或 "pValue" 列），另一列固定为 "log2FC" 列（存储基因表达的 log2 倍变化值），是后续筛选的基础数据来源；
- `cutFC`：为数值类型，用于设定差异表达基因在表达幅度上的筛选阈值，默认值为 1，实际筛选时会以 “`abs(log2FC) ≥ cutFC`” 作为判断基因表达幅度是否达标的条件；
- `pMethod`：为字符类型，用于指定筛选差异基因时采用的统计检验指标，仅允许传入 "FDR"（错误发现率）、"pAdj"（校正后 P 值）或 "pValue"（原始 P 值）三者之一，默认值为 "FDR"，决定后续显著性判断的依据列；
- `cutP`：为数值类型，用于设定统计显著性的筛选阈值，默认值为 0.05，实际筛选时会以 “`pMethod 指定列的值 < cutP`” 作为判断基因表达差异是否具有统计显著性的条件。

### 2. 火山图可视化

plotDEGvolcanoFig函数用于差异表达分析的火山图可视化，该函数在进行绘制前，差异分析需要进行一些处理。

```R
plotDEGvolcanoFig <- function(data,x,y,cut_pvalue,cutFC,title,group,colour,label)
```

data是差异分析的结果，x是x轴的列（log2FC）,y轴是p-value/FDR，cut_pvalue是显著性的截断值，cutFC是log2FC绝对值的绝对值。title是标题，group是分组所在的列，colour是颜色，长度应该以group的唯一值相同，label是需要显示的基因名所在的列。