# 一.单细胞转录组简介
单细胞 RNA 测序（Single cell RNA sequencing，scRNA-seq）是一种在单细胞水平上利用 RNA 测序对特定细胞群体进行基因表达谱定量的高通量实验技术。待测组织经过单细胞分离、RNA 提取、逆转录、文库构建和测序，便可利用数据分析获得多个细胞的基因表达谱。
## 1.单细胞测序与普通转录组测序的区别
普通转录组使用细胞混合物组成的样品进行测序，因此只能估计基因在细胞群中的平均表达水平，没有考虑样本中各个细胞的基因表达的异质性。无法分析早期发育组织或复杂组织的异质系统（如大脑组织等）。为克服这一限制，开发了单细胞水平的转录组测序技术（scRNA-seq）。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650698041431-f08e5da5-b4ce-4017-a769-f5e5d4f0e215.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=369&id=u8eeacabf&margin=%5Bobject%20Object%5D&name=image.png&originHeight=508&originWidth=1084&originalType=binary&ratio=1&rotation=0&showTitle=false&size=296588&status=done&style=none&taskId=ue28fbada-745e-4cd0-ad72-ea948044b8a&title=&width=788.3636363636364)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650715254247-1fe718b6-41a9-4018-824f-8248355c0432.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=501&id=u43604f64&margin=%5Bobject%20Object%5D&name=image.png&originHeight=689&originWidth=1538&originalType=binary&ratio=1&rotation=0&showTitle=false&size=330005&status=done&style=none&taskId=u5080dd28-3772-4a05-81c1-bfccff4b019&title=&width=1118.5454545454545)
## 2.单细胞测序的原理
单细胞测序技术以单个细胞作为对象，通过对单个细胞遗传物质均匀扩增，标记建库后进行测序，最后对单个细胞基因组或转录组展开数据分析，其技术原理主要包括单细胞分离、扩增测序和数据分析3方面。
单细胞分离：主要包括荧光激活细胞分选法( flow- activated cell sorting ，FACS) 以及微流控分选法( microfluidics) 等。市场上，较成熟的商业单细胞测序公司主要有 10X Genomis 公司 的Chromium( 液滴法) 及 BD 公司的Ｒhapsody( 微孔法)。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650715301398-583322c5-222b-4ebc-bdfd-eae06ac16f8f.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=492&id=u7f505163&margin=%5Bobject%20Object%5D&name=image.png&originHeight=677&originWidth=1255&originalType=binary&ratio=1&rotation=0&showTitle=false&size=171933&status=done&style=none&taskId=u6dd8ce96-983a-48ae-ad3e-495c1bf9071&title=&width=912.7272727272727)
### (1) 10×genomics技术
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650715398799-072b9eb2-cd03-4e93-b4af-1ec5d5ce45ff.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=597&id=Tymfn&margin=%5Bobject%20Object%5D&name=image.png&originHeight=821&originWidth=1768&originalType=binary&ratio=1&rotation=0&showTitle=false&size=468829&status=done&style=none&taskId=uc5a7b253-6966-4f24-9cf8-78c37173019&title=&width=1285.8181818181818)
首先在凝胶微珠上种上特定的DNA片段，DNA片段由三部分组成：Barcode、UMI、PolyT组成。Barcode是16个碱基的长度。一共有400万种Barcode，一个微珠是对应于一种Barcode，通过这400万种Barcode，可以把凝胶微珠给区分开。UMI是一段随机序列，也就是说每一个DNA分子，都有自己的UMI序列。10个碱基长的UMI，有100万种序列的变化（4^10 = 1,048,576），UMI的作用是为了区分哪些哪些reads是来自于一个原始cDNA分子，区分基因片段重复还是duplication及区分是真实的SNP位点还是PCR产生的突变。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650716254850-3916e61f-5b8a-4555-8def-b9dcec8aaf28.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=538&id=JVTUV&margin=%5Bobject%20Object%5D&name=image.png&originHeight=740&originWidth=1806&originalType=binary&ratio=1&rotation=0&showTitle=false&size=602118&status=done&style=none&taskId=u85d9dfed-1826-436a-ad30-d121444a752&title=&width=1313.4545454545455)

#### 3'端文库的构建
通过10×genomics仪器将单个细胞与单个凝胶微珠通过油相混在一起，形成油包水的小微滴，接下来把细胞膜破掉，让细胞当中的mRNA游离出来。游离出来的mRNA与小液滴中的水相混合，也就是和逆转录酶、结合在凝胶微珠上的核酸引物、以及dNTP底物相接触。接着，发生逆转录反应。mRNA与凝胶微珠上带标签的DNA分子相结合，在逆转录酶的作用下，逆转录出cDNA来。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650719903977-60da27ca-09c5-4640-90d0-2794a45f9742.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=215&id=Ct7aN&margin=%5Bobject%20Object%5D&name=image.png&originHeight=295&originWidth=1181&originalType=binary&ratio=1&rotation=0&showTitle=false&size=104158&status=done&style=none&taskId=ub60b7182-db66-4983-a778-3fb58aa05bb&title=&width=858.9090909090909)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650719943046-b9188746-f30a-4418-87a9-12628964721d.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=200&id=xWYx2&margin=%5Bobject%20Object%5D&name=image.png&originHeight=275&originWidth=1326&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106822&status=done&style=none&taskId=u09487d89-d908-48af-9a5e-4424ed41f72&title=&width=964.3636363636364)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650719987086-0e52567d-beec-4fe7-8759-5513a1195d0d.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=0.5891&from=paste&height=276&id=PhjUM&margin=%5Bobject%20Object%5D&name=image.png&originHeight=379&originWidth=1128&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135169&status=done&style=none&taskId=u174e127c-4ec9-4809-a13e-6c572a4f921&title=&width=820)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650720027867-db00de23-4746-4934-a798-4b34bd2ef97e.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=175&id=KJFaJ&margin=%5Bobject%20Object%5D&name=image.png&originHeight=240&originWidth=1130&originalType=binary&ratio=1&rotation=0&showTitle=false&size=95625&status=done&style=none&taskId=u9d404260-5280-4b27-a720-eee4f88d776&title=&width=821.8181818181819)
把这个乳浊液当中所有的水相抽出来，也就是把所有带了标签的cDNA分子都抽出来，再把这些cDNA分子都加上接头，经过PCR扩增，做成illumina的测序文库，放到Illumina的测序仪上进行测序。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650720089204-56a23411-98f9-477c-8a95-c86452eb351b.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=159&id=A375K&margin=%5Bobject%20Object%5D&name=image.png&originHeight=218&originWidth=1109&originalType=binary&ratio=1&rotation=0&showTitle=false&size=112245&status=done&style=none&taskId=uda79e996-a875-41a6-a4ac-9632902e796&title=&width=806.5454545454545)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650720128929-b0f4a731-d222-4c8c-a287-572bafdfbd8c.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=165&id=rRsE0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=227&originWidth=1295&originalType=binary&ratio=1&rotation=0&showTitle=false&size=122420&status=done&style=none&taskId=u5fb12b66-f931-4f62-8533-79a4c8bce72&title=&width=941.8181818181819)

#### 5'端文库的构建
与3’端文库的构建过程相似
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650720197047-bd22c500-d426-4ba4-8f1a-2c0e0d9f56b5.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=205&id=SWG1Q&margin=%5Bobject%20Object%5D&name=image.png&originHeight=282&originWidth=1138&originalType=binary&ratio=1&rotation=0&showTitle=false&size=173529&status=done&style=none&taskId=ud2d0ddb8-195d-4cf9-b967-2ff26e0c8ea&title=&width=827.6363636363636)
**小提示：**barcode和UMI是单细胞中常见的名词，barcode就像是每个凝胶微珠的身份证号码；而UMI则像是每个DNA标签分子的身份证号码。

使用scRNA-seq，可以估计基因在细胞群的表达水平分布。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650716423508-d9c5aec5-055a-4160-9cf2-398cf1cd332e.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=640&id=GM8RX&margin=%5Bobject%20Object%5D&name=image.png&originHeight=880&originWidth=1674&originalType=binary&ratio=1&rotation=0&showTitle=false&size=503083&status=done&style=none&taskId=u1aa51a3d-7562-4450-afdb-611cd6d5330&title=&width=1217.4545454545455)
 scRNA-seq 非常适合研究细胞群的异质性。例如，识别组织的细胞类型，定义不同细胞类型的"转录指纹"，研究细胞分化，探索疾病或环境因素导致的细胞组成变化等。
单细胞测序的经典流程：分离单细胞（核），将RNA转换为cDNA，准备测序文库（illumina）后测序。
 SMART-seq2是一种低通量单细胞测序法，提供全长转录组的定量，适合研究小细胞组（如差异isoform使用，低表达转录本的特征）。
10x Chromium是一种高通量方法，使用UMIs进行定量，适合研究高度异质组织和大量的细胞样本。
# 二. 如何开始单细胞RNA测序数据分析
在过去的 5 年中，单细胞方法能够在一次实验中监测数千个单个细胞的基因和蛋白质表达、遗传和表观遗传变化。随着测量的改进以及反应和测序成本的降低，这些数据集的大小正在迅速增加。关键瓶颈仍然是对单细胞实验产生的大量信息的分析。在这篇评论中，我们对分析管道进行了简化概述，因为它们通常在当今的现场使用。我们的目标是让研究人员从单细胞分析起步，以了解挑战和最常用的分析工具。此外，我们希望使其他人能够了解单细胞数据集的典型读数如何在已发表的文献中呈现。
## 1.背景
基于下一代测序的单细胞基因表达分析在1992年首次被描述。2015年，开发了基于encapsulation和barcode的分析。在过去的5年里，单细胞分析变得大众化，大多数学术机构都有专门的核心设施来进行单细胞表达、表观基因组或其他分析。新的统计分析方法得到了迅速发展。一些分析平台也已经开发出来，如Seurat，它是用R 语言写的([https://satijalab.org/seurat/get_started.](https://satijalab.org/seurat/get_started.) html) ，用Python写的Scanpy ([https://scanpy.readthedocs.io/en/](https://scanpy.readthedocs.io/en/) stable/tutorials.html)。在这里，我们回顾了基本的分析工具和概念。我们关注于10× Genomics数据，因为它们更常用(图1)。本文主要基于两个案例研究教程([https://www.](https://www.) github.com/theislab/single-cell-tutorial 和[http://scrnaseqcourse.cog.sanger.](http://scrnaseqcourse.cog.sanger.)ac.uk/website/index.html)。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650869914724-993c95cd-f3a5-438e-91fe-c8a1d2fdeaac.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1420&id=u6fbac8b8&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1952&originWidth=1660&originalType=binary&ratio=1&rotation=0&showTitle=false&size=691759&status=done&style=none&taskId=ue6dcd8f5-ddc4-41b9-81a6-c874a256c6e&title=&width=1207.2727272727273)
## 2.数据矩阵生成和质量控制
单细胞分析的一个关键技术进步是barcode的发展，它允许大规模并行化，同时保持成本最低。barcode被添加到
在逆转录过程中的RNA分子，允许识别单个细胞和独特的分子。分析的第一步是生成一个数据矩阵，由转录本数据库从原始测序文件生成一个barcode(细胞)。对于10×基因组学数据，CellRanger（表1总结了文中提到的工具，方法和数据库）是最常用的管道，包括测序读数与基因组的注释和比对，将比对的读数注释到基因，和量化基因。替代方案包括，例如唯一分子标识(unique molecular identifier , UMI)工具、zUMIs、kallisto、STAR和STARsolo ([https://github.com/](https://github.com/)alexdobin/STAR/blob/master/docs/STARsolo.md)。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650871223876-84d4bb0c-9f26-422b-b84c-6753b3cf0c38.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1698&id=u180afe60&margin=%5Bobject%20Object%5D&name=image.png&originHeight=2335&originWidth=1911&originalType=binary&ratio=1&rotation=0&showTitle=false&size=838671&status=done&style=none&taskId=u86303b40-a4bd-44e6-a857-1b4435d31eb&title=&width=1389.8181818181818)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650891534870-7ab31d04-dea0-4b51-b4e8-0382ba51cb8c.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=929&id=u5500df77&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1277&originWidth=1900&originalType=binary&ratio=1&rotation=0&showTitle=false&size=436971&status=done&style=none&taskId=uee5d1b58-6930-4f15-a8f0-04ca495d0ef&title=&width=1381.8181818181818)
每个barcode可以代表一个单细胞。一个doublets，或者一个不含细胞，但含有周围RNA的“空”液滴。需要提到的一个重要问题是，标准的测序管道将测序数据与转录组进行比对，例如处理后的成熟mRNA。然而，单核RNA数据或表观基因组数据（通过测序测定转座酶可获得的染色质，ATAC-seq）应与全基因组比对，因为细胞核主要含有premRNA，其包括内含子区域。Raw read计数通常也会过滤掉在极少数细胞中检测到的基因，从而有效地减少数据矩阵的大小。分析管道的下一步是质量控制(QC)，例如识别每个barcode的counts数，每个barcode的基因数，以及每个barcode的线粒体基因counts 的比例(图2)。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650871287221-7ba68195-e1cc-4577-95be-8d3af5b1ba04.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1168&id=u44ea0f83&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1606&originWidth=1934&originalType=binary&ratio=1&rotation=0&showTitle=false&size=631158&status=done&style=none&taskId=u08742539-472c-49a3-9212-582058727d5&title=&width=1406.5454545454545)
低基因数量和高比例的线粒体reads通常表明细胞质量差。然而，一些细胞，包括肾近端和远端曲小管细胞，含有丰富的线粒体。异常高的read和基因count可能代表doublets。现在有几种doublet检测工具可用，包括DoubletDecon，Scrublet和DoubletFinder（图2）。然而，doublet检测中的关键问题是含有来自例如上皮和间充质来源的标记基因的过渡细胞可能被标记为doublet，有时导致假阳性检测。此外，这些工具只能识别低同型的双链体，即转录相似的细胞在基因表达空间中聚集在复合细胞类型单链体之间形成的双链体。控制环境RNA污染也很重要。环境RNA是存在于单细胞溶液中的RNA，在包裹过程中被整合到油滴中。我们通常使用SoupX，它可以从空液滴中估计周围的RNA污染(图2)。另一个包是CellBender，它可以消除来自周围环境的RNA分子和随机barcode交换的count(原始)基于UMI的单细胞RNA测序(scRNA-seq)的count 矩阵。
## 3.标准化
单细胞数据需要不同类型和级别的标准化 (图1)。例如，总测序read count会改变原始count，因此基因count应该按总count深度调整。一种常用的方法假设每个细胞具有相同的转录本初始数量，简单地将数据规范化为每百万分数。Scran使用基于pooling的大小因子估计和线性回归来对数据进行归一化，除了Seurat使用的简单对数归一化之外，它也是最流行的方法之一。其他方法已经开发，如SCtransform, SCnorm和BayNorm。归一化后，数据进行log（x + 1）转换。通常从数据中回归出与细胞周期相关的变化，它包含在Seurat或Scanpy的标准分析平台中。该平台还允许其他技术或生物学变异的回归。
## 4.批处理效果校正和数据集成
大多数情况下，会生成多个数据集，需要额外的批处理和数据集成方法(图3)。包含多个不同实验和不同方法的大型数据集通常使用非线性方法进行集成。在Seurat中，有一个基于参考的集成选项，它使用典型相关分析或互反主成分分析(PCA)。Scanorama是Scanpy中使用的另一种流行且性能良好的方法。最近，Harmony越来越受欢迎，并迅速成为单细胞数据集最常用的集成方法。第一步，利用PCA衍生的嵌入矩阵和批处理元数据进行缩放，使每个单元都有一个长度参数。然后，利用正则k-means聚类对尺度数据初始化聚类质心。最后，通过迭代地将特定于批次的质心拉到聚类质心，直到收敛，消除批效应。基因组实验关系的LinkedInference 通过整合非负矩阵分解识别共享的和数据集特定的因素。通过UMI的数量归一化后，基因表达被缩放但不居中。不同的集成方法可能会显示不同的结果。一般情况下，我们期望不同实验的相同细胞类型能够整合在一起，特别是控制细胞应该与多个实验保持一致。感兴趣的读者可以参考Tran等人和Chen等人最近发表的两篇优秀论文，它们提供了一些支持基因组和谐、关联推理的最佳证据实验关系和Seurat关于批效应校正。
## ![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650873291847-4dbc6bb6-adda-4127-91e2-5bf18b7fe184.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1022&id=u9eba97da&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1405&originWidth=1905&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1127276&status=done&style=none&taskId=u56289a89-879e-495f-b947-704bc2991f0&title=&width=1385.4545454545455)5.可视化和聚类
可视化的第一步是在保留信息基因（1000–5000）并过滤掉其他基因时进行特征选择，这在Seurat和Scanpy中均已实现（图4和5）。可视化是在低维空间中总结数据集以观察模式的一种尝试。通常，降维是通过线性和非线性方法来实现的。PCA是聚类和轨迹推理的基础，是一种线性变换，在完整的PCA中保持细胞之间的欧氏距离。在常用的Seurat管道中，PCA用于预处理阶段。可以将PC投影到技术和生物协变量中以了解其性能。使用基于置换测试的jackstraw方法，对top PC和通过“elbow”启发式方法选择的PC数量汇总了PCA（图4）。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650877741182-addcf6ec-8a1a-4ee9-abd7-346437665bab.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1043&id=u7019c98f&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1434&originWidth=1893&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1454534&status=done&style=none&taskId=u694472d1-7386-4c42-a4f7-1199d7aa2e6&title=&width=1376.7272727272727)
单细胞数据可视化主要使用其他非线性降维方法，如t分布随机邻域嵌入。该方法专注于以全局结构为代价捕获局部相似性。均匀近似和投影（UMAP）方法由于其速度而受到欢迎。UMAP似乎能更好地捕捉底层数据结构，并能在两个维度以上总结数据;因此，它现在最常用于单细胞数据可视化。UMAP和t分布随机邻域嵌入的一个关键限制是它们对用户自定义参数有很强的依赖性，并且结果对这些参数有很高的敏感性。最需要注意的是，这两种可视化都不能保持细胞-细胞之间的距离，因此结果嵌入不应该被下游分析直接使用(图4)。
根据基因表达的相似性形成的细胞群是分析的第一个直接结果。细胞聚类允许根据基因表达的相似性分组细胞来推断细胞类型。聚类是一种基于距离矩阵的无监督机器学习过程。community中默认的聚类方法是使用单细胞K近邻方法进行Louvain community检测。单元在图中表示为节点。每个细胞与它的K个最相似的细胞相连接，这些细胞通常是使用pc简化表达式空间上的欧氏距离获得的。单元格在图中表示为节点。每个单元格连接到其K个最相似的单元格，这些单元格通常使用PC缩减表达式空间上的欧几里得距离获得。一个关键问题是，用户决定Louvain聚类的分辨率，而分辨率决定数据集中识别的簇或单元类型的数量。我们建议执行子聚类，例如从初始数据集设置某些聚类，然后在不使用其他单元类型的情况下重新聚类。这允许在细胞类型内出现更精细，更细粒度的数据结构。包含在Leidenbase软件包中的Leiden  community检测算法是Louvain算法的替代方案，在Monocle轨迹分析中用作默认值（见下文）。新的聚类方法使用神经网络和人工智能，例如，单细胞聚类的深度嵌入使用深度神经网络，网络权值和初始聚类从一个自动编码器获得。Clusters（簇）并不一定意味着细胞类型。这一点非常重要，因为用户定义的集群解析参数决定了观察到的集群的数量。注释和聚类是强链接的。聚类和注释以迭代方式进行，这是耗时的。目前，关于最佳聚类参数尚未达成共识。因此，可以接受多个版本的聚类和相同数据的解释。Wilcoxon 秩和检验用于通过组间表达差异对基因进行排序。经典的单元类型注释使用外部数据集，该数据集被认为是基本事实。越来越多的肾脏细胞类型注释外部数据集包括Susztak Lab，Humphreys Lab,Tabula Muris, Human Cell Atlas, Renal Epithelial Cell Ontology webpage, 和 ImmGen Consortium。最近，自动化细胞注释工具已经开发出来，如Garnett、SingleR、CHETAH和MOANA，他们提供了一种更全面和概率的细胞身份标注方法。相同细胞类型的标记基因在不同的数据集可能不同。
## 6.细胞水平分析：细胞组分变化，分解和轨迹分析
细胞组分的变化(数据集中每种细胞类型的比例)与疾病状态有很强的相关性，这是单细胞分析最简单的结果之一。这些数字可以提供条件之间的相对估计，但由于单细胞库制备过程中细胞捕获的偏差，从单细胞数据推断的细胞分数可能不准确。此外，来自肾皮质的样本中，近端小管细胞的比例比来自髓质的样本高。为了推断bulk RNA-seq数据的细胞类型组成，MuSiC是最近开发的一种以单细胞表达数据为参考的批量组织细胞类型反卷积方法。MuSiC使用加权非负最小二乘回归估计细胞类型比例。可供选择的方法包括CIBERSORT、BSEQ-sc和BisqueRNA。对样本之间的细胞识别簇比例变化的统计检验是相互依赖的，而且，因为当一个细胞识别簇的比例变化时，所有其他细胞识别簇的比例也会变化。或者，基于排列的统计测试方法可以用于差异比例分析，其中cluster比例与总细胞的随机比例进行比较。
细胞多样性不能充分地描述一个离散的分类系统，如聚类。轨迹分析捕捉转变期间细胞的显著特征，例如沿着几个时间点的器官发育期间，或疾病状态、细胞历史或拓扑信息之间的变化。驱动观察到的异质性的生物过程是连续的。因此，捕捉细胞特性、分支分化过程或生物学功能的渐进、不同步变化之间的转变需要基因表达的动态模型。Monocle是一种机器学习方法，用于重建每个细胞从一种状态转换到另一种状态时必须执行的基因表达变化序列。它基于逆图嵌入，一种高度可扩展的非线性流形学习技术。在该方法学习转换( transition)路径或轨迹之后，它将每个细胞沿着它放置在正确的位置，这被称为伪时间，即细胞在生物过程中移动多远的度量。一种分析细胞历史的新方法在最近开发的RNA速度分析中得到了应用，如包velocyto。RNA速度是基因表达状态的时间衍生物，可以通过在常见的scRNAseq协议中区分未剪接和剪接的mRNA来直接估计。RNA速度是一种高维向量，以小时为时间尺度预测单个细胞的未来状态。TradeSeq基于称为Slingshot的先前方法，在简单轨迹分析方面优于其他方法。另一个有用的软件包是PHATE，它是一种可视化方法，使用数据点之间的信息几何距离捕捉局部和全局非线性结构。推断出的轨迹不一定代表一个生物过程，应该收集进一步的证据来源来解释从这些方法得到的轨迹(图6)。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650888411295-f63075f8-272b-4f2a-9ded-5d406f783212.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1299&id=ua194b2d1&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1786&originWidth=1915&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1482203&status=done&style=none&taskId=u201fbca2-b65a-45cf-839b-4f87b7ee304&title=&width=1392.7272727272727)
## 7. 基因水平分析：差异表达，基因调控网络，驱动途径和细胞-细胞相互作用
差异表达(DE)分析是通过包括技术和生物协变量的未校正数据进行的。Seurat使用不同的模型进行DE分析（图6）。MAST使用障碍模型来解释辍学。为了将scRNA-seq数据集信息与其他表型变量相关联，基于回归的模型可以组合几个样本及其相关的表型特征，以将某些细胞类型（例如近端肾小管细胞）中的基因表达变化与相应的定量测量表型（例如GFR，Albuminuria）。尽管DE测试工具通常允许用户灵活地合并混杂器，但用户必须警惕哪些变量被添加到模型中。例如，在大多数单细胞实验设置中，样本和条件协变量是混淆的，因为在多种条件下获得单个样本几乎不可能。基因水平分析还可以与基因集富集分析方法相结合，例如基因集富集分析或加权相关网络分析。
为了解释DE结果，我们通常根据参与共同生物过程的基因进行分组。生物过程标签存储在数据库中，例如MSigDB，基因本体论或《京都议定书》的基因和基因组百科全书以及Reactome数据库。尽管我们需要记住，某些通路成员的基因表达富集可能并不一定与通路活性相关，但基因列表上注释的富集可以使用大量工具进行测试，这些工具已经在其他地方进行了审查和比较。单细胞分析领域的最新发展是使用配对基因标签来进行配体-受体分析。在这里，细胞群之间的相互作用是从受体及其同源配体的表达推断。配体-受体对标签可以从最近的数据库获得，例如CellPhoneDB或Connectome，并用于使用统计模型解释跨簇的高表达基因。
## 8.单细胞分辨率下的基因调控
通过测序获得转座酶可及染色质的单核分析(snATAC-seq)可以通过染色质可及性图谱分析单细胞的表观基因组景观(图7)。已经为snATAC-seq分析开发了多种工具。最着名的是Ren实验室开发的SnapATAC，Satija实验室开发的Signac和Greenleaf实验室开发的ArchR。我们更喜欢SnapATAC，这是一种非线性降维方法。在CellRanger中通过barcode-by-cell 矩阵生成barcode之后，我们通过使用SnapATAC将片段二值化为均匀大小的逐个cell-by-bin来预处理矩阵。QC步骤包括过滤读深过低或过高的低质量细胞或doublet，并移除基因组黑名单区中的读码。重要的QC标准是转录起始位点的富集、峰中reads的比例和启动子区reads的比例。SnapATAC利用扩散图识别异质组织中的细胞类型。从扩散图中得到的低维嵌入作为输入，以消除批处理效应。然后用Louvain算法进行聚类，选取k个最近邻算法中的k个值作为输入。为了进行聚类注释，从选定的肾细胞类型特异性标记基因中生成细胞基因活性评分矩阵。预定义的启动子区域，(例如，来自Ensembl调控构建)或基因体12kb区域用于整合所有与基因转录本重叠的片段。为了从每种细胞类型调用峰，将从相同细胞类型获得的所有片段聚合以构建伪批量ATAC数据集和MACS2，分别针对每种细胞类型进行。ArchR实现了一种改进的方法，在独立样本上调用峰值，然后保留可重现的峰值。Fisher在edgeR中的精确测试在细胞簇之间进行测试，以揭示每种细胞类型的不同可访问区域。为了鉴定不同细胞类型中富集的基序，HOMER或chromVAR可用于snATAC-seq数据的转录因子分析，尽管遗传背景将严重影响哪些转录因子基序富集。
为了研究开放染色质变化如何与细胞分化和细胞命运决定相关联，使用Monocle3进行轨迹分析，通过使用潜在语义索引和UMAP可视化来减少维度。为了了解开放染色质和目的基因的表达变化，通过分析在Cicero中实现的两个峰的可达性，进行了峰-峰相关性研究。该策略聚合相似的单元以获得一组“元单元”，并解决snATAC-seq数据中的稀疏性问题。或者，可以将峰推算到GREAT中以识别最近的基因。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650891422454-a1f0c363-0566-4ec1-a4e3-bb98719aaa01.png#clientId=u61373409-4e9c-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=1581&id=ufdbace7d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=2174&originWidth=1902&originalType=binary&ratio=1&rotation=0&showTitle=false&size=1051080&status=done&style=none&taskId=u2f8100f1-2ba7-4c2b-8ee6-9ba20c3a5f4&title=&width=1383.2727272727273)
## 9.Webtools和数据集
在过去的几年中，已经生成了大量的人类和小鼠肾脏数据集。原始数据集通常可从GEO下载。作为人类细胞图谱项目和人类生物分子图谱计划的一部分，将提供大量综合参考人类肾脏注释。肾脏精准医学项目旨在为各种人类肾脏疾病状况生成数据集。重建肾脏联盟将分析开发的人类肾脏样本和体外分化的肾脏类器官。此外，一些研究人员已经为小型单个实验数据集生成了可视化工具。Humphreys实验室的工具包站点允许快速可视化他们广泛的数据([http://humphreyslab.com/SingleCell/)](http://humphreyslab.com/SingleCell/).)。McMahon和Kim实验室使用VisCello将发育和成年小鼠的数据可视化，同时比较雄性和雌性小鼠的差异。使用VisCello平台，我们的实验室可视化开发，成人，健康和疾病小鼠模型数据([http://susztaklab.com/VisCello/)](http://susztaklab.com/VisCello/)35)和开放的染色质表观基因组数据，这也是可用于相同的时间点([http://susztaklab.com/developing_adult_kidney/igv/)](http://susztaklab.com/developing_adult_kidney/igv/).)。这些站点不允许进行全面分析，并且聚类参数（有些主观）是固定的，但它们对于查找和比较非常有用。数据分析自动化的另一个重要发展是Satija实验室的独立分析应用程序([http://azimuth.satijalab.org/app/azimuth)](http://azimuth.satijalab.org/app/azimuth))，允许将单个数据集投影到参考数据集，其中已在单个细胞中同时测量了RNA和表面蛋白表达。研究者可以上传本地生成的数据集，该软件包自动执行上述所有步骤，并与人体血液参考数据聚类。
# 三. 单细胞转录组的上游分析
## 1.从BCL到FASTQ
### (1) 软件安装和介绍
Cellranger mkfastq 管道可用于将 BCL 文件解码为单个库的 FASTQ 文件。如果测序提供程序已经完成了这一步，则可以直接使用每个库的 FASTQ 文件进行数据分析。cellranger mkfastq的本质是调用bcl2fastq生成bcl2fastq，并生成额外的10x样本信息。Bcl2fastq是 illumina开发的bcl到fastq的转换程序。cellranger下载安装地址如下：
[https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest?](https://support.10xgenomics.com/single-cell-gene-expression/software/downloads/latest?)
安装cellranger
参考：[https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/using/tutorial_in](https://support.10xgenomics.com/single-cell-gene-expression/software/pipelines/latest/using/tutorial_in)
```r
tar -xzf cellranger-6.1.1.tar.gz
```
```r
echo 'export PATH=~/softwares/cellranger-6.1.2:$PATH' >> ~/.bashrc

source ~/.bashrc
```
```shell
cellranger testrun --id=tiny
```
在conda环境中安装bcl2fastq，因为Cellranger依赖于bcl2fastq。
```shell
#https://anaconda.org/dranew/bcl2fastq
conda install -c dranew bcl2fastq
```
### (2) 案例
公司提供的bcl原始测序文件，本次教学使用使用cellranger的测试数据

```shell
curl -O https://cf.10xgenomics.com/supp/cell-exp/cellranger-tiny-bcl-1.2.0.tar.gz
curl -O https://cf.10xgenomics.com/supp/cell-exp/cellranger-tiny-bcl-simple-1.2.0.csv
```
```shell
tar -zxvf cellranger-tiny-bcl-1.2.0.tar.gz
tree -L 2 cellranger-tiny-bcl-1.2.0/
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650770361369-ef5151a0-e996-454d-8ad6-a8502f2f82da.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=453&id=u36f48aba&margin=%5Bobject%20Object%5D&name=image.png&originHeight=558&originWidth=931&originalType=binary&ratio=1&rotation=0&showTitle=false&size=54415&status=done&style=none&taskId=u9263e28b-6baa-4cf5-bfc5-b9adebc445e&title=&width=755.0909423828125)
您的数据可能看起来有点不同，这取决于测序仪器使用。查看目录的前几个级别是检查完整性的好方法。如果您没有看到 RTAComplete.txt、 RunInfo.xml 和 runParameters.xml 文件，那么管道很可能会失败。如果缺少任何这些文件，请与您的测序提供程序联系，并要求获得完整的运行目录。
```shell
cat cellranger-tiny-bcl-simple-1.2.0.csv
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650770174894-13e82ec2-8b48-4ceb-94b7-534443b68017.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=79&id=u5f7d04c9&margin=%5Bobject%20Object%5D&name=image.png&originHeight=101&originWidth=956&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14770&status=done&style=none&taskId=ue79f0326-a741-4f7f-b62d-0ee62485846&title=&width=750.2727661132812)
• Lane：要处理flowcell的哪个通道。 可以是单个泳道（1）、范围（例如 2-4）或flowcell中所有泳道（*）。
• Sample：样本名称。 所有生成的 FASTQ 表头前缀，对应于所有下游 10x 管道中的 --sample 参数。样本名称只允许使用字母、数字、下划线_和-；不允许使用其他符号，包括点（“.” ）。
• Index：用于文库构建的 10x 样本索引，例如 SI-TT-D9 或 SI-GA-A1。 

---

查看帮助文档
```shell
cellranger mkfastq --help
```
```shell
cellranger mkfastq --id=tiny-bcl --run=cellranger-tiny-bcl-1.2.0 --csv=cellranger-tiny-bcl-simple-1.2.0.csv
```
• --id： mkfastq命令输出FASTQ文件的文件夹名称
• --run： BCL（Base CALL）所在文件夹名称（该文件为illumina测序的下机文件）
• --csv：对应BCL文件的样本信息表，用于描述如何在 Illumina flow 单元上对样本进行索引。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650771729833-6b41bcc5-2c8b-4a1a-b71d-e27fce41d3e8.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=684&id=uc5ce52bd&margin=%5Bobject%20Object%5D&name=image.png&originHeight=940&originWidth=1591&originalType=binary&ratio=1&rotation=0&showTitle=false&size=189490&status=done&style=none&taskId=ucb1d65e5-9dbb-4c6d-a9fd-23dfd4984ab&title=&width=1157.090909090909)
查看输入：`tree -L 2 tiny-bcl/`
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650771780183-f6cd462a-01a0-4bf4-a038-e09668ac87cf.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=482&id=u97c1e85c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=663&originWidth=716&originalType=binary&ratio=1&rotation=0&showTitle=false&size=40621&status=done&style=none&taskId=u3ec3feba-137f-475c-89e3-e02e32c103b&title=&width=520.7272727272727)
 运行时间根据系统资源的不同而不同，但是它不应该占用多于几分钟的时间。现在转到 fastq _ path 目录。
 
```shell
 cd tiny-bcl/outs/fastq_path/
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650783084023-c1a2348f-3a16-4f78-a524-c544cca94c29.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=164&id=u7916ed27&margin=%5Bobject%20Object%5D&name=image.png&originHeight=225&originWidth=1009&originalType=binary&ratio=1&rotation=0&showTitle=false&size=46205&status=done&style=none&taskId=u10bab75f-5ef8-4ac0-813b-ddae0bcb05d&title=&width=733.8181818181819)
具有有效排序索引的Demultiplexed FASTQ 文件可以在以 flow cell id 命名的目录下找到，在本例中为 H35KCBCXY。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650783717514-2c9fcde7-e3b4-4124-8d91-136d24c60b83.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=121&id=udbf9ce09&margin=%5Bobject%20Object%5D&name=image.png&originHeight=128&originWidth=775&originalType=binary&ratio=1&rotation=0&showTitle=false&size=18924&status=done&style=none&taskId=u3d6cabb6-0f1b-433b-ad97-1626172545e&title=&width=734.6363525390625)
这些来自 `cellranger mkfastq` 管道的输出作为  `cellranger count`的输入。
## 2. 从SRA到FASTQ
### (1) 软件安装和介绍
SRAtoolkit是NCBI提供的SRA文件处理工具集， SRA文件是NCBI的SRA数据库数据的储存格式，许多公开的scRNA-seq数据都会上传到该数据库。SRAtoolkit将NCBI的SRA数据库中SRA文件转换为FastQ文件。
在conda的环境中安装SRAtoolkit，地址：[https://anaconda.org/daler/sratoolkit](https://anaconda.org/daler/sratoolkit)
```shell
conda install -c daler sratoolkit
```
在线下载后安装地址：[https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software)
```shell
curl -O https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/3.0.0/sratoolkit.3.0.0-centos_linux64.tar.gz
tar zxf sratoolkit.3.0.0-centos_linux64.tar.gz
##注意解压位置
echo 'export PATH=~/sratoolkit.3.0.0-centos_linux64/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```
安装后进行配制
```shell
vdb-config -i
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650789182028-0b438c64-7ebd-4375-9852-12cdbb56a103.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=524&id=u160eee41&margin=%5Bobject%20Object%5D&name=image.png&originHeight=721&originWidth=1319&originalType=binary&ratio=1&rotation=0&showTitle=false&size=41937&status=done&style=none&taskId=ua90e173b-4048-48c0-9b7c-70229a23ad3&title=&width=959.2727272727273)
### (2) 案例
数据地址：[https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA483959&o=acc_s%3Aa](https://www.ncbi.nlm.nih.gov/Traces/study/?acc=PRJNA483959&o=acc_s%3Aa)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650788062010-4ea76a17-9b55-4f2b-bad8-6e7891cf87ae.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=463&id=u84bb4cd7&margin=%5Bobject%20Object%5D&name=image.png&originHeight=636&originWidth=1724&originalType=binary&ratio=1&rotation=0&showTitle=false&size=114883&status=done&style=none&taskId=ue99e6aa9-c0bd-454e-a90a-601645049b5&title=&width=1253.8181818181818)
点击Total的“Accession List”下载整个研究的SRA文件编号；
点击Total的“Metadata”下载网页中SRA文件描述。
```shell
cd /mnt/f/Linux/scRNASeqTest/
mkdir sra_data
cd sra_data/
```
下载的文件放在：sra_data目录下。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1650788425804-8cc9655b-05a9-4711-b575-1882bb554b65.png#clientId=u2cc92fc1-2ece-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=106&id=u742b6b58&margin=%5Bobject%20Object%5D&name=image.png&originHeight=101&originWidth=717&originalType=binary&ratio=1&rotation=0&showTitle=false&size=14532&status=done&style=none&taskId=udb88dad4-e49c-4e7e-9907-1aee9da09cb&title=&width=751.45458984375)
SRR_Acc_List.txt：整个研究的SRA文件编号；
SraRunTable.txt： SRA文件描述。 
下载数据：
```shell
curl -O https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR7722937/SRR7722937
curl -O https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR7722938/SRR7722938
curl -O https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR7722939/SRR7722939
curl -O https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR7722940/SRR7722940
curl -O https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR7722941/SRR7722941
curl -O https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR7722942/SRR7722942
```
可以写一个循环进行下载，也可以使用[prefetch](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc&f=prefetch)下载。
下载后的数据使用`fastq-dump`命令可将sra数据转换成fastq。
```shell
fastq-dump --gzip --split-files -X 25000 -O fastqs_path data/SRR7722937
```
• --gzip：输出gz压缩格式的fastq文件
• --split-files：分隔为上传时的多个fastq文件
• -X：输出的fastq的记录数目，这里为了教学，输出前25000条记录，实际分析时，不要设置此参数
• -O： fastq文件输出的文件夹
• data/SRR7722937： SRA文件所在路径
```shell
fastq-dump --gzip --split-files -O fastqs_path data/SRR7722937
fastq-dump --gzip --split-files -O fastqs_path data/SRR7722938
fastq-dump --gzip --split-files -O fastqs_path data/SRR7722939
fastq-dump --gzip --split-files -O fastqs_path data/SRR7722940
fastq-dump --gzip --split-files -O fastqs_path data/SRR7722941
fastq-dump --gzip --split-files -O fastqs_path data/SRR7722942
```
cellranger count进行运算需要按照一定格式的形式命名，转换后的fastq文件进行重命名。
```shell
for i in `cat SRR_Acc_List.txt`
	do
	mv fastqs_path/${i}_1.fastq.gz fastqs_path/${i}_S1_L001_I1_001.fastq.gz
	mv fastqs_path/${i}_2.fastq.gz fastqs_path/${i}_S1_L001_R1_001.fastq.gz
	mv fastqs_path/${i}_3.fastq.gz fastqs_path/${i}_S1_L001_R2_001.fastq.gz
done
```
参考：[https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc](https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=toolkit_doc)
## 3.从FASTQ到count矩阵
cellranger计数管道将FASTQ文件中的测序结果与参考转录组进行比对，并生成一个`.cloupe`文件，用于在Loupe Browser中进行可视化和分析，同时还生成了一些与其他公开工具兼容的输出，用于进一步分析。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651296219558-2098ee13-af4a-4b5d-a4d2-a9e5cbace9b7.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=489&id=u8c6a9666&margin=%5Bobject%20Object%5D&name=image.png&originHeight=672&originWidth=966&originalType=binary&ratio=1&rotation=0&showTitle=false&size=74160&status=done&style=none&taskId=u7589798f-b8d1-4ed5-877f-eb916a69edb&title=&width=702.5454545454545)
接下来，需要一个参考基因组数据。从FASTQ文件的下载页面可以看到这些是人类细胞。在10x Genomics支持网站上有几个预构建的人类参考转录组包。下载最新的包并解压缩它。
```shell
#人
curl -O https://cf.10xgenomics.com/supp/cell-exp/refdata-cellranger-GRCh38-3.0.0.tar.gz
#小鼠
curl -O https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-mm10-2020-A.tar.gz
```
解压下载的基因组文件：
```shell
  tar zxvf refdata-gex-GRCh38-2020-A.tar.gz
```
接下来使用来自人类外周血单个核细胞(PBMC)的1000个 PBMC 数据集，包括淋巴细胞(t 细胞、 b 细胞和 NK 杀伤细胞)和单核细胞。
```shell
curl -O https://cf.10xgenomics.com/supp/cell-exp/refdata-gex-mm10-2020-A.tar.gz
```
这个数据集的大小是5.17 g，下载需要几分钟。
因为这是一个 tar 文件而不是 tar.gz 文件，所以您不需要使用前面的教程中使用的 -z 参数来提取它。
```shell
tar -xvf pbmc_1k_v3_fastqs.tar
```
```shell
pbmc_1k_v3_fastqs/
pbmc_1k_v3_fastqs/pbmc_1k_v3_S1_L001_R2_001.fastq.gz
pbmc_1k_v3_fastqs/pbmc_1k_v3_S1_L002_I1_001.fastq.gz
pbmc_1k_v3_fastqs/pbmc_1k_v3_S1_L001_R1_001.fastq.gz
pbmc_1k_v3_fastqs/pbmc_1k_v3_S1_L002_R1_001.fastq.gz
pbmc_1k_v3_fastqs/pbmc_1k_v3_S1_L002_R2_001.fastq.gz
pbmc_1k_v3_fastqs/pbmc_1k_v3_S1_L001_I1_001.fastq.gz
```
现在你有了一个包含两组 FASTQ 文件的目录，可以看到它们是根据 bcl2fastq 变数命名原则命名的: Sample_S1_L00X_R1_001.fastq.gz。这些文件的名称表明它们都来自同一个名为 pbmc _ 1k _ v3的样本，并且这个库在两个lanes上运行，Lane 1: L001 和 lane 2: L002.。
一旦你有了 FASTQ 文件和参考转录组，你就可以运行`cellranger count`了。
```shell
cellranger count --id=run_count_1kpbmcs \
--fastqs= /mnt/f/Linux/run_cellranger_count/pbmc_1k_v3_fastqs \
--sample=pbmc_1k_v3 \
--transcriptome= /mnt/f/Linux/genomeAnno/hsa/refdata-gex-GRCh38-2020-A \
--expect-cells=1000 \
--localcores=6 \
--localmem=8 \
--nosecondary
```
• --id：输出文件夹名
• --transcriptome：参考基因组所在文件夹
• --fastqs： fastq文件所在文件夹名，如下图所示
• --sample：用于分析的文件名
• --expect-cells：预计的细胞数，软件会根据实际情况进行估算
• --localcores：使用的线程数
• --localmem：使用的内存数
• --nosecondary：不进行下游聚类分析
```shell
cellranger count --id=cellranger_count \
--transcriptome=/mnt/f/Linux/genomeAnno/hsa/refdata-gex-GRCh38-2020-A \
--fastqs=fastq_path/H35KCBCXY/test_sample \
--sample=test_sample \
--expect-cells=1000 \
--localcores=6 \
--localmem=8 \
--nosecondary
```

```shell
cellranger count --id=cellranger_count \
--transcriptome=/mnt/f/Linux/genomeAnno/hsa/refdata-gex-GRCh38-2020-A \
--fastqs=/mnt/f/Linux/sradata/sra_data/fastqs_path \
--sample=SRR7722937 \
--expect-cells=1000 \
--localcores=6 \
--localmem=8 \
--nosecondary
```
## 4.STAR/STARsolo：单细胞FastQ文件比对
STAR是一款用于高通量转录组比对的软件，是Encode计划和TCGA计划使用的官方比对软件，基于STAR分析转录组的流程，通常称为STAR Method， STARsolo是STAR专门用于单细胞转录组定量的模块，原理类似于cellranger count， STAR官方宣称速度比cellranger快10倍。
安装：[https://anaconda.org/bioconda/star](https://anaconda.org/bioconda/star)
在conda环境中安装
```shell
#要使用 conda 安装此包，请运行以下命令之一
conda install -c bioconda star
conda install -c bioconda/label/cf201901 star
```
STAR比对需要索引， cellranger软件的索引包含基因组注释，这里可以直接使用这些数据来构建STAR
比对的索引。**注意：不同STAR软件版本构建的索引是不通用的，更换软件版本后需要重新构建索引。**
```shell
STAR --runMode genomeGenerate \
--genomeDir star_hg38_index \
--genomeFastaFiles refdata-gexGRCh38-2020-A/fasta/genome.fa \
--runThreadN 8
--sjdbGTFfile refdata-gex-GRCh38-2020-A/genes/genes.gtf
```
• --runMode：设置运行模式为构建STAR索引
• --genomeDir： STAR索引输出文件夹名
• --genomeFastaFiles： Fasta格式的基因组序列
• --runThreadN：服务器使用的线程数
• --sjdbGTFfile： gtf格式的基因注释文件

基因组fasta下载地址： [https://asia.ensembl.org/Homo_sapiens/Info/Index](https://asia.ensembl.org/Homo_sapiens/Info/Index)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651378302681-d1c01bce-9715-4b54-bd63-75caa3ad85bd.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=401&id=u38eaf383&margin=%5Bobject%20Object%5D&name=image.png&originHeight=551&originWidth=917&originalType=binary&ratio=1&rotation=0&showTitle=false&size=67760&status=done&style=none&taskId=u852066f1-008f-499e-96c3-342873688a1&title=&width=666.9090909090909)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651378333412-f5d97a76-1c2b-4183-ad34-d9f13e962b06.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=676&id=u3f3985cb&margin=%5Bobject%20Object%5D&name=image.png&originHeight=929&originWidth=1082&originalType=binary&ratio=1&rotation=0&showTitle=false&size=69169&status=done&style=none&taskId=u8a2398ff-3671-4acb-ba0e-0ff2e2bb3ce&title=&width=786.9090909090909)
基因注释gtf下载地址： [https://asia.ensembl.org/Homo_sapiens/Info/Index](https://asia.ensembl.org/Homo_sapiens/Info/Index)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651378398672-43cf6fbd-0e63-4193-bdff-71ef513e059e.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=208&id=ua4c8bfad&margin=%5Bobject%20Object%5D&name=image.png&originHeight=286&originWidth=906&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49617&status=done&style=none&taskId=u2a1d4c49-9edd-4ebe-bf91-32519c10461&title=&width=658.9090909090909)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651378437677-b0e64db3-d01d-4d81-bb10-fe7a403b4943.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=184&id=u7f8f229d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=253&originWidth=977&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19837&status=done&style=none&taskId=u248b35c4-bf62-454c-ac80-c4be6aadca2&title=&width=710.5454545454545)
以SRR7722939为例
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651378574114-6c5eb865-f216-488e-ac50-66493a27652a.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=249&id=ua833472c&margin=%5Bobject%20Object%5D&name=image.png&originHeight=342&originWidth=1419&originalType=binary&ratio=1&rotation=0&showTitle=false&size=203811&status=done&style=none&taskId=uf989af48-6f70-4d46-b529-494121b0a20&title=&width=1032)
• --genomeDir： STAR索引所在目录
• --readFilesCommand zcat：使用zcat读取gz压缩格式文件
• --readFilesIn：读入fastq文件的路径，首先是R2，然后是R1
• --soloOutFileNames：输出文件夹名
• --soloType CB_UMI_Simple：文库类型
• --soloCBwhitelist：所有使用的barcode序列
• --runThreadN：服务器使用的线程数 
 
STARsolo的结果与cellranger count的结果相同， cellranger count也是调用STAR进行比对。STARsolo的运行速度比cellranger count快10倍。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651378743825-7871882b-5b60-497b-bfb0-eead68136aad.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=450&id=ude6e68e3&margin=%5Bobject%20Object%5D&name=image.png&originHeight=619&originWidth=534&originalType=binary&ratio=1&rotation=0&showTitle=false&size=98995&status=done&style=none&taskId=u54308296-9930-4ebc-b183-85cce47f62a&title=&width=388.3636363636364)
• Barcodes.stats：对Barcode代码的统计。
• Features.stats：特征统计。
• Filtered：过滤后的表达矩阵，过滤方法与cellranger
count 相同（用于下游分析，最主要）。
• Raw：未过滤的数据。
• Summary.csv：比对汇总。
• UMIperCellSorted.txt： UMI统计信息。
## 5.Salmon/Alevin：对FastQ文件进行基因定量
Salmon是一款不基于比对的定量软件，可用于转录组数据的快速定量，准确性高，其中Alevin功能
专门用于单细胞转录组定量【PMID: 28263959】。

安装
```shell
#要使用 conda 安装此包，请运行以下命令之一
conda install -c bioconda salmon
conda install -c bioconda/label/cf201901 salmon
```
使用Salmon定量前需要首先构建索引，从ensembl数据库中下载cdna序列：
以人类cdna下载为例： [https://asia.ensembl.org/Homo_sapiens/Info/Index#](https://asia.ensembl.org/Homo_sapiens/Info/Index#)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651379412115-264f794c-1cf0-47f5-bad0-5afd5a1b5da2.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=204&id=u9118c14e&margin=%5Bobject%20Object%5D&name=image.png&originHeight=281&originWidth=905&originalType=binary&ratio=1&rotation=0&showTitle=false&size=49435&status=done&style=none&taskId=uc37461b9-6584-463b-bcb9-cda372986dc&title=&width=658.1818181818181)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651379475224-d844ff7a-daba-4698-b55d-de980760e0e1.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=160&id=u3c7ca1bc&margin=%5Bobject%20Object%5D&name=image.png&originHeight=220&originWidth=1149&originalType=binary&ratio=1&rotation=0&showTitle=false&size=19242&status=done&style=none&taskId=u002080a1-e7bc-4e04-9112-518b6c1cb74&title=&width=835.6363636363636)
构建salmon索引： 
```shell
time salmon index -t Homo_sapiens.GRCh38.cdna.all.fa.gz -i hg38_salmon
```
index：运行salmon索引构建程序； -t：之前下载的cdna序列； -i：输出索引文件夹的名称。
进行salmon定量之前还需要基因名和转录本名的对应关系，同样是从Ensembl网站获取。
以人类GRCh38为例： [https://asia.ensembl.org/Homo_sapiens/Info/Index#](https://asia.ensembl.org/Homo_sapiens/Info/Index#)
点击该页面导航栏的“BioMart”，进入BioMart数据库.
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651379868466-9230344f-80fd-434a-ae1f-9da4a8a17cd7.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=202&id=ua24102b4&margin=%5Bobject%20Object%5D&name=image.png&originHeight=278&originWidth=934&originalType=binary&ratio=1&rotation=0&showTitle=false&size=32398&status=done&style=none&taskId=ub79c4046-81c8-4381-8605-709b1802b87&title=&width=679.2727272727273)
在打开的页面中，选择数据库，一般选择第一个选项， Ensembl Genes 106， 106是当前数据库的版本号，以后可能会更新，显示如107， 108等等。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651380040507-911925ba-2127-4c69-9fdc-bd3c225afd2f.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=311&id=u3b637883&margin=%5Bobject%20Object%5D&name=image.png&originHeight=428&originWidth=759&originalType=binary&ratio=1&rotation=0&showTitle=false&size=51851&status=done&style=none&taskId=ufe7ac633-afc5-41a2-bdb6-8bd776ab7c2&title=&width=552)
勾选上“Unique results only”选项，点击“Go”下载文件。
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1651380491490-5bf77cf4-bb86-4c28-b435-efeae085f0cb.png#clientId=ub9aac30b-b8a1-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=367&id=u231a4404&margin=%5Bobject%20Object%5D&name=image.png&originHeight=504&originWidth=1458&originalType=binary&ratio=1&rotation=0&showTitle=false&size=73009&status=done&style=none&taskId=uc750b84e-06e5-4d65-9e6f-af459029f56&title=&width=1060.3636363636363)
下载好的文件名为mart_export.txt，内容如左图，修改mart_export.txt文件名为txp2gene.tsv。
# 四.单细胞下游分析
## 1.读入csv文件的表达矩阵构建Seurat对象
```r
rm(list=ls())
options(stringsAsFactors = F)
library(Seurat)
# Load data 
dir='./'
Sys.time()
raw.data <- read.csv(paste(dir,"Data_input/csv_files/S01_datafinal.csv", sep=""), header=T, row.names = 1)
Sys.time()
dim(raw.data)
raw.data[1:4,1:4]
head(colnames(raw.data)) 
# Load metadata 
metadata <- read.csv(paste(dir,"Data_input/csv_files/S01_metacells.csv", sep=""), row.names=1, header=T)
head(metadata) 

# Find ERCC's, compute the percent ERCC, and drop them from the raw data.
erccs <- grep(pattern = "^ERCC-", x = rownames(x = raw.data), value = TRUE)
percent.ercc <- Matrix::colSums(raw.data[erccs, ])/Matrix::colSums(raw.data)
fivenum(percent.ercc)
ercc.index <- grep(pattern = "^ERCC-", x = rownames(x = raw.data), value = FALSE)
raw.data <- raw.data[-ercc.index,]
dim(raw.data) 
```
有了表达矩阵，直接使用 CreateSeuratObject 函数即可，然后慢慢添加这个表达矩阵的一些其它外部属性，全部代码如下：
```r
# Create the Seurat object with all the data (unfiltered)
main_tiss <- CreateSeuratObject(counts = raw.data)
# add rownames to metadta 
row.names(metadata) <- metadata$cell_id
# add metadata to Seurat object 
main_tiss <- AddMetaData(object = main_tiss, metadata = metadata)
main_tiss <- AddMetaData(object = main_tiss, percent.ercc, col.name = "percent.ercc")
# Head to check
head(main_tiss@meta.data)

# Calculate percent ribosomal genes and add to metadata
ribo.genes <- grep(pattern = "^RP[SL][[:digit:]]", x = rownames(x = main_tiss@assays$RNA@data), value = TRUE)
percent.ribo <- Matrix::colSums(main_tiss@assays$RNA@counts[ribo.genes, ])/Matrix::colSums(main_tiss@assays$RNA@data)
fivenum(percent.ribo)
main_tiss <- AddMetaData(object = main_tiss, metadata = percent.ribo, col.name = "percent.ribo")
main_tiss

# Filter cells so that remaining cells have nGenes >= 500 and nReads >= 50000
main_tiss_filtered <- subset(x=main_tiss, subset = nCount_RNA > 50000 & nFeature_RNA > 500)
main_tiss_filtered
```
我们得到了main_tiss_filtered这个变量，是一个Seurat对象，就可以follow我们的教程后后续分析流程啦。参考代码仍然是是：

- [祖传的单个10x样本的seurat标准代码](https://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247495635&idx=1&sn=b80a060573dfc266fe9d4c7773c88c7f&scene=21#wechat_redirect)
- [祖传的单个10x样本的seurat标准代码（人和鼠需要区别对待）](https://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247495646&idx=1&sn=b24b77c21e99f11793ae8166be9ad02f&scene=21#wechat_redirect)
- [seurat标准流程实例之2个10x样本的项目（GSE135927数据集）](https://mp.weixin.qq.com/s?__biz=MzAxMDkxODM1Ng==&mid=2247495874&idx=1&sn=1189c08b96ce1ea2c70964db93f480d6&scene=21#wechat_redirect)
## 2.读入多个文件
[https://mp.weixin.qq.com/s/g_tAhFQfr2IhFyHxzcFRTg](https://mp.weixin.qq.com/s/g_tAhFQfr2IhFyHxzcFRTg)
min.cells=3表示从表达量矩阵中删除在少于3个细胞中表达的基因（行），min.features=200表示删除表达的基因数小于200的细胞（列）
质控的目的是去除掉低质量的数据，包括破损或死亡的细胞、没捕获到细胞的empty droplet和捕获到2个以上细胞的doublets。一般低质量的细胞或者empty droplet通常含有很少的基因，而doublets容易测到更多的基因。另一方面，低质量或者死亡细胞会测到更多的线粒体基因表达的RNA。
使用PercentageFeatureSet函数评估每个细胞中的线粒体表达比例：
pattern = "^MT-"表示线粒体基因的匹配模式，人的线粒体基因以MT-为前缀，小鼠的以Mt-为前缀。

Seurat对象在生成时，已经将每个细胞表达的基因数和reads数记录在meta.data的nFeature_RNA和nCount_RNA中。我们使用VlnPlot函数将nFeature_RNA、nCount_RNA和percent.mt三个指标进行可视化：

基因的表达矩阵需要经过标准化后才能进行后续的分析。使用NormalizeData函数进行标准化，方法选择LogNormalize：

通常我们会将图中拐点所对应的值作为筛选的阈值，本例中我们选择前10个PC来进行聚类分析（通常使用更高的PC对结果的影响并不大，但是使用较小的PC会对结果产生不利的影响）。

Seurat基于 PCA 空间中的欧几里德距离构建一个 KNN 图，并根据其局部邻域中的共享重叠优化任意两个单元之间的边权重，基于Louvain算法对细胞进行聚类分群。
