## 1.Biopython介绍

Biopython是Python的最大，最受欢迎的生物信息学软件包。它包含许多用于常规生物信息学任务的不同子模块。它由Chapman和Chang开发，主要使用Python编写。它还包含C代码，以优化软件的复杂计算部分。它可以在Windows，Linux，Mac OS X等操作系统上运行。

基本上，Biopython是python模块的集合，这些模块提供处理DNA，RNA和蛋白质序列操作的功能，例如DNA字符串的反向互补，寻找蛋白质序列中的基序等。它提供了很多解析器，可以读取所有主要的遗传数据库 如GenBank，SwissPort，FASTA等，以及在python环境中运行其他流行的生物信息学软件/工具(如NCBI BLASTN，Entrez等)的包装程序/接口。它具有兄弟项目，例如：BioPerl，BioJava和BioRuby。

官网：[Biopython · Biopython](https://biopython.org/)

更多请阅读：https://www.yiibai.com/biopython/biopython_introduction.html 

### (1). 特征

Biopython是可移植的，清晰的并且具有易于学习的语法。下面列出了一些突出的功能 -

- 解释性的，交互式和面向对象的。
- 支持FASTA，PDB，GenBank，Blast，SCOP，PubMed/Medline，ExPASy相关格式。
- 处理序列格式的选项。
- 管理蛋白质结构的工具。
- BioSQL-SQL表的标准集合，用于存储序列以及功能和注释。
- 访问在线服务和数据库，包括NCBI服务(Blast，Entrez，PubMed)和ExPASY服务(SwissProt，Prosite)。
- 访问本地服务，包括Blast，Clustalw，EMBOSS。

### (2).  目标

Biopython的目标是通过python语言提供对生物信息学的简单，标准和广泛的访问。下面列出了Biopython的特定目标 -

- 提供对生物信息学资源的标准化访问。
- 高质量，可重用的模块和脚本。
- 可在集群代码，PDB，NaiveBayes和Markov模型中使用的快速数组操作。
- 基因组数据分析。

### (3).  好处

Biopython只需很少的代码，并具有以下优点 -

- 提供用于聚类的微阵列数据类型。
- 读取和写入`Tree-View`类型的文件。
- 支持用于PDB解析，表示和分析的结构数据。
- 支持在Medline应用程序中使用的日记数据。
- 支持BioSQL数据库，该数据库是所有生物信息学项目中广泛使用的标准数据库。
- 通过提供将生物信息学文件解析为特定格式的记录对象或序列加特征的通用类的模块，来支持解析器开发。
- 清除基于食谱样式的文档。

### (4). 样本案例研究

让我们来看看一些用例(种群遗传学，RNA结构等)，并尝试了解Biopython在该领域如何发挥重要作用：

**人口遗传学**

种群遗传学是对种群内遗传变异的研究，涉及对种群中基因和等位基因频率随时间和空间变化的检查和建模。
Biopython提供了用于种群遗传学的`Bio.PopGen`模块。该模块包含收集经典种群遗传学信息的所有必要功能。

**RNA结构**
DNA，RNA和蛋白质是我们生活中必不可少的三个主要生物大分子。蛋白质是细胞的主力军，并作为酶发挥重要作用。DNA(脱氧核糖核酸)被认为是细胞的“蓝图”。它携带了细胞生长，吸收营养和繁殖所需的所有遗传信息。RNA(核糖核酸)在细胞中充当“ DNA影印件”。

Biopython提供了`Bio.Sequence`对象，这些对象代表核苷酸，DNA和RNA的构建基块。

## 2.安装

```python
pip install biopython
```

安装成功

```python
PS F:\gitHub\note> pip install biopython
Collecting biopython
  Downloading biopython-1.80-cp310-cp310-win_amd64.whl (2.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.7/2.7 MB 2.8 MB/s eta 0:00:00
Collecting numpy
  Downloading numpy-1.23.5-cp310-cp310-win_amd64.whl (14.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.6/14.6 MB 7.2 MB/s eta 0:00:00
Installing collected packages: numpy, biopython
Successfully installed biopython-1.80 numpy-1.23.5
PS F:\gitHub\note>
```

## 3.验证安装成功

```
import Bio           
print(Bio.__version__) 
```

![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211252041963.png)

## 4.查看帮助文档

```python
help(Bio)
```

```
NAME
    Bio - Collection of modules for dealing with biological data in Python.

DESCRIPTION
    The Biopython Project is an international association of developers
    of freely available Python tools for computational molecular biology.
    https://biopython.org

PACKAGE CONTENTS
    Affy (package)
    Align (package)
    AlignIO (package)
    Alphabet (package)
    Application (package)
    Blast (package)
    CAPS (package)
    Cluster (package)
    Compass (package)
    Data (package)
    Emboss (package)
    Entrez (package)
    ExPASy (package)
    File
    GenBank (package)
    Geo (package)
    Graphics (package)
    HMM (package)
    KEGG (package)
    LogisticRegression
    MarkovModel
    MaxEntropy
    Medline (package)
    NMR (package)
    NaiveBayes
    Nexus (package)
    PDB (package)
-- More  --
```

## 5.更新

```python
pip install biopython –-upgrade
```
## 6.完整版
[点击下载](https://github.com/BioInfoCloud/FileBank/raw/master/BioInfo/biopython_cn_release.pdf)

来源:[https://github.com/bigwiv/Biopython-cn](https://github.com/bigwiv/Biopython-cn)

在线阅读:[https://biopython-cn.readthedocs.io/zh_CN/latest/index.html](https://biopython-cn.readthedocs.io/zh_CN/latest/index.html)