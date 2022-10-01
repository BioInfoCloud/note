本文来自文章：超详细的[DESeq2和edgeR包的基本原理和实战案例](https://mp.weixin.qq.com/s/CtKlpDgtNs3f2NXaoulD5Q)
# edgeR包的基本原理

---

## RPKM等均一化的局限
在转录组测序（RNA-Seq）中，基因的表达量是我们关注的重点。基因表达量的衡量指标有：RPKM、FPKM、TPM。可参考文章：[**RNA-seq的counts,RPM, RPKM, FPK值到底有什么区别？**](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264575&idx=2&sn=69b45012dbfe61d7574446de00ec9a7b&chksm=841ef242b3697b54484a64f82bba4372a8fb2b4d411b1c1fc2bc68d12aa44756f96c3b8e48f5&scene=21#wechat_redirect)
**RPKM：**是Reads Per Kilobase per Million mapped reads的缩写，代表每百万reads中来自于某基因每千碱基长度的reads数。RPKM是将map到基因的read数除以map到基因组上的所有read数(以million为单位)与RNA的长度(以KB为单位)。说实话，这个英文说明真的很费解，其实可以理解为“Reads Per Kilobase Per Million Reads”，即“每一百万条Reads中，对基因的每1000个Base而言，比对到该1000个base的Reads数”，计算公式。
**FPKM：**Fragments per Kilobase Million，FPKM意义与RPKM极为相近。二者区别仅在于，Fragment 与 Read。RPKM的诞生是针对早期的SE测序，FPKM则是在PE测序上对RPKM的校正。只要明确Reads 和 Fragments的区别，RPKM和FPKM的概念便易于区分。Reads即是指下机后fastq数据中的每一条Reads，Fragments则是指每一段用于测序的核酸片段，在SE中，一个Fragments只测一条Reads，所以，Reads数与Fragments数目相等；在PE中，一个Fragments测两端，会得到2条Reads，但由于后期质量或比对的过滤，有可能一个Fragments的2条Reads最后只有一条进入最后的表达量分析。总之，对某一对Reads而言，这2条Reads只能算一个Fragments，所以，Fragment的最终数目是Reads的1到2倍之间。
**TPM：**Transcripts Per Million，这个英文也很费解。先不纠结字面意思了，直接解释它的计算方法。TPM的计算分3步：
step1：根据基因/转录本长度校正count值；假设某基因count值为R1，则校正后count值为：R1/(L1/1000)；  【注: L1为该基因的长度】；
step2：计算total 校正后count值；即所有基因的校正后count值总和，Rtotal；
step3：计算TPM；TPM结果为：R1*1000*1000000/(L1*Rtoatl)。
RNA-seq是二代测序技术中用来表示基因表达量或丰度的方法。在衡量基因表达量时，若是单纯以map到的read数来计算基因的表达量，在统计上是不合理的。因为在随机抽样的情况下，序列较长的基因被抽到的机率本来就会比序列短的基因较高，如此一来，序列长的基因永远会被认为表达量较高，而错估基因真正的表现量，所以Ali Mortazavi等人在2008年提出以RPKM在估计基因的表现量。
   ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013502-6190695d-8d7f-4c7e-a4fd-fdddb7524ae9.jpeg#crop=0&crop=0&crop=1&crop=1&height=391&id=p1BJd&originHeight=460&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
edgeR与DESeq2这两种方法并不使用RPKM，FPKM，TPM等方法来进行均一化，edgeR与DESeq2在对文库进行均一化时要考虑两个方面的问题：
第一，测序深度（RPKM，FPKM，TPM方法也能做到）；
第二，文库补偿（library composition没有找到相应的中文译名，此处译为“文库补偿”），因为不同的样本含有不同的活跃基因（FPKM，FPKM和TPM做不到），如下所示：
## 
## edgeR均一化步骤
下面是edgeR进行文库均一化的步骤。
**第一步：移除所有未转录的基因**
我们先看下面的一批测序数据，在这批数据中，有3个样本，每个样本有5个基因（这个数据只是虚拟的，为了方便说明问题，实际测序中不可能只有这几个基因），如下所示：
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013487-36d53bbf-5322-4e36-ab22-6873571640cb.jpeg#crop=0&crop=0&crop=1&crop=1&height=289&id=b42MD&originHeight=340&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)其中我们可以发现，Gene5在这3个样本中的reads数都是0，因此我们要把Gene 5给去掉，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013503-8574d8fc-1057-4a08-8bd4-f1f4f800a443.jpeg#crop=0&crop=0&crop=1&crop=1&height=257&id=ybLwr&originHeight=303&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)

### **第二步：选择参考样本**
在这个步骤中，我们需要在一批样本中，挑选一个样本作为“参考样本”，随后，我们会使用这个样本来均一化其他的样本，我个人理解，这个参考样本其实就相当于qPCR中的参考基因，如下所示：
          ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013558-137da6c1-4840-440c-a9df-69c7344ce6d6.jpeg#crop=0&crop=0&crop=1&crop=1&height=599&id=R7QXV&originHeight=705&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
现在我们就遇到另外一个新问题了，什么是好的参考样本，什么是坏的参考样本，好坏的标准是什么？
我们先看一个案例，这个案例讲的是坏的参考样本，所有的样本如下所示，其中Sample #3是一个非常差的参考样本，Sample #3中所有基因的reads数的均一化都只是基于一个reads数，即Gene 3，因为其它的基因都是0，因此Sample #3有很大的噪音，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013646-743cb5a4-0893-49fb-80a6-5c939b53d78c.jpeg#crop=0&crop=0&crop=1&crop=1&height=466&id=sf4Nm&originHeight=549&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
为了避免找到这样极端的样本，edgeR会选择那些最“平均”的样本，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013523-a4444f74-f9e5-414d-91a3-e586100486a9.jpeg#crop=0&crop=0&crop=1&crop=1&height=351&id=Z3ei8&originHeight=413&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
我们现在看一下edgeR如何找到这个最“平均”的样本，我们再看一批数据，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013572-4e7ffbf0-2a86-472e-ae98-b17b98d986c2.jpeg#crop=0&crop=0&crop=1&crop=1&height=454&id=jx0Hf&originHeight=463&originWidth=935&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
在寻找最“平均”的样本时，我们需要进行a，b，c，d这四步。
#### **第a步：用总reads数校正每个样本**
注：原文是Scale each sample by its total read counts，我这里使用“校正”来指scale。
计算出每个样本的所有基因的总reads数，如下图左图所示，然后使用每个样本中每个基因的reads数除以每个样本的总reads数，如下图右图所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013544-2eeb57d2-3316-4947-ba9c-9aef0f9c573f.jpeg#crop=0&crop=0&crop=1&crop=1&height=383&id=rbtKD&originHeight=451&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)**第b步：计算75%百分位数**
对于每个样本，计算出校正后的数据的75%百分位数的值，或者是小于75%百分位数的值，例如，对于样本1来说，它的75%百分位数是0.26，或者是小于0.26，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013532-8f24b916-68be-4ba8-afee-2efa9453c655.jpeg#crop=0&crop=0&crop=1&crop=1&height=447&id=xQs3b&originHeight=526&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  对于样本2来说，它的75%百分位数是0.36，或者是小于0.36，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013643-82c65169-07e1-4faa-81be-8a0393cef53a.jpeg#crop=0&crop=0&crop=1&crop=1&height=545&id=FPYdG&originHeight=545&originWidth=770&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=770)             
对于样本3来说，它的75%百分位数是0.13，或者是小于0.13，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013707-bd027282-e31a-4f21-a1eb-7cdd3bad7c8d.jpeg#crop=0&crop=0&crop=1&crop=1&height=538&id=cKnFy&originHeight=538&originWidth=786&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=786)             
现在把这3个样本的75%百分位数放在一起，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013656-75f158f9-98c9-48a2-96eb-21cf945c66dc.jpeg#crop=0&crop=0&crop=1&crop=1&height=363&id=boIG0&originHeight=363&originWidth=881&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=881)             
#### **第c步：计算平均75%百分位数**
现在计算这3个样本的平均75%百分位数，加起来，除以3即可，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013767-f18e9eca-c44d-4f82-9df4-faf11b9e8ed4.jpeg#crop=0&crop=0&crop=1&crop=1&height=354&id=dvEDU&originHeight=417&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
#### **第d步：找出最近接近于平均75%百分位数的样本**
“参考样本”的标准就是它的75%百分位数最接近于平均75%百分位数，样本1，样本2和样本3的75%百分位数分别为0.26，0.36，0.13，它们与平均75%百分位数的差值分别为0.01，0.11，0.12，其中，最接近于0.26的样本是样本1，因此样本1就是“参考样本”，如下所示：
###            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013791-ffc9c72d-6bbb-401a-aff8-74b9326a482a.jpeg#crop=0&crop=0&crop=1&crop=1&height=357&id=kUM73&originHeight=420&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)   **第三步：计算标准化因子**
#### **基本思路**
在这一步骤中，我们需要选择一些基因集（genes，复数）来创建标准化因子（scaling factors），计算的过程就是针对“参考样本”，分别选择其余的样本的基因集来创建标准化因子（也就是说不同样本创建标准化因子的基因集不同）。我们在第二步中找到了参考样本，也就是Sample #1，现在分别针对Sample #1，来计算Sample #2和样本3的标准化因子，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013649-88376eda-612f-468a-b54a-7561a4bee0df.jpeg#crop=0&crop=0&crop=1&crop=1&height=350&id=gX2SU&originHeight=412&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
这是edgeR方法的一个局限，针对不同的样本，edgeR会使用不同的基因集来计算它们的标准化因子（原文是this is one of the ramifications of edgeR’s approach. Different samples use different genes to derive their scaling factors.不知道我理解的对不对，可以对比一下原文自己理解），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013655-e60cdc9f-be54-4215-aca7-443e5060912d.jpeg#crop=0&crop=0&crop=1&crop=1&height=442&id=yST7L&originHeight=520&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
现在我们以Sample #2为例，说明一下如何选择用于创建标准化因子的基因集，我们先来看一下用于选择的基因的不同类型，下图是一个XY二维坐标系，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013618-87bb809b-5187-422b-83c2-dfcff58dc3f9.jpeg#crop=0&crop=0&crop=1&crop=1&height=527&id=yakUv&originHeight=621&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  XY轴把这个坐标系分成了四个象限，这个很好理解，我们先看下图中的第1个点（蓝色的），这个点位于左上部分，它表示这个基因主要在参考样本（reference）中转录，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013612-8459dd7a-8456-450f-8d51-d4c74e25e7fa.jpeg#crop=0&crop=0&crop=1&crop=1&height=541&id=Ryv4r&originHeight=637&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
我们再看第2个点，这个点位于最右的坐标轴上，根据坐标轴的说明，我们知道，这个基因主要在Sample #2中转录，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013608-56cc70f6-96f6-4055-af5e-97d2789f393c.jpeg#crop=0&crop=0&crop=1&crop=1&height=535&id=xDRf2&originHeight=630&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
我们再看第3个点（下图中红色圆圈标出的点），这个点位于正中间的坐标轴上，它表示这个基因的很多reads在参考样本和Sample #2中都存在，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013628-8155d344-c81f-4370-b740-50b21675faae.jpeg#crop=0&crop=0&crop=1&crop=1&height=531&id=cfd1R&originHeight=625&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
我们再看第4个点，它们于中间最下面的坐标轴上，根据坐标轴的说明，我们知道，在参考样本和Sample #2中，都很少含有这个基因的reads，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013625-128a5a7d-2b8e-48a6-b124-b600b7a562c8.jpeg#crop=0&crop=0&crop=1&crop=1&height=514&id=HXwqC&originHeight=605&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
这样，我们把所有的基因的reads数都放到这个坐标上，我们就可以发现，中间有很大一部分基因没有偏倚，没有偏倚的意思是说，在中间的这些基因，它们在参考样本和Sample #2中的reads数都差不多，区别不大，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013634-a6d49839-c929-4794-98b4-9bf67d237a85.jpeg#crop=0&crop=0&crop=1&crop=1&height=532&id=et3va&originHeight=627&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
而edgeR就会选择中间区域（红色椭圆区域）里的这些基因，排除那些有偏倚的基因，如下所示：
####            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013701-f6978de6-817f-4d66-84ba-a95e4f5b81ba.jpeg#crop=0&crop=0&crop=1&crop=1&height=548&id=xB3z3&originHeight=645&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  **计算过程**
上面只是edgeR选择基因集的基本思路。现在我们看一下edgeR是如何计算标准化因子的。
##### **第a步：过滤偏倚基因**
计算所用的数据是已经均一化后的数据（也就是每个基因的reads数除以总的reads数），下图中表示的是全部的N个基因，基因虽然很多，但是这些基因均一化的方法还是与前面所述的4个基因是一样的，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013610-c9344ad2-571a-4b78-afad-829131c753a7.jpeg#crop=0&crop=0&crop=1&crop=1&height=574&id=e2DUg&originHeight=575&originWidth=594&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=593)             
edgeR是通过倍数差异的log转换（log fold differences）来过滤偏倚基因（biased genes）的，它的公式是log fold differences = log2（Reference/sample 2)。从这个公式我们就可以看出来，如果Reference的某个基因的值相对于Sample #2比较高，那么这个log fold differences就是一个正值（图中指向3），如果Sample #2的某个基因的值相对于Reference比较高，那么这个log fold differences就是一个负值（图中指向-3），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013681-09acb41b-e957-4cfb-af88-9d2adc948688.jpeg#crop=0&crop=0&crop=1&crop=1&height=510&id=d0anl&originHeight=601&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
最终，我们会选择一个阈值，例如+/-6，超过这个范围就认为是极度偏倚的值，需要除去，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013675-0ca468ea-332a-4cfa-95bf-6fdd2544fefd.jpeg#crop=0&crop=0&crop=1&crop=1&height=525&id=jPBdB&originHeight=525&originWidth=784&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=784)
我们现在以Gene 1为例来说明一下，它的计算公式如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013826-0efabd0c-7f1f-49f7-ab4d-4ec24e7f84ef.jpeg#crop=0&crop=0&crop=1&crop=1&height=594&id=jdFpQ&originHeight=699&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
由于参考样本的Gene1是0，因此这个最终的log fold differences数值为-Inf，它表示无穷小。现在我们看一下Gene2的计算，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013779-437dc3fc-1f5c-49bc-960a-cea38622026a.jpeg#crop=0&crop=0&crop=1&crop=1&height=584&id=gvCyp&originHeight=688&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
最终计算出所有的结果，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013654-eadf8f51-acf3-4f67-bc64-6e3f14dcf9da.jpeg#crop=0&crop=0&crop=1&crop=1&height=358&id=J6IYT&originHeight=359&originWidth=437&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=436)            
此时，我们就要移除那些Inf的基因，也就是说，要移除那些在样本中（无论是同时在两个样本，还是任何一个样本中）reads数为0的基因，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013694-b099da1e-429b-45e3-820e-cfb73c99b642.jpeg#crop=0&crop=0&crop=1&crop=1&height=267&id=Jpat3&originHeight=314&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
经过上面的计算，我们就得到了一个新的数据集，这个数据集是经过log fold differences转换后的数据集，此数据集用于排除偏倚基因。
##### **第b步：计算几何均数**
现在我们还需要另外一个数据集，用于观察哪些基因在两个样本是高转录和低转录的，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013679-ebf9d214-4ff8-4e7b-b907-32d852f67e4d.jpeg#crop=0&crop=0&crop=1&crop=1&height=232&id=FR6B3&originHeight=232&originWidth=568&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=568)            
计算基因的高转录和低转录时，首选要计算每个基因的几何均数（the geometric mean），几何均数很有用，因为它不太容易受到异常值的影响，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013777-25177ed5-6c8d-4901-a75e-1a19182f3768.jpeg#crop=0&crop=0&crop=1&crop=1&height=498&id=pylVI&originHeight=586&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
这里要注明一下，严格意义来说，上面的这个公式只是经log转换后的数字的算术均数，由于经过了log转换，因此log转换后的算术均数其实上就是原始数据（未经log转换的数据）的几何均数，因为我们并不把log转换后的算术均数转换回正常的数值（也就是没有经过log转换后的数值），因此在这里，我们使用了log转换后的数值的算术均数，但它们的最终的效应是一样的，即异常值很少影响这些数据，下面以Gene 2为例说明一下这个计算过程：
Gene 2在参考样本中的数值为0.04，在Sample #2中的数值为0.05，它的几何均值其实应该是下面的这个样子：
           ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013681-7b37d4dd-6db7-4263-a38c-7f0e4838f4ce.png#crop=0&crop=0&crop=1&crop=1&height=224&id=DArvY&originHeight=224&originWidth=606&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=606)             
现在对0.0447213595进行log2转换，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013689-0bbfeab6-ed7b-4a47-a7ea-25270a24ff84.png#crop=0&crop=0&crop=1&crop=1&height=75&id=EXDPh&originHeight=75&originWidth=699&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=698)             
我们再来看一下计算结果，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013888-8f3011a2-911b-42d0-b31e-ae7800dbac65.jpeg#crop=0&crop=0&crop=1&crop=1&height=514&id=ibusU&originHeight=605&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
从上面的结果我们可以发现，这个数值是一样的，经过计算，所有的结果如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013879-a8d96dda-d425-4c5d-b8e7-c3356778e152.png#crop=0&crop=0&crop=1&crop=1&height=344&id=vn4YR&originHeight=345&originWidth=371&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=370)            
现在我们移除那些infinite的值，也就是那些没有任何reads的基因（也就是计算结果中是-Inf或Inf的值），如下所示：           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013713-7044350d-06ff-4dd1-b249-c28007c94607.jpeg#crop=0&crop=0&crop=1&crop=1&height=343&id=zeqn0&originHeight=353&originWidth=943&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
##### **第c步：计算代表基因集**
经过前面的计算，此时，我们就有了两张表，第一张表是log2(reference/Sample #2)的数据，它用于确定偏倚基因，另外一张表的数据是经log2转换后的均值数据，这批数据用于确定哪些基因是高转录的，哪些基因是低转录的，这两张表如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013729-f7e167a7-04ba-4417-9d87-64dd6dbc1db2.jpeg#crop=0&crop=0&crop=1&crop=1&height=397&id=ZoBDu&originHeight=467&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  此时，我们将这两张表中的数据都按从小到大的顺序进行排列，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013841-2e6773ec-0e1a-4b80-b730-f45f743dc183.jpeg#crop=0&crop=0&crop=1&crop=1&height=386&id=iv3uv&originHeight=455&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
在第一张表中，去掉前30%的数据，以及去掉后30%的数据，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013691-e9aff87f-73b9-431d-8cf8-7c95618e9f59.jpeg#crop=0&crop=0&crop=1&crop=1&height=505&id=HuJGi&originHeight=506&originWidth=534&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=533)         在第二张表中，去掉前5%的数据，以及去掉后5%的数据，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013704-2759d104-202d-40b2-9fe9-59817c1834e4.jpeg#crop=0&crop=0&crop=1&crop=1&height=509&id=X08bj&originHeight=509&originWidth=482&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=482)        用两张表中剩下的数据来计算标准化因子（取两张表基因的交集），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013694-e08d6981-7c0b-47d0-8799-6773fcdd997a.jpeg#crop=0&crop=0&crop=1&crop=1&height=183&id=irItg&originHeight=215&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
不过在这个案例中，这两终表中剩余的基因并没有列出，都在省略号中，但是这个案例只是在讲edgeR的算法原理，并不涉及具体的数据，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013766-c78bf428-3bfe-4e7b-a306-50b88cb3203c.jpeg#crop=0&crop=0&crop=1&crop=1&height=377&id=PLy4d&originHeight=444&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
为了方便理解，我们就假定，下图就是最终于用计算Sample #2的标准化因子的基因集，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013759-514f0c43-3605-41cf-a54b-97461ecd7f96.jpeg#crop=0&crop=0&crop=1&crop=1&height=516&id=mx3VM&originHeight=516&originWidth=806&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=806)             
同样的，还有计算Sample #3标准化因子的基因集，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013791-56ed3f2b-8c5a-4be0-ae2a-83757d218c78.jpeg#crop=0&crop=0&crop=1&crop=1&height=416&id=lS8oV&originHeight=478&originWidth=1053&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
### **第四步：计算加权均数**
在这一步骤中，edgeR会计算代表性基因集的log fold的加权平均数，在edgeR中，这个log fold的加权平均数称为为“weighted trimmed mean of the log2 ratio”，因为这些数据已经剔除掉（trim）了那些表达比较极端的基因（特别高的和特别低的），这样，计算结果就不会受到表达异常基因的影响，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013722-9a50a51c-e1e1-4bca-862b-5a6de5b4b693.jpeg#crop=0&crop=0&crop=1&crop=1&height=351&id=Gy5EF&originHeight=411&originWidth=1073&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
现在我们回到Sample #2的基因集上，这些基因是经过了第三步的筛选过的基因，只是我们假定的数据，就是我们上面说的省略号中的基因，只是用来计算的，不用管它的实际意义，它的log fold如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013764-7a076d90-0107-4793-a4b6-a77aa55d04e4.jpeg#crop=0&crop=0&crop=1&crop=1&height=413&id=zDcT1&originHeight=413&originWidth=837&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=836)
 一旦我们选择了这些基因用于计算标准化因子，那么我们就仅需要计算出它们的log 2的加权均数即可，也就是说，比对到某个基因上的reads数越多，这个基因的权重就越大，这是因为对于那些低reads数的基因来的，log fold数值的变异程度比较大，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013858-ee6d2c6d-6b0b-49f7-a105-9d739b702ad2.jpeg#crop=0&crop=0&crop=1&crop=1&height=420&id=vFtXX&originHeight=495&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917) 为了说明reads数少的基因经过log fold转换后的变异程度比较大的问题，我们这里插入一个案例，下图是几个基因的reads数，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013759-2ac35dda-e8a0-4cea-b0a2-035aa994a69a.jpeg#crop=0&crop=0&crop=1&crop=1&height=497&id=XcwGg&originHeight=582&originWidth=1074&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
从上面的数据中我们可以知道，Gene #1、Gene #2、Gene #3的reads数比较高，不过Gene #1比Gene #3的reads数还是多了4，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013782-0e0bca97-5023-4dee-aaf8-315340f5d74e.jpeg#crop=0&crop=0&crop=1&crop=1&height=424&id=WaJwW&originHeight=499&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
我们再看Gene #4和Gene #6，虽然它们的reads数比较少，不过它们之间的reads数也是差了4，这个数值与Gene #1比Gene #3的差值一样，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013753-3d358767-81b3-4c52-b4f1-d490bf8bf2fa.jpeg#crop=0&crop=0&crop=1&crop=1&height=211&id=uI5UR&originHeight=249&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)不过，我们看一下右侧的经过log2 fold转换后的数据，我们可以发现，Gene #1和Gene #3的log2 fold的值差别并不大，如下所示：         ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013922-b303d8f9-d463-4663-ab94-f0624d3392f3.jpeg#crop=0&crop=0&crop=1&crop=1&height=375&id=XPdcH&originHeight=442&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
但是，我们看一下Gene #4和Gene #6，虽然它们的reads数相差是4，但是，它们的log2 fold的值相差却是1.6，这个值是非常大的值了，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013808-ac5c00c7-b3a9-4698-9d22-a96720b1d7d7.jpeg#crop=0&crop=0&crop=1&crop=1&height=565&id=kqKCH&originHeight=666&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
针对这种情况，我们就需要对那些有着高reads数的基因加上更大的权重，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013858-32110604-cd56-4a83-aaf5-04be8167d62a.jpeg#crop=0&crop=0&crop=1&crop=1&height=487&id=MwtMn&originHeight=573&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)对于Sample #3的处理，也是如此，如下所示：
       ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013812-912007e2-3c92-49b5-b96c-759b561d6d6c.jpeg#crop=0&crop=0&crop=1&crop=1&height=508&id=X9FY8&originHeight=598&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
log2 fold的加权均数的计算公式如下所示：
简单来说就是log2 foldA的值乘以相应基因的reads数的和，然后除以所有的reads数之和。
          ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013790-8c4640c1-ee34-4b06-a942-f605dbe0a294.png#crop=0&crop=0&crop=1&crop=1&height=261&id=aJeNA&originHeight=261&originWidth=819&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=818)             
### **第五步：将加权log2 fold值转换为真值**
在这一步中，我们需要把前面过计算出来的加权平均值转换为真值（也就是log2转换前的数值）。
标准化因子的公式如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013822-f478b96a-656e-410e-a07c-e8a1baebfae4.png#crop=0&crop=0&crop=1&crop=1&height=72&id=k6QNm&originHeight=85&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)不过，此时的这个“标准化因子”并不是edgeR所使用的标准化因子，为了区分edgeR中的标准化因子，我暂时称它为“原始标准化因子”，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013785-1b0008c3-b389-4458-8f8c-b857e6b6f739.jpeg#crop=0&crop=0&crop=1&crop=1&height=304&id=MpCp8&originHeight=358&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
按照上述方法，再计算出Sample #3的“原始标准化因子”，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013806-5fae8e7c-9a37-4f81-a843-62236a0b80df.jpeg#crop=0&crop=0&crop=1&crop=1&height=128&id=UIEB8&originHeight=151&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
经过上面的计算，这个原始标准化因子还要进行进一步的计算，才是edgeR的标准化因子。
我们来看一个实际的案例，这个案例使用的一个RNA-Seq实验中的数据计算出来的原始标准化因子（就是按上面的公式计算出来的标准化因子），其中，WT2是参考样本，其余的样本根据WT2进行均一化，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013790-2386486f-1fc1-44cd-b0df-484095f30050.jpeg#crop=0&crop=0&crop=1&crop=1&height=142&id=Mt2oK&originHeight=167&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
### **第六步：原始标准化因子的中心化**
下图是我们计算出来的原始标准化因子，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013804-bc699285-111b-490b-9890-c90e64387080.jpeg#crop=0&crop=0&crop=1&crop=1&height=397&id=eP9IA&originHeight=397&originWidth=689&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=689)             
这些值在数轴上主要以0.95为中心进行排列，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013854-5c012284-4269-466d-a704-85e7d82d0378.jpeg#crop=0&crop=0&crop=1&crop=1&height=717&id=c5QLY&originHeight=718&originWidth=739&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=738)             
我们对这批数据进行“中心化”，其实就是用它们的每个值除以这4个数据的几何均数，几何均数就是如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013857-d1b5fe72-775d-47a1-8f48-f9c703607b9a.png#crop=0&crop=0&crop=1&crop=1&height=60&id=m5urw&originHeight=60&originWidth=846&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=846)             
最终计算的edgeR标准化因子（也就是中心化的原始标准化因子）如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013832-0743482d-69a5-48c5-a444-d7d1717560ce.jpeg#crop=0&crop=0&crop=1&crop=1&height=436&id=yf12D&originHeight=514&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
虽然除以几何均数并不会改变最终的计算结果，但是Mark Robinson（edgeR包的开发者）说，经过中心化的处理就能赋予标准化因子一些数学上的美感。
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013887-f7026c3e-3fab-49b6-903c-5e821dd0efae.jpeg#crop=0&crop=0&crop=1&crop=1&height=467&id=YewYi&originHeight=550&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  此时，edgeR的标准化因子计算到此，接着把表达矩阵中的数值除以这个标准化因子即可。

---

# edgeR包差异分析实战案例

## 包的安装和加载
```
BiocManager::install( "edgeR" )library( "edgeR" )
```
## 读入数据
这里我们用的数据是一个Excel文件，是原始的counts文件（想运行案例，文末获取文件）
```
# 读取数据
counts <- read.table("gene_counts.xls", sep = "\t", header = T, row.names = 1)
```
导入的数据我们通过head()函数查看前6行。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013820-50e629d3-940b-4efe-94c8-ba9c3e6a9b11.png#crop=0&crop=0&crop=1&crop=1&height=272&id=W3h9H&originHeight=272&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
行名A1,A2,A3,B1,B2,B3为样本名，列名是基因名。
## 创建分组
设置实验组别，在前面我们介绍基本原理时，有一步需要选择参考样本，在实际分析中，我们可以自己选择参考样本，一般都是对照组作为参考样本，在edgeR中，1代表control样本，2代表case样本。原始数据中有6个样本，对照和实验组各三个。所以我们可以创建一个分组向量。
```
# 创建分组group <- c(rep(1,3),rep(2,3))
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013887-606285f5-cec0-4eff-84c2-148ed3370d4e.png#crop=0&crop=0&crop=1&crop=1&height=158&id=QdhSq&originHeight=158&originWidth=616&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=616)
## 数据处理
```
# 创建DGEList类型变量
y <- DGEList(counts=counts, group=group)
```
这一步相当于创建一列表。注意group中的顺序和counts中行名要对应，也就是对照组和实验组要指定正确。这里A1,A2,A3为control，B1,B2,B3为case。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013862-f06beefc-b94d-47f6-b545-580fa945aaff.png#crop=0&crop=0&crop=1&crop=1&height=532&id=DQB3w&originHeight=532&originWidth=628&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=628)
```
# 数据过滤
keep <- filterByExpr(y)y <- y[keep, , keep.lib.sizes=FALSE]
```
filterByExpr函数用于确定哪些基因的计数足够大，可以保留在统计分析中。也就是我们在介绍原理中提到的去除表达值为0的基因，实际分析中不是0，我个人理解，counts为只为个位数的也认为是不表达的，所以这里默认的min.count = 10, min.total.count = 15，当然也可以通过参数自己设定。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013900-c96ce072-ebdf-4824-823c-28f39a043d2d.png#crop=0&crop=0&crop=1&crop=1&height=383&id=N78Wr&originHeight=383&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
filterByExpr函数返回的是一个逻辑值类型数据，所以我们需要通过索引获取过滤后的数据。即去除FALSE的基因。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013944-a34d2b16-278b-4f4a-8131-64cf1b9f7f1a.png#crop=0&crop=0&crop=1&crop=1&height=98&id=nOWWp&originHeight=98&originWidth=633&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=633)
```
# 计算标准化因子
y <- calcNormFactors(y)# 查看标准化因子y$samples
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532013886-724f9406-9051-45cf-8f9b-02ab4d65dc88.png#crop=0&crop=0&crop=1&crop=1&height=359&id=Lv2pM&originHeight=359&originWidth=949&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=949)
```
# 计算离散度
y <- estimateDisp(y)# 显著性检验
et <- exactTest(y)# 获取排名靠前的基因，这里设置n=100000是为了输出所以基因
et <- topTags(et, n=100000)# 转换为数据框类型
et <- as.data.frame(et)
```
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013900-312074b5-d76d-4705-a480-d8bacfeb5623.jpeg#crop=0&crop=0&crop=1&crop=1&height=424&id=G1lBW&originHeight=424&originWidth=759&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=759)
```
# 将行名粘贴为数据框的第一列
et <- cbind(rownames(et),et)# 指定列名
colnames(et) <- c("gene_id", "log2FoldChange", "log2CPM", "PValue", "FDR")# 保存数据到本地
write.table(et, "case-vs-control-all.gene.xls", sep = "\t", col.names = TRUE,
row.names = FALSE, quote = FALSE, na = "")
```
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013952-663dbb51-a031-4c85-ba2b-ecfa54fe1a99.jpeg#crop=0&crop=0&crop=1&crop=1&height=428&id=F7AD6&originHeight=428&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
## 差异基因筛选
```
# 差异基因筛选
etSig <- et[which(et$PValue < 0.05 & abs(et$log2FoldChange) > 1),]
# 加入一列，up_down 体现上下调信息
etSig[which(etSig$log2FoldChange > 0), "up_down"] <- "Up"
etSig[which(etSig$log2FoldChange < 0), "up_down"] <- "Down"
# 保存文件
write.table(etSig, "case-vs-control-diff-pval-0.05-FC-2-edgeR.gene.xls", sep = "\t", 
						col.names = TRUE, row.names = FALSE, quote = FALSE, na = "")
```
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013921-0d7dd705-7c5f-4d96-a5a3-9a425a1e17f9.jpeg#crop=0&crop=0&crop=1&crop=1&height=256&id=SWSJ3&originHeight=256&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
这样我们就可以获取差异表达的基因了，可以用于后面的作图，比如火山图！
案例文件和代码，后台回复：**chip-data-edgeR**，获取！

---

# DESeq2包的基本原理
上面我们介绍了edgeR包的基本原理，我们接着介绍DESeq2的基本原理。
## 文库均一化面临的问题
DESeq2是另外一个分析差异基因的R包，它的功能很多，使用也比较复杂。我们在前面提到过，RPKM，FPKM与TPM是常用的用于均一化不同的样本reads数的方法，不过DESeq2和edgeR并不使用前面的三种方法，因为在对文库进行均一化时，存在两个问题，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013868-106931b6-307c-49c1-988e-35dcd5412158.jpeg#crop=0&crop=0&crop=1&crop=1&height=339&id=VeMcv&originHeight=370&originWidth=1000&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
第1个问题就是，不同样本的文库大小还有差异，需要对其进行调整。我们先看一个简单的案例，在这个案例中，我们假设某个物种的基因组上只有6个基因，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013875-7a9a7701-70ff-4c29-b14b-4b2f405ee6e9.jpeg#crop=0&crop=0&crop=1&crop=1&height=357&id=g7XEm&originHeight=421&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
现在我们手中有这个物种的两个测序样本，其中Sample #1的reads数为635，Sample #2的reads数为1270，它们的各自基因对应的reads数如下所示，从中我们可以看到，Sample #1的reads总数是Sample #2的reads总数的一半，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013886-20808a14-63c2-425b-ad6e-35a317065a78.jpeg#crop=0&crop=0&crop=1&crop=1&height=473&id=QD8WT&originHeight=557&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)      我们再看一下这两个样本每个基因对应的reads数，从中我们可以发现，Sample #2中每个基因对应的reads数也基本上是Sample #1中每个基因对应的reads数的2倍，这种差异不可能是生物学的原因，因为物种都一样，出现这种现象的原因就是测序深度，而RPKM，FPKM和TPM都能处理这样的问题（也就是测序深度不同造成的reads不同），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013882-22f65882-c2c9-4129-bb15-3fb21e4ba39e.jpeg#crop=0&crop=0&crop=1&crop=1&height=485&id=tJTrt&originHeight=571&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)第2个问题是，我们需要调整由于文库补偿（library composition没有找到相应的中文翻译，此处译为“文库补偿”）造成的差异。RNA-seq或者是其它的高通量测序技术通常会比较不同组织类型之间的测序数据差异，例如我们可能会比较肝脏与脾脏的差异。这个时候就可能会出现问题，因为在肝脏中，存在着某些特异性基因，这些基因只在肝脏中大量转录，而在脾脏中转录不活跃，这就是文库补偿造成的差异的一个案例，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013895-6bc1e23e-76d4-4173-96b3-0ce252a9866c.jpeg#crop=0&crop=0&crop=1&crop=1&height=459&id=UqEyH&originHeight=541&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  我们看一下A2M这个基因，在Sample #1中，这个基因的reads数是635，而在Sample #2中这个基因的reads数是0，这就说明，A2M这个基因只在Sample #1中转录，它的reads数是563，但是在Sample #2中，这个563的reads数必定是分配到其它的基因上去了，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013898-a7980997-64bf-4649-a0d1-3df0c1795e0a.jpeg#crop=0&crop=0&crop=1&crop=1&height=565&id=vYbaN&originHeight=666&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在我们看一下Sample #2中所有基因的reads数，我们可以发现，在Sample #2中，A2M的reads数为0，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013980-17facb20-6ff7-45af-aa10-abb17129c334.jpeg#crop=0&crop=0&crop=1&crop=1&height=509&id=r2wG9&originHeight=599&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
如果出现了这种情况，那么RPKM，FPKM和TPM是无法处理的，此时就需要使用DESeq2（或者是edgeR）来处理，DESeq2能处理各种测序的数据集，它能解决的两个问题：
第一，不同文库大小之间的差异；
第二，文库补偿效应造成的差异。
如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013904-077a24ed-c617-49ff-9c43-ee20f30b4a2d.jpeg#crop=0&crop=0&crop=1&crop=1&height=338&id=vQnbQ&originHeight=339&originWidth=921&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)            
# DESeq2均一化的步骤
现在我们看一个简单的案例，在下面的这个案例中，我们有3个样本，每个样本有3个基因，在这个案例中，我们的目标是计算每个样本的标准化因子（scaling factor），标准化因子会解决测序深度（read depth）和文库补偿（library composition）的问题，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013935-616ee4ca-303b-4617-bdac-a65350a23fb0.jpeg#crop=0&crop=0&crop=1&crop=1&height=416&id=uIhiA&originHeight=490&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)   第一步：对reads数取自然对数
DESeq2中默认是对reads数取以e为底的对数（但是也可能设置以2或10为底的对数）如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013944-4001c4dc-55fa-4b33-ade1-ce7df341c846.jpeg#crop=0&crop=0&crop=1&crop=1&height=387&id=UaqmD&originHeight=456&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  自然对数比较好理解，以Sample #2的Gene 1为例，它的reads数是10，那么loge(10)=2.3，另外需要注意的是，如查reads数为0，那么对数就是-Infinity，缩写为-Inf，表示负无穷，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014005-f71705b9-4831-4d9e-a224-c99635d90220.jpeg#crop=0&crop=0&crop=1&crop=1&height=371&id=uov82&originHeight=437&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  第二步：求所有样本中，相同基因对数的均值
在这一步中，我们需要对同一个基因在所有样本中的数值取均数，以Gene 1为例，Gene 1在这三个样本中的数值分别为-Inf，2.3，1.4，由于-Inf是负无穷，因此加起来也是-Inf，再除以3，还是这个数，我们再看Gene 2的数值，它在3个样本中的数值分别为0.7，1.8，2.5，那么它的均值就是1.7，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013949-7cd4e984-299e-4a5b-9b47-02b681a03ee5.jpeg#crop=0&crop=0&crop=1&crop=1&height=414&id=MJGSG&originHeight=488&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  用对数的一个原因就是对数不太容易受到异常值的影响，我们看一下Gene3，它在Sample #3中的原始reads数是200，而在Sample #1和Sample #2中的数值分别为33和55，因此200明显是一个异常值，如果直接使用reads数来计算均数，那么结果就是96，我们再看一下使用对数的均值，计算结果是4.3，这个4.3是指数，现在把它转换成与reads数对应的原始数值，也就是e的4.3次方，结果为73.7，与96相比，前者还是比较小的，说明使用对数的受异常值的影响比较小（这种先取对数，后用对数求均值的方法叫几何平均数），如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013975-4ff6411f-ce59-4886-8ae2-9120da08a588.jpeg#crop=0&crop=0&crop=1&crop=1&height=510&id=C0oTu&originHeight=601&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  第三步：去除掉Infinity
在这一步中，我们要把在第二步中计算出的含有Inf的基因给剔除掉，也就是说要在样本中把reads数为0的基因给剔除掉，如果如果我们比较的是肝脏和脾脏的转录组，按这种剔除方法，我们会把那些所有只在肝脏（或脾脏）中转录的基因都给剔除掉，从理论上讲，最终剩下的基因基本上就是管家基因（house keeping genes）了，也就是说在不同组织类型中都表达相似的基因，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013997-19b462d2-a4f3-48ce-af12-84df78859eb7.jpeg#crop=0&crop=0&crop=1&crop=1&height=524&id=wQncv&originHeight=617&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  第四步：矩阵减均值
在上一步中，我们把数据中的Inf值去除了，在这一步中，把每个样本中的每个基本减去该基因在所有样本中的均值，以Gene 2为例，它在经对数转换后的Sample #1、Sample #2、Sample #3中的数值分别为0.7，1.8和2.5，它在所有样本中的均值为1.7，这3个数值都减去1.7，就是-1.0，0.1，0.5，其余基因操作均如此，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013945-f64a732b-e0fe-49de-aaf5-a3e7c6344b5a.jpeg#crop=0&crop=0&crop=1&crop=1&height=413&id=HE2ns&originHeight=487&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  在这一步骤中，我们用的是对数转换后的数值相减，其本质上是以某个基因（这里称为基因X）的平均值为参考，对每个样本中的基因X进行均一化，就是原始reads数的相除，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013972-3b06186d-8e5d-47d2-8b3a-fe90c6d74ee0.jpeg#crop=0&crop=0&crop=1&crop=1&height=263&id=rTCZx&originHeight=310&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  第五步：计算每个样本的中位数
在这一步中，我们要计算每个样本中，所有基因的对数的中位数，以Sample #1为例，在这个样本中，它所有的基因只有Gene2和Gene3，分别为-1.0和-0.8，它的中位数就是-0.9，其余的样本的计算也是如此，这里需要注明一下，因为在这个案例中，一个样本的所有基因只有2个，因此它的中位数和无数是相等的，但是如果基因的数目很大，这两个值就不一定相等了，例如某批数据，分别为1，3，5，7，10000，那么这批数据的中位数就是5，均值则为2003.2，这个均值受异常值的影响很大，再看一批数据，分别为-1000，3，5，7，9，那么这批数据的中位数还是5，均值就变成了-195.2了，从中我们可以发现，均值比较容易受异常值的影响，但中位数对异常值则不敏感。
这里使用中位数主要是为了排除一些极端表达基因的影响，极端表达指的是表达量极高或极低，它们能够对均值造成很大的影响，而那些表达量差异极大的基因对于中位数的影响，并不比那些表达量差异较小的基因对中位数的影响大。再加上那些表达量差异极大的基因数量通常情况下很少，因此，更多情况下，中等程度表达差异的基因和管家基因对中位数的影响更大一些，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013936-43610ba7-0da2-4cd7-a748-4f8bcab3015f.jpeg#crop=0&crop=0&crop=1&crop=1&height=498&id=n49Fu&originHeight=586&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  第六步：将中位数转换为真数，计算每个样本最终的标准化因子
在这一步中，我们要把第五步中的对数中位数转换为真数，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013949-d25ecedb-36c5-450f-8a8b-4c8534746cbc.jpeg#crop=0&crop=0&crop=1&crop=1&height=490&id=g78JQ&originHeight=577&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  此时，我们就得到了这3个样本的标准化因子了，此时进入第七步。
## 第七步：原始reads数除以标准化因子
在这一步中，我们要把原始的reads数除以这个标准化因子，以Sample #1为例，它的标准化因子为0.4，那么Gene 1，Gene2和Gene 3的reads数分别为0，2，33，它们分别除以0.4，结果为0，5，82.5，由于read不可能是小数，四舍五入，结果就是0，5，83，其余的样本均按此方法处理，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013965-fabe7a0e-ec21-416c-9375-1e3c2579deb9.jpeg#crop=0&crop=0&crop=1&crop=1&height=453&id=BcQRb&originHeight=534&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
## DESeq2文库标准化因子总结
log转换会剔除那些只在某个样本类型中的转录的所有基因（例如肝脏与脾脏），这种处理也会消除原始reads数的异常值（通过几何均数）。
中位数的处理会进一步降低那些高数值reads数基因的影响，从而关注那些中等表达程度的基因，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013966-97c8bcae-5652-4866-8a2f-3b8443d27700.jpeg#crop=0&crop=0&crop=1&crop=1&height=262&id=WYQnh&originHeight=309&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)不相关过滤（Independent Filtering）
在这一部分中，我们会讲一下对那些低reads数的基因过滤的方法，这个过程又叫不相关过滤（Independent Filtering没有找到相应的中文译名，这里译为“不相关过滤”），也叫解决多重检测问题，如下所示：
###            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014111-94bc5fde-bc75-46d0-adb1-bc0e8a2bcc9a.jpeg#crop=0&crop=0&crop=1&crop=1&height=552&id=pRFnh&originHeight=650&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  ** 有关假阳性**
当我们做一个统计学检验时，就有一定的概率得到的是错误结论，简单来说就是，我们认为“p值小于0.05就是有统计学差异的”，也可以这么说，“我们有5%的概率会得到一个假阳性的结果”，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013970-839d578d-c6ad-408d-803a-f3c99a262738.jpeg#crop=0&crop=0&crop=1&crop=1&height=284&id=FrAfc&originHeight=334&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  我们来用一个简单的案例来说明这个问题，在下面的这个案例中，其中红点表示突变组，黑点表示对照组，我们检测了Gene 1和Gene 2的这两个基因，它们对应的p值如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013974-378c0503-e7f7-493b-9b97-dc8542710889.jpeg#crop=0&crop=0&crop=1&crop=1&height=460&id=SpIWv&originHeight=542&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  从上面的结果可以看出，它们的p值分别为0.03和0.13，基因数目是2，2的5%是一个很小的数值，因此，我们很不太可能得到一个假阳性的结果，但是，如果我们比较了整个基因组中的所有基因（大概有2万个），用于观察哪些基因调控出现了异常时，情况就不太一样了，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014023-060115e8-2d7b-4775-a15c-8f55038aa8cb.jpeg#crop=0&crop=0&crop=1&crop=1&height=487&id=GUIHw&originHeight=573&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
2万的5%就是1000，也就是说，如果我们以p值0.05为阈值进行统计的话，我们有可能得到约1000个假阳性结果，对于这个问题，我们通常会采用FDR和Benjamini-Hochberg方法来解决，不过，即使是这样，我们还会遇到另外的一个问题，先看一个案例。
在下面的图形中，我们看到了两个独立的分布，其中红色曲线表示X品系小鼠的体重，蓝色的曲线表示Y品系小鼠的体重分布，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532013984-47e3f7ce-38b9-4bfe-9fd1-4064ff89aa89.jpeg#crop=0&crop=0&crop=1&crop=1&height=356&id=hBizu&originHeight=419&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  如果我们称量一个X品系小鼠的体重，那么它有很大的概率会落到红色曲线的中间部分，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014157-51a0c28c-fb7e-40fa-87aa-939be0b88e3c.jpeg#crop=0&crop=0&crop=1&crop=1&height=418&id=t4upr&originHeight=492&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  如果我们称量3只X品系的小鼠，它们都有可能落在红色曲线的中间部分，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014147-a57a313a-68fc-4153-8e0f-61fcb15f7f3e.jpeg#crop=0&crop=0&crop=1&crop=1&height=411&id=sFI0S&originHeight=484&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  同样类似的，还有Y品系小鼠的体重，如果我们称量3只Y品系的小鼠，那么它们也有很大的概率会落在蓝色曲线的中间区域，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014016-f61a6e3b-2070-4262-9ef0-0b7694d21e76.jpeg#crop=0&crop=0&crop=1&crop=1&height=440&id=f3DXW&originHeight=518&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  如果我们对这两批数据进行t检验，得到的p值小于0.05的话，我们就可以正确地下一个结论，即这两批数据存在着差异，这种差异是来源于两种小鼠的体重分布不同，也就是说这是由于小鼠品系不同千万的体重差异，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014011-3fc1504e-623a-4dbc-a631-0a3d78a83fba.jpeg#crop=0&crop=0&crop=1&crop=1&height=519&id=Uk6V2&originHeight=611&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  但是，有时候我们称量的小鼠体重会出现重叠，此时，我们进行t检验，它的p值有可能就是大于0.05的，这就是假阴性，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014021-d8a2240a-5036-4ddd-86dc-b99644af56d0.jpeg#crop=0&crop=0&crop=1&crop=1&height=386&id=U0FqT&originHeight=455&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  如果我们使用计算机从这些分布中进行1000次抽样（一次抽样包括从对照组中抽3只，突变组中抽3只），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014043-8895ab18-d470-4a07-9319-38b8dfd26270.jpeg#crop=0&crop=0&crop=1&crop=1&height=745&id=mRww0&originHeight=747&originWidth=920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在做1000次t检验，我们看一下这1000次的p值，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014112-5e03f72c-18dd-47c5-a97d-7638575c304f.jpeg#crop=0&crop=0&crop=1&crop=1&height=462&id=ePpKU&originHeight=544&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  其中我们可以发现，有949个结果的p值是小于0.05的，有51个假阴性（p值大于0.05），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014029-2e4391f2-2800-46c5-825b-33f14e41bcf9.jpeg#crop=0&crop=0&crop=1&crop=1&height=414&id=zyLgB&originHeight=488&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  目前为止，我们进行的每次检验都被认为应该是一个真阳性，它的p值是小于0.05的，这句话的意思是说，我们希望检验的这两个数据（也就是突变组与对照组的数据）是有差异，当然了，实际结果可能没有差异，这就是假阴性。出现真阳性是因为我们每次检验使用的样本都是来源于不同的分布，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014040-9ccb698c-0dbd-4c47-b917-b747ebae7e14.jpeg#crop=0&crop=0&crop=1&crop=1&height=487&id=Jc1JI&originHeight=573&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  当我们加入一些没有统计学差异的样本时，也就是说来源于同一个分布的样本时，它的p值就会大于0.05，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014054-21b3d9ac-cf06-49af-aa3c-b10c6ef5646c.jpeg#crop=0&crop=0&crop=1&crop=1&height=508&id=Ofb8h&originHeight=508&originWidth=670&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=670)             
但是，即使是来源于同一分布的两组数据，有的时候，也会出现p值小于0.05的情况，就像下面的这个样本，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014079-4e2c468d-9ae0-4014-bedd-e4e9cc4544d2.jpeg#crop=0&crop=0&crop=1&crop=1&height=730&id=cWdyR&originHeight=731&originWidth=752&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=751)             
现在我们绘制一个直方图，这个直方图是2000个p值，其中1000个来源于两个不同的分布的两组数据的t检验的p值，另外的1000个是来源于同一个分布的两组数据的t检验的p值，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014059-7725ad87-cb4d-4f66-a3c3-e0cf1844b59c.jpeg#crop=0&crop=0&crop=1&crop=1&height=444&id=cUqDT&originHeight=523&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  从上面的直方图我们可以知道，其中有993个小于0.05的p值，如下所示：          ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014110-c94b963d-6891-41b3-ba5f-47be64638348.jpeg#crop=0&crop=0&crop=1&crop=1&height=470&id=aYQ8T&originHeight=554&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
在这993个小于0.05的p值中，有949个是真阳性（这是由第一组p值构成的，也就是来源于两个不同分布的两组数据的t检验的p值），有44个假阳性的p值（这是由第二组p值构成的，也就是来源于同一个分布的两组数据的t检验的p值），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014133-5aa8fdc4-c396-4f92-ab2a-3351f24e1430.jpeg#crop=0&crop=0&crop=1&crop=1&height=480&id=fOcxH&originHeight=565&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  由于在这些小于0.05的p值中，只有约4%的p值是假阳性（44/993=4.4%），因此我们并不需要FDR校正，但是，如果在实际的分析中，我们并不知道p值的构成，因此就需要进行FDR校正，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014122-906ea2ed-0a52-41db-a225-666131c00dbc.jpeg#crop=0&crop=0&crop=1&crop=1&height=455&id=Xr38v&originHeight=536&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             
我们来看一下，这个数据经过FDR校正后的结果，校正后，有846个p值仍然小于0.05，在这846个数值中，有827个是来源于原来真阳性的949个，所占比例为89%，有19个是假阳性，占846的比例为2%，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014109-ec39b3a4-d6f2-4627-84da-db07afbc3e27.jpeg#crop=0&crop=0&crop=1&crop=1&height=380&id=hqg9w&originHeight=447&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在我们把数据的构成改变一下，让它更像RNA-seq的数据，此时我们增加样本的数目到6000个，其中1000个来源于两个不同的分布，5000个来源于相同的分布，这5000个样本进行t检验，它们的p值有更大的可能性大于0.05，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014087-89c30894-4bf5-4a9d-a6d1-040eeb95645a.jpeg#crop=0&crop=0&crop=1&crop=1&height=374&id=eulY4&originHeight=441&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  绘图出样本t检验的p值直方图，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014103-acaff115-7e20-4338-8fe8-50beb27f2b51.jpeg#crop=0&crop=0&crop=1&crop=1&height=430&id=q5wxf&originHeight=506&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在我们看一下这些p值的分布，其中有1215个p值小于0.05，其中949个p值是真阳性，有266个p值是假阳性，假阳性的比例为22%，此时就需要进行FDR校正，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014103-aaa66799-dbe9-4d68-b8e0-4623fe1a36c0.jpeg#crop=0&crop=0&crop=1&crop=1&height=402&id=W9gGo&originHeight=473&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917) 经过FDR校正，我们发现，只有256个校正后的p值小于0.05，其中250个来源于原来的949个真阳性，其比例为26%，剩下的6个是假阳性，来源于原来256个假阳性，比例为2%，从这个结果我们可以看出来，FDR能够限制假阳性的数目，但是它同时还能减少真阳性的数目，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014154-37651704-c212-45ca-8fd2-4fc333245ca4.jpeg#crop=0&crop=0&crop=1&crop=1&height=442&id=vkgoY&originHeight=520&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
现在我们把样本数目增加到11000，其中1000个来源于两个不同的分布的两组数据，10000个来源于相同的分布的两组数据，现在对这些样本进行t检验，将它们的p值绘制成直方图，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014118-fcaf17b4-e24b-432c-84ef-0ca593886bd8.jpeg#crop=0&crop=0&crop=1&crop=1&height=453&id=omkHQ&originHeight=534&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917) 其中1430个p值小于0.05，跟前面的结果一样，有949个真阳性的p值，但是有481个假阳性的p值，假阳性的比例高达34%（481/1430），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014184-86698b84-d094-4271-a9f0-367a40092057.jpeg#crop=0&crop=0&crop=1&crop=1&height=461&id=g2qmU&originHeight=543&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  经过FDR校正，只有56个p值仍然是小于0.05，其中54个真阳性的p值，2个假阳性的p值，也就是说，原来949个真阳性中，只剩下了54个真阳性，只有原来的6%，而假阳性占到FDR校正后的小于0.05的p值数目的4%，从前面的计算结果可以看出来（2000个样本，6000个样本，11000个样本），每当我们增加样本的检验数目时，通过FDR校正的真阳性的（p小于0.05）数目都会减少，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014167-8ba9ed44-ff6c-46b2-854c-8388a7d4fa88.jpeg#crop=0&crop=0&crop=1&crop=1&height=439&id=s1TJJ&originHeight=517&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  用折线图表示就是下面的这个样子，其中绿色曲线表示的是通过FDR校正后，p值仍然小于0.05的数目，橘黄色的线表示经过FDR校正后，p值仍然小于0.05的假阳性的数目，这张图表说明，无论检验的数目是多少，FDR总能控制假阳性的比例，这在我们的模拟数据中已经得到了很好验证，不过随着检验数目的增多，真阳性的比例却在下降，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014177-6a5baf0a-87a5-4352-b803-774636e8cbc4.jpeg#crop=0&crop=0&crop=1&crop=1&height=450&id=uY5Mj&originHeight=530&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917) 这也说明了，Benjamni-Hochberg方法时行的FDR校正还有很大的改进空间，edgeR和DESeq2都有自己的方法来对前面的模拟检验进行过滤。
## edgeR和DESeq2的过滤
edgeR和DESeq2对检验结果进行过滤的基本思路就是，那些reads数极少的基因提供的信息量有限，可以把它们从数据集中剔除掉。换句话讲，如果这个基因在一个样本中只有1个或2个转录本，在另外一个同样的样本中只有3或4个转录本，那么就很难得到它们的精确reads数，即使这些低reads数的基因有着生物学意义，那么我们也能剔除它们，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014144-a82a9364-e210-4c98-b35f-1f67080c050c.jpeg#crop=0&crop=0&crop=1&crop=1&height=529&id=ogn2Z&originHeight=529&originWidth=850&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=850)
## **edgeR的过滤**
在了解edgeR过滤数据之前，我们先了解另外一个概念，即CPM，CPM的全称是Counts Per Million，它用于校正不同文库之间的由于测序深度造成的差异，edgeR是按照CPM来剔除数据的，它的阈值是1，edgeR会保留那些在2个及2个以上的样本中CPM大于1的基因，剩余的基因就被剔除掉，具体的后面我们会讲到，如下所示：

           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014201-70de65ce-1d62-420b-b710-062a6ba43aac.jpeg#crop=0&crop=0&crop=1&crop=1&height=433&id=JVdGP&originHeight=483&originWidth=1022&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  **CPM**
下图说明了如何计算CPM，流程为：①总reads数除以100万；②用每个样本中的每个基因对应的reads数再除以①中的数字，就是CPM。
总reads数除以100万主要是为了方便计算CPM，否则CPM的数值会非常小，不方便，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014191-676a0cbc-3d32-4182-a59a-d9e25e890836.jpeg#crop=0&crop=0&crop=1&crop=1&height=375&id=kiW8C&originHeight=442&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在我们有了所有样本中的所有基因的CPM值，此时就要保留那些有2个或2个以上样本中，CPM值大于1的基因，剩下的基因除去，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014226-76364b64-e675-4259-9ce5-ab11ab60f2e5.jpeg#crop=0&crop=0&crop=1&crop=1&height=542&id=MgRWH&originHeight=627&originWidth=1061&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在我们看一下如何保留需要的基因，一个基因一个基因地来看：
gene 1，它在kidney 1和kidney 2这两个样本中的CPM值都大于1，因此保留，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014231-2f22c00d-dfbe-4dd5-9dbe-139c555a486f.jpeg#crop=0&crop=0&crop=1&crop=1&height=219&id=IeXeE&originHeight=248&originWidth=1037&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)             再看gene 2，gene2在kidney 1和kidney 2这两个样本中，CPM值都大于1（有一个是等于1），因此我们保留基因2，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014185-6b95831b-b4ad-4825-917c-21e90c8ddd9d.jpeg#crop=0&crop=0&crop=1&crop=1&height=435&id=dE8Vs&originHeight=512&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  再看gene 3，由于gene 3只在一个样本，即liver 2中的CPM值大于1，即使这个值很大，我们也不需要（下图中的这个值是103.3，跟前面视频的数据不一样的，我估计作者在这里主要是为了说明一个问题，即使某个值在一个样本中很大，在其他样本中仍然小于1，也是要剔除这个数据），如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014238-d23335a3-967b-45f1-827c-fc564ba6fea4.jpeg#crop=0&crop=0&crop=1&crop=1&height=599&id=uPif7&originHeight=705&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  再看Gene 4，由于有2个样本的CPM值小于1（可能作者没有算另外两个CPM等于0的样本），因此也要剔除，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014188-efe9c01f-e826-4531-bf96-25c9427ff3ee.jpeg#crop=0&crop=0&crop=1&crop=1&height=557&id=cFYka&originHeight=656&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  再看Gene 5，它在所有的4个样本中CPM值都小于1，因此Gene 5也不用保留，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014241-14e61356-2c59-46b6-895e-a10fbca9c2ee.jpeg#crop=0&crop=0&crop=1&crop=1&height=575&id=eznwZ&originHeight=677&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  再看Gene 6，这个基因在2个样本中CPM值大于1，即使这两个样本不是同一类型的，但我们可以保留这个基因，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014275-1a78a738-b698-4691-84dc-4ba0ab5f88ee.jpeg#crop=0&crop=0&crop=1&crop=1&height=603&id=AOS2V&originHeight=710&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)edgeR的这种方法很简单，但我们要知道，测序深度会影响这个数值，例如如果一个样本中有500万条reads，那么CPm的标准化因子就是500万/100万=5，如果我们有5条reads比对到某个基因上了，那么我们就会知道这个基因是1CPM，即5/5=1CPM，如果我们有800万个基因，那么标准化因子就是80，1CPM=80 reads，这个数值就非常大了，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014259-b510445e-b7e0-4abd-bc49-a4f7da1fdcf4.jpeg#crop=0&crop=0&crop=1&crop=1&height=529&id=CGwuh&originHeight=623&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
换句话讲，有时候，我们也需要一个比较大的CPM阈值了，例如，如果我们的一个样本中有5万条reads（单细胞测序的reads数可能就这么多了），那么它的CPM标准化因子为0.05，即5万/100万=0.05，如果一个基因有一条reads比对上了，那么这个基因的CPM就是20，即1/0.05=20。即使一个基因在生物学水平进行了转录，但是你只能低到一个低的reads数和低的总reads数，它仍然存在着很大的噪音，如下所示：
###            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014273-c31a3767-ab25-4e15-a6a3-347b55a3909a.jpeg#crop=0&crop=0&crop=1&crop=1&height=440&id=MTTTM&originHeight=518&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  **edgeR中CPM阈值的确认**
此时，我们可能面临一个问题：如何找一个很好的阈值（cutoff）？
我们来看一个真实的案例。
这个案例是从别人那里得到的一批真实数据，在这批数据中，每个样本有2200万条reads（8个样本，其中包括4个野生型，4个敲除型）；
在不剔除任何基因的情况下，运行edgeR，得到一批原始的p值；
使用不同的CPM阈值（cutoff）来过滤基因，然后对这些p值进行校正，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014242-fb67586b-2ac1-46b0-94b7-fb24fe84d4db.jpeg#crop=0&crop=0&crop=1&crop=1&height=457&id=WZRUs&originHeight=538&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  此时我们使用不同的CPM阈值来过滤一下基因，然后再校正p值，就是下图所示的内容，其中y轴表示经过FDR校正后，p值仍然小于0.05的基因的数目，x轴表示最小的CPM的阈值，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664261929035-70c79be1-c829-443f-8e54-7078a7de37d3.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u1db0551f&originHeight=760&originWidth=1038&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ue5fe4616-ed5d-4374-a162-12b46a21649&title=)  其中横坐标上的0表示，没有剔除掉任何一个基因，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664261928956-c5bc9f10-7f7f-4266-ae99-0f1e01fef992.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=uc5be0106&originHeight=737&originWidth=967&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=uec8ddd73-b114-4727-9a63-0de94f0d813&title=)  如果我们选择1，也就是Minimum CPM Threshold的值为1（也就是推荐的值），此时FDR小于0.05的基因的数目大概是3400个，在此处的reads数还是比较多的，这说明这个阈值还是比较严格的，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664261929036-3a067014-32b5-4120-a1b7-ef68a75f88a1.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u8a5839f4&originHeight=390&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ubaf135ef-b980-46b8-b638-065b87ab5c8&title=)  如果我们使用一个较低的阈值，我们就会发现，此时FDR小于0.05的值基因数目大概是3600个，比CPM=1时的数目多了约200个，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664261929086-9ac23da8-d10d-405d-9ce9-33d5aa347330.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=udcad1661&originHeight=772&originWidth=1024&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u28da486e-54cc-46ad-b909-ff9ea94f807&title=)             总之，edgeR的主旨就是：仔细选择阈值（cutoff），你需要在计算了p值之后再尝试不同的CPM阈值，如下所示：
### ![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664261929079-f9f8e944-c3dc-4e41-b4f0-fd90429aa093.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u71471827&originHeight=214&originWidth=1059&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u43b46f6e-fe4c-4fdb-8e43-bcea9af3875&title=)
  **DESeq2中CPM阈值的确认**
在确认CPM的阈值方面，edgeR和DESeq2有两点不同。
第一，edgeR计算CPM的阈值时，它会检查每个基因在不同样本中的数值，从而确定保留下来的基因中，至少有2个样本的CPM值大于阈值，在下面的这个案例中，我们就发现，gene 1在kidney 1和kidney 2这2个样本中，它的CPM值都大于1，因此保留gene 1，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262042420-23b08945-3d4c-48ff-8f51-da81585340de.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ue0786660&originHeight=438&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ubc0216dc-1b86-49b4-bc94-8375045db82&title=)
相比之下，DESeq2则是要检查某个基因在所有样本中均一化后的数值的均值，还是以上面的案例说明，如果是DESeq2，它比较的结果就是，这4个样本的平均值都在阈值之上，因此可以保留gene 1，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262069757-8ce0e2a5-cea6-4af2-b047-73504071fcdf.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u4d0cedc3&originHeight=419&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u84df0dba-3147-45a8-8d9a-e9f9e408007&title=)
             此时，你或许会想，如果我使用了DESeq2的方法，那么对于异常值，该如何处理？
看下面的案例，gene 1在kidney 1，kidney 2，liver 1中的CPM都是0，而在liver 2中则是5000，平均值是1250 CPM，按照edgeR的标准，gene 1不会被保留，因此它只有一个样本的CPM大于1，如下所示：
         ![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262089383-c5f180aa-448b-4b6e-8d21-904e4394b4ce.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u51593d17&originHeight=488&originWidth=1059&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ud5421809-9dc6-4e40-8c8b-44bbbb660fd&title=) 但是对于DESeq2来说，gene 1在4个样本中的平均值为1250，它会被DESeq2保留（这种情况下DESeq2无法处理，也就是一个类型中有2个样本），如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262111864-0edfd983-0f9c-4a85-89a4-c959cb315080.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u540f16f8&originHeight=497&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u3ce0ed70-9243-4a6f-902b-1d57c4eaf4c&title=)
但DESeq2本身具备异常值的检测方法，不过这种方法只有在每类别中，有超过2个样本的时候才发挥作用（具体的可以参考这篇文献：Moderated estimation of fold change and dispersion for RNA-seq data with DESeq2）。
下图是分别使用这两种方法（edgeR和DESeq2）对同一批数据进行计算的结果，其中横坐标表示最小CPM阈值，纵坐标表示有显著差异的基因的数目，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262128394-c5d39a8f-ee16-4140-b921-818dbccdfaeb.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u6befd032&originHeight=722&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u3179e0b5-c5fb-43c9-a4db-70f629eb51d&title=)
从中我们可以发现，这两种方法基本上都有在同一区域达到顶点，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262152937-7c64b112-feec-4c09-8f4b-61c199b821c8.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u59830226&originHeight=701&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u8e6d3d66-b7ed-43b7-9ad3-7cdf03a49b2&title=)
这两种方法同时会产生一个相似的阈值，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262184950-0e4a4148-3d4a-423b-8fce-93507a351796.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=uf26e2176&originHeight=674&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u89451bf9-0bf9-4aae-9be1-14bb0e8cde4&title=)             
现在我们看一下这两种方法不同之处，其中一处区别在于x轴，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262184963-338c430b-7ee0-46be-863a-46ddc3707f16.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u55f0b04e&originHeight=733&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ue4ad54f9-3fef-440a-a9cc-ac5a2e2c6cf&title=)             
再看另外一处差异，DESeq2能绘制X轴是百分位数（用于替代min CPM 阈值），Y轴是显著差异基因数目的二维坐标系，如下所示：
![](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664262185120-f4c9e863-329a-4413-9874-48ea2d35f666.jpeg#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ucfc5e8a8&originHeight=642&originWidth=1080&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u4376a82b-d5a6-4ae2-b692-e9fbbce85fc&title=)  根据这种二维坐标图，我们可以看出来，0表示在这个阈值之下的基因是0%，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014313-6dff47c5-ed2f-4868-b8ea-4f6907de8454.jpeg#crop=0&crop=0&crop=1&crop=1&height=569&id=IAOyG&originHeight=670&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  0.2表示在这个阈值之下，有20%的基因，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014321-bed752c4-1fce-4af6-9907-6f35c2851187.jpeg#crop=0&crop=0&crop=1&crop=1&height=547&id=HW2CN&originHeight=644&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  分位数（Quantiles）非常有用，因为我们可以看到，CPMs的计算依赖于测序深度。无论这个文库是800万条reads，还是8000万条reads，10%的基因总是总是小于0.1百分倍数，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014343-4bd13309-d92e-40b1-a4c8-a34dd30045c8.jpeg#crop=0&crop=0&crop=1&crop=1&height=547&id=QwfgM&originHeight=644&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  我们可以选择使用分位数法和最小CPM，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014391-54d31fef-3b75-426f-b1d9-b845bd4f143b.jpeg#crop=0&crop=0&crop=1&crop=1&height=530&id=g86oF&originHeight=624&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  现在看第三处差异，DeSeq2会对这些点进行拟合，找到一曲线，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014768-93299950-c936-4c1a-bf97-55ef40cce9b8.jpeg#crop=0&crop=0&crop=1&crop=1&height=547&id=tZWDc&originHeight=644&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  DESeq2就会找到这条拟合曲线的最大位置处，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014786-f7bafcea-de11-4e96-9c7f-2c98c4f37e3e.jpeg#crop=0&crop=0&crop=1&crop=1&height=676&id=Wx60U&originHeight=781&originWidth=1059&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  阈值就在这条曲线的最大位置处，关送去拟合曲线和原始值之间的标准差，换句话讲，在峰值的噪声范围内，第一个分位数就是CPM的阈值，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014784-fc84c1c7-ae35-4996-910f-9bb627bd3584.jpeg#crop=0&crop=0&crop=1&crop=1&height=493&id=Mj3tQ&originHeight=581&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  如果在这个阈值之上没有原始值，那么就不过滤，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014780-21c11040-009b-4dcc-b4f9-495a864912f4.jpeg#crop=0&crop=0&crop=1&crop=1&height=591&id=pc1lT&originHeight=696&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  至此，我们就知道了edgeR和DESeq2是如何过滤基因的，其中edgeR是保留那些在2个或2个以上样本中，CPM大于最小阈值的基因，而DESeq2则是，保留那些平均CPM大于最小CPM的基因，然后绘制显著基因与分位数的散点图，找到拟合曲线，再用最大值减去噪声，即是阈值，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014849-51836feb-6ffb-409f-93e6-77386f517654.jpeg#crop=0&crop=0&crop=1&crop=1&height=504&id=Pw9LN&originHeight=593&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)  不过现在我们知道，我们可以同时联合使用这两种方法，如下所示：
##            ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014837-0cbe14b1-6cf3-4412-9f69-df4c6a10f192.jpeg#crop=0&crop=0&crop=1&crop=1&height=501&id=GtQEN&originHeight=590&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)
## 建议
如果你使用edgeR，在计算出了p值之后，找到CPM的阈值。在edgeR的基因选择标准方面，使用DESeq2可以很容易地找到找到最优的CPM阈值。
如果你使用DESeq2时，如果在每个分类（例如野生型组和突变型组）只有2个样本，此时要尤其注意异常值，如下所示：
           ![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014920-834e4f39-aa01-4795-a969-ca1a2bfa7d1c.jpeg#crop=0&crop=0&crop=1&crop=1&height=498&id=owXx5&originHeight=586&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=917)

# DESeq2差异分析实战案例
## 包的安装和加载
```
# 包的安装和加载
BiocManager::install("DESeq2")library("DESeq2")
```
## 读入数据
这里我们用的数据是一个原始的counts数据的Excel文件，和上一讲中用的数据一样（想运行案例，文末获取文件）
```
# 读入原始的counts数据
counts <- read.table("gene_counts.xls", sep = "\t", header = T, row.names = 1)
```
导入的数据我们通过head()函数查看前6行。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532014838-ccae3949-6c65-4168-878e-07e4449d7728.png#crop=0&crop=0&crop=1&crop=1&height=272&id=OjX0O&originHeight=272&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
行名A1,A2,A3,B1,B2,B3为样本名，列名是基因名。
## 创建分组
设置实验组别，在DESeq2包的基本原理部分，我们介绍时，有一步需要选择参考样本，在实际分析中，我们可以自己选择参考样本，一般都是对照组作为参考样本，在DESeq2中，对照组是是，control样本，实验组是case。原始数据中有6个样本，对照和实验组各三个。所以我们可以创建一个分组向量。
```
# 创建分组
colData <- data.frame(row.names = c("A1","A2","A3","B1","B2","B3"),                      condition =                        factor(c("control","control","control","case","case","case"),                               levels = c("control","case")))
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532014783-311ef69d-fff8-47b4-90f8-6a644da2afa4.png#crop=0&crop=0&crop=1&crop=1&height=268&id=F4Rth&originHeight=268&originWidth=1054&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1054)
## 构建DESeqDataSet对象
构建DESeqDataSet对象用于分析，colData指定我们的样本信息和分组列表，design = ~ condition表示分组信息安装colData的condition列分组。
```
#构建DESeqDataSet对象
dds <- DESeqDataSetFromMatrix(countData = counts, colData = colData,design = ~ condition)
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612532014796-c6e401e2-6b37-4a8a-94d4-66071bec6465.png#crop=0&crop=0&crop=1&crop=1&height=267&id=U4v2i&originHeight=267&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
## 差异分析
```
# 函数分析差异dds <- DESeq(dds)# 计算标准化因子
sizeFactors(dds)#提取差异表达结果
res <- results(dds)
```
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014787-d34d0ed4-493f-4ab7-9237-6574f17a81f8.jpeg#crop=0&crop=0&crop=1&crop=1&height=508&id=cnSvQ&originHeight=508&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
```
class(res)res <- as.data.frame(res)
```
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014845-9183d62f-0cd9-4238-b4ee-1176d7331f7f.jpeg#crop=0&crop=0&crop=1&crop=1&height=270&id=jRGON&originHeight=270&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
## 结果处理与保存
```
# 添加一列
res <- cbind(rownames(res), res)
# 重命名列名
colnames(res) <- c("gene_id", "baseMean", "log2FoldChange", 
										"lfcSE", "stat", "pval", "padj")
#保存文件到本地
write.table(res, "case-vs-control-all-DESeq2.gene.xls", 
						sep = "\t", col.names = TRUE, row.names = FALSE, 
						quote = FALSE,na = "")
```
## 差异基因筛选
这里和前文edgeR差异分析实战案例差不多，不多解释！
```
# 获取差异基因
resSig <- res[which(res$pval < 0.05 & abs(res$log2FoldChange) > 1),]
resSig[which(resSig$log2FoldChange > 0), "up_down"] <- "Up"
resSig[which(resSig$log2FoldChange < 0), "up_down"] <- "Down"
write.table(resSig, "case-vs-control-diff-pval-0.05-FC-2-DESeq2.gene.xls",  
						sep = "\t", col.names = TRUE, row.names = FALSE, quote = FALSE, na = "")
```
![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1612532014887-da2d2b32-02ab-485e-840b-0459f700e068.jpeg#crop=0&crop=0&crop=1&crop=1&height=211&id=njMf5&originHeight=211&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=0&status=done&style=none&title=&width=1080)
这样我们就可以获取差异表达的基因了，可以用于后面的作图，比如火山图！
案例文件和代码，后台回复：**chip-data-DESeq2**，获取！
好了，关于DESeq2和edgeR包，就介绍到这里！！
# limma包差异表达分析
limma包最初设计用于分析芯片数据，后经扩展也可适用于RNA-seq数据。通过将read count数据转换为log2-counts per million（logCPM），估计均值-方差（mean-variance）关系以确定在线性建模之前每次观察的权重，之后将数据应用于线性建模，并通过经验贝叶斯统计差异基因。
## 包的安装
```
#Bioconductor 安装 limma
BiocManager::install('limma')
 
library(limma)
```
## 读入数据

```
library(TCGAbiolinks)
library(DESeq2)
library(limma)
library(edgeR)

dataPath <- "H:/MedBioInfoCloud/analysis/TCGA/new/processedTCGAdata/TCGA-STAR_Exp/TCGA-LUAD-STARdata.Rdata"


load(dataPath)#STARdata
count <- STARdata[["count"]]

###整理数据
source("H:/MedBioInfoCloud/analysis/TCGA/new/00-fun/filterGeneTypeExpr.R")
count <- filterGeneTypeExpr(expr = count,
                            fil_col = "gene_type",
                            filter = FALSE)
##正常组织样本ID
SamN <- TCGAquery_SampleTypes(barcode = colnames(count)[-c(1:3)],
                              typesample = c("NT","NB","NBC","NEBV","NBM"))

##肿瘤组织样本ID
SamT <- setdiff(colnames(count),SamN)

###去除重复样本
source("H:/MedBioInfoCloud/analysis/TCGA/new/00-fun/del_dup_sample.R")
nor_exp <- del_dup_sample(count[,SamN],col_rename = F)
tur_exp <- del_dup_sample(count[,SamT],col_rename = F)
data <- cbind(nor_exp,tur_exp)
head(data)[,1:3]
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1664263806190-ee6cb3d0-7d3c-47a1-a7b8-f3cdcc38e2c7.png#clientId=u1f6f6f2b-4584-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=149&id=ue665f0eb&name=image.png&originHeight=233&originWidth=1273&originalType=binary&ratio=1&rotation=0&showTitle=false&size=35038&status=done&style=none&taskId=u90cc6823-41cf-4892-93c4-f8e0d11ee1f&title=&width=814.72)
## 设计分组
limma分析需要指定一试验设计矩阵，即样本分组，要保证基因表达矩阵中的样本名称顺序和分组顺序是一一对应的。
```
#试验设计矩阵
#注意要保证表达矩阵中的样本顺序和这里的分组顺序是一一对应的
group <- factor(rep(c('control', 'treat'), each = 5), levels = c('control', 'treat'))
design <- model.matrix(~0+group)
colnames(design) = levels(factor(group))
rownames(design) = colnames(group)
design
```
## 基因表达值标准化（voom标准化）

计数数据（read count）存在不可忽视的均值-方差关系，原始计数表现出随着计数大小的增加而增加的方差，而对数计数则通常表现为均值-方差趋势减小。
limma包中voom()函数用于标准化RNA-Seq或芯片数据。该函数将计数（所有计数加0.5以避免对数取零）转换为logCPM值，之后将logCPM值矩阵进行标准化。通过估计对数计数的均值-方差趋势，然后根据其预测方差为每个观察值分配权重，用于在线性建模过程中使用权重来调整异方差。
```
#voom 标准化，详见 ?norm
norm <- voom(exprSet, design, plot = TRUE)
```
数据标准化后，根据每个基因的平均log2CPM构建线性模型，计算残差，并拟合log2CPM与残差标准差平方根的关系，得到的趋势线（红色平滑曲线）可为样本和基因分配权重。

对于该趋势线，若左侧0起点处所示残差标准差明显偏高，或者0起点处出现上式趋势，则表明数据中存在较多的低表达（low counts数）基因。若觉得它们可能会对后续的计算带来较大的误差，不妨在标准化前手动过滤下。

数据执行标准化后，原本离散程度较大的reads counts矩阵的离散程度降低。
```
#标准化前后数据比较
par(mfrow = c(2, 2))
boxplot(data)
plotDensities(data)
boxplot(norm$E)
plotDensities(norm$E)
```
此外，对于voom()标准化功能，除了像上述这样指定原始的基因表达矩阵外，也可将其应用于edgeR的DGEList对象中实现数据标准化，因此limma也常和edgeR结合使用。
## 差异分析
接下来就是使用标准化后的基因表达数据，通过加权或广义最小二乘法对每个基因拟合线性模型，并通过经验贝叶斯计算出适度的t统计值、F统计值和差异表达值，最后获得差异基因分析结果。
```
##==差异表达分析
#线性拟合，详见 ?lmFit
fit <- lmFit(norm, design, method = 'ls')

#确定比较的两组
#后续将计算标记为 1 的组相对于 -1 的组，基因表达值的上调/下调状态
contrast <- makeContrasts('Tumor-Normal', levels = design)
contrast

#使用经验贝叶斯模型拟合标准误差，详见 ?eBayes
fit2 <- contrasts.fit(fit, contrast)
fit2 <- eBayes(fit2)

qqt(fit2$t, df = fit2$df.prior+fit2$df.residual, pch = 16, cex = 0.2)
abline(0,1)

#p 值校正、提取差异分析结果，详见 ?topTable
diff_gene <- topTable(fit2, number = Inf, adjust.method = 'fdr')
head(diff_gene, 10)
```
