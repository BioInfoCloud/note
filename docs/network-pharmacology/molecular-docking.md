# 分子对接

## 一、软件安装准备

网站下载地址:<http://autodock.scripps.edu/>

进入网站首页点击 downloads，进入下载页面。需要从这里下载 2 个软件：**AutoDock 4.2** 和**MGLTools**。

**AutoDock 4.2 的下载**：右键 proceed to download page，在新窗口中打开。在打开页面底部有下载地址，根据自己的系统选择下载，这里是 Windows。懒人链接：<http://autodock.scripps.edu/downloads/autodock-registration/autodock-4-2-download-page/>

![1611822879994-5ce207ff-f7f5-4e1a-9b30-f9e333f01c0e.png](./img/molecular-docking/1611822879994-5ce207ff-f7f5-4e1a-9b30-f9e333f01c0e-447912.png)

mgltools 的下载：下载页面底部有个 ADT，新页面点击 AutoDockTools，然后选择适合自己的系统版本，懒人链接：<http://mgltools.scripps.edu/downloads>

![1611823545576-b11acf2e-496c-417c-8d55-615991bfe8de.png](./img/molecular-docking/1611823545576-b11acf2e-496c-417c-8d55-615991bfe8de-307872.png)

其他分子对接辅助软件，比如：OpenBabel，PyMOL，Python 等软件自己 Google 下载，Python 需要安装 2.0 序列的，这个必须安装，安装完成后需要配置环境变量，不知道怎么配置环境变量，Google 或者百度一下，很简单。当然，这些安装包我上传到了云盘。链接：<https://pan.baidu.com/s/1oLKITNG-mRWBVOSXepbJrg> ，提取码：mx5u

![1611823976076-964da0e3-8412-4371-9e4a-79de994c225a.png](./img/molecular-docking/1611823976076-964da0e3-8412-4371-9e4a-79de994c225a-410131.png)

安装好这些软件后，我们需要设置一个工作环境。安装好 AutoDock 4.2 和 mgltools 后，你可以选择一个盘创建一个工作环境的文件夹，以后你就在该文件夹下完成分子对接，我这里是在 F:\Autodock\文件夹。如果你没有更改安装路径，那么你会在 C:\Program Files (x86)\The Scripps Research Institute\Autodock\4.2.6 文件夹下看见这 2 个文件。将这 2 个文件复制到 F:\Autodock 中。

![1611824214987-51a1b0dd-537f-4672-a1d5-f7c404caa1fb.png](./img/molecular-docking/1611824214987-51a1b0dd-537f-4672-a1d5-f7c404caa1fb-019674.png)

同样的，安装 mgltools 软件的安装目录下有个 adt.bat，我这里的安装路径是：C:\Program Files (x86)\MGLTools-1.5.6，将 adt.bat 这个文件复制到 F:\Autodock\文件中。

![1611824454923-b39bf3cf-5b7f-4b07-8a7e-8b5cbe810c27.png](./img/molecular-docking/1611824454923-b39bf3cf-5b7f-4b07-8a7e-8b5cbe810c27-849587.png)

这里在 F:\Autodock\文件夹下就有了 3 个文件。

![1611824693853-54f125ff-d845-4d2e-b7ac-b7ade8d063ea.png](./img/molecular-docking/1611824693853-54f125ff-d845-4d2e-b7ac-b7ade8d063ea-236617.png)

然后我们打开 Autodock 软件。点击 File，选择 Preference，再选择 Set。

![1611824871069-55074d02-2910-4f99-8dd1-f5ea9bf3df72.png](./img/molecular-docking/1611824871069-55074d02-2910-4f99-8dd1-f5ea9bf3df72-712897.png)

在 Startup Directory 中粘贴你的工作路径，我上面是 F:\Autodock\，这里就输入 F:\Autodock，然后点击 Make Default。就设置好默认的工作路径了，后面我们需要对接的配体分子和蛋白分子都放在该目录下。

![1611825000869-16b17520-0082-4447-9f8e-f4e3c1ebe119.png](./img/molecular-docking/1611825000869-16b17520-0082-4447-9f8e-f4e3c1ebe119-586363.png)

## 二、选择合适的蛋白受体

关于蛋白质结构的 PDB 文件，做分子对接，估计大家都知道 PDB 这个蛋白质数据库啦。这里简单的介绍一下。

蛋白质的三级结构是指整条多肽链的三维空间结构，也就是包括碳骨架和侧链在内的所有原子的空间排列。第一个蛋白质的三维空间结构于 1958 年用 X-射线衍射法（X-ray Crystallography）测定。这种方法目前仍然是获取蛋白质三级结构的主要方法。PDB 数据库中绝大多数蛋白质结构都是用这种方法测定的。另一个测定蛋白质三维空间结构的方法是核磁共振法（Nuclear Magnetic Resonance, NMR）。无法结晶的蛋白质，可以利用核磁共振法在液体环境中进行结构测定。但是核磁共振法只能用于质量小于 70 千道尔顿的分子，大约对应 200 个氨基酸的长度。除此之外，还有一些不太常用的方法也可以测定分子的三维空间结构，比如冷冻电子显微镜技术（Cyro-Electron Microscopy）。无论用什么方法测定的空间结构，都要提交到 PDB 数据库。所以我们获取蛋白质三级结构最直接的办法就是去 PDB 搜索（<http://www.rcsb.org/>）。

![1611833310137-732bc09b-6dce-4c72-8c3b-98ae2df361ae.png](./img/molecular-docking/1611833310137-732bc09b-6dce-4c72-8c3b-98ae2df361ae-671795.png)

从 PDB 首页的搜索条里，可以通过搜索 PDB ID、分子名称、作者姓名等关键词来查找蛋白质三级结构。此外，利用高级搜索工具，可以通过序列相似性搜索获得与输入序列在序列水平上相似的蛋白质的三级结构。搜索方法选 BLAST，输入序列，点击“Result Count”。这里不详细介绍，因为我们做分子对接，通常蛋白名称是已知的。**我们重点介绍怎么选择合适的蛋白结构文件**。

![1611833461093-9a22641c-db35-4d42-939d-579da1a83367.png](./img/molecular-docking/1611833461093-9a22641c-db35-4d42-939d-579da1a83367-800424.png)

比如我们搜索 PI3K 这个蛋白，结果是有很多的。可以看到有 393 个结构信息。

![1611833917623-b77c5286-d302-444c-a719-dad8fb69a8ab.png](./img/molecular-docking/1611833917623-b77c5286-d302-444c-a719-dad8fb69a8ab-409533.png)

首先我们可以通过左边的栏进行筛选，比如物种信息，我们选择人。当然，结果的显示排序可通过结果上面的选项卡进行选择不同的排序方式。我们筛选合适的蛋白结构，常用 Score 这个选项。

![1611834166125-80607368-7e46-4db5-9c48-ac98d4911bd8.png](./img/molecular-docking/1611834166125-80607368-7e46-4db5-9c48-ac98d4911bd8-761914.png)

我们选择分辨率较好的在前。这里的 0.9Å，**Å是光波长度和分子直径的常用计量单位，值越小，分辨率越高，结构越准确。页面往下拉，可以看见这个值越来越大，我们优先选择值小的**。我们可以从页面里面看见一下基本信息，比如方法，物种以及被解析的时间等。这里 5GJI 这个结构获取的方法就是 X-RAY。

![1611834356470-b56e0bdc-a458-4ce4-8693-7d76666d2d0f.png](./img/molecular-docking/1611834356470-b56e0bdc-a458-4ce4-8693-7d76666d2d0f-208200.png)

我们点击这个蛋白，进入后可以看见详细的信息。

![1611834683964-ca4e619e-61c3-480a-8503-b3ef15fd2ae2.png](./img/molecular-docking/1611834683964-ca4e619e-61c3-480a-8503-b3ef15fd2ae2-118954.png)

然后我们还要看这个蛋白的描述是不是我们想要的蛋白，从这里面感觉看起来比较费劲。这里我们借助 uniprot 这个数据库来选择是比较方便的。这里简单介绍一下这个数据库，可能有的同学是第一次知道。**翻了多年前的笔记，粘贴在下面。**

UniProt 数据库有三个层次。

第一层叫 UniParc，收录了所有 UniProt 数据库子库中的蛋白质序列，量大，粗糙。

第二层是 UniRef，他归纳了 UniProt 几个主要数据库并且是将重复序列去除后的数据库。

第三层是 UniProtKB，他有详细注释并与其他数据库有链接，分为 UniProtKB 下的 Swiss-Prot 和 UniProtKB 下的 TrEMBL 数据库。

关系稍有点复杂，但实际上我们最常用的就是 UniProtKB 下的 Swiss-Prot 数据库。

从 UniProt 数据库查看一条蛋白质序列（[http://www.uniprot.org/](http://www.uniprot.org/)）。在 UniProt 数据库的首页上有一个关于 UniProtKB 数据库的统计表。可以看到，TrEMBL 数据库里存储的序列数量远远大于 Swiss-Prot 中的。统计表里清楚的写着：TrEMBL 是自动注释的，没有经过检查，而 Swiss-Prot 是人工注释的，并且经过检查。

![1604969277464-c1d9e0ab-8590-49b5-b8dd-29154a9a3d61.png](./img/molecular-docking/1604969277464-c1d9e0ab-8590-49b5-b8dd-29154a9a3d61-350370.png)

UniProt 数据库的首页上也有一个搜索条，选择 UniprotKB 数据库，然后输入“human dutpase”，第一条就是我们要的。Entry 这一列是蛋白质序列在 UniProtKB 数据库中的检索号，Entry_Name 是检索名，检索号与检索名平行运行，都是一条序列在数据库中的唯一标识，两者作用相同，只是写法不同。从检索名可以更直观的知道是哪个物种的什么蛋白质。从加星文档图标（Entry_Name 后一列）我们可以获知序列是被人工检查过的还是没有。也就是说，有加星文档图标的是 Swiss-Prot 中的数据，没有的是 TrEMBL 里的。后面这几列，依次是蛋白质的名字，编码这一蛋白质的基因的名字，所属物种以及序列长度。点击第一条序列的检索号，打开这条数据库记录。

![1604969277802-9b0ce776-fad3-4109-aeb2-a71160d85b5c.png](./img/molecular-docking/1604969277802-9b0ce776-fad3-4109-aeb2-a71160d85b5c-521528.png)

UniProtKB 中的数据库记录分成几个部分，左侧是注释标签，点击其中某一个标签可以直接跳转到该部分注释。上方是工具标签，可以用于和其他序列进行比较，格式转换，存储等。工具标签下方是这条蛋白质序列的基本信息，蛋白质的名字，基因的名字，所属物种，以及状态。这里有加星文档图标，是被人工检查过的，应该属于 Swiss-Prot 数据库。注释打分 5 星，说明注释得很全面，并且这些注释在蛋白质水平上有实验依据。

**Function：**功能这部分注释很详细的说明了这个蛋白质的功能。从这里可以得知 dUTPase 是一种在核酸代谢过程中的酶、它的催化反应方程式、它的辅助因子、它参与的代谢途径等。每条注释信息都提供出处来源，让你有据可查。

**Names & Taxomomy：**给出了蛋白质的各种名字，包括全称、缩写以及别名。还列出了所属物种以及该物种的分类学谱系等。

**Subcellular location：**提供蛋白质亚细胞定位（subcellular localization）的信息。目前，研究亚细胞定位的数据来源基本都是 Swiss-Prot 数据库。

![1604969277991-fba61c58-4d91-4657-adf5-ce268b4f6368.png](./img/molecular-docking/1604969277991-fba61c58-4d91-4657-adf5-ce268b4f6368-003644.png)

**Pathology & Biotechnology：**提供蛋白质突变或缺失导致的疾病及表型信息。

**PTM/Processing：**提供蛋白质翻译后修饰或翻译后加工的相关信息。

**Expression：**提供了基因在 mRNA 水平上的表达信息，或者在细胞中蛋白质水平上的表达信息，或者在不同器官组织中的表达信息。

**Interaction：**提供了蛋白质之间相互作用的信息。包括 UniProtKB 中直接与这个蛋白质有两两相互作用的蛋白质序列的链接，以及这个蛋白质在各种蛋白质相互作用数据库或蛋白质网络数据库中涉及的数据库记录链接。

**Structure：**提供蛋白质二级结构和三级结构信息。只有那些已通过实验方法测定三级结构并且已提交到蛋白质结构数据库 PDB 的蛋白质才有结构注释。二级结构以图形拓扑的形式呈现。三级结构列出了该蛋白质在蛋白质结构数据库 PDB 中涉及的数据库记录链接。这些结构经常只对应蛋白质的部分序列。

**Family & Domains：**提供蛋白质家族及结构域信息。

**Sequence：**提供蛋白质氨基酸序列信息。含有多个异构体的蛋白质会显示多条序列。

**Cross-references：**列出了所有通往其他含有该蛋白质信息的数据库的链接。

**Publications：**列出了有关这个蛋白质已发表的所有文献的信息。

**Entry information：**提供有关这条数据库记录的录入信息，外加一个免责声明。

**Miscellaneous**：杂项，包含任何无法归入前几项的内容。

**Similar Proteins**：在 UniRef 数据库里找到与该蛋白质在序列水平上相似的其他蛋白质，并按相似度高低分组。

好了，我们接着前面的介绍。我们在 UniProt 的搜索框中输入关键词，左侧选择相应的物种。

![1611835245076-06b700bc-4455-4114-8df2-9161251b13ed.png](./img/molecular-docking/1611835245076-06b700bc-4455-4114-8df2-9161251b13ed-555219.png)

新页面下直接选择 Structure。左边就是显示结果，有一个列表给我们快速查看相关参数。可以根据这些参数选择合适的结构，注意 positions 这一栏，我们首先选择 resolution 小的，但结构不是我们要的，就不行，resolution 这一栏只是该结构只是该蛋白的序列区段，比如这里 1-143 这一段氨基酸序列是不在该结构中的。我们需要根据一些文献知识，了解一般配体所在的部位即相关活性位点。有没有已知的结合区域来参考选择，我个人认为，如果不知道，越长的越好。有的还是多条肽链的复合物，如果是二聚体的，后面对接可以删除一个。总之，需要先了解这些已解析的晶体结构是否已经包含了拟对接分子的潜在结合位点，以及已知配体与我们要对接的分子的结构相似度——越相似越好。还需注意晶体结构中蛋白序列是否为野生型、是否含有 PTM、是否存在可能引起构象变化的特殊有机溶剂和别构效应分子等。如果系列晶体结构的性质都类似，则选择分辨率最高的。

![1611835781199-683f15b3-6231-475b-950d-9ae7db772def.png](./img/molecular-docking/1611835781199-683f15b3-6231-475b-950d-9ae7db772def-439614.png)

点击链接栏中的 PDB，就可以直接进入该结构的 PDB 页面了，然后点击下载文件就可以直接下载 PDB 格式的蛋白结构文件。下载的 PDB 文件可以用 pymol 或者 VMD 观察结构。能够实现蛋白质三维结构可视化的软件非常多。比专业级的 PyMOL（<https://pymol.org/2/>）。这个软件已经被世界上著名的生物医药软件公司“薛定谔公司（Schrödinger）”收购。这种专业级的可视化软件不仅能够做出非常漂亮的图片，它还有强大的插件支持各种各样的蛋白质结构分析，这款软件需要购买，如果你发表的文章里提到某些内容是使用 PyMOL 制作的，而文章中所有作者和作者单位都没有 PyMOL 的购买记录的话，你可能会面临薛定谔公司的追责。

下面给大家介绍一个功能同样强大的免费蛋白质三维结构可视化软件，VMD（<http://www.ks.uiuc.edu/Research/vmd>）。VMD 由伊利诺伊大学研发。下载 VMD 需要先注册获得一个账户，之后就可以根据你的操作系统和机器配置选择合适的版本下载了。当然，如前所述，注册和下载对于非商业用途的用户都是免费的。VMD 的安装也极其简单。不需要预装任何语言环境，完全图形化安装过程，绝对可以轻松搞定。

![1611837336863-2f5325ac-50f1-4e3c-9d46-46f82253006a.png](./img/molecular-docking/1611837336863-2f5325ac-50f1-4e3c-9d46-46f82253006a-386183.png)

最后，这些都是在蛋白结构已知的蛋白分子对接，如果我们要对接的蛋白，没有晶体结构，在 PDB 中是检索不到的，在 UniProt 中的 Structure 是不会显示的。比如 DRAM1 这个蛋白，是没有结构的，所以在 UniProt 中的 Structure 是灰色。

![1611838389721-60afa3b3-24c7-4755-a638-8074534e7b86.png](./img/molecular-docking/1611838389721-60afa3b3-24c7-4755-a638-8074534e7b86-084027.png)

如果没有结构，我们又要对接，那就只能是自己通过软件预测了。蛋白质结构预测的方法有从头计算法，同源建模法，穿线法和综合法。常用的是同源建模法，SWISS-MODEL（www.swissmodel.expasy.org）就是一款用同源建模法预测蛋白质三级结构的全自动软件，这里不详细介绍了，预测的模型还要涉及模型好坏的评价，后续有时间，介绍蛋白质三级结构的预测。

## 三、配体分子文件格式转换

我们知道，分子文件的格式很多，比如 mol，sdf 等，但 AutoDock 这个软件不识别 sdf 这样的格式文件，而我们通常下载的文件就是 sdf 这个格式的文件。我们需要转换成 mol2 或者 PDB 格式的文件，才能被 AutoDock 这个软件所读入。当然，有一些分子我们是可以从一些数据库中直接下载 mol2 格式文件的。比如一些中药成分小分子，我们可以从 TCMSP 这个数据库下载（<https://tcmspw.com/>），比如:quercetin

![1611840289434-a56f3f71-645e-4ac9-9a6a-3033c2cad3bf.png](./img/molecular-docking/1611840289434-a56f3f71-645e-4ac9-9a6a-3033c2cad3bf-369297.png)

然后点击图片，下载的就是 mol2 格式的分子文件。

![1611840390162-ab9dee25-060f-401d-a32b-e0e994c64fb9.png](./img/molecular-docking/1611840390162-ab9dee25-060f-401d-a32b-e0e994c64fb9-818580.png)

还有一个数据库能下载 mol2 格式的文件。ZINC(<http://zinc.docking.org/>)，这里就不介绍了，你要是能从上面的数据库下载到你配体小分子的 mol2 格式文件，就直接用，如果不能，那就是去 PubChem 数据库（<https://pubchem.ncbi.nlm.nih.gov/>）下载 sdf 文件，然后进行转换，这也是我这里要介绍的。

首先在 PubChem 数据库检索你的化合物，进入相应的页面，3D Conformer 处点击下载，会有 sdf 格式文件的下载选项。

![1611841011209-bb9a7ddf-0318-4a77-a0ac-0ce0c6a0e510.png](./img/molecular-docking/1611841011209-bb9a7ddf-0318-4a77-a0ac-0ce0c6a0e510-573810.png)

分子格式文件的转换，需要 OpenBabel 这个软件，这个软件能实现各种格式转换，用起来也挺简单的。

打开软件，左侧选择我们的输入文件，是什么格式的就选择什么格式的，右侧数输入文件，要什么格式选择什么格式，最后点击中间的 CONVERT，就会在输出路径的下产生相应的输出文件。我这里转换成了 PDB，因为 mol2 格式的文件我们从 TCMSP 这个数据库下载了。

![1611841382909-bbb3caca-2f38-4b3e-a8ea-c5c60767050d.png](./img/molecular-docking/1611841382909-bbb3caca-2f38-4b3e-a8ea-c5c60767050d-019759.png)

## 四、蛋白受体文件的预处理

对于蛋白质，在对接之前我们需要预处理，比如，去水，加全氢，导出为 PDBQT 文件设为受体，下面我们来介绍一下怎么做。

我们这里处理蛋白文件需要借助 pyMOL 这个软件，我在前面提到过，我也上传到了网盘，有 2 个版本，一个 2.2，一个 2.4，前面说安装时需要安装 2.0 序列的 Python，这是针对 2.2 版本的 pyMOL，如果你安装 2.4 版本，需要安装 Python3.7。我用的是 2.4 的版本，有点喜新厌旧啦。

首先我们打开 pyMOL 这个软件

![1611889623774-dda97a8d-69ca-4eb5-af5b-30f1e1083266.png](./img/molecular-docking/1611889623774-dda97a8d-69ca-4eb5-af5b-30f1e1083266-517032.png)

我们这里可以直接打开我们下载的 pdb 格式的分子结构文件，如果是 PDB 数据库的蛋白，我们可以通过命令`fetch 1e8y`下载。1e8y 是我们蛋白的 PDB ID。回车后就会在可视化窗口看见我们的蛋白结构。

![1611891878493-70af58d7-3d0b-443b-ad68-a950af41069d.png](./img/molecular-docking/1611891878493-70af58d7-3d0b-443b-ad68-a950af41069d-861800.png)

或者通过 File 里面选择 get PDB...，弹出窗口输入信息后点击下载。**下图中是 1e8y，当时输错啦**。

![1611890919715-17ffc000-db75-4787-9177-6bae0081584c.png](./img/molecular-docking/1611890919715-17ffc000-db75-4787-9177-6bae0081584c-543661.png)

如果窗口中不显示该结构的信息，我们在软件的右下角点一下 S，就出来了。或者从菜单栏 Display 里勾选 Sequence

![1611891920648-e85f8f34-08b5-4e07-9780-a4c61e808b32.png](./img/molecular-docking/1611891920648-e85f8f34-08b5-4e07-9780-a4c61e808b32-839081.png)

然后我们可以通过序列，左右滑动，删除我们不需要的部分，比如水分子，把 0 全部选中，右键点击 remove，就删除了。如果有其他金属离子，那就需要根据需要了，如果该离子是该蛋白的组成部分，那就不能去除。

![1611896854347-970a927f-fcbe-447c-a666-c01b1fd351ac.png](./img/molecular-docking/1611896854347-970a927f-fcbe-447c-a666-c01b1fd351ac-026153.png)

我们可以继续用 pymol 进行加氢处理，也可以后续用 AutoDockTools 处理。我们统一用 autodocktools 吧，因为 pymol 的功能很多，一时间介绍不完，B 站有很多教程，你可以去搜索学习，当然，你可以完成对接后，再去学习。我们这里保存为 PDB 格式蛋白文件文件名称：1E8Y_PYMOL.pdb。

![1611897926321-db22317a-3ba2-42aa-a6e9-57c8be332966.png](./img/molecular-docking/1611897926321-db22317a-3ba2-42aa-a6e9-57c8be332966-630402.png)

如果我们去掉的组分比较多，比如有多条链，去掉了其中的一些链，把不需要的水分子，离子，溶剂分子去掉，只保留对对接需要的部分，对剩下的结构我们需要进行一个修复。这里需要一个网页工具，地址：<https://swift.cmbi.umcn.nl/servers/html/model.html.> 做法是找到网页最下面的 Prepare PDB file for docking programs，点进去，输入一个 PDB ID 或者上传自己的蛋白结构文件，然后点击 send，稍等一下可以直接下载处理过的蛋白结构文件。

![1611899550703-0a88a813-d1b2-40c8-9d05-3c9fdbabc05e.png](./img/molecular-docking/1611899550703-0a88a813-d1b2-40c8-9d05-3c9fdbabc05e-231650.png)

我这里修复后的文件继续保存为：1E8Y_PYMOL.pdb，也就是覆盖了上面的那个文件。

接下来我们打开 AutoDocktools，打开我们前面保存的文件 1E8Y_PYMOL.pdb。

![1611898753855-1264bdc5-4ea9-4213-b1ab-fd4cf83629b4.png](./img/molecular-docking/1611898753855-1264bdc5-4ea9-4213-b1ab-fd4cf83629b4-072347.png)

![1611899831980-40f8c58f-ba4b-4563-8e5c-aed8ae6893cb.png](./img/molecular-docking/1611899831980-40f8c58f-ba4b-4563-8e5c-aed8ae6893cb-953979.png)

这里，颜色显示方式，我们可以点击 CL 栏的下三角符号，可以通过不同方法按照颜色选择。比如下面的，通过原子类型。

![1611902067415-b58a48f3-bf94-4328-b2ae-fc28040403cd.png](./img/molecular-docking/1611902067415-b58a48f3-bf94-4328-b2ae-fc28040403cd-788469.png)

关于什么颜色代表什么原子，如下：

![1611902197626-5aa9a1a6-bd91-4f24-9b1b-79aad96193e6.png](./img/molecular-docking/1611902197626-5aa9a1a6-bd91-4f24-9b1b-79aad96193e6-801765.png)

如果我们前面没有用 pymol 去掉水分子，那么可以按照下图去掉水分子，因为我们我们需要修复结构，有时候也不是单单的去掉水分子，所以还是先用 PyMol 处理好一些。我们这里已经去掉水分子了，所以这一步省略。

![1611899994775-8719cf2c-c85b-49b2-bc9f-90c184985bfc.png](./img/molecular-docking/1611899994775-8719cf2c-c85b-49b2-bc9f-90c184985bfc-459957.png)

接下来就是加氢，因为从 pdb 数据库中下载蛋白质晶体结构是没有氢原子的（除了很少分辨率小于 1A 的蛋白质有 H），这是一个技术问题。所以我们需要把氢原子加上，这一步是必须的。**官方解释也是：在选择一个分子作为配体或受体之前，必须把所有的氢都加到这个分子上**。**注意是全氢**。按照下面操作加氢。

![1611903586847-f0de83e1-f7a8-4178-937a-306b505c6f74.png](./img/molecular-docking/1611903586847-f0de83e1-f7a8-4178-937a-306b505c6f74-719583.png)

![1611902737955-a5a30372-5008-46ac-92fc-4c789fd7c72a.png](./img/molecular-docking/1611902737955-a5a30372-5008-46ac-92fc-4c789fd7c72a-399352.png)

我们就可以看见多了好多白色，白色就是氢原子。

![1611902774462-b631d810-2806-41b8-97c4-309a914652b6.png](./img/molecular-docking/1611902774462-b631d810-2806-41b8-97c4-309a914652b6-986800.png)

然后我们按照下面操作保存为受体文件。

![1611904189024-223ff955-c9dd-42c6-b503-32748b199269.png](./img/molecular-docking/1611904189024-223ff955-c9dd-42c6-b503-32748b199269-664816.png)

上面这一步操作方式选择大分子会自动执行以下一系列初始化步骤，ADT 检查分子是否带有电荷。如果没有，它会给每个原子加上 Gasteiger 电荷。**记住，所有的氢必须先加到大分子上**，然后才被选中。如果分子已经带电荷，

ADT 会问你是否想保留输入电荷而不是增加 Gasteiger 电荷。还有，该步骤，ADT 会合并非极性氢，如果你不需要，需要手动设置。下面是官方文档的解释。

![1611904941619-167b7b7b-7191-4392-82d7-5d0093ecdb65.png](./img/molecular-docking/1611904941619-167b7b7b-7191-4392-82d7-5d0093ecdb65-326822.png)

另外，有的人可能在保存文件之前会将原子类似设置为 AD4 type ，其实这一步不需要，因为我们按照上面的操作，软件会自动设置的。

![1611905236227-e2116a35-a94a-4f14-b8f6-ecb6d3542513.png](./img/molecular-docking/1611905236227-e2116a35-a94a-4f14-b8f6-ecb6d3542513-911716.png)

好了，保存文件后，我们可以删除分子，后续处理小分子。

![1611905686079-04c55619-41f6-4dfe-b37c-c14b54b2d6d7.png](./img/molecular-docking/1611905686079-04c55619-41f6-4dfe-b37c-c14b54b2d6d7-644484.png)

## 五、配体小分子的预处理

前面介绍了蛋白受体文件的预处理，这里处理小分子就简单多了。

同样的，打开小分子文件。我前面准备了 2 个格式的文件，选择其中一个，这里我选择了 mol2 格式的。

![1611905888973-d0c63294-08c1-4d6c-94eb-e94217a53883.png](./img/molecular-docking/1611905888973-d0c63294-08c1-4d6c-94eb-e94217a53883-232989.png)

![1611906035697-2de917c5-0437-42ac-9cd3-9e598130bfab.png](./img/molecular-docking/1611906035697-2de917c5-0437-42ac-9cd3-9e598130bfab-781086.png)

前面提到，在选择一个分子作为配体或受体之前，必须把所有的氢都加到这个分子上，而且要加全氢。这里我们打开小分子文件，这一步弹出的窗口默认即可——如果你读入的是 PDB 格式的文件，那么在方法处选择的是 noBondOrder，默认同样是 noBondOrder。

![1611906238819-5d28ab54-3831-470c-93c0-51c1140b61db.png](./img/molecular-docking/1611906238819-5d28ab54-3831-470c-93c0-51c1140b61db-442824.png)

接下来，将分子选为配体。

![1611906874635-49b1dabb-4a82-4ca3-9370-18746c4bc051.png](./img/molecular-docking/1611906874635-49b1dabb-4a82-4ca3-9370-18746c4bc051-005573.png)

输出 PDBQT 格式的配体文件。接下来检测一下扭转键和中心。

![1611907357405-f31abf0f-ebba-4cac-b727-466e376bdf40.png](./img/molecular-docking/1611907357405-f31abf0f-ebba-4cac-b727-466e376bdf40-897659.png)

导出为 PDBQT

![1611907492498-d43f2252-e733-4076-aea2-d20cbbb8384f.png](./img/molecular-docking/1611907492498-d43f2252-e733-4076-aea2-d20cbbb8384f-566073.png)

我这里保存的文件名为：quercetin.pdbqt

可能有的同学还会以如下图的方式添加电荷。

![1611907830407-d94fe6a4-e1ab-45be-a130-92d5cb1ddc47.png](./img/molecular-docking/1611907830407-d94fe6a4-e1ab-45be-a130-92d5cb1ddc47-785862.png)

但其实这一步没有必要，**而且会出错**，因为我们前面通过 Ligand 里面设置的时候，软件已经自动给我们自动处理好了。就是下图中的弹出框，比如融合了 5 个非极性氢。

![1611906874635-49b1dabb-4a82-4ca3-9370-18746c4bc051.png](./img/molecular-docking/1611906874635-49b1dabb-4a82-4ca3-9370-18746c4bc051-005573.png)

但是，有时候，我们不手动添加电荷，按照上面的操作，有的小分子也会报错，怎么解决？官方的描述是这样的：If each ligand atom already has a ‘partial charge’ those charges are used. If not or if each of the charges is zero, ADT computes Gasteiger charges for the entire ligand. For this calculation to work correctly, the molecule must already have hydrogen atoms added, including both polar and non-polar ones, prior to this step【翻译：如果每个配体原子已经带有“部分电荷”，这些电荷就会被使用。如果不是，或者每个电荷都为零，ADT 计算整个配体的 Gasteiger 电荷。为了使计算正确进行，在此步骤之前，分子必须已经添加了氢原子，包括极性的和非极性的。】，我么只需要记住，如果出错，那就是每个电荷都为零的情况，我们在选择作为配体之前需要计算 Gasteiger 电荷，具体怎么计算看下图，按照下图操作后在设置为配体。

![1611909370367-04613b64-9a11-406c-91a6-f3466739d33f.png](./img/molecular-docking/1611909370367-04613b64-9a11-406c-91a6-f3466739d33f-538306.png)

那么如果没有出错，是每个配体原子已经带有“部分电荷”的情况，在设置为配体之前，我们需要计算 Gasteiger 电荷吗？不需要，如果再计算 Gasteiger 电荷，本身原本就有部分电荷，最后对接的结合能是不一样的。只需要记住，如果设置为配体出错，再去计算 Gasteiger 电荷。

## 六、对接操作与对接结果解读

首先导入受体蛋白，这一步，ADT 会问你是否想保留输入电荷，**对于蛋白受体，无论什么情况下，我们是不需要手动计算 Gasteiger 电荷的，下面操作后会自己更正**。

![1611918269623-443daa94-ae46-4864-a325-79c41c4a422b.png](./img/molecular-docking/1611918269623-443daa94-ae46-4864-a325-79c41c4a422b-125571.png)

接下来导入小分子

![1611918586958-54daba19-5d67-4c91-9e27-2b8e12b5452f.png](./img/molecular-docking/1611918586958-54daba19-5d67-4c91-9e27-2b8e12b5452f-380354.png)

接下来你可以按照下图设置显示形式，颜色按照前面的倒三角形里面选择显示二级结构，通过链显示颜色。

![1611919319125-79e6c97a-57e7-4e48-945a-a5266f847679.png](./img/molecular-docking/1611919319125-79e6c97a-57e7-4e48-945a-a5266f847679-319155.png)

选择 Grid>Grid Box...设置对接的盒子大小、坐标、格点数、格点距离，这一步需要自己根据不同的结构来进行具体确认。一般来说最简单的方法是：查阅文献、晶体结构数据库，寻找配体可能的结合位点附近的重要氨基酸残基。对接的中心坐标并不一定非常准确，只要对接的盒子包含了配体可能结合的最大区域即可。

![1611919585552-1679972a-966a-4920-a89c-f16b65bdfeb4.png](./img/molecular-docking/1611919585552-1679972a-966a-4920-a89c-f16b65bdfeb4-117556.png)

我这里没有详细去查，所以选择全部包裹。通过调整后，蛋白已被全部包裹。

![1611919753697-0e59f915-1847-4151-8d90-d4c579cb8371.png](./img/molecular-docking/1611919753697-0e59f915-1847-4151-8d90-d4c579cb8371-277218.png)

这里看不见蛋白了。可以在 View 中勾选 Show box as lines，让盒子只显示外框。

![1611919852675-4920a50c-824f-4c91-9398-57ce154a9a07.png](./img/molecular-docking/1611919852675-4920a50c-824f-4c91-9398-57ce154a9a07-875212.png)

然后把我们的小分子取出来，弹出窗口，选择小分子，把图中的√去掉。

![1611920292101-e708f597-f512-4c2c-a6e5-10154043c4a6.png](./img/molecular-docking/1611920292101-e708f597-f512-4c2c-a6e5-10154043c4a6-703972.png)

右键选择小分子，拖动出来。

![1611920404300-eff5ddf4-a1f7-4a5d-9b75-eca144c6f141.png](./img/molecular-docking/1611920404300-eff5ddf4-a1f7-4a5d-9b75-eca144c6f141-726495.png)

然后再把上面的√勾选回去，关掉弹出窗口，接下来保存盒子。

![1611988777649-6b38c53c-0abf-4c50-a46a-2f06efe55f99.png](./img/molecular-docking/1611988777649-6b38c53c-0abf-4c50-a46a-2f06efe55f99-319429.png)

![1611920666743-6329c9e5-9dbd-4dd0-bed6-cb066bea70e9.png](./img/molecular-docking/1611920666743-6329c9e5-9dbd-4dd0-bed6-cb066bea70e9-880899.png)

然后导出 GPF 文件。

![1611920769951-a4e52dd5-d43b-4a79-9bd7-9176f493c4e5.png](./img/molecular-docking/1611920769951-a4e52dd5-d43b-4a79-9bd7-9176f493c4e5-900010.png)

我这里保存的名称为：1e8y.gpf

接下来运行 Grid，按下图操作，弹出窗中 Parameter Filename 栏点击 Browse。

![1611981582639-608d1026-fc29-4d63-869e-a6a24ec46492.png](./img/molecular-docking/1611981582639-608d1026-fc29-4d63-869e-a6a24ec46492-844206.png)

选择我们前面保存的 1e8y.gpf 文件，选择后 log Filename 这一栏就会自动填写，这里需要注意的是，工作目录需要和我们前面设置的一样。

![1611981743332-b7a4aedd-d16b-49f2-9f1a-0d2b3abd9dbc.png](./img/molecular-docking/1611981743332-b7a4aedd-d16b-49f2-9f1a-0d2b3abd9dbc-831509.png)

点击 launch 后会弹出下面这个窗口。

![1611981887348-919c2da7-f80f-4af1-9056-eea4f66506fd.png](./img/molecular-docking/1611981887348-919c2da7-f80f-4af1-9056-eea4f66506fd-224054.png)

**重要提醒！**这里不要关闭这个窗口，因为程序一直在运行，这个过程你在工作目录下生成一些 map 格式的文件。

![1611982039597-6aef7202-1bc7-436e-970a-433fb567a6f9.png](./img/molecular-docking/1611982039597-6aef7202-1bc7-436e-970a-433fb567a6f9-329824.png)

运行结束后，这些文件的大小将发生改变。

![1611982331293-20c882a2-cf1f-4d97-8ced-3b9e9906d0b2.png](./img/molecular-docking/1611982331293-20c882a2-cf1f-4d97-8ced-3b9e9906d0b2-800091.png)

接下来，我么准备 AutoDock 的运行参数以及计算方法。我这里选择的是半柔性对接，选择 Set Rigid Filename。

![1611982506582-4ee3a534-ce17-4386-b72c-982c49c17752.png](./img/molecular-docking/1611982506582-4ee3a534-ce17-4386-b72c-982c49c17752-243321.png)

然后选择我们前面选择的保存的 pdbqt 文件。

![1611982695773-abd7da30-54ae-45ab-ac93-ce0c642e801b.png](./img/molecular-docking/1611982695773-abd7da30-54ae-45ab-ac93-ce0c642e801b-346123.png)

![1611982913904-3d790032-7a6e-4a05-8723-46d6074f4e34.png](./img/molecular-docking/1611982913904-3d790032-7a6e-4a05-8723-46d6074f4e34-897087.png)

设置搜索参数和算法，在最后一个弹出框中，第一个选项，Number of GA Runs 表示我们对接多少次，这里默认 0 次，官方建议对接 50 次以上，这里演示就设置 10 次。还有，Maximum Number of evals 和 Maximum Number of generations 的值可以设置大一些，从而获得较优构象，但值越大，后面运行 AutoDock 的时间会越长。

![1611983072152-eb16a43d-0320-4d71-b9ae-43b7e1cfdf65.png](./img/molecular-docking/1611983072152-eb16a43d-0320-4d71-b9ae-43b7e1cfdf65-259392.png)

设置对接参数

![1611983138218-baeccfbe-7630-4ea2-9dbc-85cad44f3e7d.png](./img/molecular-docking/1611983138218-baeccfbe-7630-4ea2-9dbc-85cad44f3e7d-617349.png)

接下来输出 dpf 文件。

![1611983340960-648c575e-128d-4339-830c-c9f76faca419.png](./img/molecular-docking/1611983340960-648c575e-128d-4339-830c-c9f76faca419-704295.png)

接下来运行 AutoDock，这里和前面运行 Grid 差不多，选中我们的 dpf 文件，选择后 log Filename 这一栏就会自动填写，同样需要注意的是，工作目录需要和我们前面设置的一样。

![1611983512931-e55ba9ee-ab48-4f80-ab97-6c1229b1aeaf.png](./img/molecular-docking/1611983512931-e55ba9ee-ab48-4f80-ab97-6c1229b1aeaf-106679.png)

然后点击 launch 运行程序。同样不能关闭这个窗口或点击 Dismiss，这个过程会在工作目录产生一个相应的 dlg 格式文件，这个文件就是对接结果。

![1611983627998-f356cd07-a94f-477a-acc6-5cbe58162513.png](./img/molecular-docking/1611983627998-f356cd07-a94f-477a-acc6-5cbe58162513-637654.png)

在对接完成之后需要分析分子对接结果，也是做分子对接最重要的部分。我们先用文本文档软件打开我们的 dlg 文件。

文件头部是使用的软件版本等信息，然后是程序运行的一些参数记录。

![1611985101445-b057b205-6ad7-408d-92be-69cb3ef7e913.png](./img/molecular-docking/1611985101445-b057b205-6ad7-408d-92be-69cb3ef7e913-207542.png)

我们接着往下拉。FINAL GENETIC ALGORITHM DOCKED STATE 往下是我们的对接结果，如果不是用 GENETIC ALGORITHM DOCKED，该出名称不一样，结果中，Run = 1 是第一次对接的结果。我们重点看 Estimated Free Energy of Binding 这个参数，但这里的 Run = 1 不代表结合能最低，只是运行的一个顺序，一次对接有 10 个结果。

![1611985235289-d2ac631c-2f23-443c-8177-196135111287.png](./img/molecular-docking/1611985235289-d2ac631c-2f23-443c-8177-196135111287-422820.png)

我们一直往下拉，在 CLUSTERING HISTOGRAM 处会看见一个表。这里把 10 个运行结果统计在这里表示，我们可以清楚的看到，第 6 次的运行结果的结合能才是最低的。

![1611985651345-03c8fe21-73bb-4b34-800c-c6120d40d85d.png](./img/molecular-docking/1611985651345-03c8fe21-73bb-4b34-800c-c6120d40d85d-994495.png)

接下来我们用 ADT 分析对接结果，先把当前窗口的所有分子删除。

![1611988092745-36ad48cb-59b3-4930-8556-cf4a12bfe26d.png](./img/molecular-docking/1611988092745-36ad48cb-59b3-4930-8556-cf4a12bfe26d-892057.png)

通过 Analyze-Dockings-Open 来打开分子对接的输出文件 1e8y.dlg。

![1611988400604-c525190f-0144-4982-9046-27820e3a11fd.png](./img/molecular-docking/1611988400604-c525190f-0144-4982-9046-27820e3a11fd-294030.png)

![1612005343007-405babd1-f66e-4503-8367-4cbd513ccc02.png](./img/molecular-docking/1612005343007-405babd1-f66e-4503-8367-4cbd513ccc02-126498.png)

然后就显示了结果，但我们不是有 10 个对接结果吗，这里只显示一个。

![1612005414832-b97e0a94-156b-4598-8865-0b068158b8d0.png](./img/molecular-docking/1612005414832-b97e0a94-156b-4598-8865-0b068158b8d0-017644.png)

![1612005498921-66fa8aa3-79e1-4da5-afc2-cb7dc3eb6a7c.png](./img/molecular-docking/1612005498921-66fa8aa3-79e1-4da5-afc2-cb7dc3eb6a7c-127650.png)

会弹出这么一个窗口

![1612005580141-7a3abac9-0434-4106-bbbd-c3e484fbe110.png](./img/molecular-docking/1612005580141-7a3abac9-0434-4106-bbbd-c3e484fbe110-050454.png)

然后按下图操作，显示对接信息。

![1612005840703-0db3c719-6f69-4efa-85ea-9601012b39d7.png](./img/molecular-docking/1612005840703-0db3c719-6f69-4efa-85ea-9601012b39d7-857964.png)

我们可以看到，当前结果的结合能是-5.36，在对接位置处产生了 4 个氢键，位置是第 1、567、594 和 1032 个氨基酸处。

![1612006027147-3f343e79-68b0-4489-80ec-951a7c8ff209.png](./img/molecular-docking/1612006027147-3f343e79-68b0-4489-80ec-951a7c8ff209-091194.png)

我们可以加载所有的信息出来，和前面文本文件打开的信息一样，不过我这里显示的结果和前面文档不一样，是因为我后面这次是重新运行的，每一次对接的结果是不一样的，所以这里会有所区别。

![1612006284103-9292b62d-07e3-4312-afcf-2812982b6c0d.png](./img/molecular-docking/1612006284103-9292b62d-07e3-4312-afcf-2812982b6c0d-433990.png)

我们可以通过左右按钮切换显示，切换后相应的信息就会改变。

![1612006428513-e982cdfc-9a2e-4c01-a695-a83ad9a7198f.png](./img/molecular-docking/1612006428513-e982cdfc-9a2e-4c01-a695-a83ad9a7198f-089290.png)

我们切换回第一个，写出复合物，弹出保存文件窗口，输出文件是 pdbqt 格式。

![1612006572101-b819068c-7de8-462b-8c3d-920f1c739f50.png](./img/molecular-docking/1612006572101-b819068c-7de8-462b-8c3d-920f1c739f50-629834.png)

我们这里命名为 result.pdbqt。后续可以转换为 pdb 格式，用如 pymol 等其他软件进行可视化美化。

**最后，我们的对接结果怎么才算可靠？** 上面一直说的结合能，其常用单位是 kcal/mol，而标准单位是 kJ/mol，1 kcal 等于 4.184 kJ。kJ/mol 是焓的单位：因为焓是一个状态函数，某物质所含的能量会随物质的量改变，物质的量的单位是 mol、能量的单位是 J，所以焓的单位就是 J/mol 或者 kJ/mol。如果结合能小于 -1.2 kcal/mol 或者小于 -5 kJ/mol，那么我们认为对接结果是可行的，可以选择最低的那个。

到这里，对接就算结束了，后面是结果的可视化美化，如果有报错的情况，你可以阅读官方手册。

<http://autodock.scripps.edu/faqs-help/tutorial/using-autodock-4-with-autodocktools>

![1611908495900-5018bb4f-80ec-46f4-ac1b-33c30373f2fc.png](./img/molecular-docking/1611908495900-5018bb4f-80ec-46f4-ac1b-33c30373f2fc-178680.png)

## 七、一些报错的处理

有些同学可能第一次做对接，由于蛋白或者的受体不同，中途可能会产生一些错误，导致后面无法进行，一直停留在原地，这里，我简单介绍一下，可能的出现的错误，但不一定覆盖到你所遇到的问题。

首先就是准备受体时加氢的问题，其实在前文已经有过介绍：在选择一个分子作为配体或受体之前，必须把所有的氢都加到这个分子上，而且要加全氢。如果你操作时用的是我选择的蛋白或者受体，前面可能你没有发现一个问题，那就是小分子配体——我们下载的 sdf 文件和 mol2 文件，其中的 sdf 文件是在 PubChem 数据库下载的，在 3D Conformer 处左侧有一些选项勾选，比如是否显示氢键，我当时是勾选的。

![1611841011209-bb9a7ddf-0318-4a77-a0ac-0ce0c6a0e510.png](./img/molecular-docking/1611841011209-bb9a7ddf-0318-4a77-a0ac-0ce0c6a0e510-573810.png)

如果我们的小分子已经带氢，再加氢是没有什么变化的。

![1612068301775-8b925130-b245-4690-811e-a1c56b65c9b3.png](./img/molecular-docking/1612068301775-8b925130-b245-4690-811e-a1c56b65c9b3-488173.png)

当然，这一步没有什么影响。

还有就是我们是否需要计算 Gasteiger 电荷，这在前面也有所提到。对于小分子配体，我们是不自己计算的，除非出错，这在前面有解释；但**对于蛋白配体，是否也需要计算 Gasteiger 电荷？** 这里是不需要的。我们在去水加氢后选为受体时，软件会自动添加，所以对于蛋白质来说，无论是否报错，都不能做计算 Gasteiger 电荷这一步操作，否则会改变真正的对接结果。

![1612068665712-b1c2f4ae-cbab-4d11-baa1-268778c191aa.png](./img/molecular-docking/1612068665712-b1c2f4ae-cbab-4d11-baa1-268778c191aa-366590.png)

但是对于蛋白受体来说，一般不会出错的，要出错的情况最可能的原因就是你蛋白受体含有特殊离子，而这些离子在 AutoDockTools 的离子参数配置文件中没有，所以会报错，这种怎么解决？？

我们首先先看一下离子参数的配制文件，如果你安装软件的时候没有改变安装路径的话，应该在`C:\Program Files (x86)\MGLTools-1.5.6\MGLToolsPckgs\AutoDockTools` 这个路径下。

![1612069133144-2434893b-44a1-4d45-9864-de899c95ebc8.png](./img/molecular-docking/1612069133144-2434893b-44a1-4d45-9864-de899c95ebc8-414886.png)

AD4_parameters.dat 这个文件就是离子参数配置文件，不懂的话先不要更改它，你复制一份出来，用文本软件打开，你会找到如下的内容。这些就是已有的离子参数，你看一下里面有没有你的金属离子，没有的话报错的原因就是这个。

![1612069290688-af1af925-65db-4567-a309-cc74202b5e83.png](./img/molecular-docking/1612069290688-af1af925-65db-4567-a309-cc74202b5e83-308607.png)

如 3PAU 这个蛋白，含有铜离子，而铜离子在我们默认的参数里面是没有的。

![1612069944232-6a08e403-560e-4111-81a6-b9c9a57bd682.png](./img/molecular-docking/1612069944232-6a08e403-560e-4111-81a6-b9c9a57bd682-438082.png)

我们下载这个蛋白用 ADT 打开。去水加氢。

![1612070125695-aab56a9f-e01c-409a-9b4b-ca8ad0412e7a.png](./img/molecular-docking/1612070125695-aab56a9f-e01c-409a-9b4b-ca8ad0412e7a-710825.png)

我们接着讲蛋白设置为受体，准备输出为 pdbqt 文件时，认真的会发现，和前面有所不同，会提示一些原子有 0 个电荷，这种提示在前面是没有出现的。

![1612070271839-dc47eeb9-34ef-4048-87e6-ee20202fca60.png](./img/molecular-docking/1612070271839-dc47eeb9-34ef-4048-87e6-ee20202fca60-985963.png)

我们按照前面的操作流程，导入受体分子 pdbqt 文件时，还是会有类似的提示。

![1612070652093-1c59a2e2-ea8b-4948-8c79-b081f20c9861.png](./img/molecular-docking/1612070652093-1c59a2e2-ea8b-4948-8c79-b081f20c9861-325459.png)

我们继续用前面的配体往下对接。再输出 gpf 文件的时候，然后 Grid 后，没有产生相应的 map 文件，而且会运行不会结束，反正我等了好久，就是不会结束。**那么我们怎么解决呢？**

首先，可以查看官方文档：

<http://autodock.scripps.edu/faqs-help/faq/how-do-i-add-new-atom-types-to-autodock-4>

![1612072621907-5e471967-d65e-4b4c-b94c-d2af7b10f0c0.png](./img/molecular-docking/1612072621907-5e471967-d65e-4b4c-b94c-d2af7b10f0c0-589660.png)

**还有就是 Google**，你可以在 <https://www.researchgate.net/> 搜索你可能遇到的问题。类似的问题有很多人会遇到的。下面就有一些类似的问题。

<https://www.researchgate.net/post/How-to-add-Cobalt-atomic-parameter-in-autodock-42>

![1612072439812-e10b2a60-b875-4e6e-8598-76b457958e4d.png](./img/molecular-docking/1612072439812-e10b2a60-b875-4e6e-8598-76b457958e4d-201273.png)

在上面的这个问题中，有一个回答，

![1612072532594-7e23c928-891f-42c5-ba31-ba03395f14db.png](./img/molecular-docking/1612072532594-7e23c928-891f-42c5-ba31-ba03395f14db-725338.png)

将需要的参数复制到 AD4_parameter.dat 文件中。(将值对齐到正确的行)

然后你需要把修改过的 bat 文件放到 autodock 和 autogrid exe 文件所在的文件夹中。

然后我们再通过修改.gpf 和.dpf 文件。再运行。

具体怎么操作，首先，复制 AD4_parameter.dat 这个文件到工作目录（F:\AutoDock），最好不要在原来的文件下面更改。

```r
atom_par C 4.00 0.150 33.5103 -0.00143 0.0 0.0 0 -1 -1 0 # Non H-bonding
atom_par A 4.00 0.150 33.5103 -0.00052 0.0 0.0 0 -1 -1 0 # Non H-bonding
atom_par N 3.50 0.160 22.4493 -0.00162 0.0 0.0 0 -1 -1 1 # Non H-bonding
atom_par NA 3.50 0.160 22.4493 -0.00162 1.9 5.0 4 -1 -1 1 # Acceptor 1 H-bond
atom_par NS 3.50 0.160 22.4493 -0.00162 1.9 5.0 3 -1 -1 1 # Acceptor S Spherical
atom_par OA 3.20 0.200 17.1573 -0.00251 1.9 5.0 3 -1 -1 2 # Acceptor 2 H-bonds
atom_par OS 3.20 0.200 17.1573 -0.00251 1.9 5.0 3 -1 -1 2 # Acceptor S Spherical
atom_par SA 4.00 0.200 33.5103 -0.00214 2.5 1.0 5 -1 -1 6 # Acceptor 2 H-bonds
atom_par S 4.00 0.200 33.5103 -0.00214 0.0 0.0 0 -1 -1 6 # Non H-bonding
atom_par H 2.00 0.020 0.0000 0.00051 0.0 0.0 0 -1 -1 3 # Non H-bonding
atom_par HD 2.00 0.020 0.0000 0.00051 0.0 0.0 2 -1 -1 3 # Donor 1 H-bond
atom_par HS 2.00 0.020 0.0000 0.00051 0.0 0.0 1 -1 -1 3 # Donor S Spherical
atom_par P 4.20 0.200 38.7924 -0.00110 0.0 0.0 0 -1 -1 5 # Non H-bonding
atom_par Br 4.33 0.389 42.5661 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par BR 4.33 0.389 42.5661 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ca 1.98 0.550 2.7700 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par CA 1.98 0.550 2.7700 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Cl 4.09 0.276 35.8235 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-binding
atom_par CL 4.09 0.276 35.8235 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-binding
atom_par F 3.09 0.080 15.4480 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-binding
atom_par Fe 1.30 0.010 1.8400 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par FE 1.30 0.010 1.8400 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par I 4.72 0.550 55.0585 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-binding
atom_par Mg 1.30 0.875 1.5600 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par MG 1.30 0.875 1.5600 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Mn 1.30 0.875 2.1400 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par MN 1.30 0.875 2.1400 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Zn 1.48 0.550 1.7000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par ZN 1.48 0.550 1.7000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par He 2.36 0.056 15.240 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Li 2.45 0.025 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Be 2.76 0.085 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par B 4.08 0.180 12.052 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ne 3.24 0.042 15.440 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Na 3.98 0.030 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Al 4.49 0.505 11.278 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Si 4.30 0.402 12.175 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par K 3.81 0.035 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Sc 3.30 0.019 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ti 3.18 0.017 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par V 3.14 0.016 12.000 -0.00110 0.0 0.0 0 -1 -1 1 # Non H-bonding
atom_par Co 2.87 0.014 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ni 2.83 0.015 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Cu 3.50 0.005 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ga 4.38 0.415 11.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ge 4.28 0.379 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par As 4.23 0.309 13.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Se 4.21 0.291 14.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Kr 4.14 0.220 16.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Rb 4.11 0.040 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Sr 3.64 0.235 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Y 3.35 0.072 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Zr 3.12 0.069 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Nb 3.17 0.059 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Mo 3.05 0.056 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Tc 3.00 0.048 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ru 2.96 0.056 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Rh 2.93 0.053 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pd 1.34 0.048 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ag 3.15 0.036 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Cd 2.85 0.228 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par In 4.46 0.599 11.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Sn 4.39 0.567 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Sb 4.42 0.449 13.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Te 4.47 0.398 14.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Xe 4.40 0.332 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Cs 4.52 0.045 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ba 3.70 0.364 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par La 3.52 0.017 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ce 3.56 0.013 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pr 3.61 0.010 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Nd 3.58 0.010 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pm 3.55 0.009 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Sm 3.52 0.008 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Eu 3.49 0.008 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Gd 3.37 0.009 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Tb 3.45 0.007 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Dy 3.43 0.007 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ho 3.41 0.007 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Er 3.39 0.007 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Tm 3.37 0.006 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Yb 3.36 0.228 12.000 -0.00110 0.0 0.0 0 -1 -1 1 4 # Non H-bonding
atom_par Lu 3.64 0.041 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Hf 3.41 0.072 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ta 3.71 0.081 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par W 3.07 0.067 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Re 2.95 0.066 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Os 3.12 0.120 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ir 2.84 0.073 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pt 2.75 0.080 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Au 3.29 0.039 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Hg 2.71 0.385 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Tl 4.35 0.680 11.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pb 4.30 0.663 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Bi 4.37 0.518 13.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Po 4.71 0.325 14.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par At 4.75 0.284 15.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Rn 4.77 0.248 16.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Fr 4.90 0.050 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ra 3.68 0.404 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Ac 3.48 0.033 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Th 3.40 0.026 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pa 3.42 0.022 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par U 3.40 0.022 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Np 3.42 0.019 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Pu 3.42 0.016 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Am 3.38 0.014 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Cm 3.33 0.014 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Bk 3.34 0.013 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Cf 3.31 0.013 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par E 3.30 0.012 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
atom_par Fm 3.29 0.012 12.000 -0.00110 0.0 0.0 0 -1 -1 4 # Non H-bonding
```

将上面的原子参数复制到 AD4_parameter.dat 文件中相应的位置。就是下图中红框的区域。然后保存。

![1612072978897-f671d35e-b372-41c7-aa4b-c1f0ec16a2e4.png](./img/molecular-docking/1612072978897-f671d35e-b372-41c7-aa4b-c1f0ec16a2e4-252848.png)

我们再生产 gpf 文件后，先不要往下运行，我们用文本软件打开 gpf 文件。

![1612073463390-61737cf1-abac-445b-9d59-7583525c7245.png](./img/molecular-docking/1612073463390-61737cf1-abac-445b-9d59-7583525c7245-406175.png)

我们在第一行回车后添加一行：`parameter_file AD4_parameters.dat`。其实就是指定参数文件

![1612073785209-d4794e09-fefe-4462-9809-b53e6671a6bc.png](./img/molecular-docking/1612073785209-d4794e09-fefe-4462-9809-b53e6671a6bc-630296.png)

然后我们在运行 Auto Grid，接种一直往下，生成 dpf 文件后，同样用文本软件打开 dpf 文件，在首行同样添加`parameter_file AD4_parameters.dat`，保存后再往下运行 AutoDock。

![1612074505361-5631bacc-495d-4600-b15d-d10cdf4265d0.png](./img/molecular-docking/1612074505361-5631bacc-495d-4600-b15d-d10cdf4265d0-719719.png)

这样就不会出错了。

上面这种处理方式，适合你能找到原子参数的情况下，假设你找不到你要的原子参数，上面这种方法就不可行。但这些原子几乎都够你用啦，放心吧。

还有一种方法是给金属离子添加形式电荷，我个人觉得有上面方法，就不需要这种，感觉人为添加，加几个？感觉不靠谱，但做法就是打开一开始准备的 pdbqt 文件。找你离子，你会发现电荷是 0，这也是为什么一开始处理会提示电荷为 0 的原因，这里你可以更改，就是人为的改变。后面就不会出错啦。

![1612074996261-1df86244-0685-48ed-9023-5931b7b51b58.png](./img/molecular-docking/1612074996261-1df86244-0685-48ed-9023-5931b7b51b58-798068.png)

好了，关于一下常见问题就介绍到这里，如果你还有错误，那么官方文档是最好的解决办法。

<http://autodock.scripps.edu/faqs-help>

这里会有各种问题的解决方法。**如果你的主要工作是做对接，那么你需要掌握的远不止这些**。

![1612075212535-a98c997a-8b3e-496c-9c39-bff467dfe497.png](./img/molecular-docking/1612075212535-a98c997a-8b3e-496c-9c39-bff467dfe497-719882.png)

## 八、PyMOL 可视化对接结果

在介绍之前，先简单介绍一下这个软件，虽然前面我们简单的使用，但没有过多介绍，这里就简单介绍一下，具体细节上的东西，需要你不断取用，才能熟悉。下面是软件界面。

![1612062641169-62e3b5d9-0a47-4485-bb0a-2d403f85743c.png](./img/molecular-docking/1612062641169-62e3b5d9-0a47-4485-bb0a-2d403f85743c-711635.png)

### 1. 设定工作目录，打开文件

打开 PyMOL 软件，设置我们的工作目录。

![1612061513517-c739256a-3ffe-4b95-93a4-c08ef1fbb259.png](./img/molecular-docking/1612061513517-c739256a-3ffe-4b95-93a4-c08ef1fbb259-325449.png)

或者通过命令`cd F:\AutoDock`来实现，这与 Windows 的 DOS 命令行和 Linux 系统的 cd(Change Directory)命令一样。

![1612062377228-2e8519a1-af18-4fec-8c4a-b6b575740adc.png](./img/molecular-docking/1612062377228-2e8519a1-af18-4fec-8c4a-b6b575740adc-294279.png)

导入刚才下载的复合物 PDB 文件（1e8y.pdb）。

**注意**：有两种方法导入文件，一种是鼠标点击菜单栏 File -> Open…，另一种是通过命令行。通过`load`命令加载：`load 1e8y.pdb`，因为这样可以同时把工作目录设置好，方便后续保存文件。

假设我们的工作目录为`F:\AutoDock`。注意：路径中不要有中文和空格，这是导致很多计算类软件（尤其是免费软件）出现问题的原因。

如果是从 PDB 网站上下载蛋白，如 1e8y.pdb, 也可以直接通过 PyMOL 下载蛋白，点击菜单栏中的 File->Get PDB，或者通过 fetch 命令下载，这在前面有介绍。

### 2. 对象属性操作介绍

加载到蛋白后。

![1612062941485-5e2eaa76-7867-4d20-a78b-c09f8e512be0.png](./img/molecular-docking/1612062941485-5e2eaa76-7867-4d20-a78b-c09f8e512be0-591007.png)

* 1 个是 all, all 不是真实的 object，它代表了所有的 object
* 1 个是 1e8y ，1e8y 就是我们刚刚载入的蛋白

每个 object 都有对应的 A S H L C 操作：

A：代表 Action ，主要包含了对 object 的常用操作的集合，如 复制、删除 object，对 object 加氢，展示 Object 等，

S：代表 Show ，将 object 渲染成 cartoon 、line、stick lines sphere surface mesh dots ribbon 等模式

H：Hide 根据 object 的状态或者描述进行相应的掩藏

L：Label 显示 object 中残基、原子等名称或者属性

C：Color 对 Object 进行着色

知道这些含有，里面的内容多试试几次就知道怎么回事啦。比如下面 2 种操作。

* 点击 A->preset->simple 显示蛋白的简单形式

![1612063409303-229e0df4-0ccf-4bdf-b5ec-e6a9b8338b36.png](./img/molecular-docking/1612063409303-229e0df4-0ccf-4bdf-b5ec-e6a9b8338b36-917272.png)

* 点击 A->preset->ball and stick 显示球棍模型

![1612063467705-19c1ca05-c5e8-430f-80e0-e27233b321d3.png](./img/molecular-docking/1612063467705-19c1ca05-c5e8-430f-80e0-e27233b321d3-970496.png)

再如下面的一些操作介绍；

L->residue 在α碳原子上标记其残基名字和编号 （常用）

L->residue name 在所有原子上标记残基名字 （不常用）

L->clear 删除该对象上所有的 Label

L->element symbol 显示对象上所有原子的元素名字

L->vdw radius 产看原子的范德华半径

### 3. 可视化窗口操作

* 平移，按住鼠标中键不放，然后上下左右移动，进行体会，蛋白会随着鼠标而移动
* 旋转，按住鼠标左键不放，然后上下左右移动鼠标，蛋白会进行旋转
* 缩放，按住鼠标右键不放，然后上下移动，蛋白会进行缩放
* 切割 滚动鼠标中键， 建议将蛋白渲染成 surface 模式，然后滚动鼠标中键

多的不介绍了，B 站有很多视频教程，这里我给大家找到了一个文本教程。<http://pymol.chenzhaoqiang.com/> ，对作者的贡献表示感谢。

下面我们就简单处理一下前面对接的结果。

### 4. 对接结果简单处理演示

我们前面对接的结果文件，result.pdbqt，我们同样用 OpenBabel 这个软件转换成 pdb 格式。

![1612009645505-528f9c24-41ce-4714-9a8c-867a78a832e3.png](./img/molecular-docking/1612009645505-528f9c24-41ce-4714-9a8c-867a78a832e3-248707.png)

我们用 pymol 打开 result.pdb 文件，在右下角处 Selecting 处点击切换到 Chains，然后选种蛋白质，在左上角 sele 处选择 A，然后选择 rename selection，然后在左上角的窗口处会弹出一行，在：后面输入名称。我这里是 protein。或者通过命令 set_name sele,protein 实现。

![1612009978089-2757ff09-b512-4d70-bf0a-488d3f27b4d1.png](./img/molecular-docking/1612009978089-2757ff09-b512-4d70-bf0a-488d3f27b4d1-103013.png)

我下面通过命令`set_name protein,p`又将 protein 改为 p。

![1612010461093-141ba7e4-8b97-4677-8ee3-a13e676f80a6.png](./img/molecular-docking/1612010461093-141ba7e4-8b97-4677-8ee3-a13e676f80a6-648951.png)

为了更好的区分受体和配体，我们通过 C(color）来更改，根据自己喜好。

![1612010612522-78c21c8e-17ce-48cb-9649-ce1e9050a2bb.png](./img/molecular-docking/1612010612522-78c21c8e-17ce-48cb-9649-ce1e9050a2bb-437886.png)

Selecting 处切换到残基。

![1612012224507-b9862498-5ee6-492c-b017-25e474c33f09.png](./img/molecular-docking/1612012224507-b9862498-5ee6-492c-b017-25e474c33f09-421607.png)

然后选择小分子，右侧又多了一个 sele，我们同样可以更改名字。

![1612010749203-39802f14-d2ed-4132-a487-ed804023ff37.png](./img/molecular-docking/1612010749203-39802f14-d2ed-4132-a487-ed804023ff37-213137.png)

我这里把名称改成了 ligand，我们选中小分子，按下图选择，让小分子显示氢键。

![1612011230897-146f240f-db9d-4ddc-b155-2dad3e7d751a.png](./img/molecular-docking/1612011230897-146f240f-db9d-4ddc-b155-2dad3e7d751a-382842.png)

我们鼠标旋转，可以看见 4 个氢键。

![1612011337134-68ec7454-7c79-4f81-9f8f-a7a0f602d25d.png](./img/molecular-docking/1612011337134-68ec7454-7c79-4f81-9f8f-a7a0f602d25d-590945.png)

接下来我们显示这 4 个氢键对接在氨基酸上的那几个残基上。首先，点击蛋白质（p）的 S，点击 sticks。

![1612011495950-97e18e47-1996-483d-ac80-5df467d56f1d.png](./img/molecular-docking/1612011495950-97e18e47-1996-483d-ac80-5df467d56f1d-469523.png)

然后点击 ligand 的 A，点击 center，将配体小分子设置为中心。后面可以通过鼠标放大缩小旋转都以它为中心。

![1612011796225-1ed342d4-1cf2-449c-9d40-e1eb8340a81f.png](./img/molecular-docking/1612011796225-1ed342d4-1cf2-449c-9d40-e1eb8340a81f-829119.png)

然后我们放大(长按鼠标右键拖动），旋转到合适角度，可以看见。

![1612012376988-358b3b74-245d-4830-8a20-3e6ebca2ca8d.png](./img/molecular-docking/1612012376988-358b3b74-245d-4830-8a20-3e6ebca2ca8d-292812.png)

然后鼠标选中对接的残基

![1612012652536-222e18d8-0cbd-4467-aa55-f8b89ccca7c8.png](./img/molecular-docking/1612012652536-222e18d8-0cbd-4467-aa55-f8b89ccca7c8-178080.png)

同样将残基改一个名字，我这里是 rr。

在 p 中的 H 点击 sticks，将蛋白的棍状结构隐藏起来。

![1612012801170-28f75343-3b34-4941-89b2-2b6d0abce408.png](./img/molecular-docking/1612012801170-28f75343-3b34-4941-89b2-2b6d0abce408-520597.png)

然后是在 rr 中选择 S 里面的 sticks，单独显示残基的棍状结构。

![1612012926764-bff630f7-76bb-4589-a03c-d4ba773190f7.png](./img/molecular-docking/1612012926764-bff630f7-76bb-4589-a03c-d4ba773190f7-777673.png)

我们可以给残基换一个颜色（C）。

![1612013077114-96cd44e8-0677-49e9-8099-d3045560b2f5.png](./img/molecular-docking/1612013077114-96cd44e8-0677-49e9-8099-d3045560b2f5-125476.png)

改变背景色，这里改为白色，同时我再把残基改成了蓝色。

![1612013558231-df2c29c0-2850-4cb3-9a59-0700c61c4abc.png](./img/molecular-docking/1612013558231-df2c29c0-2850-4cb3-9a59-0700c61c4abc-524132.png)

可以保存文件编辑好的图片。

![1612013748418-86406c98-1686-4eaf-9652-ab32e4bed496.png](./img/molecular-docking/1612013748418-86406c98-1686-4eaf-9652-ab32e4bed496-008339.png)

## 九、蛋白三级结构可视化软件 VMD

这一部分来自多年前我在学习山东大学在 MOOC 网上的生物信息学课程的笔记，对此表示感谢。

能够实现蛋白质三维结构可视化的软件非常多。比专业级的 PyMOL（<https://pymol.org/2/>）。这个软件已经被世界上著名的生物医药软件公司“薛定谔公司（Schrödinger）”收购。这种专业级的可视化软件不仅能够做出非常漂亮的图片，它还有强大的插件支持各种各样的蛋白质结构分析，这款软件需要购买，如果你发表的文章里提到某些内容是使用 PyMOL 制作的，而文章中所有作者和作者单位都没有 PyMOL 的购买记录的话，你可能会面临薛定谔公司的追责。

下面给大家介绍一个功能同样强大的免费蛋白质三维结构可视化软件，VMD（<http://www.ks.uiuc.edu/Research/vmd>）。VMD 由伊利诺伊大学研发。下载 VMD 需要先注册获得一个账户，之后就可以根据你的操作系统和机器配置选择合适的版本下载了。当然，如前所述，注册和下载对于非商业用途的用户都是免费的。VMD 的安装也极其简单。不需要预装任何语言环境，完全图形化安装过程，绝对可以轻松搞定。

对于 Windows 用户，VMD 默认安装在 C :\Program Files(x86)\University of Illinois\VMD 文件夹下。打开 VMD。VMD 打开后，会弹出三个窗口：VMD Main（主窗口），VMD Display（显示窗口），和命令窗口。

![1604969312088-add16c19-b4bd-4c2c-8874-2cebf8527366.png](./img/molecular-docking/1604969312088-add16c19-b4bd-4c2c-8874-2cebf8527366-055871.png)

图 4.14 VMD 主窗口、显示窗口和命令窗口

打开一个蛋白质结构（图 4.15）：主窗口中点 File\New Molecule，弹出新窗口 Molecule File Browser（文件读取窗口），文件读取窗口中点 Browse，自动打开 VMD 安装目录，进入 proteins 文件夹，选择 VMD 自带的演示结构 bpti.pdb，文件读取窗口中点 Load，显示窗口出现蛋白质结构。

![1604969312294-9aaebee4-1506-4697-8eaf-b7993fc33657.png](./img/molecular-docking/1604969312294-9aaebee4-1506-4697-8eaf-b7993fc33657-117611.png)

图 4.15 打开一个蛋白质结构

默认的蛋白质结构显示方案（图 4.16）：把显示窗口拖大后可以看到，VMD 读取了 PDB 文件中的原子坐标，把每一个原子以细线的形式展示在 3D 空间中。不同的原子应的细线颜色不同。碳原子是青色的，氮原子是蓝色的，氧原子是红色的，氢原子是白色的，还有少量黄色的硫原子。

![1604969312435-739aa4a7-867e-48d9-91a0-b1809b6a3f32.png](./img/molecular-docking/1604969312435-739aa4a7-867e-48d9-91a0-b1809b6a3f32-375392.png)

图 4.16 默认的蛋白质结构显示方案

##### 1、VMD 中鼠标的使用

把鼠标移到显示窗口里，按住左键，随意拖动，蛋白质就会在 3D 空间内任意旋转；按住鼠标右键拖动，蛋白质会在当前平面内 360 度旋转；前后滚动鼠标中键，可以将蛋白质放大或缩小。此外，鼠标还有更多的使用方法：主窗口上的 Mouse 菜单里可以切换鼠标模式。默认的鼠标模式是 Rotate Mode（旋转模式，R）。R 模式下，鼠标在显示窗口内为单箭头。操作即为上述三种。将鼠标模式改为 Translate Mode（移动模式，T）后，鼠标在显示窗口内变为十字箭头。T 模式下，按住鼠标左键拖动为移动结构；右键和中键都为放缩功能。此外，还有 Scale Mode（缩放模式，S）。S 模式下，鼠标在显示窗口内变为左右箭头，按住鼠标左键或右键后，左右移动，即可完成连续的缩放。这种连续的缩放，不同于滚动中键实现的缩放。在默认的情况下，所有旋转是围绕整个结构的中心点进行的。我们也可以自己指定旋转的中心。这需要把鼠标模式切换为 Center（中心模式，C）。C 模式下，鼠标在显示窗口内为十字。将十字放在想要作为旋转中心的原子上点一下，再按住鼠标左键旋转，就会以新定义的中心进行旋转。

##### 2、恢复结构初始位置

主窗口中点 Display → Reset View。或者在显示窗口内单击鼠标左键以激活窗口后，点击“=”键。

##### 3、改变蛋白质结构的外观

有关外观的设置在主窗口中的 Graphic 菜单下的 Representation 窗口里（图 4.17）。一个 Representation（显示状态）由三个元素构成。第一个元素是用什么样式（Style）显示，当前使用的样式是以细线显示原子（Lines）。第二个元素是用什么颜色（Color）显示，当前使用的颜色是按原子名定义的不同颜色（Name）。最后一个元素是要显示什么内容（Selection），当前显示的内容是所有原子（all）。这三个元素分别在 Representation 窗口里的 Draw style 标签下的 Drawing Method 下拉条、Coloring Method 下拉条和 Selected Atoms 输入框里进行设置。

![1604969312891-611e9f53-f189-41f3-b6bf-ef2c4679ce29.png](./img/molecular-docking/1604969312891-611e9f53-f189-41f3-b6bf-ef2c4679ce29-417286.png)

图 4.17 Representation 窗口

##### 4、Drawing Method 下拉条（图 4.18）

Lines 以细线显示原子。CPK 以不同大小的球来显示原子，原子间的连线是相应的化学键，比如碳与碳之间的共价键，硫与硫之间的二硫键等。NewCartoon 只显示蛋白质的碳骨架（backbone），并形象地展示出不同的二级结构。每一种 Drawing Method 都可以再进一步设置显示效果。比如对于 CPK，可以调整原子球的大小（Sphere Scale）、改变化学键的粗细（Bond Radius）、以及设置更高或更低的分辨率（Sphere/Bond Resolution）。

![1604969313037-1a5426e2-1586-4eb1-9508-ae3b10b601c3.png](./img/molecular-docking/1604969313037-1a5426e2-1586-4eb1-9508-ae3b10b601c3-393527.png)

4.18 不同的几种 Drawing Method

##### 5、Coloring Method 下拉条（图 4.19）

Name 颜色方案是一种原子一种颜色，常见的比如碳原子青色、氧原子红色、氮原子蓝色、硫原子黄色。在 NewCartoon 显示样式下，只有碳骨架被显示出来，再配以 Name 颜色方案，整个结构都是青色的。Secondary Structure 颜色方案可以为不同的二级结构赋予不同的颜色，常见的比如α螺旋紫色、β折片黄色、转角青色、松散 coil 结构白色。颜色方案 Res Type 根据氨基酸类型的不同赋予不同的颜色，比如非极性氨基酸白色、极性带正电荷的氨基酸（碱性的氨基酸）蓝色、极性带负电荷的氨基酸（酸性的氨基酸）红色、极性不带电荷的氨基酸绿色。这种颜色方案适合在显示氨基酸侧链的 Drawing Method 下观看，比如 CPK 样式。颜色方案 ResName 为 20 种氨基酸设置了 20 种不同的颜色。

![1604969313314-c266f453-0ca0-416f-9fca-79cb26dc1cb1.png](./img/molecular-docking/1604969313314-c266f453-0ca0-416f-9fca-79cb26dc1cb1-340940.png)

4.19 不同 Drawing Method 和 Coloring Method 组合

##### 6、Selected Atoms 输入框

输入框里输入需要显示的内容，比如，写“all”代表显示所有原子，也就是整个蛋白质、写“backbone”代表显示碳骨架。输入框里允许输入的关键词和语法在 Selections 标签下有详细定义。可以写 Singlewords 里面单个的单词，也可以写 Keyword 和 Value 组成的词组，还可以利用逻辑词“and/or/not”把多个单词和词组串成句子。举例：

（1）点击 Reset 清空输入框里的内容→Keyword 里双击 ResName→Value 里双击 ALA（输入框里出现“ResName ALA”） →点击 Apply。显示名字为 Alanine 的氨基酸上的原子，即显示所有丙氨酸。配合 Drawing Method 设置为 CPK，Coloring Method 设置为 ResName。

（2）点击 Reset 清空输入框里的内容→Keyword 里双击 Resid→Value 里双击 1→点击 Apply。显示第一个氨基酸。利用这个 Keyword 和 Value 组合可以根据残基的编号选择某个或某一段氨基酸，比如，想要显示第 1 到第 10 个氨基酸，可以直接在输入框里输入“resid 1 to 10”，回车。此时显示的就是前 10 个氨基酸。

（3）Draw style 标签下，Drawing Method 设置为 NewCartoon，Coloring Method 设置为 Secondary Structure→Selections 标签下，点击 Reset 清空输入框里的内容→Singlewords 里面双击 alpha_helix→点击“or” → Singlewords 里面双击 beta_sheet（输入框里出现“alpha_helix or beta_sheet”） →点击 Apply。通过逻辑词显示出所有的α helix 和β sheet。

VMD 可以设置多个 representations（简称 rep），也就是将多个显示状态的显示效果叠加在一起（图 4.20）。

##### 7、representations（简称 rep）

设置第一个 rep：当前处于编辑状态下的 rep 背景色为浅绿色。设置 Drawing Method 为 NewCartoon，Coloring Method 为 Secondary Structure，Selected Atoms 为“all”，回车（或点击右下角 Apply 按钮）。创建第二个 rep：点击 Create Rep。点击后，复制产生了和第一个一模一样的第二个 rep。浅绿色背景自动跳转到第二个 rep，即目前第二个 rep 处于可编辑状态。设置 Drawing Method 为 cpk，Coloring Method 为 colorid，并选择“1 red”（红色），Selected Atoms 为“resname PRO”，回车（或点击右下角 Apply 按钮）。设置两个 representations 后，蛋白质中的所有脯氨酸就以红色的原子球的形式叠加显示在以二级结构着色的碳骨架上了。

![1604969313470-df6f82ee-0e5f-4817-9eb8-76804acd8cf7.png](./img/molecular-docking/1604969313470-df6f82ee-0e5f-4817-9eb8-76804acd8cf7-656555.png)

图 4.20 设置两个 representations

创建第三个 rep：点击 Create Rep。设置 Drawing Method 为 Surface，Coloring Method 为 colorid，并选择“8 white”（白色），Selected Atoms 为“all”，回车（或点击右下角 Apply 按钮）。此时，可以看到填满肉的蛋白质，也就是蛋白质的外表面。继续设置 Coloring Method 右侧的 Material（材质）为 Transparent（透明材质）。如果显卡支持，可以打开 GLSL 显示模式：主窗口中点 Display → Render Mode，选中 GLSL。GLSL 打开后的 Transparent Surface 变得更加柔美了（图 4.21）。

![1604969313659-c0bb66c3-3f90-455b-bcb3-8a5afb47b05e.png](./img/molecular-docking/1604969313659-c0bb66c3-3f90-455b-bcb3-8a5afb47b05e-744365.png)

图 4.21 设置三个 representations 及 GLSL 显示模式

如果要删除某一个 rep，比如删除第二个 rep，需要先选中它（选中后背景色变为浅绿色），再点击 Delete Rep，就删掉了。或者你可以双击某一个 rep，比如双击第三个 rep，将其暂时隐藏，等需要的时候再双击它取消隐藏（图 4.22）。

![1604969314050-15715d93-2c45-4743-981c-fdbadd15d7b1.png](./img/molecular-docking/1604969314050-15715d93-2c45-4743-981c-fdbadd15d7b1-042208.png)

图 4.22 删除和隐藏 representation

##### 8、保存与打开

当把蛋白质结构的显示效果调整到比较满意的状态后，可以保存当前所有的 representations（注意保存的是显示状态，而不是结构）：主窗口中点击 File→Save Visualization State→保存在桌面上，起名叫 mystate.vmd。接下来关闭 VMD 再重新打开。这次我们不需要 Load 蛋白质结构，分别设置三个 rep，我们只需要直接载入刚刚保存的 mystate.vmd ， 即可恢复刚刚的显示状态：主窗口中点击 File → Load Visualization State→找到并打开 mystate.vmd。这时，之前保存的显示状态就自动显示出来了（图 4.23）。

![1604969314214-1ce023a8-ee88-4235-8df2-7cf426b2f85c.png](./img/molecular-docking/1604969314214-1ce023a8-ee88-4235-8df2-7cf426b2f85c-145247.png)

图 4.23 保存和载入显示状态

##### 9、调换背景颜色（图 4.24）

主窗口中点击 Graphics→Colors→弹出 Color Controls 颜色控制窗口→Categories 选 Display→Names 选 Background→Colors 选 8 white。

![1604969314596-572126d2-cf9d-4971-8dcf-c1a130143d28.png](./img/molecular-docking/1604969314596-572126d2-cf9d-4971-8dcf-c1a130143d28-941132.png)

图 4.24 Color Controls 窗口调换颜色方案

Color Controls 窗口里可以调整各种 VMD 默认的颜色方案。比如 Coloring Method 选 Name 的时候，默认的颜色方案是：氢原子白色，氧原子红色，碳原子青色等。这里，你可以根据需要把它们设置成其他颜色。

##### 10、隐藏坐标轴

主窗口中点击 Display→Axes→off。

##### 11、显示 Label

有时我们需要标记出某些氨基酸的序号或原子的名称（图 4.25）。主窗口中点击 Mouse→Label→Atom。把鼠标模式设置为 Label 模式，让它标记原子。此时，鼠标变为十字。接下来在显示窗口中，要标记哪个原子就在哪里点一下。点击后出现文本显示的氨基酸名字、氨基酸序号以及被点击的原子的名字。

![1604969314768-1c451f10-76ba-41ae-8422-dacea8649172.png](./img/molecular-docking/1604969314768-1c451f10-76ba-41ae-8422-dacea8649172-460779.png)

图 4.25 显示 Label

##### 12、调整 Label

1）改变字体颜色（图 4.26）：主窗口中点击 Graphics→Colors→弹出 Color Controls 颜色控制窗口→Categories 选 Label→Names 选 Atoms→Colors 选 16 black。

![1604969315105-9c16c70a-1ae8-4300-89c1-ec58bb1e77c0.png](./img/molecular-docking/1604969315105-9c16c70a-1ae8-4300-89c1-ec58bb1e77c0-573730.png)

图 4.26 Color Controls 窗口改变 Label 字体颜色

2）改变字体大小/粗细（图 4.27）：主窗口中点击 Graphics→Labels→弹出 Label 窗口→Global Properties 标签下设置 Text Size 改变字体大小，Thickness 改变粗细。

3）改变显示位置和内容（图 4.28）：主窗口中点击 Graphics→Labels→弹出 Label 窗口→Properties 标签下，选中要调整的 Label→按住鼠标左键在 Offset 坐标系内移动来改变 Label 的位置，再写入 Format 来改变 Label 的内容。默认 Format 为：%R（氨基酸名字）%d（氨基酸序号）:%a（原子名字）。比如，只想显示氨基酸名字和编号，删掉“:%a”这部分代表原子信息的代码即可。

![1604969315279-1be91064-a69b-40ab-95af-c361941e420f.png](./img/molecular-docking/1604969315279-1be91064-a69b-40ab-95af-c361941e420f-319041.png)

图 4.27 Label 窗口改变 Label 字体大小/粗细

![1604969315666-ee2aa9b8-d06e-4453-b796-b9afd5c3d389.png](./img/molecular-docking/1604969315666-ee2aa9b8-d06e-4453-b796-b9afd5c3d389-734780.png)

图 4.28 Label 窗口改变 Label 位置和内容

##### 13、保存结构图

以刚刚 bpti.pdb 这个蛋白质结构文件为例，设置了三个 representations，添加并调整了 Label，得到了最终的蛋白质 3D 结构（图 4.29）。最后要做的就是保存结构图片。屏幕截图是较为方便快捷的方法，但是所得图片分辨率不高。如果想要高质量的图片，可以用主窗口下的 File → Render，弹出 File Render Controls 窗口。File Render Controls 窗口里可以选择多种图片导出方式。

![1604969316147-50e3d28c-0632-442f-99f1-7c15ee93d674.png](./img/molecular-docking/1604969316147-50e3d28c-0632-442f-99f1-7c15ee93d674-086415.png)

图 4.29 bpti.pdb 的最终结构图片

<https://novopro.cn/tools/molstar.html>

> 更新: 2021-01-31 18:46:13
> 原文: <https://www.yuque.com/doublehelix/bioinfonotes/xz134k>
