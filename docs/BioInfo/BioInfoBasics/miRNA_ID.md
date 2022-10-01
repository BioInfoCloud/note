# 
![](https://cdn.nlark.com/yuque/0/2021/gif/1234840/1615612397098-b5f27f54-47eb-474d-8ec2-96bc53c8f7c6.gif#align=left&display=inline&height=76&margin=%5Bobject%20Object%5D&originHeight=76&originWidth=640&size=0&status=done&style=none&width=640)
[**TCGA**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338047035672526848&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**GEO**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1385753371944239106&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**文献阅读**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338481272770953216&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**数据库**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338487030963142656&__biz=MzA4NDAzODkzMA==#wechat_redirect)[** **](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338487030963142656&__biz=MzA4NDAzODkzMA==#wechat_redirect)**| **[**理论知识**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1338473418617946113&__biz=MzA4NDAzODkzMA==#wechat_redirect)
[**R语言**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1337050529440104449&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | **[**Bioconductor**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1369789283514761218&__biz=MzA4NDAzODkzMA==#wechat_redirect)** | 服务器与**[**Linux**](https://mp.weixin.qq.com/mp/appmsgalbum?action=getalbum&album_id=1410264757734817793&__biz=MzA4NDAzODkzMA==#wechat_redirect)

---

![](https://cdn.nlark.com/yuque/0/2021/jpeg/1234840/1615612397077-df598621-69b4-4dad-98d4-ffcab0a35c45.jpeg#align=left&display=inline&height=150&margin=%5Bobject%20Object%5D&originHeight=150&originWidth=600&size=0&status=done&style=none&width=600)

---

![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397190-aaebddc7-2d48-4b7a-89d4-1aecd7d5f74e.png#align=left&display=inline&height=241&margin=%5Bobject%20Object%5D&originHeight=241&originWidth=795&size=0&status=done&style=none&width=795)

---

在前面我有文章介绍过生信中各种ID转换【文章:[**生信中各种ID转换**](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651265466&idx=1&sn=021a10503d338e09abe07b578e734566&chksm=841efdc7b36974d13b7ad95e2272d293089d49adff9b74667bbeed78306328f0a42b0259c030&scene=21#wechat_redirect)】，我们可以通过各种基因注释包来转换各种基因ID，这里给大家介绍一下miRNA注释包：miRBaseVersions.db。这个包是基于miRbase数据库的。
由于数据库不断的增长和变化，miRNA的名称可能在不同的版本中有不同的名称，甚至不再被列为有效的miRNA。这个注释包作为一个存储库，可以用于快速查找成熟的miRNA名称。
如果没有安装包先安装：
```
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("miRBaseVersions.db")
```
如果安装出错，参考下面文章。
[R包安装时安装程序包****时退出的状态不是0，或者版本不适的一种解决方法。](http://mp.weixin.qq.com/s?__biz=MzA4NDAzODkzMA==&mid=2651275325&idx=1&sn=b46a6eeeb46273b68bcf29ab382f37a7&chksm=841ea440b3692d5609777a5496b455400cfe6583021df0d5e20368ddf7b711e482976d048d63&scene=21#wechat_redirect)
我们可以使用使用keytypes这个函数来查看可以检索数据的版本，最新版本是22。键类型“MIMAT”是主表，包含所有支持的miRBase版本的所有记录。以前缀“VW-MIMAT”开头的键类型被称为SQL views。你可以理解为不同的版本，例如，键类型“VW-MIMAT-22.0”是来自“MIMAT”表的SQL views，它只保存来自miRBase版本22.0的记录。
```
keytypes(miRBaseVersions.db)
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397060-9a87e913-51da-42b7-b49f-90f98f0df24b.png#align=left&display=inline&height=187&margin=%5Bobject%20Object%5D&originHeight=187&originWidth=1080&size=0&status=done&style=none&width=1080)
使用columns函数来检索关于你可以在最终输出中检索的变量类型的信息:
```
columns(miRBaseVersions.db)
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397065-c41c3c07-2f27-495c-bfb7-1e6e920a7ac0.png#align=left&display=inline&height=102&margin=%5Bobject%20Object%5D&originHeight=102&originWidth=907&size=0&status=done&style=none&width=907)
keys函数返回指定keytypes的所有可行的key。以下示例检索miRBase版本22.0的所有可能key。
```
head(keys(miRBaseVersions.db, keytype = "VW-MIMAT-22.0"))
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397062-8edb2bbb-0bb0-4b5d-84b2-c6b57eac126f.png#align=left&display=inline&height=118&margin=%5Bobject%20Object%5D&originHeight=118&originWidth=1080&size=0&status=done&style=none&width=1080)
select函数用于提取数据。作为输入值，该函数接受从其他三个函数(键、列和键类型)接收的输出。
例如，要提取关于成熟accession' MIMAT0000092 '的所有信息，我们可以运行以下命令:
```
result <- select(miRBaseVersions.db, 
                keys = "MIMAT0000092", 
                keytype = "MIMAT", 
                columns = "*")
result;
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397093-065f7d54-f493-40d2-9468-1403c25176c6.png#align=left&display=inline&height=464&margin=%5Bobject%20Object%5D&originHeight=464&originWidth=1042&size=0&status=done&style=none&width=1042)
我们可以看到，结果返回了不同miRBase版本中加入的所有miRNA名称。参数columns = "*"表示返回所有列。例如，如果我们只想提取' accession '， ' name '和' version '的字段，我们只需运行以下命令:
```
result <- select(miRBaseVersions.db, 
                keys = "MIMAT0000092", 
                keytype = "MIMAT", 
                columns = c("ACCESSION", "NAME", "VERSION"))
result;
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397085-a83ce74d-6ad1-408c-9741-5928a0b4e1f9.png#align=left&display=inline&height=729&margin=%5Bobject%20Object%5D&originHeight=729&originWidth=811&size=0&status=done&style=none&width=811)
与前面的参数columns = "*"的输出相比，这次只返回选定的列。
当然，除了用注释包以外，我们可从数据库找那个下载所有的miRNA信息文件，下面是地址：
```
ftp://mirbase.org/pub/mirbase/CURRENT/
```
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397104-1b948651-c3c1-4817-8e83-3a34644441a4.png#align=left&display=inline&height=845&margin=%5Bobject%20Object%5D&originHeight=845&originWidth=808&size=0&status=done&style=none&width=808)
下载后打开文件是这样的。这里有很详细的信息，包括序列等。
![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397109-aabe0b61-f733-4e3f-aadd-83ff29382265.png#align=left&display=inline&height=363&margin=%5Bobject%20Object%5D&originHeight=363&originWidth=1080&size=0&status=done&style=none&width=1080)
你可以很清楚的看到一个前体可以对应多个成熟体。好了，关于这个包就介绍到这里了。

---

参考:
【1】.miRBaseVersions.db帮助文档

---


经    典    栏    目



| [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397123-74e1598f-104c-4078-9e4c-2ff79baa096f.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1338047035672526848#wechat_redirect) | [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397239-af9f5668-9291-4a4f-8bb1-577be61d6040.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1385753371944239106#wechat_redirect) |
| --- | --- |
| [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397205-6e3a4252-1a82-4f74-90a9-d15ce75d1219.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1410264757734817793#wechat_redirect) | [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397676-035d97c3-33b8-41c3-8344-28d92f244192.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1369789283514761218#wechat_redirect) |
| [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397618-8788ec70-1e10-4d5d-aa1a-f1fd52794129.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1519504738202025984#wechat_redirect) | [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397646-d4b408a8-292e-4b1b-8ead-8b804eccb875.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1519504738034253825#wechat_redirect) |
| [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397747-ba94b1af-762f-468e-9a61-27f4dc84d25f.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1687484069455986690#wechat_redirect) | [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397709-c29045a3-4fc1-4f7e-b54b-7fc42990e1a3.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1521974159344533507#wechat_redirect) |
| [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397604-e1621675-8845-4b96-b2a3-0bdfac845750.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1715194110111776770#wechat_redirect) | [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397669-c1f6fbef-b59d-49d6-acd6-441f088761e8.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1715194110212440067#wechat_redirect) |
| [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397603-1fecb1e8-dd71-4c35-a4ca-9599f68d4aa6.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1712569781846933508#wechat_redirect) | [![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397628-6ee91d3b-7edf-4099-a48b-579ba57499b2.png#align=left&display=inline&percent=0&size=0&status=done&width=184)](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA4NDAzODkzMA==&action=getalbum&album_id=1338481272770953216#wechat_redirect) |

![](https://cdn.nlark.com/yuque/0/2021/png/1234840/1615612397710-3717bdf8-bb78-4b29-b70d-febe19e95baa.png#align=left&display=inline&height=165&margin=%5Bobject%20Object%5D&originHeight=165&originWidth=715&size=0&status=done&style=none&width=715)




