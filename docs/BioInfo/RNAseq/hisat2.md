## Hisat2自定义索引文件

已有index的物种文件：[Download | HISAT2 (daehwankimlab.github.io)](http://daehwankimlab.github.io/hisat2/download/)



```sh
extract_splice_sites.py tRNA.fragments.hg19.gtf > tsRNA.ss
```

```sh
extract_exons.py tRNA.fragments.hg19.gtf > tsRNA.exon
```

```sh
hisat2-build --ss tsRNA.ss --exon tsRNA.exon gencode.v42.transcripts.fa tsRNA
```

后续比对，参考文章：[转录组分析 | 使用Hisat2进行序列比对](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273450&idx=1&sn=efab631b255e12cf5ffd259dd53fb2b3&chksm=841edc97b3695581de924856b0e6901c67b87648f85bd491729eaa2ee0592271d84042b9eb76&token=108642787&lang=zh_CN#rd)

