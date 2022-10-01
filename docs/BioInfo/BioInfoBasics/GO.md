## **1.GO怎么就出现了？**
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612928292771-05baccb1-4063-443e-9c7e-84b821631c79.png#crop=0&crop=0&crop=1&crop=1&height=536&id=PPIgg&originHeight=536&originWidth=692&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=692)
现今的生物学家们浪费了太多的时间和精力在搜寻生物信息上。这种情况归结为生物学上定义混乱的原因：不光是精确的计算机难以搜寻到这些随时间和人为多重因 素而随机改变的定义，即使是完全由人手动处理也无法完成。举个例子来说，如果需要找到一个用于制抗生素的药物靶点，你可能想找到所有的和细菌蛋白质合成相 关的基因产物，特别是那些和人中蛋白质合成组分显著不同的。但如果一个数据库描述这些基因产物为“翻译类”，而另一个描述其为“蛋白质合成类”，那么这无 疑对于计算机来说是难以区分这两个在字面上相差甚远却在功能上相一致的定义。Gene Ontology (GO)项目正是为了能够使对各种数据库中基因产物功能描述相一致的努力结果。这个项目最初是由1988年对三个模式生物数据库的整合开始：: FlyBase (果蝇数据库Drosophila),t Saccharomyces Genome Database (酵母基因组数据库SGD) and the Mouse Genome Database (小鼠基因组数据库MGD)。从那开始，GO不断发展扩大，现在已包含数十个动物、植物、微生物的数据库。GO的定义法则已经在多个合作的数据库中使用，这使在这些数据库中的查询具有极高的一致性。这种定义语言具有多重结构，因此在各种程度上都能进行查询。举 例来说，GO可以被用来在小鼠基因组中查询和信号转导相关的基因产物，也可以进一步找到各种生物地受体酪氨酸激酶。这种结构允许在各种水平添加对此基因产 物特性的认识。
## **2.GO的发展和组织形式**

GO发展了具有三级结构的标准语言（ontologies），根据基因产物的相关分子功能，生物学途径，细胞学组件而给予定义，无物种相关性。三种本体论的内容如下：
1）分子功能本体论 基因产物个体的功能，如与碳水化合物结合或ATP水解酶活性等2）生物学途径本体论 分子功能的有序组合，达成更广的生物功能，如有丝分裂或嘌呤代谢等3）细胞组件本体论 亚细胞结构、位置和大分子复合物，如核仁、端粒和识别起始的复合物等
基本来说，GO工作可分为三个不同的部分：第一，给予和维持定义；第二，将位于不同数据库中的本体论语言、基因和基因产物进行联系，形成网络；第三，发展相关工具，使本体论的标准语言的产生和维持更为便捷。
## **3.GO的形式**

![](https://cdn.nlark.com/yuque/0/2021/gif/1234840/1612928258821-e9e653c0-3bae-4477-bb82-4dce73d29774.gif#crop=0&crop=0&crop=1&crop=1&height=118&id=cuTCk&originHeight=118&originWidth=540&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=540)
GO 定义的术语有着直接非循环式（directed acyclic graphs (DAGs)的特点，而并非是传统的等级制定义方式（随着代数增加，下一级比上一级更为具体）。举个例子来说，生物学途径中有一个定义是己糖合成，它的上 一级为己糖代谢和单糖合成。当某个基因被注解为“己糖合成活性”后，它自动地获得了己糖代谢和单糖合成地注解。因为在GO中，每个术语必须遵循“真途径 “法则，即如果下一代的术语可以用于描述此基因产物，其上一代术语也可以适用。
## **4.GO的注释（Annotation）**

![](https://cdn.nlark.com/yuque/0/2021/webp/1234840/1612928258854-90a90e5e-401e-450d-95b2-bba26f46d9a8.webp#crop=0&crop=0&crop=1&crop=1&height=300&id=K1Q9B&originHeight=300&originWidth=450&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=450)那么，GO中的术语如何和相对应的基因产物相联系的呢？这是由参与合作的数据库来完成的，它们使用GO的定义方法，对它们所包含的基因产物进行注解，并且 提供支持这种注解的参考和证据。每个基因或基因产物都会有一个列表，列出与之相关的GO术语。每个数据库都会给出这些基因产物和GO术语的联系数据库，并 且也可以在GO的ftp站点上和WEB方式查询到。而且，GO联合会提供了简化的本体论术语（GO slim），这样，可以在更高级的层面上研究基因组的功能。比如，粗略地估计哪一部分的基因组与信号传导、代谢合成或复制有关。GO对基因和蛋白的注释阐明了基因产物和用于定义他们的GO术语之间的关系。基因产物指一个基因编码的RNA或蛋白产物。因为一个基因可能编码多个具有很不相同性质的产物，所以GO推荐的注释是针对基因产物的而不是基因的。一个基因是和所有适用于它的术语联系在一起的。一个基因产物可以被一种本体论定义的多种分支或多种水平注释。注释需要反映在正常情况下此基因产物的功能，生物途径，定位等，而并不包括其在突变或病理状 态下的情况。GO联合会的各个数据库成员采用手动或自动的方式生成注释，这两种方式共有的原理是：一.所有的注释都需要有来源,可以是文字、另一个数据库 或是计算机分析结果；二.注释必须提供支持这种基因产物和GO术语之间联系的证据。
## **5.GO文件格式**
![](https://cdn.nlark.com/yuque/0/2021/gif/1234840/1612928258865-09993e0d-1f05-4dad-bf2d-dac18463f17b.gif#crop=0&crop=0&crop=1&crop=1&height=446&id=dECro&originHeight=446&originWidth=502&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=502)
GO的所有数据都是免费获得的。GO数据有三种格式：flat（每日更新）、XML(每月更新)和MySQL（每月更新）。这些数据格式都可以在GO ftp的站点上下载。XML 和 MySQL 文件是被储存于独立的GO数据库中。如果需要找到与某一个GO术语相关的基因或基因产物，可以找到一个相应表格，搜寻到这种注解的编号，并且可以链接到与之对应的位于不同数据库的基因相关文件。
## **6.GO浏览器和修改器（browser and editor）**

GO 术语和注释使用了多种不同的工具软件，它们都可以在web方式的“GO 浏览器”下“GO software page”中找到。大多数GO浏览器都是web模式的，允许你直观的看到术语和其相关信息，如定义、同义词和数据库参考等。有些GO浏览器如AmiGO和 QuickGO,可以看到每个术语的注释。而可下载的DAG-Edit编辑器，一样可以离线地显示注释和所有本体论定义的信息。对于每一个浏览器来说，都可以选择最适用于你要求的工具软件。
**1）常见的三种浏览器**
AmiGO from BDGP 在 **AmiGO**中，可以通过查询一个GO术语而得到所有具有这个注释的基因产物，或查询一个基因产物而得到它所有的注释关系。还可以浏览本体论，得到术语之间的关系和术语对应的基因产物数目。AmiGO直接连接GO下的MySQL。MGI GO Browser **MGI GO**的功能类似于AmiGO,所不同的在于它所得到的基因为小鼠基因。MGI GO浏览器直接连接GO下的MGI数据库。**QuickGO** at EBI QuickGO,整合在EBI下的InterPro中，可以通过查询一个GO术语而得到它的定义与关系描述、在SWISS-PROT中的定位、在酶分类学（EC）和转运分类学（TC）中的定位和InterPro中的定位等。
其他还有一些特殊的浏览GO的浏览器，其中括号中为建立机构和主要特色：EP GO Browser（EBI,基因表达情况）,、GoFish (Harvard，Boolean查询、GenNav（NLM, 图像化展示）、GeneOntology@RZPD （RZPD，UniGene）、ProToGO （Hebrew University，GO的亚图像化）、CGAP GO Browser （癌症基因组解剖工程，癌症）、GOBrowser （Illuminae，perl.、TAIR Keyword Browser （TAIR，拟南芥）、PANDORA （Hebrew University，非一致化蛋白）。
**2）修改器**
GO 术语和本体论结构可以由任何可以读入GO平板文件的文本修改器进行编辑，但是这需要对平板文件非常熟悉。因此，**DAG-Edit**是被推荐使用的，它是为 GO特别设计的，能够保证文件的句法正确。GO注释可以被多种数据库特异性的工具所编辑，如TIGR的Manatee和EBI的Talisman tool。但是GO数据库中写入新的注释是需要通过GO认证的管理员方可进行的，如果想提出新的注释或对本体论的建议，可以联系GO。
主要修改器为DAG-Edit和COBrA。DAG-Edit基于Java语言，提供了能浏览、查询、编辑具有DAG数据格式的GO数据界面。在 SourceForge可以免费下载，伴随着帮助文件。COBrA能够编辑和定位GO和OBO本体论。它一次显示两个本体论，因此可以在不同的水平相应定位。（如组织和细胞类型水平）优点在于可以综合几种本体论，支持的文件格式多，包括GO平板文件、GO RDF和OWL格式等。
如图为DAG-Edit的界面，可以分为四个部分：
> **1） 定义编辑面板（term editor panel）**显示当下的本体论。也是主要的编辑本体论结构的工具，可以通过点击和拖动术语来修改本体论的从属关系。**2） 文本编辑面板（text editor panel）**修改术语中的内容。在修改多个术语时，会出现一个选择菜单，可以选中后逐个修改。**3) DAG浏览器**DAG浏览器是一个插件，能够以图形的方式展示具有复杂的从属关系的术语。**4) 搜寻/屏蔽面板**可搜寻术语、术语类型和术语间关系。可自定义屏蔽条件，限制得出的搜寻结果。

## ** **
## **7.GO数据库的查找和浏览FAQ**

**1）如何搜寻注释？**
使用AmiGO浏览器，可以在所有参与的数据库中搜寻一个特定的注解。AmiGO允许使用GO术语或基因产物的搜寻。搜寻结果包括GO对这个术语的等级分级情况，定义和近义结构，外部链接，所有相联系的基因产物和它的下一级术语。**2）如何得到全部的GO注释？**
在GO网站上，基因产物与GO联系的组信息都有提供。这些文件储存了基因/基因产物的ID和引用文献等支持证据(如FlyBase 基因ID, SWISS-PROT蛋白ID),在ftp站点上都可以获得。
**3）**在一些模式生物中,一个基因通常有多个与之相关的核苷酸序列,如EST、蛋白序列等。要查询到这些序列，可以从该模式生物数据库中通过基因联系（gene association）查询到基因获得ID(gene accession ID),或是分别在Compugen中查询大的转录产物（transcipt）和SWISS-PROT/TrEMBL中查询蛋白。**4）如何得到由GO术语注解的蛋白序列？**
在GO网页上选择能查询到所有数据库的Amigo浏览器，键入GO术语（如“线粒体”），在结果中显示了被注释的基因。然后选择你所需基因，在网页的最低端把选项拖至“get fasta sequence”区域，再确定即可。
**5）如何能够找到所有和一个特定的GO术语相关的人类基因呢？**
GO术语是和SWISS-PROT/TrEMBL/InterPro and Ensembl中的蛋白序列无赘余地对应的。这些注释在EBI上的GOA-Human 文件中，GO的FTP站点上，Ensembl，EMBL－Bank上都可找到。
**6）可以直接使用GenBank的gi获取码在GO数据库中进行查询吗？**
GO 数据库中除了Compugen所提供的GenBank获取码之外，没有包含其他GenBank获取码的信息，但是在EBI的GOA(GO Annotation)中，有一个综合的对GenBank/EMBL/DDBJ进行查询的方式，详细请见：ftp: //ftp.ebi.ac.uk/pub/databases/GO/goa/HUMAN/xrefs.goa.
**7）GO与其他分类系统的定位关系（Mapping to GO）**
GO 并不只是希望为基因组建立一个标准化的、结构清晰的注释语言。GO致力于各种基因组数据库的标准化。GO为各种基因组分类系统和GO注释之间的转化提供了转化表，见[http://www.geneontology.org/GO.indices.html](http://www.geneontology.org/GO.indices.html)需要注意的是，这些转化不是完全而精确的。其中的一个原因可能是GO有一套完整的定义系统，而很多数据库并不具有。
## **8.GO的应用**

**GO的局限性**
1）. GO 不是基因序列或基因产物数据库，相反的，GO强调基因产物在细胞中的功能。2）. GO不是整合数据库的一种方式（如联邦式整合数据库），它并不能做到这点是因为：
a. 更新速度较慢b. 由于每个人对数据定义的方式不同，标准难以达到一致。c. GO并不对生物学的每个方面进行描述。如功能域的结构、3D结构、进化等。
3）．GO 是对基因功能的注解，但是有其局限性。比如说，GO不能反映此基因的表达情况，即是否在特定细胞中、特定组织中、特定发育阶段或与某种疾病相关。GO虽然不涉及这些方面，但是支持其他的OBO(open biology ontologies)成员成立其他类型的本体论数据库（如发育本体学、蛋白组本体学、基因芯片本体学等）
**用于基因组分析**
基因组和全长 cDNA序列工程通常会根据序列的相似性，推测基因与已注释的基因功能类似。现在最常用的手段是在SWISS-PROT序列中设定一个相似性的域值，使用 计算机化的方法来判断。因此，根据这一原理，也可以得到新的GO注释（被标记为“根据电子注释推测”）。一个GO的重要应用方面是对于一个GO术语，能形 成一个相联系的基因产物组。举例来说，某一基因产物可以被精确地注释为在碳水化合物代谢的一个特定的功能，如葡萄糖代谢，而在总结碳水化合物代谢时，所有 这些基因产物都会聚集到一起。GO计划为每一个高频出现的术语建立文档总汇，现在有些已经在“GO Slim”中实现了。
**用于基因表达分析**
如在芯片数据中引入GO注释，通常可以揭示出为什么一个特定组的基因拥有相似的表达模式。共表达的基因可能编码在同一个生物过程中出现的基因产物，或定位 于同一个细胞部位的。如果未知基因和一些已被GO过程术语相似地注释了的基因共表达，那么这个未知基因很有可能在同一个过程中发挥功能。分析和操作基因表 达芯片数据，并且又能结合GO注释的软件已产生。EBI 提供的Expression Profiler，和EP:GO都具有此功能。
**GO可能的应用**
GO的应用前景很广阔，不可能一一列出，现在已用到的包括：

   - 整合来自于不同生物的蛋白组信息。
   - 判定蛋白结构域的功能。
   - 找到在疾病/衰老中异常表达的基因的功能类似性。
   - 预测与一种疾病相关的基因
   - 分析在发育中同时表达的基因
   - 建立起自动的能从文献中获取基因功能信息的工具。
   - 

## **9.GO规模**

如上所述，GO的三层结构是**分子功能**、**生化途径**和**细胞组件**。GO包含的大部分为平板格式文件（GO flat file），由每一种本体论中定义的文件为文本文件，而包含本体论和定义两种格式的是OBO格式的平板文件，XML作为可以用于三种本体论和所有定义的文件格式也有提供。这些文件都在每月的1日更新，GO每月将给出月份更新报告。
## **10.GO的使用和引用**

**GO 的使用**
基因本体论联合会是由国家人类基因组研究所 (NHGRI) 的R1拨款所赞助，此外还有欧盟RTD项目“生活质量和生活资源管理”拨款。Gene OntologyTM 由AstraZeneca公司提供资金赞助，而SGD小组得到了IncyteGenomics的赞助。GO数据库中的术语、注释等都属于公共范畴。GO的资源是免费的，但是必须在以下三种情况下使用：

- 必需引用基因本体论联合会。
- 所使用的GO文件必需标明GO的版本号和日期。（GO处于不断更新中）
- GO文件的内容和内在的逻辑关系不得被更改。

**引用GO**
当使用GO资源时，请引用以下文献：Gene Ontology: tool for the unification of biology. The Gene Ontology Consortium (2000) Nature Genet. 25: 25-29.当引用亚数据库资源时，请参考GO的 publication list 。
**参考**[http://www.360doc.com/content/11/0301/23/5690405_97308626.shtml](http://www.360doc.com/content/11/0301/23/5690405_97308626.shtml)[http://home.bbioo.com/space.php?uid=110070&do=blog&id=5201](http://home.bbioo.com/space.php?uid=110070&do=blog&id=5201)[http://blog.sina.com.cn/s/blog_416cfd6b0100qjn7.html](http://blog.sina.com.cn/s/blog_416cfd6b0100qjn7.html)[http://www.geneontology.org/](http://www.geneontology.org/)
**文章来源：**[http://fhqdddddd.blog.163.com/blog/static/1869915420128289474633/](http://fhqdddddd.blog.163.com/blog/static/1869915420128289474633/)
