RNA-seq的counts值，RPM, RPKM, FPKM, TPM 的异同
现在常用的基因定量方法包括：RPM, RPKM, FPKM, TPM。这些表达量的主要区别是：通过不同的标准化方法为转录本丰度提供一个数值表示，以便于后续[差异分析](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651264493&idx=1&sn=2164cc4d202fc081551f8918c8cbd7a4&chksm=841ef190b36978866b9bd71a989960370614bf234453b3bd070a56fbe324deb4ecaea2305923&scene=21#wechat_redirect)。
标准化的主要目的是去除测序数据的技术偏差：测序深度和基因长度。
测序深度：同一条件下，测序深度越深，基因表达的read读数越多。
基因长度：同一条件下，不同的基因长度产生不对等的read读数，基因越长，该基因的read读数越高。
# **Counts值**
对给定的基因组参考区域，计算比对上的read数，又称为raw count（RC）。

计数结果的差异的影响因素：落在参考区域上下限的read是否需要被统计，按照什么样的标准进行统计。
RPM (Reads per million mapped reads)
           ![](https://cdn.nlark.com/yuque/0/2021/webp/1234840/1612327456381-348a7eba-98fc-46c5-89f1-842bad956883.webp#align=left&display=inline&height=117&margin=%5Bobject%20Object%5D&originHeight=138&originWidth=1080&size=0&status=done&style=none&width=918)            
**RPM方法：**10^6标准化了测序深度的影响，但没有考虑转录本的长度的影响。
RPM适合于产生的read读数不受基因长度影响的测序方法，比如miRNA-seq测序，miRNA的长度一般在20-24个碱基之间。
# RPKM/FPKM (Reads/Fragments per kilo base per million mapped reads)
           ![](https://cdn.nlark.com/yuque/0/2021/webp/1234840/1612327456547-72ac595c-f07e-43e5-b5f2-ef515bda83ea.webp#align=left&display=inline&height=86&margin=%5Bobject%20Object%5D&originHeight=101&originWidth=1080&size=0&status=done&style=none&width=918)            
**RPKM/FPKM方法**：10^3标准化了基因长度的影响，10^6标准化了测序深度的影响。FPKM方法与RPKM类似，主要针对双末端RNA-seq实验的转录本定量。在双末端RNA-seq实验中，有左右两个对应的read来自相同的DNA片段。在进行双末端read进行比对时，来自同一DNA片段的高质量的一对或单个read可以定位到参考序列上。为避免混淆或多次计数，统计一对或单个read比对上的参考序列片段（Fragment），来计算FPKM，计算方法同RPKM。
**RPKM/FPKM与RPM的区别：**考虑了基因长度对read读数的影响。
**RPKM与FPKM的区别**：RPKM值适用于单末端RNA-seq实验数据，FPKM适用于双末端RNA-seq测序数据。
RPKM/FPKM适用于基因长度波动较大的测序方法，如lncRNA-seq测序，lncRNA的长度在200-100000碱基不等。
# **TPM (Transcript per million)**
           ![](https://cdn.nlark.com/yuque/0/2021/webp/1234840/1612327456537-2e153026-f935-4d94-8e1d-89404e81eef3.webp#align=left&display=inline&height=110&margin=%5Bobject%20Object%5D&originHeight=110&originWidth=1080&size=0&status=done&style=none&width=1080)            
TPM的计算方法也同RPKM/FPKM类似，首先使用式2计算每个基因的表达值，去除基因长度的影响。随后计算每个基因的表达量的百分比，最后再乘以10^6，TPM可以看作是RPKM/FPKM值的百分比。
直接说事情，我有一个基因A，它在这个样本的转录组数据中被测序而且mapping到基因组了 5000个的reads，而这个基因A长度是10K，我们总测序文库是50M，所以这个基因A的RPKM值是 5000除以10，再除以50，为10. 就是把基因的reads数量根据基因长度和样本测序文库来normalization 。那么它的TPM值是多少呢？这个时候这些信息已经不够了，需要知道该样本其它基因的RPKM值是多少，加上该样本有3个基因，另外两个基因的RPKM值是5和35，那么我们的基因A的RPKM值为10需要换算成TPM值就是 1,000,000 *10/(5+10+35)=200,000，看起来是不是有点大呀，其实主要是因为我们假设的基因太少了，一般个体里面都有两万多个基因的，总和会大大的增加，这样TPM值跟RPKM值差别不会这么恐怖的。
相当于重新标准化的文库，保证每个样本中所有TPM的总和是相同的。
**TPM与RPKM/FPKM的区别**：从计算公式来说，唯一的不同是计算操作的顺序，TPM是先去除了基因长度的影响，而RPKM/FPKM是先去除测序深度的影响，具体可看这篇博文，有计算步骤的详细说明；TPM实际上改进了RPKM/FPKM方法在跨样品间定量的不准确性。
TPM的使用范围与RPKM/FPKM相同。
# 总结
raw count作为原始的read计数矩阵是一个绝对值，而绝对值的特点是规模不同（基因长度、测序深度），不可以比较。进行这些基因标准化方法的目的是将count矩阵转变为相对值，去除技术偏差的影响，使后续的差异分析具有统计学的意义。
           ![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1612327456384-40358485-b080-42bf-8484-207f44081d88.png#align=left&display=inline&height=587&margin=%5Bobject%20Object%5D&originHeight=587&originWidth=613&size=0&status=done&style=none&width=613)
