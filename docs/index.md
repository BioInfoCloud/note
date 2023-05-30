## 你好

这里是**微信公众号：生物信息云**的索引网站： <https://bioinfocloud.github.io/note/>

- 通过主题和目录以打开文章
  - PC端 在上方标签栏选择主题 在左侧目录选择文章
  - 移动端 点击左上角图标选择主题和文章
- 搜索关键词以打开文章

---



## **入门学习历程**

**2~3周时间熟悉R语言语法，教程如下：**

- B站：[R语法视频](https://www.bilibili.com/video/BV1MS4y1i7yU?spm_id_from=333.999.0.0&vd_source=ad7486d1c0a79f7459d20781ce805fbc)

**3~5天快速了解ggplot2绘图思想，不需要精通。**

- [R语言数据可视化【视频】——解读ggplot2绘图思想视频教程](https://www.bilibili.com/video/BV1aT411V73F?spm_id_from=333.999.0.0)【B站视频：[ggplot2绘图思想](https://www.bilibili.com/video/BV1aT411V73F?vd_source=ad7486d1c0a79f7459d20781ce805fbc)】

- 为什么不需要精通？参考文章：[我有必要花大量时间去学习R语言绘图吗？？](https://mp.weixin.qq.com/s/9OEoqaNAeC0OrkU75QHhEw)

**1~2周学习数据的基础分析**

- B站：[R语言数据分析基础](https://www.bilibili.com/video/BV13a411P7Yk/?spm_id_from=333.788&vd_source=ad7486d1c0a79f7459d20781ce805fbc)

其他的学习资源（后期需要再学习）：
[https://github.com/XSLiuLab/Workshop](https://github.com/XSLiuLab/Workshop)
[https://xsliulab.github.io/Workshop/](https://xsliulab.github.io/Workshop/)

接下来，就是了解转录组测序的基本原理，其中涉及到的一些文件格式，这些文件格式主要是上游数据分析中会涉及的，只是你需要知道这些。【关于各种测序原理，你可以在B站或者微信搜索：陈巍学基因，有好多视频，也不需要掌握所有，普通转录组(bulk-RNASeq)先掌握，其他的结合自己需要了解，原理上很多是相通的】,**后面了解单细胞测序技术和空间转录组技术**。

- [生物信息学入门必须了解的名词](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264680&idx=2&sn=363f93cbf9659d0e6d2817d3b9946dff&scene=21#wechat_redirect)
- [illumina、Sanger、第三代和第四代测序技术原理](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272832&idx=1&sn=7d208df1a65e3696c41c666ef78f5881&scene=21#wechat_redirect)
- [生信中常见的数据文件格式](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272899&idx=1&sn=6779b2bd21f3b607a08227d31c7212c6&scene=21#wechat_redirect)
- [常用生物信息 ID的介绍](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265423&idx=2&sn=288f3c8acaad8670d35a031cd9794d58&scene=21#wechat_redirect)
- [生信中各种ID转换](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265466&idx=1&sn=021a10503d338e09abe07b578e734566&scene=21#wechat_redirect)

至于转录组测序的原理了解后，基础的分析你不需要知道上游怎么分析的，我用一句话解释：送出去测序的样本，提取总RNA，定量，使得每个样本中的RNA总量一样，打断后进行PCR扩增，然后测序，测序得到很多序列，如果基因表达量越高，测序得到的序列就越多【当然过程没有这么简单，比如还有去除核糖体RNA等】，怎么去量化这个表达量？这时候你就需要了解[RNA-seq的counts,RPM, RPKM, FPK值到底有什么区别？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264575&idx=2&sn=69b45012dbfe61d7574446de00ec9a7b&scene=21#wechat_redirect)。至于counts,RPM, RPKM, FPK怎么得到的中间过程，属于上游分析，你能理解这些counts,RPM, RPKM, FPK就是用来量化基因表达量之间的关系就行。上游的分析，需要基于Linux系统。

**【-------------------------下面这部分跳过-------------------**

后续感兴趣的话，可参考： [《转录组基础知识》](https://www.yuque.com/docs/share/e9dbfaba-752e-4f89-a072-e95dc4fed0ef?#)（密码：um4i）；

分析流程：

[转录组分析 | fastqc进行质控与结果解读](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273374&idx=1&sn=dfac9e82a09fbb18cd8b2c8179afcad8&scene=21#wechat_redirect)

[转录组分析 | 使用trim-galore去除低质量的reads和adaptor](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273401&idx=1&sn=ff9e3478309d805950c40d0ebae74296&chksm=841edcc4b36955d2a5bf8c85429114b5b83ec4e5afe869378b42ec4f659d4953d5f6c8e9e379&token=151105890&lang=zh_CN&scene=21#wechat_redirect)

[转录组分析 | 使用Hisat2进行序列比对](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273450&idx=1&sn=efab631b255e12cf5ffd259dd53fb2b3&chksm=841edc97b3695581de924856b0e6901c67b87648f85bd491729eaa2ee0592271d84042b9eb76&token=108642787&lang=zh_CN&scene=21#wechat_redirect)

[转录组分析 | 使用SAMtools将SAM文件转换为BAM文件、排序、建立索引](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273488&idx=1&sn=f5ed53f20164b19720d31f0a2cfcd268&chksm=841edd6db369547bc04ae15a2a8a7661fefa1193cabbe05d7e2f9e2fa986211603537cf8fbd0&token=108642787&lang=zh_CN&scene=21#wechat_redirect)

[转录组分析 | 使用RSeQC软件对生成的BAM文件进行质控](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273531&idx=1&sn=8a9b12fe030f6c0f8bb1d6c8abbf622d&chksm=841edd46b36954501a57801f8149301d1bbb7b2d62a6f0d73b8a4795071e2aace94e02c2f392&token=108642787&lang=zh_CN&scene=21#wechat_redirect)

[转录组分析 | 使用Stringtie对数据进行下游处理](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273566&idx=1&sn=947e61eb19a63943f8c56bfcad81cc82&chksm=841edd23b36954359fe559dc4a832ffd66a0792868d2d2ea65123765cc0b7dc4424ca4344549&scene=21#wechat_redirect)

曾健明老师的教程链接：[https://share.weiyun.com/1R1Oar3m](https://share.weiyun.com/1R1Oar3m) 密码：y6a5ce

**-------------------------上面这部分跳过-------------------】**

普通的分析的话我们都是从counts/FPKM/TPM开始的。得到的数据，基础的分析都差不多。
对于癌症方向，TCGA数据库是最好的数据资源，我们可以从TCGA中下载各种数据进行分析。
要分析数据就先了解TCGA数据库。
 [TCGA数据库介绍](https://www.yuque.com/docs/share/912e43c5-2b9d-4a31-982c-30d419bd1473?#) （密码：vtdx）；可看视频【[TCGA数据库介绍](https://mp.weixin.qq.com/s/i5hLNXQiXoeqF-ogOxm8Uw)】
注意：网上搜索的教程，注意发布时间在2022年4月份之前的，很多数据处理教程不在适用，因为TCGA发生了重大更新。这里有一些更新后的教程【[点击查看](https://mp.weixin.qq.com/s/urGDqQh1L-FK8olpW20_iw)】。TCGA数据库中有些癌症类型是没有正常样本的，或者正常样本数太少，有时候分析就不是很好，如果需要正常样本，可以下载GTEx数据库中的正常样本，但是，这是不同的数据来源，不能简单的使用，需要归一化。当然，你也不需要做这一步，UCSC中有标准化好的数据，直接下载使用就行了，可参考文章：[我要研究的癌症在TCGA数据库没有正常样本或正常样本数少怎么办？](https://mp.weixin.qq.com/s/hi-Jy57tN15-o7VRjESDFg)这里，我需要提一下，TCGA的数据都能在UCSC上直接下载的，但我自己不是很推荐这种方式，因为数据不是最新的，特别是临床数据，没有正常样本的数据才选择这种方式，当然下载使用也是没有问题的。可参考文章：[UCSC数据库下载TCGA数据需要注意的细节](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273247&idx=1&sn=008928dbfc6c6976d53369cd20c26f87&scene=21#wechat_redirect)。如果你只是单一的看几个基因在正常和肿瘤组织之间的表达高低话，在线工具GEPIA就可以了。

counts数和TPM以及FPKM之间是可以转换的。得到的数据以后，可以尝试转换他们，count数没有考虑基因长度。FPKM已经考虑了基因长度。counts转换为其他类型的的数据需要知道基因长度，FPKM转化为其他的就不需要。[RNA-Seq的Counts和FPKM数据如何转换成TPM？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272981&idx=1&sn=d5ef893cb6a61210ae765ae2cf0f93c4&scene=21#wechat_redirect)【[视频：TCGA-RNASeq数据转换](https://mp.weixin.qq.com/s/WXQ0iSfAQwLqq2ost2hHbghttps://mp.weixin.qq.com/s/WXQ0iSfAQwLqq2ost2hHbg)】，这里提取的数据基因名称需要转换成symbol，可以[了解gtf文件信息提取](https://mp.weixin.qq.com/s/jh2xPRi97teeGIPPfU2PiQ)。当然这在文章：[生信中各种ID转换](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265466&idx=1&sn=021a10503d338e09abe07b578e734566&scene=21#wechat_redirect)中已经有介绍。

得到这些数据以后我们就要进行数据的分析了。**常见的就是差异表达分析**。DESeq2和edgeR包
[超详细的DESeq2和edgeR包的基本原理和实战案例](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651267481&idx=1&sn=40a8715a333ff47f6e96c37b4182d1b1&scene=21#wechat_redirect)。

如果只是分析TCGA数据库中RNA的数据，还可以了解GDCRNATools包，参考文章：[GDCRNATools包下载数据、处理数据以及差异分析](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265127&idx=2&sn=8c866e064995e6feb251a5db00282fd2&scene=21#wechat_redirect)【不确定现在是否可用】

得到的差异表达基因可视化，火山图，这在[R语言数据可视化【视频】——解读ggplot2绘图思想视频教程](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273946&idx=1&sn=9fe780c87675cfae7b69f62516105ce7&chksm=841edea7b36957b1b7b5c794333e6d6b438f80351a54d4d962b2df1cba6ba1e2188687d3a2a2&scene=21#wechat_redirect)有介绍，你可以在搜狗微信栏搜索，模仿绘制，保存自己的代码，以后就不需要再写，改改参数就行。

对于数据来源GEO，因为GEO数据比较复杂，特别是芯片数据，公司不一样，芯片不一样，会有区别的。这部分
[基因芯片数据挖掘分析表达差异基因](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651263385&idx=1&sn=63528ffd7901f36387cd4f484c99e188&chksm=841ef5e4b3697cf28e4590d3509be675bc5d44fe1a1cb6f54fe6ad5cc419139c8720a5fb299d&token=1937927307&lang=zh_CN&scene=21#wechat_redirect)
[GEO数据库使用教程及在线数据分析工具](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651263601&idx=1&sn=443d0dddebb12f21cfd976d50473856b&chksm=841ef60cb3697f1aecc6c310ee3a77e6182a728d5b6711a5cc8f49f0739feaba904f565ce176&scene=21#wechat_redirect)
【视频】[-GEO数据库使用教程](https://mp.weixin.qq.com/s/Bb0r6s8HMT2hSZFrt7Rt0A)
[Bioconductor：GEOquery包](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266556&idx=1&sn=05fe660c9241f3a850584d73b5e8e665&scene=21#wechat_redirect)
[GEO数据库表达数据的提取以及limma包进行差异分析](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266701&idx=1&sn=23f3e83000c659abdbe045b9c18d3269&scene=21#wechat_redirect)
关于GEO数据库分析的详细教程阅读文章： [《基因芯片与GEOquery包》](https://www.yuque.com/docs/share/437c2f29-e88e-4c34-aed4-f14aebd330c6?#)（密码：wbso）
**GEO芯片数据的万能代码，问我要！**

如果你自己测序的数据，测序公司会给你数据，应该都会有count/FPKM的数据。差异分析都一样。
如果数据是小鼠的，得到的差异基因有时候需要转换成人的同源基因。因为很多分析工具或数据集都是基于人的。参考文章：

[biomaRt包实现不同物种之间同源基因转换](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273598&idx=1&sn=391ef32ddddbf123624b04c08d1d4939&chksm=841edd03b3695415dfcf9304e3eda459c484e85b423f0f3b5ab54ac996d4ed6d275b24339655&scene=21#wechat_redirect)。

[生信基础 | 人-小鼠同源基因之间的转换](生信基础 | 人-小鼠同源基因之间的转换)

[生信基础 | 人-小鼠基因之间的比较](https://mp.weixin.qq.com/s/TupjY-l0Bux_uP_c5ZzOzQ)

接下来的下游数据分析都差不多。
富集分析，具体：[clusterProfiler包进行KEGG,GO,GSEA富集分析](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266484&idx=1&sn=b3fdeca6d8df8b6f4b2baae83b5dcd3c&scene=21#wechat_redirect)【视频：[基于R语言的GO-KEGG富集分析](https://mp.weixin.qq.com/s/6aL_tZh9okGGlE6mM4o7KQ)】，当然，也有一些在线工具，比如：[FunRich数据库：一个主要用于基因和蛋白质的功能富集以及相互作用网络分析的独立的软件工具](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265340&idx=1&sn=5c3608661698d2332b992269a8721833&scene=21#wechat_redirect)。但是，既然都学习了R了，还是用[clusterProfiler包](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266484&idx=1&sn=b3fdeca6d8df8b6f4b2baae83b5dcd3c&scene=21#wechat_redirect)吧！！！【相关文章问我要】

差异分析后的结果，不筛选，根据差异倍数从大到小排序基因，进行GSEA分析。用到的也是[clusterProfiler包](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266484&idx=1&sn=b3fdeca6d8df8b6f4b2baae83b5dcd3c&scene=21#wechat_redirect)。这里有GSEA分析【[GSEA分析【视频】](https://mp.weixin.qq.com/s/2F_pyBeHiO_4YWMMYOcd3A)】，具体区别：[为什么选择GSEA分析？和KEGG和GO分析有什么区别？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265618&idx=1&sn=3c5365ed2c437d3b7b034431ab4ac934&scene=21#wechat_redirect)。虽然数据库给了好多基因集，但是，基因集我们是可以自定义的，可参考：[生信笔记 | 自定义GSEA分析中的gmt格式文件](https://mp.weixin.qq.com/s/kTanWDxtvbhujC-yZmGEow)。

得到的差异基因，也可以做蛋白互作分析【[视频STRING数据库](https://mp.weixin.qq.com/s/IlboWwtNB8jbc8G_lawQIg)】

如果你做湿实验，得到的差异基因，也可以做一下转录因子富集分析：[教你如何预测参与调节差异基因的转录因子](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651275223&idx=1&sn=00c88ae70cfe9676e56d1b51abc6b175&chksm=841edbaab36952bc5fad7b37251b695c88b3b6bc74dc7db6f7057330c847ef5d0cc908cb0b67&scene=21#wechat_redirect)。这是做机制的一个思路。

