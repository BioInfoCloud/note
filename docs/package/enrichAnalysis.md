### 富集分析相关函数

#### （1）enrichGO富集结果的可视化

GO_KEGG.enrichVisual_barplot函数用于绘制富集分析的柱状图：
`enrichResult`：一个enrichResult对象，即clusterProfiler::enrichGO的返回结果；

`showCategory`：需要显示的术语（term）条目数，默认为6，如果富集的结果条目数少于设定值，使用富集的结果数目；

`palette` ：绘制图片的调色板，默认"RdPu"；

`axisTitle.x/y`：绘制图像的x/y轴的标题；

`title`：标题；

`save`：逻辑值，表示是否保存图片到本地，如果设置为TRUE，fileName，height，width将会被使用；

`fileName`：一个字符串，表示保存文件的文件名称；

`height/width`：图的高/宽。

```R
GO_KEGG.enrichVisual_barplot(enrichResult,
                             showCategory = 6,
                             palette = "RdPu",
                             axisTitle.x = "Number of Gene",
                             axisTitle.y = "Term",
                             title = "Enrichment barplot",
                             save = FALSE,
                             folder = "./",
                             fileName = "EnrichBar",
                             height = 6,
                             width = 10)
```

#### （2）exeGO_KEGG()一步完成GO和KEGG富集分析

| geneset         | a vector of entrez gene id.                                  |
| --------------- | ------------------------------------------------------------ |
| `OrgDb`         | OrgDb                                                        |
| `keyType`       | keytype of input gene                                        |
| `pvalueCutoff`  | adjusted pvalue cutoff on enrichment tests to report         |
| `pAdjustMethod` | one of "holm", "hochberg", "hommel", "bonferroni", "BH", "BY", "fdr", "none" |
| `qvalueCutoff`  | qvalue cutoff on enrichment tests to report as significant. Tests must pass i) `pvalueCutoff` on unadjusted pvalues, ii) `pvalueCutoff` on adjusted pvalues and iii) `qvalueCutoff` on qvalues to be reported. |
| `minGSSize`     | minimal size of genes annotated by Ontology term for testing. |
| `maxGSSize`     | maximal size of genes annotated for testing                  |
| `readable`      | whether mapping gene ID to gene Name                         |
| KEGG            | 如果执行分析过程中KEGG报错，请将KEGG设置为FALSE。            |
| Prefix          | 一个字符串，输出文件的文件名前缀。                           |
| organism        | KEGG分析时使用                                               |

```R
exeGO_KEGG(geneset,
           keyType = "SYMBOL",
           organism = "hsa",
           showCategory = 6,
           pvalueCutoff = 0.05,
           OrgDb = "org.Hs.eg.db",
           pAdjustMethod = "BH",
           qvalueCutoff = 0.2,
           minGSSize = 10,
           maxGSSize = 500,
           readable = FALSE,
           KEGG = TRUE,
           save = TRUE,
           folder = "./",
           Prefix = "enrich",
           height = 6,
           width = 10)
```

#### （3）GSEA

preRankedGeneList()用于准备排序的基因数据。data通常是差异表达分析的结果。rangeColName指定值的列名，根据该列从大到小排序，每一个值对应的名称由geneColName指定。返回一个排序好的向量。

```
preRankedGeneList(data,geneColName = "symbol",rangeColName = "log2FC")
```

##### GSEA.baseMSIGDB

基于MSIGDB数据库的背景基因集执行GSEA。data可以是差异表达分析好的结果，也可以是已经排序好的有名称的数值型向量。详细参数介绍查看帮助文档。

```R
GSEA.baseMSIGDB (data,
                 geneColName = NULL,
                 rangeColName = NULL,
                 species = "Homo sapiens",
                 collection = "C5",
                 subcollection = "GO:BP",
                 pvalueCutoff = 0.05)
```

collection和subcollection的常用取值对：

```R
collection = "C2"
subcollection = "KEGG_LEGACY"

collection = "C2"
subcollection = "KEGG_MEDICUS"

collection = "C2"
subcollection = "CP:REACTOME"

collection = "C2"
subcollection = "CP:WIKIPATHWAYS"

collection = "C5",
subcollection = "GO:BP"

collection = "C5",
subcollection = "GO:MF"

collection = "C5",
subcollection = "GO:CC"
```

##### GSEA.baseCustomGeneSet 

如果自定义的背景基因集，使用GSEA.baseCustomGeneSet函数。

```R
GSEA.baseCustomGeneSet (data,
                        TERM2GENE,
                        geneColName = NULL,
                        rangeColName = NULL) 
```

##### exe.gseGO_GSEA

该函数包含可视化结果，参数参考前面的函数。

| 参数          | 参数解释                                                     |
| ------------- | ------------------------------------------------------------ |
| data          | 差异分析得到的结果，geneDEAnalysis和arrayDataDEA_limma函数的返回结果 |
| gseGO.ont     | 仅仅执行gseGO时有用，"MF", "CC", "BP"中的一个                |
| OrgDb         | OrgDb，仅仅执行gseGO时有用，org.Hs.eg.db                     |
| TERM2GENE     | "msigdbr",表示使用msigdbr数据库中的数据（基于msigdbr包），也可以是自己自定义的基因集。user input annotation of TERM TO GENE mapping, a data.frame of 2 column with term and gene. Only used when gson is NULL. |
| `species`     | Species name, such as Homo sapiens or Mus musculus. 当TERM2GENE 设置为msigdbr包时有用。 |
| `category`    | MSigDB collection abbreviation, such as H or C1. 当TERM2GENE 设置为msigdbr包时有用。 |
| `subcategory` | MSigDB sub-collection abbreviation, such as CGP or BP. 当TERM2GENE 设置为msigdbr包时有用。 |

```R
exe.gseGO_GSEA(data,
               gseGO.ont = "BP",
               keyType = "SYMBOL",
               OrgDb = org.Hs.eg.db,
               species = "Homo sapiens",
               TERM2GENE = "msigdbr",
               category = "C5",
               subcategory = "BP",
               showCategory = 6,
               pvalueCutoff=0.01,
               fileName = "enrich",
               save = TRUE,
               height =4,
               width = 7,
               folder = "./")
```

##### preVisEnrishResults

obj是富集分析的数据对象enrichResult。通常是clusterProfiler::enrichGO的返回结果。type是"GO"或"KEGG"种的一种。

```
preVisEnrishResults(obj,type,nTerm = 6,p.adjust = 0.05)
```



##### enrichCirBarchar()

Data frame with columns: group, term, count (output from preVisEnrishResults)。

```R
# 
preCirBarchartData(data)
```

