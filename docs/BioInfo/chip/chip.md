# 一. 基因芯片的基本原理
基因芯片(genechip)（又称DNA芯片、生物芯片）的原型是80年代中期提出的。基因芯片的测序原理是杂交测序方法，即通过与一组已知序列的核酸探针杂交进行核酸序列测定的方法，在一块基片表面固定了序列已知的靶核苷酸的探针。当溶液中带有荧光标记的核酸序列TATGCAATCTAG，与基因芯片上对应位置的核酸探针产生互补匹配时，通过确定荧光强度最强的探针位置，获得一组序列完全互补的探针序列。据此可重组出靶核酸的序列。
## 1. Affymetrix生物芯片介绍
美国Affymetrix公司是目前全球基因芯片行业的领头羊，以其专利的寡聚核苷酸原位光刻合成技术，年产各类寡聚核苷酸基因芯片达到几十万张，占据了表达谱基因芯片科研市场的一半以上，经过了将近十年的研究和开发，已经在国际上赢得了很高的盛誉，同时也成为为数极少的已经盈利的生物芯片公司。Affymetrix公司的基因芯片为寡核苷酸芯片（Oligo芯片），这种类型的芯片具有极高的特异性和灵敏度，重复性好，假阳性率非常低，是目前世界上最先进的基因芯片。Affymetrix所利用的原位光刻专利技术可使一张芯片上合成多达500,000 个寡核苷酸。该系统可以分析样品中DNA或者RNA序列的相对含量。
Affymetrix公司率先开发的寡聚核苷酸原位光刻专利技术，是生产高密度寡核苷酸基因芯片的核心关键技术。采用的技术原理是在合成碱基单体的5＇羟基末端连上一个光敏保护基。首先使支持物羟基化，并用光敏保护基团将其保护起来。每次选取适当的蔽光膜(mask)使需要聚合的部位透光，其它部位不透光。这样，光通过蔽光膜照射到支持物上，受光部位的羟基脱保护而活化。因为合成所用的单体分子一端按传统固相合成方法活化，另一端受光敏保护基的保护，所以发生偶联的部位反应后仍旧带有光敏保护基团。因此，每次通过控制蔽光膜的图案(透光与不透光)决定哪些区域应被活化，以及所用单体的种类和反应次序就可以实现在待定位点合成大量预定序列寡聚体的目的。 使用多种蔽光膜能以更少的合成步骤生产出高密度的阵列，在合成循环中探针数目呈指数增长。某一含N个核苷酸的寡聚核苷酸，通过4×N个化学步骤能合成出4N个可能结构。例如：一段8个碱基的寡核苷酸有65，536种排列的可能，通过32个化学步骤，8个小时就能合成65，536个探针。其基本原理如图所示：
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629791811289-9dc9a6ed-748a-4dbe-ad51-5974ddb28335.png#clientId=ud07b1a42-41f6-4&from=paste&height=358&id=uc3cd0007&margin=%5Bobject%20Object%5D&name=image.png&originHeight=556&originWidth=1259&originalType=binary&ratio=1&size=658301&status=done&style=none&taskId=u62837631-8a87-4a0e-a325-51d4b60a83b&width=810.5)
视频讲解：[https://v.qq.com/x/page/j0173fqkgbb.html](https://v.qq.com/x/page/j0173fqkgbb.html)
昂飞的表达谱芯片，分成传统的 **「In Vitro Transcription」** 芯片，简称 IVT 芯片和新一代的 **「Whole Transcriptome」** 芯片，简称 WT 芯片。
IVT 芯片用 Oligo dT 引物和 T7 逆转录酶来得到 cDNA 链，所以，它得到的 cDNA 主要是靠近 mRNA 3'位末端的 cDNA。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629793161121-6688acd9-bdc1-405a-9b31-f1b03f37eaf2.png#clientId=ud07b1a42-41f6-4&from=paste&id=u72394b4d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=553&originWidth=552&originalType=binary&ratio=1&size=208527&status=done&style=none&taskId=ub67b9693-4db6-4f3c-8c41-5af96ad9acc)


WT 芯片用随机引物和 T7 逆转录酶来得到 cDNA 链，所以其 cDNA 会覆盖转录本上更多区域。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629793268904-50586415-d2ba-4904-addd-2e8c8b303865.png#clientId=ud07b1a42-41f6-4&from=paste&id=u1d043f9e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=625&originWidth=551&originalType=binary&ratio=1&size=229871&status=done&style=none&taskId=u9d8dfbe0-17ed-420a-b5db-d22675cba62)
WT 芯片的好处：

- 可以覆盖转录本上更多的区域，实验结果的代表性就会更强（如图绿框）。
- 可以针对因为差异剪接所形成的不同转录本分别设计探针，方便得到不同转录本的表达量变化情况（如图红框）。
- 可以检测到 lncRNA。

比较著名的 WT 芯片有 HTA 2.0、Exon 1.0、Gene 2.0/2.1 等。
参考文章：[https://mp.weixin.qq.com/s/OURXVzaQF05ykQEWpXsLGw](https://mp.weixin.qq.com/s/OURXVzaQF05ykQEWpXsLGw)
## 2. illumina的原理
illumina 方案的测序芯片称为「Infinium」（曾用名「Bead Array」），顾名思义由玻璃基片和微珠组成。
玻璃基片形状大小与普通载玻片相近，其作用主要是为了给测序微珠提供容器。
基片内表面，通过光蚀刻的方法，做出许多排列整齐的微米级小孔，作为容纳测序微珠的空间。两者大小恰好匹配，一个小孔正好能容纳一个微珠。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629795222311-9e6545a3-61b1-4c29-87fe-4de5efc5812e.png#clientId=ud07b1a42-41f6-4&from=paste&height=365&id=ue6410702&margin=%5Bobject%20Object%5D&name=image.png&originHeight=546&originWidth=1091&originalType=binary&ratio=1&size=485451&status=done&style=none&taskId=ue5d6aebf-56bc-4eb7-a2dd-1e81e70c646&width=729.5)
微珠则为芯片的核心部分，每个微珠的表面，都各偶联某种序列的 DNA 片段。每个微珠上，有几十万个片段，而一个珠子上的片段，都是同一种序列。
其序列设计如图所示，由靠近微珠端的 Address 序列和 Probe 序列构成。Address 序列是标识微珠的标签序列，通过碱基的排列组合组成该微珠的 ID。在 illumina 生产芯片的过程当中，是把要做芯片的几十万种微珠，按设定的比例或者客户需求进行混合，撒到玻璃基片上。在一张芯片的一个反应当中，每种珠子平均有 15 颗或以上。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629795346605-4227e299-ed6a-4c88-aa7d-c1104f861e9f.png#clientId=ud07b1a42-41f6-4&from=paste&height=383&id=u7fea8283&margin=%5Bobject%20Object%5D&name=image.png&originHeight=541&originWidth=1170&originalType=binary&ratio=1&size=468201&status=done&style=none&taskId=udb6672ad-1f47-4651-89cf-c6947504581&width=829)
微珠随机地落入基片的小孔当中，再通过检测芯片上每个小孔当中的微珠上的 Address 序列，就可以知道，这个小孔当中是哪种微珠。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629795726269-7babc3b9-3bb4-4c2f-84c4-9456e4af1790.png#clientId=ud07b1a42-41f6-4&from=paste&height=298&id=u8645112a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=322&originWidth=783&originalType=binary&ratio=1&size=403066&status=done&style=none&taskId=ue38651d5-61ba-4418-8b60-ce7ea3965ab&width=724.5)
所以，illumina 公司出厂的每一张芯片，都要跟一个.dmap文件，标注每一张芯片的每一个微孔当中，分别是哪种微珠。自然地，获得芯片相应的地图文件之后，才能解读测序数据。
**Probe 序列**：作为探针序列，其作用是与目标 DNA 互补杂交；且与 Address 序列存在一一对应的关系。

检测样本的制备和 Affymetrix 芯片基本相似，也是要产生带标记的 cRNA，再和探针杂交，这里我们常用的标记有两种，一种是生物素（biotin）标记，再加荧光结合的抗生物素蛋白与生物素结合即可，见于最常用的 Human HT-12 系列，目前为 V4 版本。
另一种是待检测 cRNA 上直接标记荧光，比如专供石蜡包埋（FFPE）标本的 Human Whole Genome DASL HT 芯片就是这种。大家可以看到，标记了荧光的 cRNA 被探针“毛珠”粘住了，表达量越高的 RNA 被粘住的机会也越多，荧光就越强。这些荧光的点阵正是一个个长满探针排列在硅片孔里的微珠。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629804901311-1b90f721-9752-4c24-b248-a031384e556e.png#clientId=ud07b1a42-41f6-4&from=paste&height=470&id=u70ad8c3b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=498&originWidth=221&originalType=binary&ratio=1&size=40066&status=done&style=none&taskId=ud748079f-e92c-4eed-b032-163116eda3e&width=208.5)
上图显示了 WG-6 BeadChip 芯片中典型珠子(顶部)的示意图，其中标记了阳性(红色正方形)和局部背景(黄色正方形)信号的像素。许多包含 50-mer 探针的微珠位于每个 BeadArray 反应池中。图示为了清晰一些，大大降低了微珠的密度。
视频讲解：[https://v.qq.com/x/page/d0171ihr74i.html](https://v.qq.com/x/page/d0171ihr74i.html)
参考文章：[https://mp.weixin.qq.com/s/7D0TmxWubcMnnaXOtn4bow](https://mp.weixin.qq.com/s/7D0TmxWubcMnnaXOtn4bow)
## 3. Agilent 生物芯片原理
Agilent芯片的基片是一个玻璃片。它的大小和一张标准的病理载玻片一样大小。
它的芯片制作过程，是用和喷墨打印一样的技术来进行制作的。喷墨打印机，是在墨盒里面是装了“红、黄、蓝、黑”四种颜色的墨水。而Agilent打印生物芯片的墨盒里面，是用带保护基团的A/C/G/T四种碱基底物，来代替了颜色墨水。分别含有4种碱基底物的小液滴，被按照设计的探针序列，依次、层叠地喷到玻璃板的确定的位置上。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629813267156-65de3523-458d-4cb3-a643-80351268c35d.png#clientId=ue984c4d8-a874-4&from=paste&height=221&id=uec4635ed&margin=%5Bobject%20Object%5D&name=image.png&originHeight=331&originWidth=754&originalType=binary&ratio=1&size=424953&status=done&style=none&taskId=u4b984f1b-12fc-4534-90b9-5530c48c3a1&width=504)
在每一个碱基的延伸过程当中都有 3 个步骤，分别是偶联、氧化、 去除保护基团，即先把一个核苷酸喷到玻璃板上，然后再喷上第二个碱基，让两个碱基之间发生偶联，继而经过氧化，把亚磷酸基团氧化成磷酸基团。然后，把连在第二个碱基 5’ 位羟基上的 DMT 保护基团去掉， 留下一个自由的 5’ 位羟基，再进行下一步的延伸反应。 不断重复这个过程，DNA 链就会不断地延长。 Agilent 的这个 DNA 链合成技术，每一步的合成效率都非常高，可以达到 99%以上。这让 Agilent 可以在芯片上得到很长的 DNA 链， 最长可以达到 300 个碱基的长度。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1629813345659-9265f36d-f3b8-4e93-b0d2-a80e3f89cacc.png#clientId=ue984c4d8-a874-4&from=paste&height=175&id=ufaad8623&margin=%5Bobject%20Object%5D&name=image.png&originHeight=276&originWidth=954&originalType=binary&ratio=1&size=286801&status=done&style=none&taskId=ucfd977ec-2f6d-4940-8f98-ccf4bbf9e8f&width=605)
Agilent 表达谱芯片的检测原理也是基于 3’ IVT 原理。首先用 Oligo dT 引物和 T7 逆转录酶来得到第一链的 cDNA， 然后再转录或复制出第二链的 cDNA，得到双链 cDNA，这个双链cDNA 是带有 T7 启动子的。接下来， 如果是单色（或单通道）芯片杂交流程，我们只进行这张图的左边的蓝色部分，使用 T7 逆转录酶，以带有 A、 T、 U 碱基的核苷酸和标有 Cy5 荧光基团 CTP 为底物逆转录出 cRNA 来；如果是双色（或双通道）杂交流程，要加上图示的右半边红色的部分，即对于另一个样本（参照组 reference），就用标有 Cy3 荧光基团 CTP 做为底物之一。这样， Cy3（或 Cy5） 荧光基团就在体外逆转录过程当中，被带入到新合成的 cRNA链当中去了。 经纯化后，将这个制备好的 cRNA 与芯片探针进行杂交，在激光扫描仪下检测每个点的荧光强度，并计算出对应基因的 RNA 表达量来。不同于单色芯片以计算荧光强度作为表达值，双色芯片的表达值则计算的是实验组和参照组的比值。
视频连接：[https://v.qq.com/x/page/h0174dobvcb.html](https://v.qq.com/x/page/h0174dobvcb.html)
参考：[https://mp.weixin.qq.com/s/8qUblDoNV3AobGdiwl8Aig](https://mp.weixin.qq.com/s/8qUblDoNV3AobGdiwl8Aig)
需要注意的是，对于双色芯片，我们称标记第二种颜色的样本为参照组（reference），它可以是对照组样本（如用同一个患者的癌旁组织作为癌的对照），也可以仅仅是一个基因表达的参考，如使用一种或几种肿瘤细胞系的 RNA 混合物作为参照组。 **GEO 上使用 Agilent 双色芯片的数据集的表达谱，常常给出的是两种基因的表达强度比值，并取 log2；但也有些数据集虽然用的也是这款芯片，但只使用了单色单样本，这时候就直接和普通单色芯片一样分析即可**。
# 二. 芯片数据库
比较大的芯片数据库有美国 NCBI 的 GEO，欧洲 EMBL-EBI 的 ArrayExpress，日本 DDBJ 的 GEA，不过这个 GEA 直接连接到 ArrayExpress，还有美国 NCI 下属的 TCGA，里面也有大量肿瘤芯片数据，不要误以为 TCGA 全是测序数据。其中 GEO 是最大的芯片数据库，其次是 ArrayExpress。这里就介绍GEO这个数据库。
## 1. GEO数据库简介
GEO，全称 Gene Expression Omnibus（基因表达综合数据库），是由美国国立生物技术信息中心NCBI创建并维护的基因表达数据库。它创建于2000年，收录并整理了全球范围内研究工作者上传的微阵列芯片、二代测序以及其他形式的高通量基因组数据，这些数据包括基于单通道和双通道微阵列的实验，检测mRNA，基因组DNA和蛋白质丰度，以及非阵列技术，如基因表达系列分析（SAGE），质谱蛋白质组学数据和高通量测序数据。也就是说只要是目前已经发表的论文，论文中涉及到的基因表达检测的数据都可以通过这个数据库中找到。关键是这个数据是免费的！随着芯片和测序技术的蓬勃发展和应用， 2000 年美国国立生物技术信息中心, NCBI 创建了 GEO 并维护至今。 2003 年到 2004 年 GEO 数据库逐渐开放供研究者获取和分析， 2001 年到 2006 年， GEO 数据上传的规则，也就是 MIAME（The MinimumInformation About a Microarray Experiment guidelines）逐渐形成并实行，并成为提交芯片数据的全球规范。
GEO 数据库收录的数据类型有：

- 01）基因芯片或高通量测序的基因表达数据，包括 ncRNA
- 02）基因芯片或高通量测序的 ChIP 数据
- 03）基因芯片或高通量测序的基因组甲基化数据
- 04）高通量实时定量 PCR 的数据
- 05）微阵列比较基因组杂交技术（arrayCGH）的基因组变异数据
- 06）单核苷酸多态性（SNP）芯片数据
- 07）基因表达系列分析（SAGE）的数据
- 08）蛋白芯片数据
- 09）十几组大规模平行测序 MPSS 数据
- 10）十几组质谱 MS 数据
- 11）其他
## 2.ArrayExpress 数据库
NCBI 的基因表达综合数据库 GEO 和欧洲生物信息学研究所(EBI)的 ArrayExpress 是芯片数据的两个主要公共数据库。尽管它们具有不同的设计，但两个数据库都支持由 MIAME 定义的所有数据元素。 因此 GEO 和ArrayExpress 数据库及数据集结构十分相似，可以类比的学习。ArrayExpress 数据库在 2002建立，开始收录芯片数据， 2008 年开始收录高通量测序数据，同样，近几年测序数据的增长量逐渐超过芯片数据。 ArrayExpress 是 GEO 数据的一个良好的补充。
ArrayExpres数据库的主页链接（[https://www.ebi.ac.uk/arrayexpress/](https://www.ebi.ac.uk/arrayexpress/)）
# 三. GEO数据库使用教程
## 1.检索 
检索界面，网址：[http://www.ncbi.nlm.nih.gov/geo](http://www.ncbi.nlm.nih.gov/geo)

![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180966-58be52c0-3280-4693-9d4c-fdd9ab3c95c9.jpeg#height=601&id=qCHlu&originHeight=601&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
或者通过NCBI首页，All Databases下拉框中选择GEO DataSets，输入关键词即可搜索。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180955-fbaaf877-28b6-42ce-86db-e432257dbb35.jpeg#height=601&id=f8Q3z&originHeight=601&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
这里以检索肺癌（lung caner）的数据为例。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180948-15a80dec-629f-43f0-89d9-929d68dab099.jpeg#height=577&id=YsPX8&originHeight=577&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
搜索结果可以通过7来设置每页显示个数，通过8选择排序方式，可以通过左侧的选项对搜索结果进行筛选。Entry type有四种:Datasets，Series，Samples，Platforms。分别对应的是，GEO Dataset (GDS) 数据集的ID号、GEO Series (GSE) 研究的ID号、GEO Sample (GSM) 样本ID号和GEO Platform (GPL) 芯片平台。
### 平台
平台记录描述阵列上的元件列表（例如，cDNA，寡核苷酸探针组，ORF，抗体）或可在该实验中检测和定量的元件列表（例如，SAGE标签，肽）。每个平台记录都分配有唯一且稳定的GEO登录号（GPLxxx）。平台可以引用多个提交者提交的许多样本。
### 样品
样品记录描述了处理单个样品的条件，它经历的操作以及从中得到的每个元素的丰度测量。每个样品记录都分配有唯一且稳定的GEO登录号（GSMxxx）。Sample实体必须仅引用一个Platform，可以包含在多个Series中。
### 系列
系列记录定义了一组被认为是组的一部分的相关样本，样本如何相关，以及它们是否以及如何排序。A系列提供了整个实验的焦点和描述。系列记录还可能包含描述提取数据，摘要结论或分析的表格。每个系列记录都分配有唯一且稳定的GEO登记号（GSExxx）。
### 数据集
GEO DataSet（GDSxxx）是GEO样本数据的精选集合。GDS记录代表了一系列具有生物学和统计学意义的GEO样本，构成了GEO数据显示和分析工具套件的基础。GDS中的样本指的是同一个平台，也就是说，它们共享一组共同的探测元素。假设GDS中每个样本的值测量值以等效方式计算，即背景处理和标准化等考虑因素在整个数据集中是一致的。通过GDS子集提供反映实验设计的信息。
记住大小关系：一个GDS可以有多个GSM，一个GSM可以有多个GSE，至于GPL，一般不接触，我们通常接触的都是GSE系列（一个GSE里面有多个GSM）的数据。
接下来的几个就好理解了，2是指物种类型，点击一下会弹出一个对话框，选择自己要的就可以对搜索结果进行筛选了，也可以直接点击9处进行筛选，一般不是人就是鼠，通常是选择人。
3通过研究类型进行筛选，比如甲基化，单核苷酸突变等进行筛选。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180974-91664b08-26c0-44de-95fe-bdb37383b195.jpeg#height=845&id=HM5qs&originHeight=845&originWidth=618&originalType=binary&ratio=1&size=0&status=done&style=none&width=618)
4是根据作者进行筛选，个人感觉一般用不到。5是属性名称，表示数据来自于组织还是特定的细胞类型。6是指初版日期。
上面是通过关键词检索，只是为了让大家了解一下检索页面，通常在文章中我们会看到作者都是用GSE****号，我们知道GSE编号，我们也可以直接通过检索GSE编号获取信息，同时也可以通过GDS***,和GSM来检索。GSE编号检索比较常用。
GDS编号检索结果页面，以GDS402为例
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180993-ca39eb59-ce80-4e90-90d9-f7846d9a3be7.jpeg#height=518&id=UsBuE&originHeight=518&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
GSE编号检索结果页面
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180998-101dd059-1b48-4b03-b5ec-6cf373c3ebc8.jpeg#height=848&id=WgRho&originHeight=848&originWidth=1075&originalType=binary&ratio=1&size=0&status=done&style=none&width=1075)![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181119-b1d12809-a13f-4e35-8a2d-52071a308399.jpeg#height=870&id=UR16M&originHeight=870&originWidth=1073&originalType=binary&ratio=1&size=0&status=done&style=none&width=1073)
soft和miniml都是表示该platform的基础信息，比如GPL编号，上传日期等，soft文件的部分内容如下:
```
^DATABASE = GeoMiame!Database_name = Gene Expression Omnibus (GEO)!Database_institute = NCBI NLM NIH!Database_web_link = http://www.ncbi.nlm.nih.gov/geo!Database_email = geo@ncbi.nlm.nih.gov^PLATFORM = GPL20814!Platform_title = Human miRNA Array miRbase release 19!Platform_geo_accession = GPL20814!Platform_status = Public on Jun 12 2017!Platform_submission_date = Aug 18 2015!Platform_last_update_date = Jun 12 2017
```
在soft文件中，每种类别的信息以^开头，常见的类别如下所示
DATABASE
PLATFORM
SAMPLE
SERIES

DATABASE代表GEO数据库的基本信息，PLATFORM代表该平台的基本信息，SAMPLE代表用该平台得到的样本信息，SERIES代表使用该平台得到的一组样本。
在每种类别中，!开头代表一种类型的信息，常规格式为key = value, 比如:Platform_geo_accession = GPL17515
对于芯片平台而言，还会提供探针和基因之间的对应关系等信息，在对应的网页上，我们可以看到如下的表格.
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180973-b5885c18-8a9a-4f3d-97e1-897eba10db39.jpeg#height=332&id=MC3kI&originHeight=332&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
这部分内容在soft文件中也是存在的，示意如下:
```
!platform_table_beginID    Reporter Name    miRNA_ID    SPOT_ID272    hsa-miR-99b-5p    MIMAT0000689    271    hsa-miR-99b-3p    MIMAT0004678    270    hsa-miR-99a-5p    MIMAT0000097    269    hsa-miR-99a-3p    MIMAT0004511    268    hsa-miR-98-5p    MIMAT0000096...!platform_table_end
```
采用配对的两个!叹号来表示数据的开始和结束，在中间存放对应的表格数据。
miniml中的内容和soft是一样的，只是用XML格式来存储上述信息，而supplement file则是由提交者自己上传的一些补充文件，没有明确的格式。
GSM编号检索页面
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181100-1a505a42-9890-4cb3-adc5-ef4b67f47487.jpeg#height=696&id=N1lgZ&originHeight=696&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180989-710e8c3d-4d61-4716-946a-9200376bae8a.jpeg#height=597&id=Su6yP&originHeight=597&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773180988-9b3fc174-95ab-4548-aa46-5c760884e0d3.jpeg#height=643&id=B3RDq&originHeight=643&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181018-bd8ef1ce-7e8f-4eb7-8359-8ad71f2d9512.jpeg#height=273&id=fPWNR&originHeight=273&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
在这个页面，我们可以看见样本在进行试验处理的详细描述，以及每个探针所检测的的信号值。


除此以外，我们还可以通过GEO数据库的仓库浏览器就行特定的检索。
在GEO数据库首页点击Repository Browser
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181002-5bab859e-426e-45b8-9b6e-3fc0924dcc48.jpeg#height=437&id=fYTFy&originHeight=437&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
进入的页面我们可以看见，序列，平台，样本和物种的选项卡，我们可以通过其进行检索。
比如我们通过序列进行检索芯片表达数据或者甲基化数据，就点击相应的选项
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181005-d87f2908-cc37-41d9-81e6-b87e95ce3e54.jpeg#height=540&id=NdXaE&originHeight=540&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
点击Methylation profiling by array进入新的页面，我们就可以看到具有甲基化数据的GSE数据集的详细描述，包括标题，序列类型，样本数，物种等。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181016-02f541ad-9121-4304-8b2f-d4d924c98691.jpeg#height=540&id=MmMv7&originHeight=540&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
我们还可以通过关键词对结果进行筛选。比如你只和癌症有关的数据。输入cancer，结果就只有151个。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181201-e3038a56-595b-43b3-987d-bcad9feb73ad.jpeg#height=543&id=sTTGI&originHeight=543&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
关于GEO数据库检索就介绍到这里，我们接下来就介绍GEO在线的分析工具。
## 2.分析工具 
我们再看看GDS号检索的结果页面
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181042-b4d1a3e4-b6b0-438e-9f56-291fe7ecbafd.jpeg#height=525&id=erJ4N&originHeight=525&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)

### (1).Find gene工具
该工具用于直接查找该数据集中该基因的表达谱数据。
我们以检索brca1基因为例
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1610773181177-7d4e05f2-b687-4fb0-ba32-f2e96be0ab4c.png#height=237&id=Hn8hc&originHeight=237&originWidth=639&originalType=binary&ratio=1&size=0&status=done&style=none&width=639)

我们会跳到一个新的检索结果页面
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181028-7b456457-5f88-4fd1-81b1-69e0ebf38d07.jpeg#height=511&id=fv1iZ&originHeight=511&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
往下拉我们会找到一个Brca1的一个表达谱数据集。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181026-b3e7202a-54b9-487c-afb0-fcd688e64c1b.jpeg#height=267&id=t17Hw&originHeight=267&originWidth=1072&originalType=binary&ratio=1&size=0&status=done&style=none&width=1072)
点击右侧的图进入详细页面，该页面具有该基因在各个样本中的表达信息，并且样本的分组信息也有。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181122-8a3d3a8f-4865-4de3-ab8c-69af6180659d.jpeg#height=939&id=VhVvN&originHeight=939&originWidth=582&originalType=binary&ratio=1&size=0&status=done&style=none&width=582)
Find genes that are up/down for this condition(s)可以根据选择的实验筛选条件来找到一序列随该筛选条件有较明显表达差异的基因表达谱。假设我们要检索和疾病分期有关的上调或下调的基因。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1610773181060-2f9037f3-dda9-4b68-b829-2a86688ff036.png#height=106&id=yocrz&originHeight=106&originWidth=632&originalType=binary&ratio=1&size=0&status=done&style=none&width=632)
可以看到检索到了79个基因。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181010-85c03d9a-0f6e-4f5d-8cee-293ef5040b8d.jpeg#height=496&id=qf4mj&originHeight=496&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
我们点击第一个基因，同样可以看到该基因的详细信息。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181160-abe9ac68-cc83-4d56-a3e8-c6b718302fc9.jpeg#height=937&id=smIVe&originHeight=937&originWidth=582&originalType=binary&ratio=1&size=0&status=done&style=none&width=582)
### (2).Compare 2 sets of samples工具

![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181057-0380bfb7-4cb1-4130-b577-e89393118e81.jpeg#height=241&id=XL2Zi&originHeight=241&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181037-0e29a148-d33b-4947-b428-269fe21e2fae.jpeg#height=242&id=LTnGQ&originHeight=242&originWidth=808&originalType=binary&ratio=1&size=0&status=done&style=none&width=808)
我们点击Step2： Select which Samples to put in Group A and Group B会弹出一个窗口，让我们自己进行分组。我们可以看见A组合B组的GSM号是一样的，需要将他分在哪一组就在哪一组点击一下就行。背景变为深灰色就表示被选中，这里将GSM9920-GSM9925定位A组，其余定位B组。点击OK.
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181061-50ba3299-f571-4f5d-89d6-b6865e654afd.jpeg#height=567&id=BXKdz&originHeight=567&originWidth=760&originalType=binary&ratio=1&size=0&status=done&style=none&width=760)
点击OK后我们会看见Step2下面会出现分组的样本编号。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181071-ed5a3cac-f882-4996-b84d-56dc699ddf47.jpeg#height=272&id=f4cc1&originHeight=272&originWidth=700&originalType=binary&ratio=1&size=0&status=done&style=none&width=700)

点击Query Group A vs. B我们就会获得5608个表达差异的基因。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181068-7e7defb9-d4bb-4ec6-9e2b-88206b5a3fc1.jpeg#height=503&id=im3qE&originHeight=503&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
### (3).Cluster heatmaps工具
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181061-bc68b9db-a031-4e9b-9a83-1ee261250c99.jpeg#height=318&id=J42qs&originHeight=318&originWidth=679&originalType=binary&ratio=1&size=0&status=done&style=none&width=679)
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181059-f521c4a7-6168-44ab-8ed0-110431832cd9.jpeg#height=261&id=iYItt&originHeight=261&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
点击Display，或获取一个聚类的热图，鼠标放在热图上谁有一个红色的虚线框，可以通过上下拖动边框调整选择的区域大小。可以点击DOWNLOAD 下载数据。

![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181176-6e29afd8-afb3-46a7-a923-5249f0100eeb.jpeg#height=837&id=BxZ8k&originHeight=837&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
点击Stack up 可以将所选择的区域放大，能够看见基因名称。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181102-3c98575a-eced-4087-8efd-0abcbdbe9ae7.jpeg#height=838&id=QvDxQ&originHeight=838&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
点击Plot value可以看见探针在样本中的曲线图。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181106-db34785e-563b-499b-89f6-ffba422a0b6b.jpeg#height=859&id=tcBWJ&originHeight=859&originWidth=962&originalType=binary&ratio=1&size=0&status=done&style=none&width=962)

此外Cluster heatmaps工具中还有一个Partitional (K-means/K-medians)的聚类。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181098-f21812aa-8f25-4731-a489-ae0fd69cf8f0.jpeg#height=278&id=Vt5pm&originHeight=278&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
然后通过设置高低表达的颜色，设置聚类个数（cluster，2-15），这里选择4，点击Display
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181106-766212a2-21db-4ca2-8bd7-6eae576ab071.jpeg#height=391&id=bg0Fr&originHeight=391&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181184-b71ed816-d9d0-4589-8678-0ff2b8669d1a.jpeg#height=727&id=llzOM&originHeight=727&originWidth=993&originalType=binary&ratio=1&size=0&status=done&style=none&width=993)
而对于By location on chromosome，是将基因定位于染色体上进行分析。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181112-bd93a65c-2c0b-4a2e-9df7-9f4dc3849863.jpeg#height=217&id=lKQr2&originHeight=217&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
结果如下：
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181244-ff18a941-36a8-4fb8-a5c9-8017904302cf.jpeg#height=822&id=nbucW&originHeight=822&originWidth=807&originalType=binary&ratio=1&size=0&status=done&style=none&width=807)


### (4).Experiment design and value distribution工具
这个工具就是一些箱线图

![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1610773181135-d8e27770-c2cb-4c71-9a54-1723cfed8b01.png#height=364&id=tlR6k&originHeight=364&originWidth=967&originalType=binary&ratio=1&size=0&status=done&style=none&width=967)
这就是每个样本中所有基因表达值的一个汇总，这是归一化后的箱线图，看起来质量不错。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181170-f77bcab3-df62-4f82-ad24-88fac7a4eb98.jpeg#height=903&id=hN7r4&originHeight=903&originWidth=545&originalType=binary&ratio=1&size=0&status=done&style=none&width=545)

### (5).GEO2R
GEO2R是一个交互式web工具，它允许用户比较GEO系列中的两组或两组以上的样本，以便识别在不同实验条件下表达不同的基因。结果显示为按重要性排序的基因表。
GEO2R使用Bioconductor项目中的GEOquery和limma R包对原始提交者提供的处理过的数据表执行比较。
与GEO的其他数据集分析工具不同，GEO2R不依赖于精心设计的数据集，而是直接查询原始的系列矩阵数据文件。这使得及时分析更多的地理数据成为可能。然而，重要的是要认识到，无论数据类型和质量如何，这个工具几乎可以访问和分析任何GEO系列。

在GSE检索结果页面就可以看到这个工具，这里以GSE49382为例，
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181116-efc48269-0bc4-47fb-9680-aff3103d4826.jpeg#height=400&id=f16L4&originHeight=400&originWidth=929&originalType=binary&ratio=1&size=0&status=done&style=none&width=929)
点击Analyze with GEO2R进入页面可以看见所有样本的信息列表
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181150-035ba3e8-031a-4cf6-a208-ad74be48d384.jpeg#height=540&id=p4g58&originHeight=540&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)

通过Define groups将样本进行分组,输入相应的组名，
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1610773181122-c8056737-4ce8-454a-a62a-96036f0a325c.png#height=260&id=nHl79&originHeight=162&originWidth=179&originalType=binary&ratio=1&size=0&status=done&style=none&width=287)
点击组A，会弹出一个对话框，让你选择要归入A组的样本，点击相应的样本即可（按住Crtl多选），我这里随便点。

![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181137-dd368768-f836-4781-9a3e-daffb96d8e7e.jpeg#height=342&id=rWG2X&originHeight=342&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)

点击Top250会显示前250个基因
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181200-013f342f-1349-42e6-a390-7f7a8a2e5103.jpeg#height=241&id=Cw5r4&originHeight=241&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
结果在浏览器中显示为按p值排列的前250个基因的表。p值最小的基因最显著。单击一行显示该基因的基因表达谱图。图中的每个红条表示从原始提交者提供的样例记录的value列中提取的表达式度量。

使用Select columns特性修改表中包含哪些数据和注释列。有关数据列含义的信息在Summary statistics部分中提供。
在Options选项卡中编辑测试参数，然后回到GEO2R选项卡并单击Recalculate来应用编辑。
要查看超过前250个结果，或者如果想保存结果，可以使用save all results按钮下载完整的结果表。下载的文件以制表符分隔，适合在Excel等电子表格应用程序中打开。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181285-a0673523-b4fc-40ee-8f5d-c837174bf1f9.jpeg#height=503&id=xwuDM&originHeight=503&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)

编辑options和features
#### （1）Value distribution
计算和查看所选示例值的分布。值是提交者提供的原始数据，在此基础上执行GEO2R计算。查看分布对于确定选择的样本是否适合进行比较非常重要。通常，以中间值为中心的值表示数据是标准化的和可交叉比较的。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181144-0a1764ff-c74f-419b-9737-8cfe7e122c00.jpeg#height=674&id=k8g0X&originHeight=674&originWidth=742&originalType=binary&ratio=1&size=0&status=done&style=none&width=742)

#### （2）Options

![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181138-cb31aab9-834c-4b83-be8d-fa149197a58b.jpeg#height=446&id=dqsuO&originHeight=446&originWidth=979&originalType=binary&ratio=1&size=0&status=done&style=none&width=979)
Apply adjustment to the P-values

Limma包提供了几个p值调整选项。这些调整，也称为多次测试纠正，试图纠正错误阳性结果的发生。默认选择Benjamini & Hochberg错误发现率方法，因为它是对微阵列数据最常用的调整，并在发现统计上重要的基因和限制假阳性之间提供了良好的平衡。

Apply log transformation to the data

GEO数据库接受各种数据值类型，包括logged和未logged的数据。Limma包需要使用logged数据为了解决这个问题，GEO2R有一个自动检测特性，它检查所选样本的值，并自动执行log2转换。可选择是否自动转换。

 Category of Platform annotation to display on results

选择要在结果上显示的注释类别。基因注释来自于相应的平台记录。有两种注释类型:

NCBI生成的注释可用于许多记录。这些注释是通过从平台中提取稳定的序列识别信息，定期查询Entrez基因和UniGene数据库，生成一致的、最新的注释而得到的。默认情况下选择基因符号和基因标题注释。NCBI生成的注释的其他类别包括GO术语和染色体位置信息。
提交者提供的注释可用于所有记录。这些表示提交者提供的原始平台注释。请注意，提交者提供的注释在样式和内容上有很多多样性，而且自提交时起可能就没有更新过。
#### （3）Profile graph
通过从平台记录的ID列输入相应的标识符来查看特定的基因表达谱图。此功能不执行任何计算;它只是在样本间显示基因的表达值。要使此功能正常工作，不需要定义示例组。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181141-0ddca2cf-db69-4ede-95f6-cb13146afc53.jpeg#height=303&id=U1ZbS&originHeight=303&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
#### （4）R script
此选项卡打印用于执行计算的R脚本。这些信息可以保存下来，作为计算结果的参考。
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1610773181240-0ac125a3-8d52-47ad-b136-586907527201.jpeg#height=348&id=yL4vZ&originHeight=348&originWidth=1080&originalType=binary&ratio=1&size=0&status=done&style=none&width=1080)
# 四. ArrayExpress 数据库使用教程
进到主页之后，我们可以先看一下这个数据库的信息，比如它是功能基因组数据，目前有74700个实验的数据，2556953个芯片数据，60.91TB的存档数据，这都是在描述ArrayExpres数据库的数据量的大小。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630052271282-b10c29f9-d2ce-4b3e-ae28-de951a4e22bf.png#clientId=ue984c4d8-a874-4&from=paste&height=392&id=u5f494ca8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=784&originWidth=1896&originalType=binary&ratio=1&size=189936&status=done&style=none&taskId=u98643f1d-e2a4-476a-b416-ef4229712c6&width=948)
了解完之后，我们可以在Search栏进行数据的搜索，举个栗子：我想要搜一个关于breast cancer 的研究，那我就输入关键字：breast cancer ，然后点击搜索。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630052517630-43e088d6-154b-4d6e-8ca2-a5c21d956d8c.png#clientId=ue984c4d8-a874-4&from=paste&height=308&id=u1792fbf3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=616&originWidth=1521&originalType=binary&ratio=1&size=116040&status=done&style=none&taskId=ue0ca34bf-ddf5-494b-b8c5-db94b81362e&width=760.5)
搜索完之后，我们看一下结果，有2896个实验的研究出来了，其中有一些可能不是你想要的，怎么办呢，咱们可以加一些过滤条件，限定一下，以减少实验研究的数量。"Filter search results"这个就是添加过滤条件的地方，我现在加一些条件，然后点击filter即可过滤。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630052632880-c5e4c70f-1d49-4b14-b0fb-97f4bd55c41a.png#clientId=ue984c4d8-a874-4&from=paste&height=418&id=u42f8b39e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=535&originWidth=438&originalType=binary&ratio=1&size=32808&status=done&style=none&taskId=u0dab22e6-8a87-4a9d-b621-2f21f2a9a7a&width=342)
过滤后的结果就少了很多。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630052712983-47a7bb67-5044-4285-80d0-7384c9b87aba.png#clientId=ue984c4d8-a874-4&from=paste&height=281&id=ufdea3d2d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=561&originWidth=1520&originalType=binary&ratio=1&size=130743&status=done&style=none&taskId=u40debbe3-307e-424b-b222-e69d4ad83f2&width=760)
我把出来的这个结果对应的每个字段解释一哈：（以E-MTAB-8310为例）
1. Accession:数据库ID，芯片的数据库编号；
2. Title:题目也就是文章的研究方向；
3. Type:实验类型，转录组分析；
4. Organism：物种，研究的物种是人；
5. Assays：芯片样本数，有8个样品；
6. Released:上传日期，2021年3月2号；
7. Processed：处理过的数据（包括：矩阵数据和单样品数据）。如果这里有下载的箭头，可以下载到它们。
8. Raw:原始数据链接，打开后可以下载数据。下载的页面如下。
我们可以点击Accession ID 查看该数据集的详细信息，该信息页面也有下载数据的地址。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630052957911-b5bcfe82-6879-4f3c-b6aa-e24e11b5ed59.png#clientId=ue984c4d8-a874-4&from=paste&id=ueb269301&margin=%5Bobject%20Object%5D&name=image.png&originHeight=721&originWidth=1149&originalType=binary&ratio=1&size=172571&status=done&style=none&taskId=uecf7f473-2d14-4c02-ae34-f547e533985)
参考：[https://mp.weixin.qq.com/s/UWMcXFjtydTU9W3JTnUrhA](https://mp.weixin.qq.com/s/UWMcXFjtydTU9W3JTnUrhA)
# 五. 芯片数据分析
## 1. 处理芯片数据的R包
芯片原始数据文件包括： ① 芯片图像扫描得到的记录光信号强度的Intensity文件 ② 包含芯片类型、探针排布等芯片具体设计信息的Design文件 ③ 包含探针注释信息、探针序列等信息的Annotation文件 ④ 包含样本分组、实验处理等信息的Targets文件。不同芯片厂商的文件格式不同，下面是三大厂商芯片数据相应文件的格式信息：
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630117712817-09b037f7-2dd7-4391-890a-fd2864b5e6cb.png#clientId=ue984c4d8-a874-4&from=paste&id=u199b8592&margin=%5Bobject%20Object%5D&name=image.png&originHeight=258&originWidth=606&originalType=binary&ratio=1&size=56968&status=done&style=none&taskId=u09bf8361-c216-4b46-a1f8-e6d972ec9a2)
原始芯片数据的来源： ①  GEO、ArrayExpres等多个存储芯片实验数据的数据库 ② 芯片公司的官方网站。
处理这些数据会用到下面这些R包：
affy/oligo；beadarray/lumi；limma ；AgiMicroRna ；GEOquery ；readr/readxl。
### (1). Affymetrix芯片
Affymetrix芯片原始数据最常用的格式是CEL格式，从读取原始数据到转化为基因表达量矩阵表格,可以使用affy ,oligo等R包进行数据的质量控制,背景矫正,数据标准化,其中标准化方法常用的为rma算法和mas5算法。
#### 1). affy包
R包affy用于读取Affymetrix芯片CEL文件，也可用于读取一些较早期的affy芯片数据，如3'IVT 芯片，常见的U133系列(GPL570、GPL57K GPL96) ，不适合用于读取较新的affy芯片类型，如Exon ST、 GeneSK SNP芯片。  affy读取CEL文件函数是`read.affybatch`/`ReadAffy` 读取后的对象类别：AffyBatch
#### 2). oligo包
oligo读取Affymetrix芯片CEL文件，也可以读取affymetrix的几乎所有芯片类型的CEL文件，此外，oligo还可读取Roche NimbleGen芯片的.xys原始数据文件 ，oligo读取CEL文件函数是`read.celfiles`，读取后的对象类别：

| 芯片数据 | 对象 |
| --- | --- |
| Expresssion arrays | ExpressionFeatureSet |
| Gene ST arrays | GeneFeatureSet |
| Exon ST arrays | ExonFeatureSet |
| SNP arrays | SnpFeatureSet |
| Tiling arrays | TilingFeatureSet |

### (2). Illumina芯片
Illumina芯片数据分析的4个起点： ① Pixel-level,每个像素点对应一个数据， tif/tiff 格式； ②  Bead-level,每个bead对应一个数据， 类似于affymetrix的单个probe数据， 具体数据包括txt/idat/Iocs /sdf/ xml等多种格式； ③ Summary-level,每个bead type对应 —个数据，类似于affy的probe set数据， txt/CSV 格式； ④ 公共数据库存储的表达矩阵数据，如 GEO/ArrayExpress，部分数据集已经过预处理，属于summary-level。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630119701339-1b6023a9-d14c-4e60-97a7-ca246f162e41.png#clientId=ue984c4d8-a874-4&from=paste&id=u428ecf54&margin=%5Bobject%20Object%5D&name=image.png&originHeight=521&originWidth=839&originalType=binary&ratio=1&size=402592&status=done&style=none&taskId=u7ae9cfc8-96ab-48ba-8a8e-551c63cc725)

使用iScan/BeadScan扫描图像及处理图像信息时，因软件的具体版 本和设置参数不同，产生多种不同格式的原始数据文件。 ① `.txtfiles`,包含所有beads坐标数据和已减去背景值的光信号强度值 ② `.tiffiles`,扫描后得到的图像文件 ③ `.Iocs files`,包含所有beads的坐标信息 ④ `.idatfiles`,专有的二进制文件用于储存光信号强度数据，可供 BeadStudio/GenomeStudio读取进行后续分析 ⑤ `.xml files`,包含仪器的扫描参数设置和提取光强度值数据的具体方法信息 ⑥ `.bgx files`,包含探针注释信息 ⑦ `Metrics.txt`,包含扫描芯片的质量参数信息 ⑧ `.sdf files`,包含样本/芯片的具体构架、布局信息 ⑨ IBS (Illumina Bead Summary) files，`.csv`格式，summary-level 数据。
#### 1). limma包
`read.ilmn`函数读取summary-level数据 ， `read.idat`读取idat数据。
#### 2). beadarray包 
`readlllumina`函数最常用，用于读取bead-level数据 ；`readTIFF`函数读取pixel-level图像数据 ；`readldatFiles`函数读取idat文件； `readLocsFile`函数读取.Iocs文件； `readBeadSummaryData`函数读取summary-level数据。
#### 3). lumi包
`lumiR`函数读取summary-level数据 ` lumiR.batch`函数批量读取summary-level数据 
#### 4). illuminaio包
` readIDAT`函数读取idat数据 ；`readBGX`函数读取.bgx文件。
### (3). Agilent芯片
#### 1). limma
limma包中的`read.maimages`函数不限于Agilent芯片数据，可用于读取多个平台芯片文件，但不适用于affymetrix及illumina芯片数据 ，可读取单色及双色芯片数据；可读取多种图像分析程序产生的txt数据，如：Agilent Feature Extraction, Arrayvision, BlueFuse, GenePix, ImaGene, QuantArray (Version 3 or later), Stanford Microarray Database (SMD)，SPOT。
#### 2). AgiMicroRna 
` readMicroRnaAFE` 函数适用于Agilent的miRNA芯片数据。
## 2. 数据下载与处理
数据下载方法： 可以通过GEO网站链接、FTP站点直接下载，也可以通过R 包 GEOquery 的 getGEOSuppFiles 函数下载，在Linux系统下，可以使用wgetx axek arial2等软件下载。
### (1). GEOquery包
#### 1). getGEO()函数
这个函数是GEOquery包中的主要用户级函数。它指导下载(如果没有指定文件名)，并将GEO SOFT格式文件解析为专门设计的R数据结构，使GEO SOFT格式的每个重要部分易于访问。
```r
getGEO(GEO = NULL, filename = NULL, destdir = tempdir(),
  GSElimits = NULL, GSEMatrix = TRUE, AnnotGPL = FALSE, getGPL = TRUE,
  parseCharacteristics = TRUE)
Arguments
```
 参数介绍：

| GEO | 用于下载和解析的表示GEO对象的字符串。(如。,‘GDS505’,‘GSE2’,‘GSM2’,‘GPL96’) |
| --- | --- |
| filename | 以前下载的GEO SOFT格式文件的文件名或它的gzip文件(在这种情况下，文件名必须以.gz结尾)。可以指定GEO或文件名中的一个，不能同时指定两个。GEO系列矩阵文件也进行了处理。注意，由于解析的是单个文件，所以返回值不是集合列表，而是解析GSE矩阵文件时的单个集合。 |
| destdir | 任何下载的目标目录。默认为当前工作目录。如果要保存文件供以后使用，您可能需要指定一个不同的目录。如果你的连接速度很慢，这样做是个好主意，因为有些GEO文件太大了! |
| GSElimits	 | 此参数只能用于从GSE加载GSMs的一个连续子集。它应该被指定为长度为2的向量，指定要加载的开始和结束(包括)GSMs。例如，这对于将大型GSE拆分为更易于管理的部分可能很有用。 |
| GSEMatrix | 一个布尔值，告诉GEOquery是否使用GEO的GSE Series Matrix文件。这些文件的解析比GSE SOFT格式文件的解析快许多数量级。默认为TRUE，意味着不会发生SOFT格式解析;如果出于某种原因需要GSE记录中的其他列，则设置为FALSE。 |
| AnnotGPL | 一个布尔值，默认值为FALSE，用于决定是否使用Annotation GPL信息。这些文件很好用，因为它们包含定期从Entrez Gene映射的最新信息。然而，它们并不适用于所有gpl;一般来说，它们只适用于GDS引用的GPLs |
| getGPL | 当获取GSEMatrix文件时，是否下载和包含GPL信息的布尔值默认为TRUE。如果你知道你将使用Bioconductor工具注释你的特征数据，而不是依赖于NCBI GEO提供的信息，你可能想把这个设置为FALSE。通过指定FALSE还可以大大减少下载时间。 |
| parseCharacteristics | 一个默认为TRUE的布尔值，用于判断是否解析GSE Matrix文件的特征信息(如果可用)。如果在解析特征时遇到麻烦，请将此设置为FALSE。 |

案例：
```r
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")

BiocManager::install("GEOquery")
gds <- getGEO(filename=system.file("extdata/GDS507.soft.gz",package="GEOquery"))
```
```r
gse2553 <- getGEO('GSE2553',GSEMatrix=TRUE)
show(gse2553)
show(pData(phenoData(gse2553[[1]]))[1:5,c(1,6,8)])
```
#### 2). getGEOSuppFiles()函数
NCBI GEO允许将补充文件附加到GEO系列(GSE)、GEO平台(GPL)和GEO样本(GSM)。这个函数“知道”如何获得基于GEO加入的这些文件。没有对下载的文件进行解析，因为计算机通常不知道文件格式。
```r
getGEOSuppFiles(GEO, makeDirectory = TRUE, baseDir = getwd(),
  fetch_files = TRUE, filter_regex = NULL)
```
参数介绍：

| GEO |  GEO accession number such as GPL1073 or GSM1137 |
| --- | --- |
| makeDirectory | 应该为下载的文件创建一个“子目录”吗?默认是正确的。如果为FALSE，文件将直接下载到baseDir中。 |
| baseDir | 下载的基本目录。默认是当前工作目录。 |
| fetch_files | 逻辑值。如果为TRUE，则实际下载文件。如果为FALSE，只返回将要下载的文件名。有用的测试和获得一个列表的文件没有实际下载。 |
| filter_regex | 一个字符(1)正则表达式，用于过滤来自GEO的文件名，以限制那些将被下载的文件。这有助于限制，例如，仅下载bed文件。 |

### (2). Affymetrix芯片原始数据的下载与处理
#### 1). 数据下载
这里以GEO数据库中的数据为例
```r
##下载芯片原始数据
ifelse(!dir.exists("geodata"),dir.create("geodata"),message("文件夹已存在"))
getGEOSuppFiles("GSE5823", baseDir ="geodata", makeDirectory = T)  # 新建一个文件夹
#getGEOSuppFiles("GSE5823", baseDir = "geodata", makeDirectory = F) # 不会新建对应的文件夹
```
也可以获取数据地址URL后使用download.file函数下载，但这种下载方式比较慢，不推荐。
```r
##获取下载链接 
data_url <- getGEOSuppFiles("GSE5823", fetch_files = F, makeDirectory = F)
##是一个数据框
url <- as.character(data_url$url)
#使用R函数download.file下载
download.file(url, destfile = "geodata/GSE5823.tar")
```
如果是在Linux系统中，获取下载链接后，使用axel软件下载。
Axel 是 CLI (command-line interface) 下的一个多线程下载工具，通常我都用它取代 wget 下载各类文件，适用于 Linux 及 BSD 等 UNIX 类平台。在Ubuntu 上安装 axel 命令是：`sudo apt-get install axel`。在CentOS上安装命令是：`sudo yum install axel`。
#### 2). 整理Targets文件
Targets文件包含样本信息的Tab分割的文本文件，每行对应一个芯片样本，每列对应样本名、样本分组、处理因素等变量信息 等，列名可以自己定义，该文件数据来源芯片原始数据文件，部分信息可能会整合在每个样本的原始数据文件中，但有时不全面，所以通常我们需要从GSE数据主页的实验设计信息和原始文献中去获取，然后自己整理， GSE页面Samples栏目下常有简要分组、处理信息。比如数据集【GSE5823】：
[https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5823](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE5823)
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630242330859-3f1ad290-cded-4dac-98b2-0b222da8b0af.png#clientId=ue984c4d8-a874-4&from=paste&id=u09d68953&margin=%5Bobject%20Object%5D&name=image.png&originHeight=559&originWidth=579&originalType=binary&ratio=1&size=51905&status=done&style=none&taskId=u52a47fdf-561f-46f1-a6b6-94bd5766db2)
我们可以将Samples的内容复制到一个txt文本中读入，然后进行整理。下面是我整理GSE5823数据集的代码。
```r
sampleInfo <- read.table("geodata/GSE5823/sampleInfo.txt",header = F,sep = "\t")
colnames(sampleInfo) <- c("sampleName","description")

celFileNames <- list.files("geodata/GSE5823/GSE5823_RAW",pattern = ".CEL.gz$",full.names = F)
sampleName <- str_split(celFileNames, pattern = "[.]", simplify = T)[,1]
celFlieInfo <- data.frame(fileName = celFileNames,sampleName = sampleName)
celFlieInfo <- merge(celFlieInfo,sampleInfo,by = "sampleName")
celFlieInfo$cellType <- str_split(str_split(celFlieInfo$description, pattern = "\\s+", simplify = T)[,3], 
                                 pattern = "_", simplify = T)[,1]
celFlieInfo$group <- ifelse(grepl("control",celFlieInfo$description),"control","c-myc KD")
write.table(x = celFlieInfo,
            file = "geodata/GSE5823/Targets.txt",
            quote = F,
            sep = "\t",
            row.names = F)
```
得到的信息如下，说白了，Targets文件就是样本信息，文件名对应的样本名称，分组等信息而已，你可以用Excel整理也是可以的，总之最后在R中读入可以得到类似下面的数据框就行。列名没有特殊要求，内容有一列就文件名称。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630242613469-8967efac-cf9d-4b68-a958-3ba49dd1fd55.png#clientId=ue984c4d8-a874-4&from=paste&id=u1b7d1b4c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=205&originWidth=1029&originalType=binary&ratio=1&size=48652&status=done&style=none&taskId=ub91eda00-69ca-4522-9612-281944b86b1)
#### 3). 数据读入
根据前面介绍的R包，读入数据的函数很多。affy包中有2个读取CEL文件的函数：`read.affybatch()`和`ReadAffy()`。
```r
library(affy)
cel_files <- affy::list.celfiles("geodata/GSE5823/GSE5823_RAW", 
                                 full.name = T)
## affy包中有2个读取CEL文件的函数，推荐ReadAffy(),更灵活易用
cel1 <- read.affybatch(filenames = cel_files)
```
`affy::list.celfiles()`函数先获取cel文件的完整路径，其实与`list.files()`和`dir()`函数通过正则表达式获取一样，就是cel文件的路径而已。
```r
cel_files
list.files(path = "geodata/GSE5823/GSE5823_RAW", pattern = ".CEL.gz$",
           full.name = T)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630243276694-f0703b2a-9082-43fd-9a08-572a28a3fb35.png#clientId=ue984c4d8-a874-4&from=paste&id=u859e9607&margin=%5Bobject%20Object%5D&name=image.png&originHeight=582&originWidth=1266&originalType=binary&ratio=1&size=217479&status=done&style=none&taskId=u3467a11d-767e-4826-b34b-946059e1767)
接着我们接可以通过read.affybatch()函数读取了，这里的参数就是前面的cel文件路径。
```r
cel1 <- read.affybatch(filenames = cel_files)
```
查看一下cel1这个数据的类型：AffyBatch类
```r
> class(cel1)
[1] "AffyBatch"
attr(,"package")
[1] "affy"
```
这里我们可以看一下里面的信息，AffyBatch对象是一个S4类，你可以通过@符号索引出来看看里面的内容。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630243708251-8dbf46e2-9083-4eb4-a5d2-23d73abe2345.png#clientId=ue984c4d8-a874-4&from=paste&id=u2e3211bc&margin=%5Bobject%20Object%5D&name=image.png&originHeight=272&originWidth=595&originalType=binary&ratio=1&size=27169&status=done&style=none&taskId=u964c77b1-c919-48ac-b317-608dfe157f1)
比如：`head(cel1@assayData[["exprs"]])[,1:3]`
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630243917141-e16fc96b-40ad-43db-b232-27a30eec166e.png#clientId=ue984c4d8-a874-4&from=paste&id=u3d28a40f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=232&originWidth=725&originalType=binary&ratio=1&size=25100&status=done&style=none&taskId=uaf6f50c4-78b1-43b7-b44f-9dc894e73a9)
其实这个就是我们的表达数据了，列名数文件名，具体信息可以通过前面整理的Targets文件来识别。
下面是通过ReadAffy()函数来读入，这个函数读入需要Targets文件信息。Targets这个数据框的行名最后是获取矩阵的列名，所以可以把Targets这个数据框的行名设置成对应的样本名称。
```r
Targets <- read.table("geodata/GSE5823/Targets.txt",header = T,sep = "\t")
rownames(Targets) <- Targets$sampleName
cel2 <- ReadAffy(filenames = Targets$fileName,
                         celfile.path = "geodata/GSE5823/GSE5823_RAW",
                         phenoData = Targets)
# 表达矩阵 exprs
head(exprs(cel1))[, 1:5]
head(exprs(cel2))[, 1:5]
affexp <- exprs(cel2)
```
得到的cel2对象和cel1是一样的。可以像前面一样通过索引的方式提取矩阵，但我们有现成的轮子，可以直接通过`exprs()`函数直接提取出来。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630244369522-a7a2ebd2-7c8a-4f4d-a3fe-580386744643.png#clientId=ue984c4d8-a874-4&from=paste&id=u7f803ceb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=430&originWidth=1124&originalType=binary&ratio=1&size=60200&status=done&style=none&taskId=u3e1e78d4-41e8-4f41-8ab2-22e78eaa0b1)
我们可以看到2个函数提取的数据是一样的。就是列名有点不同，有Targets文件的话，用`ReadAffy()`函数会好一些。样本数少，`read.affybatch()`函数可能会更加方便。
得到的数据可以保存为R对象：
```r
GSE5823_data <- cel2
save(GSE5823_data,file="geodata/GSE5823/GSE5823_data.Rdata")
```
#### 4). 数据质量评估
芯片数据的获取经历多个步骤，每个环节都有可能出现问题: 

- ① 样本收集：准备细胞、组织、动物样本；样本的储存 
- ② RNA提取：DNA污染？ RNA降解？ 
- ③ 荧光标记/探针杂交：RNA反转录、标记、杂交、清洗 
- ④ 图像扫描：信号的检测、转换、数据存储 
- ⑤ 从图像提取信号值：匹配坐标与探针、提取前景和背景信号值 

质量评估是芯片数据分析过程中不可缺少的步骤 ：单个芯片的水平(array level) ；整个实验设计分组的水平(experimental level)；针对芯片原始数据(raw data)的评估；针对标准化处理后的数据(normalized data)的评估。
Affymetrix芯片数据质量评估的R包有： affy, affyPLM, simpleaffy, arrayQualityMetrics
下面我们加载前面处理得到的数据。
```r
####  加载Affymetrix芯片GSE5823数据 ----
load("geodata/GSE5823/GSE5823_data.Rdata")#变量名GSE5823_data
library(affy)
GSE5823_exp <- exprs(GSE5823_data)#提取表达矩阵
head(GSE5823_exp)[, 1:5]
GSE5823_targets <- pData(GSE5823_data) #就是前面Targets的信息，在phenoData中的data
```
查看数据。
```r
###  查看数据----
affy::pm(GSE5823_data)[1:5, 1:5]# perfect matches 
affy::mm(GSE5823_data)[1:5, 1:5]# mismatches 这是一个背景数据，没有完全匹配的数据
GSE5823_exp[1:5, 1:5]

affy::pm(GSE5823_data)[1, 1:5]#369707这是id号
GSE5823_exp["369707", 1:5]#定位到369707这一行，发现两者是一致的
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630292289110-7ebdacf4-6a15-4b4f-a1d5-9457bb75144d.png#clientId=ue984c4d8-a874-4&from=paste&id=u959f1fe4&margin=%5Bobject%20Object%5D&name=image.png&originHeight=808&originWidth=1254&originalType=binary&ratio=1&size=140418&status=done&style=none&taskId=ufc3f1698-b345-4887-9e6b-4d21af3afa1)
查看某一探针集的表达情况。
```r
## 查看某个探针集的表达情况 
library(tidyverse)#%>% 管道符就是tidyverse里的

GSE5823_pm_1007 <- affy::pm(GSE5823_data, "1007_s_at") %>% 
  as.data.frame() %>% 
  rownames_to_column("probe_id") %>% 
  pivot_longer(cols = starts_with("GSM"),
               names_to = "sampleName",
               values_to = "pm_value") %>% 
  left_join(GSE5823_targets %>% dplyr::select(sampleName, group), 
            by = "sampleName") %>% 
  mutate(probe_id = factor(probe_id, levels = c(paste0("1007_s_at", 1:16))))

ggplot(GSE5823_pm_1007, aes(x = probe_id, y = pm_value, col = group)) +
  geom_point() +
  labs(x = "Probe set 1007_s_at", y = "Intensity of PM values") +
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5))
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630292703445-e6e09a40-f9a1-44a5-a841-6798e011a07d.png#clientId=ue984c4d8-a874-4&from=paste&id=u6abe21df&margin=%5Bobject%20Object%5D&name=image.png&originHeight=573&originWidth=642&originalType=binary&ratio=1&size=33267&status=done&style=none&taskId=u73754bfa-dd6a-4eca-85be-7e3673f6c5c)
我们可以将数据转换为图片信息。
```r
image(GSE5823_data[, 1], main = GSE5823_targets$sampleName[1])
image(GSE5823_data[, 2], main = GSE5823_targets$sampleName[2])
image(GSE5823_data[, 6], main = GSE5823_targets$sampleName[6])

dir.create("geodata/GSE5823/GSE5823_plots/")
for (i in 1:20) {
  tiff(filename = paste0("geodata/GSE5823/GSE5823_plots/",
                         GSE5823_targets$sampleName[i], "_", i,".tif"),
       height = 10,
       width = 10,
       units = "in",
       res = 300)
  image(GSE5823_data[, i], main = GSE5823_targets$sampleName[i])
  dev.off()
}
```
可以根据图片的亮点分布是否均匀看数据质量好坏。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630293069696-c1e7e29d-d0c3-416e-a50c-d9d0e384e45b.png#clientId=ue984c4d8-a874-4&from=paste&height=287&id=ua4737cca&margin=%5Bobject%20Object%5D&name=image.png&originHeight=573&originWidth=642&originalType=binary&ratio=1&size=212110&status=done&style=none&taskId=uded6cba7-5815-4d29-be52-ab88981aa60&width=321)![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630293034554-ff0b371f-4337-4195-b735-402dc2ce93e4.png#clientId=ue984c4d8-a874-4&from=paste&height=287&id=u7d08d101&margin=%5Bobject%20Object%5D&name=image.png&originHeight=573&originWidth=642&originalType=binary&ratio=1&size=214685&status=done&style=none&taskId=u50201048-b433-4580-b1e3-90233d6af1f&width=321)
我们可以查看芯片的扫描时间。这个日期可作为一种重要的批次效应因素。
```r
GSE5823_targets$batch <- GSE5823_data@protocolData@data$ScanDate %>% 
  str_sub(1, 8)#提取时间日期(年月日)，去掉具体详细的时间点。
GSE5823_targets$batch
table(GSE5823_targets$batch)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630293449236-263a6e0d-4097-43d5-ad63-56493cd04ad3.png#clientId=ue984c4d8-a874-4&from=paste&height=178&id=u3c04f90d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=282&originWidth=1197&originalType=binary&ratio=1&size=45247&status=done&style=none&taskId=u22dc7b69-073f-44cf-9d72-6f56cf68b56&width=754.5)
20个样本分了2批，还是有明显的批次效应的，但也不是说同一个数据集中就有问题。需要根据实验信息判断。比如我们这里的数据集中，是不同细胞control组和c-myc敲低组的芯片数据，如果每种细胞类型是通一批次的，不影响，因为我们分析的时候是按同一细胞类型去分析，但如果同一实验设计中，不同批次，那我们需要注意。这个数据会带来批次效应。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630293581885-7940e27c-2a97-4135-bb70-350f55be3568.png#clientId=ue984c4d8-a874-4&from=paste&height=280&id=ude45dab9&margin=%5Bobject%20Object%5D&name=image.png&originHeight=249&originWidth=666&originalType=binary&ratio=1&size=34386&status=done&style=none&taskId=u2ec3889d-cf01-4a85-85d9-e203df39f62&width=749)评估RNA的讲解程度：RNA降解从5‘端开始降解，所5'信号值要比3'信号值低一些，所以假如低得多了，斜率就大了，说明降解得很厉害。
```r
#评估RNA的讲解程度
RNAdeg <- AffyRNAdeg(GSE5823_data)
summaryAffyRNAdeg(RNAdeg)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630294076194-6edc5558-c22f-49d6-af00-c89d364a27de.png#clientId=ue984c4d8-a874-4&from=paste&id=u1cd36207&margin=%5Bobject%20Object%5D&name=image.png&originHeight=279&originWidth=1250&originalType=binary&ratio=1&size=46744&status=done&style=none&taskId=u0dc417d2-5dcc-491f-8564-0bd58086a5c)
可以可视化查看：
```r
cols <- rainbow(nrow(GSE5823_targets))
plotAffyRNAdeg(RNAdeg, cols = cols)
legend("bottomright",
       ncol = 2,
       legend = sampleNames(GSE5823_data), 
       lty = 1, 
       lwd = 2,
       cex = 0.8,
       box.lty=0,
       bg = "transparent",
       col = cols)
box()
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630294335470-6d682f0b-50fe-4660-90f0-42b90ee93bb0.png#clientId=ue984c4d8-a874-4&from=paste&height=430&id=uf481d246&margin=%5Bobject%20Object%5D&name=image.png&originHeight=573&originWidth=516&originalType=binary&ratio=1&size=33992&status=done&style=none&taskId=u977a68bb-9b87-4ed3-82f3-a329ab92776&width=387)
simpleaffy包的质量评估函数qc()函数可以查看数据的质量。
```r
library(simpleaffy)
GSE5823_qc <- simpleaffy::qc(GSE5823_data)
plot(GSE5823_qc)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630294577062-a61d433b-31e9-460e-b9bc-766a51e68700.png#clientId=ue984c4d8-a874-4&from=paste&id=ud0c870e2&margin=%5Bobject%20Object%5D&name=image.png&originHeight=649&originWidth=1044&originalType=binary&ratio=1&size=59791&status=done&style=none&taskId=u7d7878cc-8e17-4a5f-bbcd-eb9dcc74233)

这里的 P/M/A 分别代表 present/ marginal present/ absent
绘制箱型图，颜色是根据不同细胞类型设定。
```r
#箱线图
library(RColorBrewer)
display.brewer.all()
col <- brewer.pal(4, "Set2")
cols <- c(rep(col[1],4), rep(col[2],6),rep(col[3],4),rep(col[4],6))
boxplot(GSE5823_data, las = 2, 
        col = cols )
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630298391767-90b64a1b-1322-4c1e-b5a8-b6d5d23613b9.png#clientId=ue984c4d8-a874-4&from=paste&height=520&id=uc0b33c62&margin=%5Bobject%20Object%5D&name=image.png&originHeight=693&originWidth=701&originalType=binary&ratio=1&size=33125&status=done&style=none&taskId=u47ee4ed9-15dc-42a9-a04b-056d8428a99&width=526)
我们发现同一实验设计中，数据直接还是有差异的。
绘制密度分布图查看一下表达值的分布情况。
```r
#密度图
hist(GSE5823_data, lty = 1:3, col = cols)
legend(x=12,
       y=0.85,
       legend = sampleNames(GSE5823_data),
       lty = 1:3,
       cex = 0.8,
       col = cols,
       box.col = "transparent",
       xpd = TRUE)
box()
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630298356483-d4ce0102-3317-40a5-be48-62d6a00b7d78.png#clientId=ue984c4d8-a874-4&from=paste&height=520&id=u6eb1d1f6&margin=%5Bobject%20Object%5D&name=image.png&originHeight=693&originWidth=701&originalType=binary&ratio=1&size=52246&status=done&style=none&taskId=u649d4bb9-cf4a-4563-a7f3-9a2ee13c8be&width=526)
看见表达值的分布有的高有的低，整体来看的话说明是有问题的。
Deseq2包的的PCA函数进行主成分分析查看一下数据的分类情况。我这里的数据集有不同的细胞，所以我按照细胞类型来看。
```r
#参考了Deseq2包来写的PCA函数
PCA_new <- function(expr, ntop = 500, group, show_name = F){
  library(ggplot2)
  library(ggrepel)
  rv <- genefilter::rowVars(expr)
  select <- order(rv, decreasing = TRUE)[seq_len(min(ntop, length(rv)))]
  pca <- prcomp(t(expr[select, ]))#最核心的代码
  percentVar <- pca$sdev^2/sum(pca$sdev^2)
  d <- data.frame(PC1 = pca$x[, 1], 
                  PC2 = pca$x[, 2], 
                  group = group, 
                  name = colnames(expr))
  attr(d, "percentVar") <- percentVar[1:2]
  if (show_name) {
    ggplot(data = d, aes_string(x = "PC1", y = "PC2", color = "group")) + 
      geom_point(size = 2) +
      xlab(paste0("PC1: ", round(percentVar[1] * 100), "% variance")) + 
      ylab(paste0("PC2: ", round(percentVar[2] * 100), "% variance")) +
      geom_text_repel(aes(label = name),
                      size = 3,
                      segment.color = "black",
                      show.legend = FALSE )
  } else {
    ggplot(data = d, aes_string(x = "PC1", y = "PC2",color = "group")) + 
      geom_point(size = 2) +
      xlab(paste0("PC1: ", round(percentVar[1] * 100), "% variance")) + 
      ylab(paste0("PC2: ", round(percentVar[2] * 100), "% variance"))
  }
}

PCA_new(log2(GSE5823_exp), 
        nrow(GSE5823_exp), 
        group = GSE5823_targets$cellType,
        show_name = T)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630298786576-f9d5e9a4-cc3c-422b-9748-311daaa4df6b.png#clientId=ue984c4d8-a874-4&from=paste&height=520&id=u67a5bc81&margin=%5Bobject%20Object%5D&name=image.png&originHeight=693&originWidth=701&originalType=binary&ratio=1&size=40505&status=done&style=none&taskId=u096471b4-abe0-4260-908e-77c91855eb8&width=526)
但我们做评估的话，这样慢慢看效率是很低下的，有专门的函数生成数据的评估报告。arrayQualityMetrics包就可以用来评估数据，会在设定的文件加下生成很多文件，可以打开index.html网页文件打开查看。
```r
library(arrayQualityMetrics)
dir.create("geodata/GSE5823/GSE5823_QC_raw")
arrayQualityMetrics(GSE5823_data, 
                    outdir = "geodata/GSE5823/GSE5823_QC_raw", #通过该文件夹下的index来看结果
                    force = TRUE,#如果本身有个文件夹的话就把文件夹刷新了
                    intgroup = "group",#GSE5823_data@phenoData@data[["group"]]
                    do.logtransform = TRUE)
dev.off()
```
打开index.html网页文件。网页顶部有报告的目录信息，分为5部分。我们可以慢慢的查看。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630306907380-eba22419-cc4e-4810-9d1e-4e0eec9df50a.png#clientId=ue984c4d8-a874-4&from=paste&height=347&id=uf194758b&margin=%5Bobject%20Object%5D&name=image.png&originHeight=462&originWidth=480&originalType=binary&ratio=1&size=46482&status=done&style=none&taskId=u71a142b9-16e6-4596-8fb7-2bf24f2455d&width=360)
可以根据下面这个图来确认数据的好坏，有×的点，代表该数据样本在对应的方法检测下是不合格的数据。如果数据样本多，可以去除不合格的样本，数据样本少的时候没法，但如果一个样本6种检测方法中有3个即以上都不通过，说明数据是有问题的。当然，有的作者也使用。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630307051833-86e497c0-db5f-47c6-ae42-cc997a94cfeb.png#clientId=ue984c4d8-a874-4&from=paste&height=401&id=ufc4e3916&margin=%5Bobject%20Object%5D&name=image.png&originHeight=534&originWidth=773&originalType=binary&ratio=1&size=96824&status=done&style=none&taskId=u97c0d2f5-3d5b-45f9-995d-cc5761d36d6&width=580)![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630307160276-6deac82b-4b22-4404-8ab1-81e7c46197ea.png#clientId=ue984c4d8-a874-4&from=paste&id=ue5e72838&margin=%5Bobject%20Object%5D&name=image.png&originHeight=144&originWidth=557&originalType=binary&ratio=1&size=15795&status=done&style=none&taskId=u714e4835-afe6-45ee-a9f6-0a952de6594)
这6种方法对应的可视化图片在网页下面可以查看。
#### 5). 数据的背景校正
Affymerix芯片背景校正的主要R包：从CEL文件读取后的数据出发，可使用affy包及oligo包中的相应函数处理。
Affymetrix芯片原始数据的背景校正可以用affy包中的bg.correct()函数。该函数提供5种计算方法，最常用rma方法。可以通过bgcorrect.methods()查看这5种方法。这里不需要了解各种算法，就用rma方法就行了。
```r
library(RColorBrewer)
display.brewer.all()
col <- brewer.pal(4, "Set2")
cols <- c(rep(col[1],4), rep(col[2],6),rep(col[3],4),rep(col[4],6))
bgcorrect.methods()
GSE5823_bgc <- affy::bg.correct(GSE5823_data, method = "rma")#最常用rma方法
#背景矫正后作图
boxplot(GSE5823_bgc, las = 2, col = cols)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630308008816-c8c4b2fa-eee4-4e9c-9065-0c7e71be7f87.png#clientId=ue984c4d8-a874-4&from=paste&height=520&id=ud369a5ba&margin=%5Bobject%20Object%5D&name=image.png&originHeight=693&originWidth=701&originalType=binary&ratio=1&size=35865&status=done&style=none&taskId=u474cd58c-da03-420c-9bb3-ee46c0bb09a&width=526)
可以比较一下，前面数据质量报告，GSM136093和GSM136094这2个样本在质量评估中6种检测方法是不合格的，这里背景校正后还是和另外4个是有偏离的，可以从前面的质控报告汇中看到，这2个样本的扫描时间和其他的不一样，这可能就是批次效应带来的误差所引起的。所以这2个数据是需要去除的。类似的还有GSM136084这个样本。
再做一个主成分分析看看。
```r
PCA_new(log2(exprs(GSE5823_bgc)), 
        nrow(GSE5823_bgc), 
        group = GSE5823_targets$cellType,
        show_name = T)

PCA_new(log2(exprs(GSE5823_bgc)), 
        nrow(GSE5823_bgc), 
        group = GSE5823_targets$group,
        show_name = T)
```

![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630308417005-126d49bd-44b5-4e14-9b80-f59cfde9fe50.png#clientId=ue984c4d8-a874-4&from=paste&height=320&id=u894731e0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=597&originWidth=701&originalType=binary&ratio=1&size=37638&status=done&style=none&taskId=uac92ec33-d88d-4abf-8940-98e62ec6856&width=375.5)![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630308481417-d863850e-9ef9-447d-b896-3c305b6d5eaa.png#clientId=ue984c4d8-a874-4&from=paste&height=299&id=ue35fcbe8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=597&originWidth=701&originalType=binary&ratio=1&size=36797&status=done&style=none&taskId=u2a89afc4-803d-4f23-a565-172e0c4eca2&width=350.5)

从细胞类型来看的确分为了4个类别，这个和符合，本身就是不给不同的实验设计。但同一实验设计中就不是那么好了，只有MCF-7细胞这组的实验设计能很好的将control组和敲低组区分出来。
#### 6). 芯片数据标准化
通过对芯片数据标准化可以弥补一部分系统偏差对数据的影响 ，使各个样本芯片数据的分布相似，使不同的芯片之间可以进行比较 。
芯片数据标准化方法类别： 

- ① 基于所有基因的标准化，需要满足两个假设前提： 一是不同样本中的绝大部分基因表达是稳定不变的 ，二是上调和下调的基因数量是相似的，具有对称性。 
- ② 基于管家基因的标准化 ：认为管家基因在不同的处理条件下均是恒定的 
- ③ 基于芯片实验中设置的已知表达水平的对照基因 

对于Affymerix芯片来说，rma或者gcrma已经把背景矫正整合进去了，所以没有必要单独做背景矫正。我们先来看rma方法。
```r
GSE5823_rma <- affy::rma(GSE5823_data)#用的是原始cel数据，不是背景矫正后的数据
boxplot(GSE5823_rma, las = 2, col = cols)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630309393710-648413fc-5e8e-4bd9-bef3-ae44c664f38e.png#clientId=ue984c4d8-a874-4&from=paste&height=335&id=u0358b0dc&margin=%5Bobject%20Object%5D&name=image.png&originHeight=446&originWidth=701&originalType=binary&ratio=1&size=21081&status=done&style=none&taskId=ue9de94a5-075a-4b49-9ea9-46b1de9ff6b&width=526)
**这里需要注意，我这里的数据集里面有4个不同的实验设计，一起校正。我认为，真正分析的时候，将他们区分出来，分别校正，会好一些**。
```r
GSE5823_rma_BT474 <- affy::rma(GSE5823_data[,1:4])
boxplot(GSE5823_rma_BT474, las = 2, 
        col = rep(c("#66C2A5","#FC8D62"),2))
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630309848183-883b92f9-8b16-42fc-8724-59e8b864aa24.png#clientId=ue984c4d8-a874-4&from=paste&height=388&id=uc711d15a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=517&originWidth=701&originalType=binary&ratio=1&size=18495&status=done&style=none&taskId=u0a0f017b-0715-4ce4-aa47-36f75281376&width=526)
芯片数据标准化之后看数据质量是否改善。
```r
arrayQualityMetrics(GSE5823_rma, 
                    outdir = "affymetrix/GSE5823/GSE5823_QC_rma", 
                    force = TRUE,
                    intgroup = "group",
                    do.logtransform = TRUE)
```
和前面一样，就不多说啦。
下面我们使用gcrma方法进行标准化
```r
GSE5823_gcrma <- gcrma(GSE5823_data)
GSE5823_expr_gcrma <- exprs(GSE5823_gcrma)
boxplot(GSE5823_gcrma, las = 2, col = cols)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630310771990-8bc231fc-0c02-4c3c-9733-e1eacef99fac.png#clientId=ue984c4d8-a874-4&from=paste&height=388&id=u16ef0c1c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=517&originWidth=701&originalType=binary&ratio=1&size=24436&status=done&style=none&taskId=ub6012afe-651b-4c00-b529-3ee10a019aa&width=526)

标准化后的数据和未标准化的数据是有很大区别的。
```r
head(GSE5823_expr_gcrma)[,1:4]
head(GSE5823_exp)[,1:4]
dim(GSE5823_expr_gcrma)
dim(GSE5823_exp)
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630311364873-afb7d280-04cf-4756-9faa-8b6d52029f35.png#clientId=ue984c4d8-a874-4&from=paste&height=395&id=u91cfeacc&margin=%5Bobject%20Object%5D&name=image.png&originHeight=526&originWidth=644&originalType=binary&ratio=1&size=64727&status=done&style=none&taskId=u2c6a8d7c-92f6-46da-a534-7c6f31b33eb&width=483)
为标准化之前有135万行的数据，任何芯片都没有这么多探针的，我们标准化后就可以看见行名变成了探针名称，行数只有5万多。
我们在看，不同实验设计一起标准化合和分别标准化多多少少是有区别的。所以像本案例这类似的数据集，最好是分别标准化。
```r
GSE5823_gcrma_BT474 <- gcrma(GSE5823_data[,1:4])
GSE5823_expr_gcrma_BT474 <- exprs(GSE5823_gcrma_BT474)
head(GSE5823_expr_gcrma)[,1:4]
head(GSE5823_expr_gcrma_BT474)[,1:4]
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630311766451-2eb38936-50e8-4023-be43-67c7537dfb74.png#clientId=ue984c4d8-a874-4&from=paste&height=319&id=ue7de8a03&margin=%5Bobject%20Object%5D&name=image.png&originHeight=425&originWidth=651&originalType=binary&ratio=1&size=62646&status=done&style=none&taskId=ud30765b0-f032-4d60-9c1c-9fdc59a35b8&width=488)
同样标准化后可以再检测一下数据质量。
```r
arrayQualityMetrics(GSE5823_gcrma, 
                    outdir = "affymetrix/GSE5823/GSE5823_QC_gcrma", 
                    force = TRUE,
                    intgroup = "group",
                    do.logtransform = TRUE)
```





```r
sampleInfo <- read.table("geodata/GSE5823/sampleInfo.txt",header = F,sep = "\t")
colnames(sampleInfo) <- c("sampleName","description")

celFileNames <- list.files("geodata/GSE5823/GSE5823_RAW",pattern = ".CEL.gz$",full.names = F)
sampleName <- str_split(celFileNames, pattern = "[.]", simplify = T)[,1]
celFlieInfo <- data.frame(fileName = celFileNames,sampleName = sampleName)
celFlieInfo <- merge(celFlieInfo,sampleInfo,by = "sampleName")
celFlieInfo$cellType <- str_split(str_split(celFlieInfo$description, pattern = "\\s+", simplify = T)[,3], 
                                 pattern = "_", simplify = T)[,1]
celFlieInfo$group <- ifelse(grepl("control",celFlieInfo$description),"control","c-myc KD")
write.table(x = celFlieInfo,
            file = "geodata/GSE5823/Targets.txt",
            quote = F,
            sep = "\t",
            row.names = F)
```
#### 7). 缺失值处理
我们标准化后可能有缺失值，缺失值主要来自原始图像信息处理过程 、数据后续处理、转换过程。如果有，那么我们需要处理这些缺失值。补充缺失值的方法有邻近平均值局部法和删除等。
```r
#首先看一下有没有缺失值
> sum(is.na(exprs(GSE5823_gcrma)))
[1] 0
```
在R中，impute包提供的impute.knn()函数来补充缺失值，该函数使用最近邻平均替换缺失值。我们这里模拟一下，缺失值处理。
```r
library(impute)
na_test <- GSE5823_expr_gcrma

row_index <- sample(1:50000)[1:5]
col_index <- sample(1:20)[1:5]

na_test[row_index, col_index] <- NA#造出NA
sum(is.na(na_test))

na_knn <- impute.knn(na_test, maxp = 30000)#maxp默认的是1500，根据数据维度大小设置大些
sum(is.na(na_test))
#比较一下原始的和补充之后的数值
GSE5823_expr_gcrma[row_index, col_index]
na_knn$data[row_index, col_index]
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630314520914-1aa7a2ac-e880-4791-b51b-c5ebd4450cbb.png#clientId=ue984c4d8-a874-4&from=paste&height=288&id=u85c4b094&margin=%5Bobject%20Object%5D&name=image.png&originHeight=384&originWidth=803&originalType=binary&ratio=1&size=66919&status=done&style=none&taskId=uf2ee6484-0524-439c-a3f7-9b7306dd70c&width=602)
我们发现部分探针填补后和原来的缺失值是和大的。你可以多运行几次看看。部分探针没有差别，但部分还是差别很大。如果缺失值不多，缺失值所在的行不是你要的探针(不是你研究的探针/基因)，我个人觉得直接删除该行会好一些。
### (3). Illumina芯片原始数据的下载与处理
#### 1). 数据的下载
GEO数据库中，Illumina芯片原始数据下载后解压，哪怕同一芯片，里面的数据也有些不同，甚至有的有缺失，作者并没有上传，比如数据集GSE32873，下载后的原始数据里面只有探针的注释文件。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630458543141-b05915fe-6358-45e6-867e-3d1e0233fac1.png#clientId=ue984c4d8-a874-4&from=paste&height=194&id=ufc584201&margin=%5Bobject%20Object%5D&name=image.png&originHeight=259&originWidth=764&originalType=binary&ratio=1&size=26895&status=done&style=none&taskId=ue9690a56-c07d-48f7-8063-ad2d97589fe&width=573)
下面我们下载几个数据集来比较一下。
```r
library(GEOquery)
##下载芯片原始数据
ifelse(!dir.exists("geodata"),dir.create("geodata"),message("文件夹已存在"))
getGEOSuppFiles("GSE32873", baseDir ="geodata", makeDirectory = T) 
getGEOSuppFiles("GSE140882", baseDir ="geodata", makeDirectory = T) 
getGEOSuppFiles("GSE59183", baseDir ="geodata", makeDirectory = T) 
```
下载后得到的原始数据文件GSE***_RAW.tar。我们解压到GSE***_RAW文件夹下。你需要查看一下里面有没有注释信息的文件，下面是3个不同的数据集，它们使用的是同一芯片。解压后会有相同的GPL文件。我们还可以看到，除了这2个文件，其他的GSM开头的就是样本数据文件，但他们个格式有所不同。前面说过Illumina芯片数据分析的4个起点： ① Pixel-level,每个像素点对应一个数据， tif/tiff 格式； ②  Bead-level,每个bead对应一个数据， 类似于affymetrix的单个probe数据， 具体数据包括txt/idat/Iocs/sdf/xml等多种格式； ③ Summary-level,每个bead type对应 —个数据，类似于affy的probe set数据， txt/CSV 格式； ④ 公共数据库存储的表达矩阵数据。这就看作者上传的是什么数据文件，通常都是 Bead-level的数据文件，所以会有txt/idat/Iocs/sdf/xml这样的数据格式文件，比如数据集GSE59183，而且该数据集还有tif格式的数据文件。但在GSE140882数据集中只有txt格式的Bead-level的数据。GSE32873数据集里面处理GPL文件外，就没有其他的，也就是说没有原始数据，所以该数据集你无法从原始数据开始分析，但作者提供了非标准化的表达矩阵文件。

![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630458879744-f128b553-35ee-47f3-9210-080d7ff388ee.png#clientId=ue984c4d8-a874-4&from=paste&height=116&id=u682398e8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=155&originWidth=763&originalType=binary&ratio=1&size=16709&status=done&style=none&taskId=u5a4dfe2c-9880-44aa-bc63-e6faa187846&width=572)
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630458965380-43a49d5b-e5e0-4b4b-a98f-576103c88492.png#clientId=ue984c4d8-a874-4&from=paste&height=230&id=u43b480d6&margin=%5Bobject%20Object%5D&name=image.png&originHeight=316&originWidth=773&originalType=binary&ratio=1&size=41904&status=done&style=none&taskId=ub1c67995-35e0-447e-bed3-1486f00d783&width=562)
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630459214930-016146a2-5a97-4948-8744-637a3961016d.png#clientId=ue984c4d8-a874-4&from=paste&height=208&id=uc39df09c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=298&originWidth=749&originalType=binary&ratio=1&size=40529&status=done&style=none&taskId=uee14995b-8462-40d9-8526-c2051557384&width=524)
再如GSE108369这个数据集，解压后是还是压缩包需要进一步再解压。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630548085778-3441049a-18c0-48d9-a5e7-836cf68f4c0e.png#clientId=u1315abab-3476-4&from=paste&height=273&id=ua7e7458e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=364&originWidth=723&originalType=binary&ratio=1&size=54550&status=done&style=none&taskId=uee87cbe7-01ed-4733-91e5-06c2bba3e98&width=542)
#### 2). 数据的读入
关于 Illumina芯片原始数据读入使用什么R包在前面有介绍。数据的读入我们首先介绍beadarray包的`readIllumina()`函数。下面介绍`readIllumina()`函数。
```r
readIllumina(dir = ".", useImages = FALSE, 
             illuminaAnnotation = NULL, sectionNames = NULL, metricsFile = "Metrics.txt", 
             forceIScan = FALSE, dec = ".", sampleSheet="sampleSheet.csv",...)
```
dir就是数据所在的路径。useImages指定是否通过图像数据读入，设置为TRUE时，前体是有tif/tiff格式的数据。数据集GSE140882中是没有的，所以处理该数据集时不能通过这种方式。但数据集GSE59183数据很全，是可以的，其实就是如果useImage设置为TRUE，则使用文本文件中提供的珠子中心坐标从TIFF图像中提取强度。对于其他格式文件信息如下：

- .txt文本文件：列出数组部分中每个解码珠的ID、坐标和强度。强度经过了局部背景校正。如果useImages = FALSE，这些强度将用作分析的起点。
- .sdf文件：Illumina的整个芯片或SAM的样本描述文件。这在beadarray中用于确定剖面的物理属性。
- .locs文件：数组中所有珠子的位置(即包括所有无法解码的珠子)

illuminaAnnotation参数：指定生成数据的Illumina平台的字符串。这是可选的，将有助于自动化对表达式数据的一些分析。目前这个参数的选择是Humanv4, Humanv3, Humanv2, Humanv1, Mousev2, Mousev1, mouse1p1, Ratv1。比如这里的芯片是Illumina HumanHT-12 V4.0 expression beadchip，对应的就是Humanv4。
读入数据集GSE140882的数据。
```r
## 读取目录中的文件, bead-level
library(beadarray)
path1 <- "geodata/GSE140882/GSE140882_RAW/"
GSE140882_BLdata <- readIllumina(dir = path1)
##添加注释
annotation(GSE140882_BLdata) <-  suggestAnnotation(GSE140882_BLdata)

## 查看数据
head(GSE140882_BLdata[[10]])
slotNames(GSE140882_BLdata)
str(GSE140882_BLdata)
dim(GSE140882_BLdata)
## 保存数据
save(GSE140882_BLdata, 
     file = "geodata/GSE140882/GSE140882_beadlevel1.Rda")
```
因为这个数据集只有txt文件，没有其他的格式文件，所以在Targets中相应的变量为NA，如果有，这些数据也会被读入进来。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630463362511-f43966b4-0915-4cb1-9cf8-09af1c562803.png#clientId=u1315abab-3476-4&from=paste&height=293&id=u81d086a6&margin=%5Bobject%20Object%5D&name=image.png&originHeight=390&originWidth=953&originalType=binary&ratio=1&size=44280&status=done&style=none&taskId=ud7d63a63-ab54-4efa-99f7-c3551e8bd16&width=715)
取一个值看看，第一列是探针ID，第二列和第三列是坐标值，第四列是信号值，用来指示表达水平。
```r
> head(GSE140882_BLdata[[10]])
     ProbeID     GrnX      GrnY Grn
[1,]   10008 1266.670 14383.660 747
[2,]   10008 1816.482  2781.520 523
[3,]   10008 1944.487  3564.491 342
[4,]   10008 2116.688  1204.003 444
[5,]   10008  684.497  3372.999 639
[6,]   10008 1445.521  5622.521 554
```
dim函数查看数据维度，总共有27芯片，每个芯片有的Beads数也被列出来。
```r
> dim(GSE140882_BLdata)
 nArrays  nBeads1  nBeads2  nBeads3  nBeads4  nBeads5  nBeads6  nBeads7  nBeads8  nBeads9 nBeads10 
      27  1049985   979585  1032451   999011  1020257  1017478   987157   975496   976775   976596 
nBeads11 nBeads12 nBeads13 nBeads14 nBeads15 nBeads16 nBeads17 nBeads18 nBeads19 nBeads20 nBeads21 
  944583   953363  1029041  1043010  1095933  1040761  1086987  1097331  1093468  1117748  1112479 
nBeads22 nBeads23 nBeads24 nBeads25 nBeads26 nBeads27 
 1115702  1126377  1120570  1120508  1125320  1122439 
```
接下来，读入GSE59183数据集，通过设置useImages参数来确认是否从TIF图像中读入数据。
```r
## 文件所在目录
path2 = "geodata/GSE59183/GSE59183_RAW"
## 读取目录中的文件, bead-level
library(beadarray)
data_ntiff <- readIllumina(dir = path2, useImages = F, dec = ".", 
                           illuminaAnnotation = "Humanv4")
data_tiff <- readIllumina(path2, useImages = T, dec = ".", 
                          illuminaAnnotation = "Humanv4")
head(data_ntiff[[1]])
head(data_tiff[[1]])

```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630462718750-4a40813c-8bdc-442b-bca2-29683e96222a.png#clientId=u1315abab-3476-4&from=paste&height=319&id=ua55f318e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=426&originWidth=739&originalType=binary&ratio=1&size=64599&status=done&style=none&taskId=u64f817c5-3345-4373-8571-bf593b0da90&width=554)
我们发现，useImages参数是否设置为TRUE，他们的信号强度值(Grn)不一样。GrnF是图片的前景值，GrnB是图片的背景值。前面介绍useImage设置为TRUE，则使用文本文件中提供的珠子中心坐标从TIFF图像中提取强度。前景值是从图像的锐化版本计算出来的。背景值计算为围绕珠心的17x17像素正方形中5个最低像素的中值。所以useImages参数是否设置为TRUE，导致计算的背景值方法不一样，所以Grn的值有区别，但整体的分析的差异应该是不大的。我们的原始数据中大多是没有tif格式的图像文件的，这种你就不用纠结要不是设置为TRUE，如果有，其实设置与否都行，我没有去比较这2者之间最后的差异。但我认为是没有太大差异的（我们验证过）。还要说一下Grn的值其实就是前景值(GrnF)减去背景值(GrnB)。背景值计算的算法参考文献如下：

- Kuhn K, Baker SC, Chudin E, Lieu MH, Oeser S, Bennett H, Rigault P, Barker D, McDaniel TK, Chee MS. A novel, high-performance random array platform for quantitative gene expression profiling. Genome Research. 2004;14(11):2347-2356
- Smith ML, Dunning MJ, Tavare S, Lynch AG. Identification and correction of previously unreported spatial phenomena using raw Illumina BeadArray data. BMC Bioinformatics. 2010;11:208

下面介绍一下计算过程。
首先我们需要读入tif文件。用readTIFF()函数读入，该函数一次只能读入一个文件。可以用lapply()函数遍历读入。
```r
### read TIFF 
tif_files_path <- list.files("geodata/GSE59183/GSE59183_RAW/", 
                        pattern = "tif$", full.names = T)
tif_data <- lapply(tif_files_path, function(p){readTIFF(p)})
```
我们去第一个图片信息查看一下
```r
head(tif_data[[1]])[,1:4]
dim(tif_data[[1]])
class(tif_data[[1]])
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630468251297-33e66b04-c531-4878-9b76-bd2236d9011e.png#clientId=u1315abab-3476-4&from=paste&height=251&id=u1c0bfde4&margin=%5Bobject%20Object%5D&name=image.png&originHeight=334&originWidth=581&originalType=binary&ratio=1&size=26218&status=done&style=none&taskId=u14b61f93-2a67-4116-8959-1e34f0a1e28&width=436)
读入的图片数据是一个矩阵。
我们将前面读入的 data_ntiff数据赋值给一个新变量进行操作。getBeadData()函数获取芯片数据。array=1，表示第一个芯片，what是芯片数据的列名。下面是提取第一个芯片的坐标信息。
```r
data <- data_ntiff
xcoords <- getBeadData(data, array = 1, what = "GrnX")
ycoords <- getBeadData(data, array = 1, what = "GrnY")
```
下面我们计算前面读入tif图片矩阵数据的背景值。有2个函数可以计算。medianBackground()函数和illuminaBackground()函数。2个函数计算结果差不多。
```r
bg <- medianBackground(tif_data[[1]], cbind(xcoords, ycoords))
bg2 <- illuminaBackground(tif_data[[1]], cbind(xcoords, ycoords))
```
将计算的背景值添加到data中。what指定添加数据的列名
```r
data <- insertBeadData(data, array = 1, what = "GrnRB", bg)
data <- insertBeadData(data, array = 1, what = "GrnRB2", bg2)
```
计算图形前景值，利用illuminaSharpen()函数先过滤一下数据，再用illuminaForeground()函数计算。backgroundCorrectSingleSection函数计算信号值（前景值-背景值=信号值）。
```r
# apply Illumina's image filtering
Tif <- illuminaSharpen(tif_data[[1]])
fg <- illuminaForeground(Tif, cbind(xcoords, ycoords))
data <- insertBeadData(data, array = 1, what = "GrnF", fg)
##
data <- backgroundCorrectSingleSection(data, array = 1, 
                                       fg = "GrnF", 
                                       bg = "GrnRB", 
                                       newName = "GrnR")
head(data[[1]])
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630472547814-3b79a841-fcd8-4d5a-9fa5-810cdb1ecf75.png#clientId=u1315abab-3476-4&from=paste&height=172&id=u80ec25a9&margin=%5Bobject%20Object%5D&name=image.png&originHeight=229&originWidth=912&originalType=binary&ratio=1&size=42311&status=done&style=none&taskId=uff80ddb5-cd3d-4645-9e22-0b9951d1488&width=684)
 我们可以看到我们自己计算的信号值GrnR与前面直接读入数据Grn是差不多的。也就是说， 对于illumina数据而言，就不需要矫正背景数据了，就没有了背景矫正这个环节，在useImages参数设置为TRUE时，得到的数据已经进行了背景校正。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630472987572-98c5bd8b-6411-4ff2-ada3-00919f6d4b4d.png#clientId=u1315abab-3476-4&from=paste&height=470&id=u9b7c25cd&margin=%5Bobject%20Object%5D&name=image.png&originHeight=627&originWidth=917&originalType=binary&ratio=1&size=109306&status=done&style=none&taskId=ud3c1a9e7-17e8-480f-ba98-f5cf742578d&width=688)
添加注释
```r
suggestAnnotation(data_ntiff, verbose = T)
annotation(data) <- suggestAnnotation(data, verbose = TRUE)
```
查看数据结构
```r
slotNames(data)
data@sectionData$Targets$greenImage
data@sectionData$Targets$textFile
head(data[[1]])
colnames(data[[1]])
sectionNames(data)
numBeads(data)
```
接着，我们读入idat的数据。使用readIdatFiles()函数读入数据。这里以这个数据集GSE113440为例
```r
idat_dir <- "geodata/GSE113440/GSE113440_RAW"
idat_files <- list.files(idat_dir, pattern = ".idat$", full.names = T)
## 读取idat files
library(beadarray)
GSE113440_idat <- readIdatFiles(idatFiles = idat_files)
```
可以通过索引的方式提取原始数据的表达矩阵
```r
## 原始表达矩阵数据
GSE113440_expr_idat <- GSE113440_idat@assayData$exprs
dim(GSE113440_expr_idat)
head(GSE113440_expr_idat)[,1:3]
```
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630503413021-9d9fb670-c09d-4eba-89e6-29bca305a8c7.png#clientId=u1315abab-3476-4&from=paste&height=214&id=u698eb5fb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=285&originWidth=1099&originalType=binary&ratio=1&size=48763&status=done&style=none&taskId=u91849fdf-c954-4f0e-809e-68e81b5c079&width=824)
保存数据用于后续的分析。
```r
save(GSE113440_idat,file = "geodata/GSE113440/GSE113440_idat.Rdata")
```
下面我们介绍如何使用lumi包读取illumina芯片数据。GSE108369这个数据集解压后需要处理一下，将所有GSM样本的txt文件放在同一目录下，方便后面处理。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630548514727-d8f0c543-0510-48de-893e-322dc84664d1.png#clientId=u1315abab-3476-4&from=paste&height=233&id=u17ef88c2&margin=%5Bobject%20Object%5D&name=image.png&originHeight=311&originWidth=799&originalType=binary&ratio=1&size=42045&status=done&style=none&taskId=u6c681e78-9fda-4ba0-a5d0-53cdd60f264&width=599)
虽然都是txt文件，用的芯片也是一样的，但这里面的数据有所区别，数据总共有6列。第一列就是探针，第二列是信号值的log值，第三列是原始的信号值，第5列是该探针的重复数(Beads数)，第四列就是该探针在所有beads中信号值的标准差，第6列就是p值。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630548775173-2d627d24-fc6d-48a6-aa1e-944ff1213d68.png#clientId=u1315abab-3476-4&from=paste&height=193&id=uf68abdb3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=257&originWidth=859&originalType=binary&ratio=1&size=34979&status=done&style=none&taskId=ud58e953f-c6b1-4f94-b42f-1c0573dce64&width=644)
先整理一个target文件：
```r
## 整理targets
library(tidyverse)
files
targets <- data.frame(FileName = files,
                      sample_id = str_match(files, "GSM\\d+")[, 1],
                      sample_name = str_match(files, "eum_(.*).txt")[, 2],
                      group = str_match(files, "eum_(.*)_")[, 2],
                      row.names = str_match(files, "GSM\\d+")[, 1],
                      stringsAsFactors = F)
```
我们去掉第二列的数据，其他列的列名"ProbeID", "AVG_SIGNAL","BEAD_STD",'Avg_NBEADS','DETECTION'都要加上样本ID，如下这种样子。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630551481922-59e3465b-73b2-4cbc-8b78-706f25a3ef0a.png#clientId=u1315abab-3476-4&from=paste&height=90&id=u686f3f69&margin=%5Bobject%20Object%5D&name=image.png&originHeight=120&originWidth=1184&originalType=binary&ratio=1&size=17333&status=done&style=none&taskId=ud3d2065f-3514-4a0c-a3c9-9cd3efce052&width=888)我们读入数据然后再重新命名列名后输出就可以啦。
```r
dir.create("geodata/GSE108369/GSE108369_RAW_processed")
for (i in 1:length(files)) {
  # read_tsv读入，dplyr::select选择第1列和第3到第6列
  tmp <- readr::read_tsv(files[i]) %>% dplyr::select(1,3:6)
  
  # 改列名
  colnames(tmp) <- paste0(c("ProbeID", "AVG_SIGNAL","BEAD_STD",'Avg_NBEADS','DETECTION'),
                          "_", targets$sample_id[i])
  # 写出
  readr::write_tsv(tmp, path = paste0("geodata/GSE108369/GSE108369_RAW_processed/", basename(files[i])))
  # write.table(tmp, file = basename(files[i]), sep = "\t", col.names = T,row.names = F, quote = F)
}
```
然后再读入重新命名列名的数据。
```r
## 应用 lumi读取文件 
library(lumi)
GSE108369_lumi <- lumiR.batch(fileList = paste0("geodata/GSE108369/GSE108369_RAW_processed/", 
                                                basename(files)), 
                              detectionTh = 0.01,
                              sampleInfoFile = targets)

## exprssion matrix
GSE108369_expr_lumi <- exprs(GSE108369_lumi)
dim(GSE108369_expr_lumi)
sum(is.na(GSE108369_expr_lumi))#判断是否有缺失值，如果有的话就返回1，再计算总和就可以知道有几个缺失值

## save data 
save(GSE108369_lumi, GSE108369_expr_lumi, 
     file = "geodata/GSE108369/GSE108369_lumi.Rdata")
```
最后介绍一下limma包读入数据，limma包中read.ilmn函数适合读入下面这种类型的数据，下载后的原始数据只在一个文件中。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630554641937-7e98300f-f1a8-4ea9-aa5b-c89b30620fde.png#clientId=u1315abab-3476-4&from=paste&height=163&id=ua10cb8ef&margin=%5Bobject%20Object%5D&name=image.png&originHeight=217&originWidth=824&originalType=binary&ratio=1&size=35741&status=done&style=none&taskId=ub4c62323-a974-477f-ad67-a4e63bfef45&width=618)
有一些是非标准化的数据。比如数据集GSE42242。
![image.png](https://cdn.nlark.com/yuque/0/2021/png/1234840/1630569626242-80ba2e41-2ac1-4144-a327-06f8db30cffd.png#clientId=u1315abab-3476-4&from=paste&height=164&id=lCkIa&margin=%5Bobject%20Object%5D&name=image.png&originHeight=252&originWidth=962&originalType=binary&ratio=1&size=46179&status=done&style=none&taskId=u03097219-8e56-402b-9310-2ce1aafdcaf&width=626)
```r
preview <- read_tsv("geodata/GSE42242/GSE42242_non-normalized.txt")
colnames(preview)

GSE42242_non_norm <- read.ilmn(files = "geodata/GSE42242/GSE42242_non-normalized.txt",
                               expr = "SAMPLE",#这里要根据数据实际的样子来改，有时候又变成了sample全
                               other.columns = "Detection",
                               probeid = "ID_REF")
head(GSE42242_non_norm$E)
dim(GSE42242_non_norm$E)
## save data 
save(GSE42242_non_norm, file = "geodata/GSE42242/GSE42242_non-normalized.Rdata")
```
但是有的不规则的，我们要重新改一下列名。比如GSE32873这个数据集。
```r
preview <- read_tsv("geodata/GSE32873/GSE32873_non_normalized.txt")
colnames(preview)
colnames(preview) <- c("ID_REF",
                       "AllStar_control_1","Detection.Pval",
                       "AllStar_control_2","Detection.Pval",
                       "AllStar_control_3","Detection.Pval",
                       "AllStar_UBE2C_1","Detection.Pval",          
                       "AllStar_UBE2C_2","Detection.Pval",          
                       "AllStar_UBE2C_3","Detection.Pval",          
                       "AllStar_MELK_1" ,"Detection.Pval",           
                       "AllStar_MELK_2" ,"Detection.Pval" ,          
                       "AllStar_MELK_3" ,"Detection.Pval"  
                       )
write.table(preview,file = "geodata/GSE32873/GSE32873_non_normalized_new.txt",
            sep = "\t",row.names = F,quote = F)
GSE32873_non_norm <- read.ilmn(files = "geodata/GSE32873/GSE32873_non_normalized_new.txt",
                               expr = "AllStar_",#这里要根据数据实际的样子来改，有时候又变成了sample全
                               other.columns = "Detection",
                               probeid = "ID_REF")
head(GSE32873_non_norm$E)
dim(GSE32873_non_norm$E)
## save data 
save(GSE42242_non_norm, file = "geodata/GSE32873/GSE32873_non-normalized.Rdata")
```
总结：我们解压后的数据文件，可以打开看一下，如果数据量很大，每个GSM整百万行的那种，一般都是bead-level的数据，用beadarray::readIllumina函数读取；对summary-level来说，如果是idat格式的，可以用 beadarray::readIdatFiles()来读取。看到数据有四列，"ProbeID", "AVG_SIGNAL", "BEAD_STD", 'Avg_NBEADS', 'DETECTION'，需要做转换，就是改个名字+GSM的ID，limma包读取一个列sample一列detection这种数据。
#### 3). 数据的标准化
**A.数据集GSE140882的标准化**
前面下载数据和读入的代码：
```r
library(beadarray)
library(tidyverse)
library(GEOquery)
##下载芯片原始数据
ifelse(!dir.exists("geodata"),dir.create("geodata"),message("文件夹已存在"))
getGEOSuppFiles("GSE140882", baseDir ="geodata", makeDirectory = T) 

path <- "geodata/GSE140882/GSE140882_RAW/"
GSE140882_BLdata <- readIllumina(dir = path)
## add annotation
annotation(GSE140882_BLdata) <-  suggestAnnotation(GSE140882_BLdata)
save(GSE140882_BLdata, 
     file = "geodata/GSE140882/GSE140882_beadlevel1.Rda")
```
加载前面处理的数据。提取targets仅仅是一部分信息，还需要自己整理。
```r
load(file = "geodata/GSE140882/GSE140882_beadlevel1.Rda")
BLdata <- GSE140882_BLdata
rm(GSE140882_BLdata)
targets <- BLdata@sectionData$Targets#
```




### (4). 下载SOFT格式的数据
```r
gset <- getGEO(GEO = "GSE7765",AnnotGPL=F ,destdir = "./geodata")
exp <- exprs(gset[[1]])
head(exp[,1:4])
```
```r
> head(exp[,1:4])
          GSM188013 GSM188014 GSM188016 GSM188018
1007_s_at 15630.200 17048.800 13667.500 15138.800
1053_at    3614.400  3563.220  2604.650  1945.710
117_at     1032.670  1164.150   510.692  5061.200
121_at     5917.800  6826.670  4562.440  5870.130
1255_g_at   224.525   395.025   207.087   164.835
1294_at     799.786   839.787   592.434   593.632
```
