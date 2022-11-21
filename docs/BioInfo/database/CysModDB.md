> 文章来源：[https://mp.weixin.qq.com/s/iZ-qkVnpPf2KrA2HbDzqYA](https://mp.weixin.qq.com/s/iZ-qkVnpPf2KrA2HbDzqYA)
> 
> 公众号：生物信息云

# 1.背景知识
半胱氨酸（Cys）上的硫醇基团可以经历多种翻译后修饰（PTM）， 作为分子开关维持氧化还原稳态并调节一系列生物 活性，包括改变酶促反应、蛋白质-蛋白质相互作用和蛋白质 稳定性。
![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211211552593.png)
半胱氨酸含有具有高亲核性和氧化还原敏感性的硫醇侧链，这使得半胱氨酸对许多反应性分子敏感并产生不同的半胱氨酸PTM类型（CysPTM）。修饰类型根据其特性可分为三类：氧化翻译后修饰（PTM）[1]，脂质PTM [2，3]和代谢物PTM [4]。氧化PTM是指半胱氨酸被活性氧、活性氮、活性硫或谷胱甘肽（GSH）氧化[1]。它包括s-亚硝基化，s-亚硝基化，s-磺酰化，s-磺酰化，s-谷硫磺酰化，s-二硫化和S-过硫化。脂质PTM是指半胱氨酸脂化[3，5]，包括s-棕榈酰化和S-异戊二烯化。代谢物PTM涵盖了由反应性代谢物[6]引起的一系列非酶修饰，例如s-斜锥化，s-琥珀酸和S-羰基化。半胱氨酸残基起多种功能作用，如金属结合、酶活化和结构稳定，半胱氨酸修饰可调节蛋白质结构和功能[7]。已经发现CysPTM与许多疾病有关，如癌症和神经退行性疾病[8，9]。

鉴定蛋白质组上的CysPTM位点是探索其在生物活动中的功能作用的基础。然而，由于CysPTM位点的低丰度和显著的动态变化，在蛋白质组学尺度上直接检测CysPTM位点具有挑战性。与一些容易被抗体富集的PTM类型（例如酪氨酸磷酸化和赖氨酸酰化）不同，CysPTM位点的富集主要基于化学蛋白质组学技术，其中已经发明了各种化学探针[10]。例如，开发了一种名为半胱氨酸反应性磷酸盐标签（CPT）的化学探针用于检测半胱氨酸氧化，在~9400种小鼠蛋白质上鉴定出约34 000个氧化位点[11]。然而，CPT探针无法区分不同的氧化亚型。相比之下，DYn-2亚磺酸探针对s-磺酰化具有特异性，使用该探针从人RKO细胞中鉴定出1105个S-亚磺酰化位点[12]。

随着大量CysPTM站点的确定，已经开发了几个数据库来托管CysPTM信息（例如RedoxDB [13]，dbPTM [14]，dbSNO [15]，dbGSH [16]，SwissPalm [17]和iCysMod [18]）。然而，它们有一些限制。首先，这些数据库涵盖了特定或有限的CysPTM类型。例如，许多新发现的类型（例如s-斜体[19]和S-琥珀[20]）尚未收集。其次，它们包含的信息不足。通常，省略了有关鉴定技术或样品来源的信息，这对于估计PTM数据质量，比较使用不同探针鉴定的PTM谱图以及指导进一步的功能研究至关重要[21]。第三，很少提供可视化浏览器来显示蛋白质序列上的CysPTM位点，或者它们不能用于估计修饰位点对蛋白质功能的潜在影响。总之，缺少一个平台，该平台集成了数据收集，修饰位点和蛋白质的注释以及表征CysPTM位点的分析工具，例如PTM串扰，序列特征及其对蛋白质结构和功能的影响。
# 2.CysModDB数据库
CysModDB的集成平台包含70536个CysPTM位点，这些位点在从原核生物到真核生物的12种生物的21654种蛋白质上实验鉴定。这些站点由12种不同的CysPTM类型组成，与以前的数据库相比，这是最广泛的。CysModDB由五个部分组成：（1）PTM位点注释，包括侧翼区域，样品起源和富集技术，（2）蛋白质注释，涵盖具有突出显示的CysPTM位置，功能区域，亚细胞位置和结构信息的序列，（3）蛋白质途径（Reactome [22]），蛋白质 - 蛋白质相互作用（STRING [23]）和蛋白质PTM（dbPTM [14]），（4）用于预测CysPTM位点的在线计算工具和5）分析工具包，由基因富集分析，调控网络和序列特征研究组成。这五个部分使用定制的图形浏览器和购物篮进行集成。浏览器使用图表来表示具有不同CysPTM类型的修饰位点在蛋白质序列上的分布，CysPTM共现以及这些位点与蛋白质结构和功能区域的映射，这有助于探索修饰位点之间的串扰以及这些位点对蛋白质功能的潜在影响。篮子将选定的蛋白质链接到分析工具包或外部资源，用于分析这些CysPTM的序列特征和串扰。简而言之，CysModDB是一个综合平台，具有手动策划的资源和用于半胱氨酸修饰的分析工具。

# 3.数据库地址

 做相关研究的，赶快用起来！
 https://cysmoddb.bioinfogo.org/
![](https://medbioinfocloud-1251590549.cos.ap-guangzhou.myqcloud.com/notepic202211211524588.png)

# 4.引用
Yanzheng Meng, Lin Zhang, Laizhi Zhang, Ziyu Wang, Xuanwen Wang, Chan Li, Yu Chen, Shipeng Shang, Lei Li, CysModDB: a comprehensive platform with the integration of manually curated resources and analysis tools for cysteine posttranslational modifications, Briefings in Bioinformatics, 2022;, bbac460, https://doi.org/10.1093/bib/bbac460