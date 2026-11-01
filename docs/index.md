---
title: 首页
hide:
  - navigation
  - toc
---

<section class="hero">
  <div class="hero__inner">
    <p class="hero__eyebrow">🌱 生物信息学 · 学习笔记</p>
    <h1 class="hero__title">生物信息<span>云</span></h1>
    <p class="hero__lead">
      从 Linux、R、Python 到转录组、单细胞与机器学习，这里整理了一条可以按图索骥的生信学习路线，以及公众号文章的全部索引。
    </p>
    <div class="hero__actions">
      <a class="hero__btn hero__btn--primary" href="导读与基础/导读/绪论_uXODe8dBs4oLosqJ.html">开始学习 →</a>
      <a class="hero__btn" href="Programming/index.html">编程入门</a>
      <a class="hero__btn" href="https://github.com/BioInfoCloud/note" target="_blank" rel="noopener">GitHub 仓库</a>
    </div>
    <ul class="hero__tags">
      <li>R</li>
      <li>Python</li>
      <li>Linux</li>
      <li>转录组</li>
      <li>单细胞</li>
      <li>机器学习</li>
      <li>数据可视化</li>
    </ul>
  </div>
  <div class="hero__visual" aria-hidden="true">
    <span class="hero__orb hero__orb--1"></span>
    <span class="hero__orb hero__orb--2"></span>
    <span class="hero__orb hero__orb--3"></span>
  </div>
</section>

## 为什么用本站

<div class="grid cards" markdown>

-   :material-map-marker-path:{ .lg .middle } __系统路线__

    从入门到进阶按阶段梳理，按图索骥不迷路。

-   :material-code-braces:{ .lg .middle } __实战代码__

    ggplot2、DESeq2、TCGA 挖掘等可直接复制的代码。

-   :material-link-variant:{ .lg .middle } __资源整合__

    公众号、B 站、数据库与工具一站索引。

-   :material-package-variant:{ .lg .middle } __自研工具__

    MedBioInfoCloud R 包随取随用，覆盖基础到挖掘。

</div>

## 内容导航

<div class="grid cards" markdown>

-   :material-console:{ .lg .middle } __生信编程__

    ---

    Linux、Git、Markdown、R 与 Python 的入门与进阶。

    [:octicons-arrow-right-24: 进入](Programming/index.md)

-   :material-dna:{ .lg .middle } __生信基础__

    ---

    测序原理、文件格式、表达定量与富集分析。

    [:octicons-arrow-right-24: 进入](生信基础/生物信息学入门必须了解的名词_QyC0NHqMJR7AqyqQ.md)

-   :material-chart-scatter-plot:{ .lg .middle } __数据可视化__

    ---

    ggplot2 绘图思想与常见图形的实战代码。

    [:octicons-arrow-right-24: 进入](Programming/R/ggplot2.md)

-   :material-robot-outline:{ .lg .middle } __机器学习__

    ---

    从 kNN 算法开始，逐步补齐理论与代码实践。

    [:octicons-arrow-right-24: 进入](ML/knn/kNN.md)

-   :material-book-open-variant:{ .lg .middle } __文献解读__

    ---

    RNA-seq、免疫治疗与人工智能相关综述笔记。

    [:octicons-arrow-right-24: 进入](Literature/RNAseq_review1.md)

-   :material-database-outline:{ .lg .middle } __数据库工具__

    ---

    在线数据库与生信软件的速查手册。

    [:octicons-arrow-right-24: 进入](BioInfo/database/database.md)

-   :material-molecule:{ .lg .middle } __单细胞资源__

    ---

    单细胞相关数据库、工具与分析流程汇总。

    [:octicons-arrow-right-24: 进入](BioInfo/database/scList.md)

-   :material-package-variant-closed:{ .lg .middle } __MedBioInfoCloud__

    ---

    自研 R 包：从安装、基础函数到 TCGA 数据挖掘。

    [:octicons-arrow-right-24: 进入](package/MedBioInfoCloud.md)

</div>

## 入门学习路线

<div class="roadmap" markdown>
<div class="roadmap__step" markdown>
### 第一步 · R 语言基础 <small>2~3 周</small>

熟悉 R 的语法、数据结构与常用函数，先把「能读懂、能改写」作为目标。

- [R 语法视频（B 站）](https://www.bilibili.com/video/BV1MS4y1i7yU?spm_id_from=333.999.0.0&vd_source=ad7486d1c0a79f7459d20781ce805fbc)
- [我有必要花大量时间去学习 R 语言绘图吗？](https://mp.weixin.qq.com/s/9OEoqaNAeC0OrkU75QHhEw)
</div>

<div class="roadmap__step" markdown>
### 第二步 · 绘图思想 <small>3~5 天</small>

快速了解 ggplot2 的图层语法，不需要精通，够用即可。

- [R 语言数据可视化 —— 解读 ggplot2 绘图思想（B 站）](https://www.bilibili.com/video/BV1aT411V73F?spm_id_from=333.999.0.0)
- [ggplot2 综合教程](Programming/R/ggplot2.md)
</div>

<div class="roadmap__step" markdown>
### 第三步 · 数据分析基础 <small>1~2 周</small>

学会读入数据、整理数据、做基础统计与差异分析。

- [R 语言数据分析基础（B 站）](https://www.bilibili.com/video/BV13a411P7Yk/?spm_id_from=333.788&vd_source=ad7486d1c0a79f7459d20781ce805fbc)
- [XSLiuLab Workshop 学习资源](https://xsliulab.github.io/Workshop/)
</div>

<div class="roadmap__step" markdown>
### 第四步 · 转录组与 TCGA <small>持续深入</small>

理解测序原理与文件格式，再从 counts / FPKM / TPM 出发做差异表达与富集分析。

- [生物信息学入门必须了解的名词](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264680&idx=2&sn=363f93cbf9659d0e6d2817d3b9946dff&scene=21#wechat_redirect)
- [illumina、Sanger、第三代和第四代测序技术原理](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272832&idx=1&sn=7d208df1a65e3696c41c666ef78f5881&scene=21#wechat_redirect)
- [生信中常见的数据文件格式](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272899&idx=1&sn=6779b2bd21f3b607a08227d31c7212c6&scene=21#wechat_redirect)
- 详细流程与资料见下方折叠区 ↓
</div>
</div>

## 使用小贴士

!!! tip "如何高效使用本站"

    - **PC 端**：在上方标签栏选择主题，在左侧目录选择文章。
    - **移动端**：点击左上角图标选择主题和文章。
    - **搜索**：按 <kbd>/</kbd> 或点击右上角搜索框，输入关键词直接定位文章。
    - **主题切换**：点击顶栏右侧图标，可在浅色 / 深色之间切换。

## 延伸阅读

??? note "转录组测序原理与上游分析流程"

    了解转录组测序的基本原理，其中涉及的一些文件格式主要在上游分析中用到，知道即可。关于各种测序原理，可以在 B 站或微信搜索「陈巍学基因」，不需要掌握所有，普通转录组（bulk RNA-seq）先掌握，其他的结合自己需要了解，原理上很多是相通的。后面再了解单细胞测序技术和空间转录组技术。

    - [常用生物信息 ID 的介绍](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265423&idx=2&sn=288f3c8acaad8670d35a031cd9794d58&scene=21#wechat_redirect)
    - [生信中各种 ID 转换](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265466&idx=1&sn=021a10503d338e09abe07b578e734566&scene=21#wechat_redirect)
    - [RNA-seq 的 counts、RPM、RPKM、FPKM 值到底有什么区别？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264575&idx=2&sn=69b45012dbfe61d7574446de00ec9a7b&scene=21#wechat_redirect)
    - [《转录组基础知识》](https://www.yuque.com/docs/share/e9dbfaba-752e-4f89-a072-e95dc4fed0ef?#)（密码：um4i）

    上游分析流程（基于 Linux）：

    - [fastqc 进行质控与结果解读](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273374&idx=1&sn=dfac9e82a09fbb18cd8b2c8179afcad8&scene=21#wechat_redirect)
    - [使用 trim-galore 去除低质量的 reads 和 adaptor](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273401&idx=1&sn=ff9e3478309d805950c40d0ebae74296&scene=21#wechat_redirect)
    - [使用 Hisat2 进行序列比对](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273450&idx=1&sn=efab631b255e12cf5ffd259dd53fb2b3&scene=21#wechat_redirect)
    - [使用 SAMtools 将 SAM 转换为 BAM、排序与建索引](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273488&idx=1&sn=f5ed53f20164b19720d31f0a2cfcd268&scene=21#wechat_redirect)
    - [使用 RSeQC 对 BAM 文件进行质控](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273531&idx=1&sn=8a9b12fe030f6c0f8bb1d6c8abbf622d&scene=21#wechat_redirect)
    - [使用 StringTie 对数据进行下游处理](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273566&idx=1&sn=947e61eb19a63943f8c56bfcad81cc82&scene=21#wechat_redirect)
    - [曾健明老师教程](https://share.weiyun.com/1R1Oar3m)（密码：y6a5ce）

??? note "TCGA 数据库与表达量转换"

    普通分析一般从 counts / FPKM / TPM 开始。对于癌症方向，TCGA 是最好的数据资源。

    - [TCGA 数据库介绍](https://www.yuque.com/docs/share/912e43c5-2b9d-4a31-982c-30d419bd1473?#)（密码：vtdx）
    - [TCGA 数据库介绍（视频）](https://mp.weixin.qq.com/s/i5hLNXQiXoeqF-ogOxm8Uw)
    - [TCGA 重大更新后的教程](https://mp.weixin.qq.com/s/urGDqQh1L-FK8olpW20_iw)
    - [癌症在 TCGA 没有正常样本或正常样本少怎么办？](https://mp.weixin.qq.com/s/hi-Jy57tN15-o7VRjESDFg)
    - [UCSC 数据库下载 TCGA 数据需要注意的细节](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273247&idx=1&sn=008928dbfc6c6976d53369cd20c26f87&scene=21#wechat_redirect)
    - [RNA-Seq 的 Counts 和 FPKM 数据如何转换成 TPM？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651272981&idx=1&sn=d5ef893cb6a61210ae765ae2cf0f93c4&scene=21#wechat_redirect)
    - [了解 gtf 文件信息提取](https://mp.weixin.qq.com/s/jh2xPRi97teeGIPPfU2PiQ)
    - [超详细的 DESeq2 和 edgeR 包的基本原理和实战案例](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651267481&idx=1&sn=40a8715a333ff47f6e96c37b4182d1b1&scene=21#wechat_redirect)
    - [GDCRNATools 包下载数据、处理数据以及差异分析](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265127&idx=2&sn=8c866e064995e6feb251a5db00282fd2&scene=21#wechat_redirect)（不确定现在是否可用）

??? note "GEO 芯片数据挖掘"

    GEO 数据比较复杂，芯片平台与公司不同都会有区别。

    - [基因芯片数据挖掘分析表达差异基因](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651263385&idx=1&sn=63528ffd7901f36387cd4f484c99e188&scene=21#wechat_redirect)
    - [GEO 数据库使用教程及在线数据分析工具](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651263601&idx=1&sn=443d0dddebb12f21cfd976d50473856b&scene=21#wechat_redirect)
    - [GEO 数据库使用教程（视频）](https://mp.weixin.qq.com/s/Bb0r6s8HMT2hSZFrt7Rt0A)
    - [Bioconductor：GEOquery 包](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266556&idx=1&sn=05fe660c9241f3a850584d73b5e8e665&scene=21#wechat_redirect)
    - [GEO 表达数据提取与 limma 差异分析](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266701&idx=1&sn=23f3e83000c659abdbe045b9c18d3269&scene=21#wechat_redirect)
    - [《基因芯片与 GEOquery 包》](https://www.yuque.com/docs/share/437c2f29-e88e-4c34-aed4-f14aebd330c6?#)（密码：wbso）
    - [biomaRt 包实现不同物种之间同源基因转换](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651273598&idx=1&sn=391ef32ddddbf123624b04c08d1d4939&scene=21#wechat_redirect)
    - [生信基础 | 人-小鼠基因之间的比较](https://mp.weixin.qq.com/s/TupjY-l0Bux_uP_c5ZzOzQ)

??? note "富集分析与下游分析"

    - [clusterProfiler 包进行 KEGG、GO、GSEA 富集分析](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651266484&idx=1&sn=b3fdeca6d8df8b6f4b2baae83b5dcd3c&scene=21#wechat_redirect)
    - [基于 R 语言的 GO-KEGG 富集分析（视频）](https://mp.weixin.qq.com/s/6aL_tZh9okGGlE6mM4o7KQ)
    - [FunRich：基因与蛋白质功能富集及互作网络分析工具](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265340&idx=1&sn=5c3608661698d2332b992269a8721833&scene=21#wechat_redirect)
    - [GSEA 分析（视频）](https://mp.weixin.qq.com/s/2F_pyBeHiO_4YWMMYOcd3A)
    - [为什么选择 GSEA 分析？和 KEGG、GO 分析有什么区别？](https://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265618&idx=1&sn=3c5365ed2c437d3b7b034431ab4ac934&scene=21#wechat_redirect)
    - [自定义 GSEA 分析中的 gmt 格式文件](https://mp.weixin.qq.com/s/kTanWDxtvbhujC-yZmGEow)
    - [STRING 数据库蛋白互作分析（视频）](https://mp.weixin.qq.com/s/IlboWwtNB8jbc8G_lawQIg)
    - [教你如何预测参与调节差异基因的转录因子](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651275223&idx=1&sn=00c88ae70cfe9676e56d1b51abc6b175&scene=21#wechat_redirect)

<div class="cta" markdown>
### 关注「生物信息云」

公众号持续更新生信教程与实战笔记，欢迎在 B 站、GitHub 一起交流。

[:fontawesome-brands-bilibili: B 站](https://space.bilibili.com/434318322){ target=_blank } &nbsp; [:fontawesome-brands-github: GitHub](https://github.com/BioInfoCloud){ target=_blank } &nbsp; [:material-newspaper-variant-outline: 文章索引](WeChatOfficialAccount/articleIndex.md)
</div>
