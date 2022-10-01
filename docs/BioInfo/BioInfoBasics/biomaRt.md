![](https://cdn.nlark.com/yuque/0/2020/gif/1234840/1608888587087-e2ea2dbe-b203-4b76-afa3-07276a400ae8.gif#height=76&id=tY3am&originHeight=76&originWidth=640&originalType=binary&ratio=1&size=0&status=done&style=none&width=640)
[**TCGA**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338047035672526848&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**GEO**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1385753371944239106&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**文献阅读**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338481272770953216&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**数据库**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338487030963142656&__biz=MzA4NDAzODkzMA==#wechat_redirect)[** **](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338487030963142656&__biz=MzA4NDAzODkzMA==#wechat_redirect)**| **[**理论知识**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338473418617946113&__biz=MzA4NDAzODkzMA==#wechat_redirect)
[**R语言**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1337050529440104449&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**Bioconductor**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1369789283514761218&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | 服务器与**[**Linux**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1410264757734817793&__biz=MzA4NDAzODkzMA==#wechat_redirect)

---

在之前，我介绍过生物学中常听见的各种ID名称【参考文章：[常用生物信息 ID的介绍](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265423&idx=2&sn=288f3c8acaad8670d35a031cd9794d58&chksm=841efdf2b36974e40e29d906fe4f3a46528ea5a84d17f656ad6119f612059489b9df1416c337&scene=21#wechat_redirect)】，然后介绍了这些ID名称之间的转换。【参考文章：[生信中各种ID转换](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265466&idx=1&sn=021a10503d338e09abe07b578e734566&chksm=841efdc7b36974d13b7ad95e2272d293089d49adff9b74667bbeed78306328f0a42b0259c030&scene=21#wechat_redirect)】，这些转换通常都是基于同一物种而言，但在基础医学研究中，很多实验模型都是在动物上完成的，比如小鼠。假如我们研究某药物的抗肿瘤效果，涉及到机制，最终都会往人上靠的，一般几个基因，数据库直接查一下就可以啦。但如果基因很多，人工查就不太现实，一般也是测序后的数据。所以在这里我给大家介绍一下，不同物种之间的同源基因名称转换，这种转换是基于物种间基因的同源性的。同源基因是由一个共同祖先在不同物种中遗传的基因。虽然同源基因在序列上是相似的，但相似的序列不一定是同源的。
可能常见的转换是小鼠和人之间的转换，因为小鼠的基因和人的基因的同源性
，约80%的小鼠蛋白质在人类基因组中具有严格的1:1种间同源体，其序列同一性通常介于70%~100%。当然跟人类亲缘关系最近的物种是黑猩猩。
好了，我们正式介绍如何把小鼠的gene ID进行同源性映射到人的基因上去？
我们用到的R包是biomaRt包。bioMart包是一个连接bioMart数据库的R语言接口，能通过这个软件包自由连接到bioMart数据库。可以进行各种基因转换。
没有安装过的需要先安装包。
```
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("biomaRt")
library(biomaRt)
```
使用biomaRt包的第一步是选择要使用的BioMart 数据库和数据集。使用useMart函数可以连接到指定的BioMart 数据库和数据库中的数据集。要知道哪些BioMart 数据库是可用的，可以利用listMarts函数查看。
```
> listMarts()
               biomart                version
1 ENSEMBL_MART_ENSEMBL      Ensembl Genes 101
2   ENSEMBL_MART_MOUSE      Mouse strains 101
3     ENSEMBL_MART_SNP  Ensembl Variation 101
4 ENSEMBL_MART_FUNCGEN Ensembl Regulation 101
```
要知道在一个BioMart数据库中哪些数据集是可用的，首先选择使用useMart的BioMart数据库，然后使用listDatasets函数在选定的BioMart，见listDatasets函数。
listDatasets()用于查询当前数据库所含的基因组注释。比如查看人的和鼠的。
```
> listDatasets(human)
                           dataset
1         acalliptera_gene_ensembl
2       acarolinensis_gene_ensembl
3        acchrysaetos_gene_ensembl
4        acitrinellus_gene_ensembl
..........
79             hhucho_gene_ensembl
80           hsapiens_gene_ensembl
...........
```
```
> listDatasets(mouse)
                           dataset
1         acalliptera_gene_ensembl
2       acarolinensis_gene_ensembl
3        acchrysaetos_gene_ensembl
4        acitrinellus_gene_ensembl
...........
105          mmurinus_gene_ensembl
106         mmusculus_gene_ensembl
...........
```
我们后面用到的是hsapiens_gene_ensembl这个数据集。还有小鼠的mmusculus_gene_ensembl数据集。
用useDataseq()函数选定数据库中的基因组。
```
useDataset(dataset,mart, verbose = FALSE)
```
dataset就是要使用的数据集。可能的数据集的列表可以使用listDatasets函数检索，也就是我们上面介绍的。mart是使用useMart函数创建的Mart对象。
```
mart <- useDataset("hsapiens_gene_ensembl", useMart("ensembl"))
```
用lsitFilters()函数查看可选择的类型，选定要获取的注释类型，以及已知注释的类型。
```
> listFilters(mart)
                                     name
1                         chromosome_name
2                                   start
3                                     end
4                              band_start
5                                band_end
6                            marker_start
```
那么我们怎进行同源基因转换呢？按照开始说的，**使用BioMart 包的第一步是选择要使用的BioMart 数据库和数据集**。使用useMart函数可以连接到指定的BioMart 数据库和数据库中的数据集。所以第一步是构建mart对象。
```
human <- useMart('ensembl',dataset = "hsapiens_gene_ensembl")
mouse <- useMart('ensembl',dataset = "mmusculus_gene_ensembl")
```
也就是选择数据库ensembl，数据集是人的hsapiens_gene_ensembl或者小鼠的mmusculus_gene_ensembl。
getLDS函数是biomaRt查询的主要功能，连接两个数据集，并从这些链接的biomaRt数据集检索信息。在Ensembl中，这转化为同源映射。
我这里有一串小鼠基因。mouse.gene
![](https://cdn.nlark.com/yuque/0/2020/png/1234840/1608888587084-c888f886-3bdf-407e-af83-2153813c8839.png#height=207&id=O5nHM&originHeight=207&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
将其映射到人的基因上。
```
m2h.g <- getLDS(attributes = c("mgi_symbol"),filters = "mgi_symbol",
       values = mouse.gene,mart = mouse,
       attributesL = c("hgnc_symbol","chromosome_name","start_position"),
       martL = human,uniqueRows = T)
```
attributes：属性参数：代表我们所要检索的数据集的属性参数，比如这里我们用的是mgi_symbol，代表的就是小鼠的基因的symbol名字。可以使用listAttributes函数检索可能的属性列表。
```
> head(listAttributes(mouse))
                           name                  description         page
1               ensembl_gene_id               Gene stable ID feature_page
2       ensembl_gene_id_version       Gene stable ID version feature_page
3         ensembl_transcript_id         Transcript stable ID feature_page
4 ensembl_transcript_id_version Transcript stable ID version feature_page
5            ensembl_peptide_id            Protein stable ID feature_page
6    ensembl_peptide_id_version    Protein stable ID version feature_page
```
filter：参数过滤器，应在查询中使用的过滤器。这些过滤器将应用于主数据集。可以使用函数listFilters检索可能的过滤器列表。
value：代表我们想要输入的数据集，就是输入我们构造的要查询的向量。
mart ：指的是输入数据的mart对象，由于输入数据是小鼠的基因，自然选择的mart对象为小鼠。
attributesL：代表的是我们需要同源转化的另外一个数据库，这里我们自然是由小鼠转为人，选择的就是需要连接到的人的Mart对象，在属性参数里面我们填写了三个参数，分别是gene_symbol ,染色体位置，基因起始位点。
useMartL：参数是代表我们需要链接的Mart对象，这里自然就是人的。

---

我们查看一下结果：
```
> head(m2h.g)
  MGI.symbol HGNC.symbol Chromosome.scaffold.name Gene.start..bp.
1     mt-Nd1      MT-ND1                       MT            3307
2     Ube2j2      UBE2J2                        1         1253909
3   Aurkaip1    AURKAIP1                        1         1373730
4     mt-Nd5      MT-ND5                       MT           12337
5       Agrn        AGRN                        1         1020120
6     mt-Co3      MT-CO3                       MT            9207
```
这样我们就完成了转换。可以看的出来，人的基因和小鼠的基因名称就是大小写的区别（大多数，不是全部）。
最后额外介绍一下用getBM()函数获取注释。给定一组过滤器和相应的值，它从连接到的BioMart数据库中检索用户指定的属性。
```
ensg <- c("ENSG00000242268","ENSG00000270112",
  "ENSG00000167578","ENSG00000273842",
  "ENSG00000078237","ENSG00000146083",
  "ENSG00000225275","ENSG00000158486",
  "ENSG00000198242","ENSG00000259883",
  "ENSG00000231981","ENSG00000269475")
```
```
hg_symbols<- getBM(attributes=c('ensembl_gene_id','hgnc_symbol',"chromosome_name", "start_position","end_position", "band"), filters= 'ensembl_gene_id', values = ensg, mart = mart)
```
![](https://cdn.nlark.com/yuque/0/2020/png/1234840/1608888587171-17a052c4-8601-46b0-b2b6-be70d87187e1.png#height=405&id=yomTq&originHeight=405&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
这也达到的注释的目的。
**更多功能，参考官方文档。**

---

参考：
[http://www.bioconductor.org/packages/release/bioc/html/biomaRt.html](http://www.bioconductor.org/packages/release/bioc/html/biomaRt.html)
本公众号文章目录：[https://www.yuque.com/doublehelix/mbictitles/dmiy4u](https://www.yuque.com/doublehelix/mbictitles/dmiy4u)
![](https://cdn.nlark.com/yuque/0/2020/jpeg/1234840/1608888587131-861c6a16-5c10-49bf-b135-9c969ee7e39c.jpeg#height=720&id=k2K3k&originHeight=720&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
