我们做转录组分析，得到的数据通常是raw counts 的数据，raw counts 的数据有很多R包进行归一化。在TCGA数据库中下载的RNA-Seq的数据就有2种形式，raw counts 和FPKM，**尽管有很多文章是直接利用FPKM进行分析的**，但是FPKM存在不准确性，通常我们会使用TPM。关于什么是FPKM？什么是TPM？我在前面的文章中就有介绍：[**RNA-seq的counts,RPM, RPKM, FPK值到底有什么区别？**](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264575&idx=2&sn=69b45012dbfe61d7574446de00ec9a7b&chksm=841ef242b3697b54484a64f82bba4372a8fb2b4d411b1c1fc2bc68d12aa44756f96c3b8e48f5&scene=21#wechat_redirect)。这里再简单回归一下：
**count：**原始测序得到的count数就是比对到某个基因i上的总数目；不知道大家是否了解测序的简单过程？在测序分析过程中，我们首先是将测得的短reads比对到参考基因组上，然后通过软件来计算该片段上比对到reads的数量，也就是说呢，count是一个整数值。
**FPKM：**我们把比对到的某个基因i的Fragment数目，除以基因的长度，其比值再除以所有基因的总长度。注意，严格来讲，这里的基因长度是指基因i外显子的总长度。
**TPM：**与FPKM不同的地方在于，其基因的比值是再除以（基因的总数目/基因的总长度）。因此，其得到的结果是一个相对的比值。
如果从原始的下机数据开始分析，那就根据自己需要进行转换，但通常我们大多数拿到的是raw counts数据，一般送测序，也会要求返回raw counts的数据，从数据库下载的数据我们通常也是选择raw counts数据或者FPKM的数据。那么我们如何将这些数据进行转换成TPM的数据呢？read count和FPKM结果都可以转成TPM，但是因为FPKM跟TPM的计算都考虑了基因长度，所以从FPKM转TPM最方便快捷。只需要按照下面公式就可以计算：
具体可参考前面的文章：[**RNA-seq的counts,RPM, RPKM, FPK值到底有什么区别？**](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264575&idx=2&sn=69b45012dbfe61d7574446de00ec9a7b&chksm=841ef242b3697b54484a64f82bba4372a8fb2b4d411b1c1fc2bc68d12aa44756f96c3b8e48f5&scene=21#wechat_redirect)，这里提供的是R代码。
首先我们得有FPKM的数据，这里我以之前TCGA数据库的数据为例。
链接：[https://pan.baidu.com/s/1rsRPgcdB9tCK7oGRWQLxYw](https://pan.baidu.com/s/1rsRPgcdB9tCK7oGRWQLxYw)  提取码：molg 
```r
load("F:/TCGA/HTSeq-FPKM/Rdata/data/TCGA-COAD-Exp.Rdata")
exp <- transomeData[["proteinCodingExpData"]][["Exp"]]
```
之前上传的数据是字符串，需要转换成数值。
```r
library(dplyr)
exp <- exp %>% data.matrix() %>% as.data.frame()
head(exp)[,1:2]
```
首先，我们定义个函数，也就是上面的公式。
```r

FPKM2TPM <- function(fpkm){
  exp(log(fpkm) - log(sum(fpkm)) + log(1e6))
}
```
然后我们利用apply函数进行遍历，就可以转换啦。
```r
TPMs <- apply(exp,2,FPKM2TPM)
```
上面是FPKM转TPM，但是如果是count转TPM就比较麻烦一下，虽然我在文章【[RNA-Seq的Counts和FPKM数据如何转换成TPM？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272981&idx=1&sn=d5ef893cb6a61210ae765ae2cf0f93c4&scene=21#wechat_redirect)】中有给出函数，但是，并每天给出里面一个参数的计算，那就基因长度的计算。这里，我们来看一下基因Length的计算方法。
相信大家必然听说过可变剪切的概念，也正是因为可变剪切的存在，同一个基因会产生不同的转录本。在这里呢，又会产生两种不同的分析思路：
思路1:计算基因在染色体的起始和结束之差；

思路2：计算每个基因的最长转录本或所有外显子之和；
那么，又有一个问题产生了，如何去获取基因在染色体上的位置信息呢？对基因组测序或分析有些了解的小伙伴应该对这几个文件类型有所接触，想fasta文件是保存基因DNA或RNA的测序信息，gtf、gff以及gf3文件则都是保存基因注释的文件。我在[各种基因ID装换](https://www.yuque.com/doublehelix/bioinfonotes/ey6aby)的文章中就用到这个文件。不过这里用的是人的基因注释文件，如果你的是其他物种，需要下载相应物种的注释文件。

我们读入gtf注释文件
```r
library(GenomicFeatures)
txdb <- makeTxDbFromGFF("gencode.v22.annotation.gtf",format="gtf")
exons.list.per.gene <- exonsBy(txdb, by = "gene")
```
```r
#通过reduce函数避免重复计算重叠区
exonic.gene.sizes <- lapply(exons.list.per.gene,
                            function(x){sum(width(reduce(x)))})
#生成的geneID为ensemble编号
eff_length <- do.call(rbind,lapply(exonic.gene.sizes, data.frame))
eff_length <- data.frame(gene_id = rownames(eff_length),effLen = eff_length[,1])
rownames(eff_length)<-eff_length$gene_id 
rownames(eff_length) <- do.call(rbind,strsplit(as.character(eff_length$gene_id),'\\.'))[,1]
head(eff_length)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612335546177-992eecd0-0aaf-4523-8ccc-9eb272059d11.png#align=left&display=inline&height=187&margin=%5Bobject%20Object%5D&name=image.png&originHeight=268&originWidth=1069&size=43888&status=done&style=none&width=746)
```r
##读取count数据
rt <- read.table("data_count.txt", row.names = 1, header = TRUE, sep="\t")
str(rt)
##选取两者的交集基因
gen <- intersect(rownames(rt), rownames(eff_length))
rt <- rt[gen,]
eff_length <- eff_length[gen,]
```
上面是取交集，使得基因顺序一样。
下面介绍过的函数
**Counts转FPKM**
```r
##count2Fpkm函数
Counts2FPKM <- function(counts, effLen){
  N <- sum(counts)
  exp( log(counts) + log(1e9) - log(effLen) - log(N) )
}
```
**Counts转TPM**
```r
Counts2TPM <- function(counts, effLen){
  rate <- log(counts) - log(effLen)
  denom <- log(sum(exp(rate)))
  exp(rate - denom + log(1e6))
}

```
**FPKM转TPM**
```r
##FPKM转TPM
FPKM2TPM <- function(fpkm)
{
  exp(log(fpkm) - log(sum(fpkm)) + log(1e6))
}
```
下面是转换
```r
##count转换为FPKM值
fpkms <- as.data.frame(apply(rt, 2, Counts2FPKM, effLen = eff_length$effLen))
```
```r
tpms <- as.data.frame(apply(rt, 2, Counts2TPM, effLen = eff_length$effLen))
```
```r
tpms2 <- apply(fpkms,2,FPKM2TPM)
```

