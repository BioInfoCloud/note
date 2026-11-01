# GDCRNATools包

关于TCGA数据库的数据下载与整理：前面的文章已经介绍了一部分：

[TCGA数据库：RNA-Seq数据的下载与处理](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265067&idx=1&sn=39c75f795ad560540e2309569a68c718&chksm=841efc56b3697540fc2443869d615ea48acd5e7c11f6ed5f910963bcb0dda613bdb69ef0da72&scene=21#wechat_redirect)

[TCGA数据库：SNP数据的下载整理及其可视化](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265108&idx=1&sn=1b630022c486f75e4e0e00175b8ddf9d&chksm=841efc29b369753ff95dbc5508b446032c8ea3fb083ad25b1bce913804ea5a33c67bebf31c8d&scene=21#wechat_redirect)

[TCGA数据库：miRNA数据下载与整理](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264993&idx=1&sn=8681cbce6c7314b6db27ad465434cf18&chksm=841ef39cb3697a8a1a64403e8a03317fbb19693dc547f674cbb9e0110eb4ba613d2713bf7aae&scene=21#wechat_redirect)

[TCGA数据库：ATAC-Seq数据的下载整理及其可视化](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265040&idx=2&sn=a617872e041cda6a90a7c7fb270e8a09&chksm=841efc6db369757b41989830a159d1e211a4e6f97290dab7dca7ef0151dcd182b4bbf5938bcb&scene=21#wechat_redirect)

[TCGA数据库：临床数据下载与整理](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265078&idx=1&sn=1d6e6365a19762d18005380d56dc623b&chksm=841efc4bb369755d0cf25ac9f4cbde3fbec5bb6141eab39c0920eb560cf04273bcbd0c6f9375&scene=21#wechat_redirect)

这些文章中处理方式都是自己写代码，从头处理，有些人可能会问，为何如此多余，不是有很多R包吗？
为什么那么麻烦？
各有各的好处，对于很多初学者来说，直接用一些R包，出错后不知道所以然，那是因为不知道底层代码都进行了什么。
关于TCGA数据库挖掘的R包很多，TCGAbiolinks包就很不错，在差异分析的文章【[一文就会TCGA数据库基因表达差异分析](https://mp.weixin.qq.com/s/e05YajG5nR5HhVC1xxisOA)】中就有提到这个包，当时录制视频的时候这个包好像因为R版本的更新问题，就没有过多介绍，但很久很久前也有文字描述的教程，大家可以通过[差异分析](https://mp.weixin.qq.com/s/e05YajG5nR5HhVC1xxisOA)的文章中的链接进行查看，但关于GDCRNATools包的介绍，是我第一次介绍。
这个包主要用于处理lncRNA, mRNA和miRNA数据，不足之处没有其他数据的处理方式，比如甲基化，SNP和CNV的数据不能处理分析，或者就是因为名字限制了它的发展。
话就不多说啦，看视频。

> 更新: 2021-02-17 15:52:31
> 原文: <https://www.yuque.com/doublehelix/bioinfonotes/ugmwwk>
