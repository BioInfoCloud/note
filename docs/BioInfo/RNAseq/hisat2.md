---
title: HISAT2 比对与索引构建
---

# HISAT2 比对与索引构建

## Hisat2自定义索引文件

已有index的物种文件：[Download | HISAT2 (daehwankimlab.github.io)](http://daehwankimlab.github.io/hisat2/download/)

```
extract_splice_sites.pytRNA.fragments.hg19.gtf>tsRNA.ss
```

```
extract_exons.pytRNA.fragments.hg19.gtf>tsRNA.exon
```

```
hisat2-build--sstsRNA.ss--exontsRNA.exongencode.v42.transcripts.fatsRNA
```

后续比对，参考文章：[转录组分析 | 使用Hisat2进行序列比对](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273450&idx=1&sn=efab631b255e12cf5ffd259dd53fb2b3&chksm=841edc97b3695581de924856b0e6901c67b87648f85bd491729eaa2ee0592271d84042b9eb76&token=108642787&lang=zh_CN#rd)
