# **第一章：初识Linux**

# **一.Linux 简介**

Linux 内核最初只是由芬兰人林纳斯·托瓦兹（Linus Torvalds）在赫尔辛基大学上学时出于个人爱好而编写的。

Linux 是一套免费使用和自由传播的类 Unix 操作系统，是一个基于 POSIX 和 UNIX 的多用户、多任务、支持多线程和多 CPU 的操作系统。

Linux 能运行主要的 UNIX 工具软件、应用程序和网络协议。它支持 32 位和 64 位硬件。Linux 继承了 Unix 以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。

# **二.Linux 的发行版**

Linux 的发行版说简单点就是将 Linux 内核与应用软件做一个打包。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/6C2A0099E69FF7938F80694FA55792F1/0)

目前市面上较知名的发行版有：Ubuntu、RedHat、CentOS、Debian、Fedora、SuSE、OpenSUSE、Arch Linux、SolusOS 等。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/1E439FF77D798B17C6AC2AD3A6DA44BB/0)

生信专业我看好多人用的是CentOS，也有用Ubuntu的。我用的是CentOS。

# **三.Linux 安装**

CentOS可以去官网下载最新版本：https://www.centos.org/download/

但通常我们不会自己把电脑安装成Linux系统，毕竟大家都习惯了Windows和苹果系统。学习的时候我们通常会安装虚拟机，安装方法很多，百度或者谷歌一堆文章有介绍，可参考：http://c.biancheng.net/view/714.html

但你也可以通过购买服务器进行学习，市场上有很多云服务器厂商，阿里，腾讯，百度，华为，亚马逊等等。阿里可以免费申请试用半年，当然配制比较低，用来学习够了。大家可以根据自己喜好选择。可以选择阿里或者腾讯。

腾讯云地址：https://cloud.tencent.com/

阿里云地址：https://www.aliyun.com/

亚马逊云、百度云和华为云我没用过，我只用过阿里云和腾讯云，不好评价。阿里云学生可以申请免费使用6个月，腾讯云学生120元可以买一年的，1核2G（50G），可以以120元的价格续费2年，新用户可以99元一年，但续费就不优惠啦，有时候有活动288元3年，后期还有没有活动不清楚，大家可以关注官网，这活动比学生身份还便宜。亚马逊云也可以免费申请试用一年，你可以去申请。

# **四.登录Linux服务器**

这里只介绍登录服务器，就是网页登录，软件工具登录，后期介绍。

## **1. 登录阿里云服务器**

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/5C9E2DD71D3B9F65FE57CED70ED6D392/0)

输入密码，用户名是root，这里先不要管用户名为什么是root。刚购买的服务器，第一次登录需要设置密码。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/543C780044EDA542DF07F134ED95405B/0)

点击确定就登录到了终端。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/7FA8B6F2D55BC6F4805E468943452A6E/0)

## **2. 登录腾讯云服务器**

在购买的服务器实例页面，服务器右侧就会有登录入口。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/F88FB2392A225481AD9290B299FDBC13/0)

点击登录后，这里先点击立即登录。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/B43DC2756EE494DFD0BB701B37A87961/0)       

同样，选择密码登录。

​     ![img](https://qqadapt.qpic.cn/txdocdl/1004417556/81FACB71C068D70D04905A93583C537F/0)       输入相应的信息，就登录啦，腾讯云的密码是在购买后会给你发一个邮件，里面有密码，后面可以自己更改。

![img](https://qqadapt.qpic.cn/txdocdl/1004417556/98EEF28DD2AE8137F74FBEAD85C6E936/0)

参考：https://www.runoob.com/linux/linux-install.html

# **第二章：登录服务器软件**

# **一.登录服务器的软件——MobXterm**

在实际开发或者计算的时候可以使用一些第三方的工具对远程的服务器进行控制。目前常用的Linux远程登录工具有：putty、xshell、secureCRT等等。**我推荐使用MobXterm。**secureCRT其实也是一款很强大的终端工具，但是，它毕竟是收费软件。Putty非常小巧，而且免费，因此也有不少人使用，但Putty真的不好用，不支持标签，开多个会话的话就需要开多个窗口，窗口切换也很不方便。当然还有其它终端工具，比如XShell，XShell6是一款高效专业的实用型免费SSH客户端。XShell5简单强悍，支持标签式的环境，动态端口转发，自定义键的映射关系，用户定义的按钮，VB脚本，显示2字节字符和国际语言支持UNICODE的终端。

**MobaXterm——一款集万千于一身的全能型终端神器**，先说说这款神器的优点：

- 功能十分强大，支持SSH，FTP，串口，VNC，X server等功能；
-  支持标签，切换也十分方便；
-  众多快捷键，操作方便；
-  有丰富的插件，可以进一步增强功能；
- 虽然有收费版，但免费版已经可以让我们装逼装上天……

当然优点、功能远不止这些。

官网下载地址:HYPERLINK https://mobaxterm.mobatek.net/ normalLink https://mobaxterm.mobatek.net/

点击Session，然后选择SSH，输入服务器IP地址。如果你安装的是虚拟机，可在终端输入ifconfig -a ，回车查看。

![img](https://docimg10.docs.qq.com/image/vEuUB0juuTBxuxiP4L0m5g?w=881&h=225)

第一个ens33中的192.168.153.132就是我虚拟机的IP地址。需要注意的是，要用MobaXterm等软件登录虚拟机的话，事先得开机。

自己的服务器的话指定root用户名登录，也可以是普通用户名，后面介绍。端口就是22，这是基于ssh协议的，ssh是协议的一种，我们常见的协议有http/https、ftp、tcp/ip、tcp/upd等等，常见端口有80、3306、21、11211、443等。而ssh协议的端口是22。在Linux中ssh协议的应用最典型的就是我们可以使用终端去连接Linux，这个终端它使用的协议就是ssh协议。这里不深入介绍。

![img](https://qqadapt.qpic.cn/txdocpic/0/23d8eba66d22c3b64590553dea8ae34a/0?_type=png&w=1920&h=1030)

会提示输入密码，密码正确的话，软件会提示，是否保存密码，保存密码，以后就不需要再输入，不保存，以后每次都要输入密码。

![img](https://qqadapt.qpic.cn/txdocpic/0/75d5df9a87543dc94d4e4582ccd28cad/0?_type=png&w=1920&h=1030)

这样我们就登录成功啦。

![img](https://qqadapt.qpic.cn/txdocpic/0/0f4c8be55953acbd0f2f40d045d93a2c/0?_type=png&w=1920&h=1030)

我们在左侧菜单栏就会有不同的服务器列表。

![img](https://qqadapt.qpic.cn/txdocpic/0/f371cca9af5736262c633e63ba473673/0?_type=png&w=1085&h=498)

可以通过右键进行编辑，比如重命名。

![img](https://qqadapt.qpic.cn/txdocpic/0/1c3fa593f2083231f8f4c45df2020eeb/0?_type=png&w=1114&h=746)

该工具的左侧还可以实现数据的传输，所以功能还是挺强大的。当然，MobaXterm上传数据和下载数据不是很方便。

![img](https://qqadapt.qpic.cn/txdocpic/0/2afa547bf765335dcaf548fa27e5e555/0?_type=png&w=312&h=553)

# **二.利用sftp工具实现文件的上传/下载**

我们在生物信息分析过程中经常会进行数据的传输，可能会遇到要往Linux中传输数据文件，我们分析的结果也要传到我们的Windows系统，这个时候可以使用sftp工具实现文件的传输：FileZilla软件就是一个很不错的工具，可以去这里下载：https://www.filezilla.cn/download/client 安装完成打开之后会看到以下的界面：

![img](https://docimg5.docs.qq.com/image/AAli2bh8H4c3WZtmFnwcyQ?w=1920&h=1030)

同样，输入IP地址，用户名，密码，端口填22，点击**快速连接**。连接服务器后界面如下：

![img](https://docimg2.docs.qq.com/image/LX6ta3mh7Aj77tRJR2HXxQ?w=1920&h=1030)

登录之后左右两侧各有一个框，左边显示的本地的文件系统，右侧的显示服务器的文件系统。在左侧的文件上右键“上传”，即可将文件传输到右侧的文件目录中。从Linux到Windows也是一样的。或者直接鼠标拖动也是可以的。也可以创建文件夹。

# **第三章：Linux系统目录结构与基本命令**

# **一.Linux系统目录结构**

linux的文件系统是采用级层式的树状目录结构，在此结构中最上层是根目录“/”，然后在此目录下再创建其它的目录。在linux世界里。一切皆文件。

![img](https://docimg7.docs.qq.com/image/S5Iux5bAZYR6J8LAfZZz5A?w=1600&h=614)

以下是对这些目录的解释：

- /bin：bin是Binary的缩写, 这个目录存放着最经常使用的命令。
- /boot：这里存放的是启动Linux时使用的一些核心文件，包括一些连接文件以及镜像文件。
- /dev ：dev是Device(设备)的缩写, 该目录下存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。
- /etc：这个目录用来存放所有的系统管理所需要的配置文件和子目录。
- /home：用户的主目录，在Linux中，每个用户都有一个自己的目录，一般该目录名是以用户的账号命名的。
- /lib：这个目录里存放着系统最基本的动态连接共享库，其作用类似于Windows里的DLL文件。几乎所有的应用程序都需要用到这些共享库。
- /lost+found：这个目录一般情况下是空的，当系统非法关机后，这里就存放了一些文件。
- /media：linux 系统会自动识别一些设备，例如U盘、光驱等等，当识别后，linux会把识别的设备挂载到这个目录下。
- /mnt：系统提供该目录是为了让用户临时挂载别的文件系统的，我们可以将光驱挂载在/mnt/上，然后进入该目录就可以查看光驱里的内容了。
- /opt： 这是给主机额外安装软件所摆放的目录。比如你安装一个ORACLE数据库则就可以放到这个目录下。默认是空的。
- /proc：这个目录是一个虚拟的目录，它是系统内存的映射，我们可以通过直接访问这个目录来获取系统信息。
- 这个目录的内容不在硬盘上而是在内存里，我们也可以直接修改里面的某些文件，比如可以通过下面的命令来屏蔽主机的ping命令，使别人无法ping你的机器：echo 1 > /proc/sys/net/ipv4/icmp_echo_ignore_all
- /root：该目录为系统管理员，也称作超级权限者的用户主目录。
- /sbin：s就是Super User的意思，这里存放的是系统管理员使用的系统管理程序。
- /selinux：这个目录是Redhat/CentOS所特有的目录，Selinux是一个安全机制，类似于windows的防火墙，但是这套机制比较复杂，这个目录就是存放selinux相关的文件的。
- /srv： 该目录存放一些服务启动之后需要提取的数据。
- /sys：这是linux2.6内核的一个很大的变化。该目录下安装了2.6内核中新出现的一个文件系统 sysfs 。sysfs文件系统集成了下面3种文件系统的信息：针对进程信息的proc文件系统、针对设备的devfs文件系统以及针对伪终端的devpts文件系统。该文件系统是内核设备树的一个直观反映。当一个内核对象被创建的时候，对应的文件和目录也在内核对象子系统中被创建。
- /tmp：这个目录是用来存放一些临时文件的。
- /usr： 这是一个非常重要的目录，用户的很多应用程序和文件都放在这个目录下，类似于windows下的program files目录。
- /usr/bin：系统用户使用的应用程序。
- /usr/sbin：超级用户使用的比较高级的管理程序和系统守护程序。
- /usr/src：内核源代码默认的放置目录。
- /var：这个目录中存放着在不断扩充着的东西，我们习惯将那些经常被修改的目录放在这个目录下。包括各种日志文件。
- /run：是一个临时文件系统，存储系统启动以来的信息。当系统重启时，这个目录下的文件应该被删掉或清除。如果你的系统上有 /var/run 目录，应该让它指向 run。
- 在 Linux 系统中，有几个目录是比较重要的，平时需要注意不要误删除或者随意更改内部文件。
- /etc： 上边也提到了，这个是系统中的配置文件，如果你更改了该目录下的某个文件可能会导致系统不能启动。
- /bin, /sbin, /usr/bin, /usr/sbin: 这是系统预设的执行文件的放置目录，比如 ls 就是在/bin/ls 目录下的。值得提出的是，/bin, /usr/bin 是给系统用户使用的指令（除root外的通用户），而/sbin, /usr/sbin 则是给root使用的指令。
- /var： 这是一个非常重要的目录，系统上跑了很多程序，那么每个程序都会有相应的日志产生，而这些日志就被记录到这个目录下，具体在/var/log 目录下，另外mail的预设放置也是在这里。

参考：https://www.runoob.com/linux/linux-install.html 

# **二.基本命令**

## **1. ls 命令**

用于显示指定工作目录下之内容（列出目前工作目录所含之文件及子目录)，这与你在Windows中进入某个文件夹看一下有什么文件一个意思。下面是常用选项与参数：

- -a 显示所有文件及目录 (. 开头的文件不会列出)
- -l 除文件名称外，亦将文件型态、权限、拥有者、文件大小等资讯详细列出
- -r 将文件以相反次序显示(原定依英文字母次序)
- -t 将文件依建立时间之先后次序列出
- -A 同 -a ，但不列出 "." (目前目录) 及 ".." (父目录)
- -F 在列出的文件名称后加一符号；例如可执行档则加 "*", 目录则加 "/"
- -R 若目录下有文件，则以下之文件亦皆依序列出

\#ls [路径]，表示列出指定路径下的文件夹和文件的名字，如果路径没有指定则列出当前路径下的。

例如：在root用户的家目录中输入：



```
ls /
```





则会看到以下的效果：

![img](https://docimg8.docs.qq.com/image/5EnA7qfLPvCuWo66ziUjrg?w=1211&h=114)

我们查看一下etc目录下有什么文件。



```
 ls /etc/
```





![img](https://docimg5.docs.qq.com/image/Fk6hO5i7uXnh-t1LhL5T8w?w=1485&h=641)

我们带参数使用， ls -l 表示以列表的形式列出指定路径下的文件夹和文件的名字例如：使用 ls –l /etc 的命令列出 /etc 目录中的文件夹和文件信息。



```
 ls -l /etc
```





![img](https://docimg8.docs.qq.com/image/jgg55uK21QDXZeaPP7QEyw?w=793&h=304)

ls -la [路径]，表示以列表的形式列出指定路径下的文件夹和文件名（包含隐藏文件）。例如：在当前用户的家目录中输入ls –la命令可以查看全部的文件夹和文件名，并且包含了隐藏文件（特点是以“.”开头的名字）

![img](https://docimg4.docs.qq.com/image/oijPhpp9i5xV8PXtW9USQw?w=689&h=358)

其他的自己去试试。

## **2. clear 命令**

表示的含义：清空当前屏幕中全部的命令（其实质是没有清空，只不过是顶到上面去了）

语法：#clear

你自己输入一次就知道什么意思了。

## **3. pwd 命令**

作用：打印当前的工作路径（print working directory）。相当于在Windows系统中，你当前所在文件夹的路径，比如：K:\MyWebSite\BioInfoNotes\，在Linux中我们直接输入pwd就可以查看自己当前在哪个目录中。

![img](https://docimg1.docs.qq.com/image/h6vgc0sASHrxs8IyUR-FVw?w=561&h=86)

## **4. cd 命令**

作用：切换目录（change directory）。

语法：



```
#cd 需要切换到的路径
```





路径可以是相对路径，也可以是绝对路径。

相对路径是指，相对于当前工作路径来说；而绝对路径，其实其本质上也可以理解成相对路径，只不过它相对于盘符根目录“/”。

例如：从root用户家目录中切换到 /etc 目录中：

先输入：



```
cd etc
```





![img](https://docimg10.docs.qq.com/image/3XohefpRxaqpu24Kc3wTMg?w=606&h=79)

我们发现会有错误提示，原因就是在当前路径（/root/）下没有etc这个目录，我们前面通过 ls / 查看，知道etc目录在根(/)目录下。

相对路径的写法：



```
cd ../etc
```





![img](https://docimg4.docs.qq.com/image/MmiwetKt3sSSKrLdY8tOSQ?w=554&h=115)

“.”表达式当前目录，“..”表示上一级目录，我们之前是在/root目录下，上一级目录就是 /，所以相对路径就是 “../etc” 。

绝对路径就是从根目录“/”开始写，如果从当前路径（/etc）,我们要切换到/root目录下，命令如下：



```
 cd /root/
```





回到家目录最快的命令是：



```
 cd ~
```





用 “~” 表示，就不需要输入完整路径。

## **5. man命令**

Man表示Manual（手册），在使用Linux的时候因为其中的命令语法太多，太复杂，并不好记，有些时候在使用的时候可能会忘记某个命令的语法，这个时候我们可以去找man。其实就是用man命令查看某个命令的帮助文档。

语法：#man 命令名称

\#man ls 的结果

![img](https://qqadapt.qpic.cn/txdocpic/0/50eb09a2b8f01f7a6076aeb361987bfb/0?_type=png&w=1920&h=808)

在帮助信息中如果想退出，则按下q键就可以了。

## **6. 快捷键**

### **(1) Ctrl + C 和Ctrl + Z**

Ctrl + C 和Ctrl + Z 在Linux中不是复制和撤销，都是中断命令，但是他们的作用却不一样。Ctrl + C 是强制中断程序的执行，进程已经终止。 Ctrl + Z 的是将任务中止（暂停的意思），但是此任务并没有结束，他仍然在进程中他只是维持挂起的状态，用户可以使用fg/bg操作继续前台或后台的任务，fg命令重新启动前台被中断的任务，bg命令把被中断的任务放在后台执行。关于Ctrl + Z先不需要了解太多，知道有这么一个东西就行，后续介绍，这里**知道Ctrl + C就行，就是有时候有些命令一直执行，需要终止，你就直接按Ctrl + C就行啦**。    

### **(2) ctrl+e**

作用：将光标快速的切换到命令行的最后面，e表示end

### **(3) ↑和↓**

作用：用于切换历史命令

### **(4) table 键的使用**

就是一个自动补全功能，比如你要输入命令“cd /root/ ” ，你闲麻烦，你输入“cd /r”以后就直接按 table 键，会给你补全，剩下的就不用输入，减少输入时间。但如果同时有多个r开头的文件，会把这些文件列出来，提示你再输入一部分。我们可以看见有2个r开头的目录文件。

![img](https://docimg8.docs.qq.com/image/Hgm4KFc32rKGZ-AAEh4Afw?w=568&h=77)

这些我们在接着输入一个o，再按table键，后面的就自动补全，不用输入了。

# **第四章：文件/文件夹的基本操作命令**

# **一.文件操作命令**

## **1.创建**

命令：touch

语法：#touch 文件的名字	文件名可以是一个完整的路径

如果后面的参数文件名指定了路径，则表示在指定的路径下创建；如果只是传递一个文件名，则表示在当前目录创建文件。

例如，在当前路径下创建一个文件名字叫bioinfo.txt。

命令：#touch bioinfo.txt

![img](https://docimg5.docs.qq.com/image/njM0inBq0hlYNP_x0ZmEhA?w=502&h=121)

## **2.复制**

命令：cp	（copy）

语法：#cp 需要复制的文件 需要保存的位置

例如：将刚才在root用户家目录中创建的bioinfo.txt文件复制到/data/文件夹目录中

命令：#cp /root/bioinfo.txt /data/bioinfo.txt

![img](https://docimg4.docs.qq.com/image/GpcZpCa-euYfNrNat2j4ng?w=635&h=142)

## **3.移动**

命令：mv	（move）

语法：#mv 需要移动的文件 需要移动到的位置(包含文件名)

选项与参数：

-f ：如果目标文件已经存在，不会询问而直接覆盖；

-i ：若目标文件已经存在时，询问用户是否覆盖

例如：将/data/目录中的bioinfo.txt移动到/root/目录下

命令：



```
mv -i /data/bioinfo.txt /root/bioinfo.txt
```





经过移动操作之后，原先目录下的bioinfo.txt就应不存在了。我们知道/root/目录下就有这个文件，加参数i，就会询问我们是否覆盖，输入y表示覆盖。

![img](https://docimg8.docs.qq.com/image/QLcc71fMMWZ-bWIegd_aWA?w=667&h=175)

## **4. 删除**

命令：rm	（remove）

选项与参数：

-f ：忽略不存在的文件，不显示警告讯息

-i ：在删除会先询问用户

-r ：递归删除文件夹

语法：#rm [-f] 需要删除的文件		-f表示force（强制）

例如：删除/root/目录中的bioinfo.txt文件。

命令：#rm /root/bioinfo.txt

![img](https://docimg3.docs.qq.com/image/Zay_atwqV-TnlUmSHrpwCA?w=547&h=113)

在上述删除过程中，会提示是否删除文件，如果想删除则输入：yes/y；如果不想删除则输入：no/n。

如果不想有上面的删除提示，则删除命令可以写成：#rm -f /root/bioinfo.txt，当然文件我刚刚已经删除了，没有改文件也没有报错。如果不加 -f 就会提示没有改文件。

![img](https://docimg6.docs.qq.com/image/vRAx1mS3gHYrjrU1-VfoUQ?w=650&h=132)

## **5.重命名**

命令：mv

语法：#mv 需要重命名的文件 新的名字

例如：在“/”目录下存在一个bioinfo.txt，现在需要对其进行重命名，将名称改为bioinfonotes.txt。命令如下：



```
mv /root/bioinfo.txt /root/bioinfonotes.txt
```





![img](https://docimg9.docs.qq.com/image/rY4gMt2_EX5l0Nk-Mo8e4Q?w=683&h=192)

重命名命令本质上就是文件的移动命令，将文件移动到原先所在的目录，可以重新命名。

# **二.文件夹的操作**

文件夹的常见操作有：创建、复制、移动、删除、重命名。

## **1.创建**

命令：mkdir（make directory）

语法：#mkdir 需要创建的目录名	（可以是路径也可以是名称）

​	  例如：在当前工作目录下创建一个名为RNASeqData的目录，然后可以在其中创建一个任意文件。

创建文件夹：

![img](https://docimg7.docs.qq.com/image/uNyPqnptC6-pqExdgNE3cg?w=580&h=126)

创建文件夹 BioInfoFiles



```
mkdir BioInfoFiles
```





## **2.复制**

命令：cp	（copy）

语法：#cp –r 需要复制的文件夹 复制到地方（-r表示递归，必须得加上这个参数）

例如：将当前工作路径下的RNASeqData目录复制到/data目录下

不加-r参数的结果：

![img](https://docimg7.docs.qq.com/image/Vtixqa_tWiF4W31vFPlw6w?w=531&h=60)

加上-r参数的结果：

![img](https://docimg6.docs.qq.com/image/APyzpA_ACBg8MkNRQKqrJg?w=547&h=103)

## **3.移动**

命令：mv（move）

语法：#mv 需要移动的目录 移动到的地方

例如：将/data/目录下的RNASeqData目录，移动到当前目录的BioInfoFiles文件夹下（/root/BioInfoFiles）。



```
mv /data/RNASeqData /root/BioInfoFiles
```





![img](https://docimg5.docs.qq.com/image/JnUeEqK0D8RrFq-5G1o6zA?w=635&h=207)

## **4. 删除**

命令：rm（remove）

语法：#rm -rf 需要删除的文件夹名称（-r表示递归删除，-f表示强制不提示）

例如：删除当前目录（/root/）中的RNASeqData目录。



```
[root@VM-0-2-centos ~]# rm -rf RNASeqData/
[root@VM-0-2-centos ~]#
```





## **5.重命名**

命令：mv（move）

语法：#mv 需要重命名的文件夹 新的文件夹名称

​	  例如：将当前目录下的BioInfoFiles目录重命名，新的名字叫做BioInfoData。



```
mv BioInfoFiles BioInfoData
```





![img](https://docimg3.docs.qq.com/image/n4OfOmU8r1Oa56V80hJsug?w=580&h=127)

# **第五章：vim编辑器（重点）**

Vim是Linux下一款编辑器软件，它的地位等同于windows下的notepad（记事本）。其功能上要比windows的记事本要强上很多倍，这个vim在开发行业来说，有一个称号“编辑器中的神器”。

# **一.准备工作**

先将/etc/passwd复制一份，复制到当前的用户工作目录（/root），后期的vim操作都会在这个工作目录下进行修改。



```
#cp /etc/passwd ./passwd
```





![img](https://docimg4.docs.qq.com/image/g7H5Gxl1HEUVESuv22zkbQ?w=638&h=269)

# **二.打开文件**

第一种方式：#vim 需要打开的文件

例如：打开当前目录下的passwd，则命令可以写成



```
#vim ./passwd
```





回车后就打开文件了。

![img](https://docimg2.docs.qq.com/image/-pU5GmolQlLlaE2TBxYv_w?w=1920&h=841)

提示：如果想从文件内容中退出可以输入“:q”，然后回车退出。

第二种方式：#vim +数字 需要打开的文件（打开文件之后快速的将光标定位到数字指定的行）

命令：



```
#vim +6 ./passwd
```





提示：vim默认是不显示行号的，我的会显示，是因为我修改过配制文件，如果你的不显示，想在当前文件中显示出行号可以输入:set nu，然后按下回车就可以显示出行号，如下：

第三种方式：#vim +/字符串 需要打开的文件（打开文件，之后高亮显示/后的字符串）



```
vim +/login ./passwd
```





例如：使用vim打开当前目录下的passwd文件，并且高亮显示“login”

![img](https://docimg7.docs.qq.com/image/RK4yqZriEIxHFUNrijBUmQ?w=1010&h=551)

如果这个时候想在搜索高亮结果中进行光标的快速跳转，可以按下键盘上的“n”（向下切换），或者按下“N”（向上切换）。

如果想去除高亮显示，则可以输入:nohl，按下回车即可。（no highlight）。还有，腾讯云服务器从网页端登录，没有高亮效果。

特别说明：

​		以上三个打开文件的方法，都有一个共同的特点，当打开的文件不存在的时候，它会以新文件的方式进行打开。

# **三.vim的三种模式**

在vim中存在三种模式：命令模式、末行模式、编辑模式。

三个模式之间的相互关系：

![img](https://qqadapt.qpic.cn/txdocpic/0/e66e5fc1737c97d5f08dae32e63d18a8/0?_type=png&w=886&h=499)

默认是命令模式，如果说需要进入到末行模式，则可以在命令模式中按下英文“:”。

## **1.末行模式**

保存语法： 



```
:w	（write）
```





另存语法：



```
:w 文件的路径
```





退出语法：



```
:q（quit）
```





输入:wq，回车保存退出。

提示：有些时候，如果对当前编辑的文档已经进行了修改，但是又不想保存想直接退出，则可以输入:q!，同样也有:wq!。其中的感叹号表示强制的意思。

查找语法（末行模式下）：



```
/字符串
```





对于查找的结果，同样会和打开文件的第三种方式一样，进行高亮显示，可以使用N和n进行上一个和下一个结果的切换。

末行模式下输入/root

![img](https://docimg9.docs.qq.com/image/poHpNMxh1He_9mON7EexIw?w=997&h=864)

替换

第一种情况，语法：



```
:s/需要替换的字符串/替换成的字符串（表示替换当前光标所在的行的第一处符合条件的字符串）
```





如果当前行没有要替换的内容，会有提示，比如光标在第一行，想查找login体会为logout。



```
：s/login/logout
```





就会出现这样的提示：Pattern not found: login

将光标移到第二行，再替换。

![img](https://docimg9.docs.qq.com/image/gpLiOHhb7uhNN4t3Tly7_A?w=1005&h=861)

第二种情况，语法：



```
:s/需要替换的字符串/替换成的字符串/g	（替换光标所在行全部符合条件的地方，g表示global）
```





例如：



```
s/bin/BioInfoNotes/g
```





![img](https://docimg8.docs.qq.com/image/UyUpnLPGzJn2lRiCRCklbw?w=1019&h=861)

第三种情况，语法：



```
:%s/需要替换的字符串/替换成的字符串	（表示替换当前文档中每一行第一个符合条件的地方）
```





例如：%s/bin/BioInfoNotes

![img](https://docimg10.docs.qq.com/image/dM_HBJxLa4ux769keujYLQ?w=1103&h=866)

第四种情况，语法：



```
:%s/需要替换的字符串/替换成的字符串/g	（替换整个文档中全部符合条件的地方）
```





例如：



```
%s/BioInfoNotes/bin/g
```





## **2.命令模式**

编辑模式就是使用vim打开一个文件后的一个默认模式。

**光标移动：**

- 将光标在默认的命令模式中快速的定位到文档的最后一行，可以按下按键G。
- 将光标从命令模式中快速的切换到文档的第一行，可以按下按键gg。
- 将光标快速的定位到当前文档中的指定行，可以输入数字G。
- 将光标以当前行为准，向上或者向下移动指定的行数，可以输入数字↑/↓。

**删除命令：**

- 删除当前行，可以使用按键dd，删除之后下一行上移。
- 删除当前行，下一行不上移，可以按下键盘的按键D，删除之后当前行留空。
- 删除多行，可以使用数字dd，表示以光标所在行为基准，向下删除指定的行数。
- 特别说明：在vim中，删除命令和剪切命令是一样，已经删除的内容可以通过粘贴命令显示出来。

**复制命令：**

- 复制当前行，可以在光标所在的行按下键盘按键yy。
- 复制多行，可以按下数字yy，表示以当前行为准，向下复制指定的行数。
- 复制完成之后可以按下按键p，进行粘贴，粘贴是粘贴在光标所在行的下一行开始。

## **3.编辑模式**

编辑模式中没有什么像之前的命令。需要记住的就是如何进入/退出编辑模式。进入编辑模式，可以按下i键或者a键。a键表示在光标的下一个字符处，after insert。I键表示在光标所在的位置进行编辑，insert。退出编辑模式，按下键盘的esc键就可以退出编辑模式。

# **四.vim知识扩展（重点）**

## **1.默认显示行号**

在一般情况下，vim是默认不显示行号的，我们可以通过在末行模式中输入set nu来让当前文件显示行号。

![img](https://docimg2.docs.qq.com/image/ROcBoDDkwcxByiPyMo5Vkw?w=1043&h=862)

但是在关闭之后再次打开又不会显示行号。如何让vim直接默认显示行号呢？解决办法：

修改vim的配置文件进行配置。Vim的配置文件在当前用户的家目录中（如果没有的话自己创建，文件名字叫做.vimrc）。然后在.vimrc文件中，进入编辑模式，然后输入set nu，输入完毕之后退出保存 。



```
 vim .vimrc
```





## **2.别名机制**

在以后的工作中，我们可能会看到这种情况：我们自己现在使用的清屏命令是clear，可能会看到有些人在使用Linux的清屏命令的时候使用cls。但是我们自己通过命令行输入cls发现会报错。别人使用的就是clear的别名，别名就是cls。

别名是通过别名文件来设置的，别名文件位于当前用户家目录中，文件名叫做.bashrc。在别名文件中设置cls=clear，也就是给clear设置别名。

![img](https://docimg7.docs.qq.com/image/1c2L1qkXJADVko-3AfM2mg?w=640&h=463)



```
vim .bashrc
```





![img](https://docimg2.docs.qq.com/image/i0gbjhXZVPZnwLJ3OzMc6Q?w=513&h=254)

打开文件后，输入：alias cls='clear' ，保存并退出。

![img](https://docimg10.docs.qq.com/image/THcR86qGls1U-FPSHgLliw?w=620&h=251)

设置别名文件之后，需要重新登录之后别名才会生效，因此当前用户需要重新登录：

第一个方法：切换用户；

第二个方法：重新/关机；

当然，还有一种方法，就是直接使用alias命令。

![img](https://docimg7.docs.qq.com/image/gHvcUvjVFQ0khhzxEzTc-A?w=878&h=647)

## **3.异常关闭处理**

当一个文件在vim中进行打开，打开之后没有正常关闭（直接关闭远程窗口），再下一次打开该文件的时候就会提示E325的错误。

![img](https://qqadapt.qpic.cn/txdocpic/0/58effe39d5a61e59a4ed11b3d1413206/0?_type=png&w=769&h=451)

这种问题的处理办法就是删除交换文件，交换文件的名称一般都是在原有的文件名后面加上.swp。比如：rm -f .passwd.swp（是隐藏文件，记得在文件名前加"."）

## **4.重做/撤销**

当文件进行修改之后，如果想撤销/重做，则可以在末行模式中输入:u，来撤销上一步的操作。如果这个时候想取消撤销，可以在命令模式中按下组合键ctrl+r。如果想撤销多步，则可以在末行模式中输入:数字u。

## **5.另一种退出保存方式**

前面学习的保存退出方法叫做:wq。其实在Linux的vim中还支持另外一种保存退出方式，这个方式是在末行模式中输入:x。（千万不要输入大写的x，大写的x表示给当前文档进行加密）。

经典的面试题：

在Linux中:wq退出方式和:x的退出方式有什么区别？

答：在实际开发的时候还是建议使用:x的方式进行退出。这两个方式的区别在于，wq的方式无论文件是否有修改，都会对文件的最后修改时间进行改变；而x方式只有在文件内容真的发生变化了才会去修改文件的最后修改时间。

# **第六章：用户及用户组**

# **一.用户管理**

## **1.添加用户**

命令：useradd

语法：#useradd 用户名

例如：使用当前帐号(root)创建一个新的用户，用户名叫做yunsen。

![img](https://docimg10.docs.qq.com/image/_zHa-z7o__IqpsoaDtD4-Q?w=466&h=104)

所有的用户添加之后都会存储在一个文件中，会存储在passwd文件中，位置位于/etc/passwd

通过打开/etc/passwd文件可以查看到新增的用户。



```
vim /etc/passwd
```





![img](https://docimg10.docs.qq.com/image/iMj4YMnLxqDeQgU8tVc5xw?w=1053&h=576)

关于passwd文件中的每一个段表示的含义

天蓝色：表示用户名；

紫色：x表示密码部分。此段的x并非表示密码是x，而是一个占位符；因为passwd文件是每个用户都有读权限，所以如果将紫色部分直接显示密码肯定是不安全的，所以Linux中密码是单独的存储在另外一个文件中，使用了shadow的技术，将密码等重要信息存储在shadow文件中，文件的位置在/etc/shadow。

前面的红色数字：表示是用户的id；

后面的红色数字：表示用户的用户组id；

蓝色：注释或者说是备注；

绿色：用户对应的家目录位置；

黄色：表示用户所对用的解释器的位置，如果后面是bash则表示该用户可以登录系统，如果是nologin，则表示该用户无法登录操作系统；

## **2.设置密码**

命令：passwd

语法：#passwd 需要设置密码的用户名

例如：将刚才创建好的用户yunsen，给它设置一个密码。

![img](https://docimg5.docs.qq.com/image/X9chzYCw7XO_GWpHb0tTYg?w=624&h=149)

如同使用root账户远程登录一样，在输入密码的时候没有任何的提示，直接输入即可，输入完毕按下回车即可。

## **3.用户编辑**

命令：usermod（user modify）

语法：#usermod 参数 需要修改的用户名

参数说明：

​		在Linux中，经常会用到的用户修改的参数有2个。

​		-l：表示给后面传递的用户修改用户名，语法格式：usermod -l 新的用户名 需要修改的用户名

​		-g：表示给后面传递的用户名修改用户组，语法格式：usermod –g 用户组id 需要修改的用户名

例如：将yunsen用户的用户名，修改成BioInfoNotes。



```
usermod -l BioInfoNotes yunsen
```





![img](https://docimg4.docs.qq.com/image/ZRcT161OqNH8K2OFUtfo3Q?w=630&h=87)

## **4.删除用户**

命令：userdel	（user delete）

语法：#userdel 用户名

例如：删除 BioInfoNotes这个用户。

命令：#userdel  BioInfoNotes

![img](https://docimg10.docs.qq.com/image/lFN7qaTKRPItPPyIn0z-WA?w=498&h=80)

# **二.用户组**

## **1.添加用户组**

命令：groupadd

语法：#groupadd 用户组名

例如：往当前的计算机中添加一个用户组：bioinfogroup

![img](https://docimg5.docs.qq.com/image/eIIVKY93F5axawcisfG2rA?w=460&h=78)

用户组添加完成之后也不会有任何的提示，此时我们可以查看用户组的管理文件，文件名叫做group，位置位于/etc/group。



```
 vim /etc/group
```





![img](https://docimg8.docs.qq.com/image/Ej-27rwMulOarHJ4W-Kkfg?w=693&h=227)

group文件中每个颜色所表达的含义:

天蓝色：表示用户组的名字；

紫色：x表示密码的占位符，但是这个占位符没有意义，真的不存在密码；

红色：用户组的id；

最后的天蓝色：表示当前用户组内的成员名称；

蓝色：表示备注说明；

## **2.用户组编辑**

命令：groupmod	（group modify）

语法：#groupmod 参数 用户组名

参数说明：

​		常规的用户组编辑操作就需要了解用户组的重命名：

​		语法格式：#groupmod -n 新的用户组名 旧的用户组名

例如：给创建好的用户组bioinfogroup进行重命名，新的名字叫BioInfoGroup。



```
groupmod -n BioInfoGroup bioinfogroup
```





![img](https://docimg7.docs.qq.com/image/OLJn4EPA75FdPvY_YGlr3A?w=621&h=60)

不写-n参数会报错提示。

## **3.用户组删除**

命令：groupdel

语法：#groupdel 需要删除的用户组名

删除刚刚创建的用户

![img](https://docimg1.docs.qq.com/image/GqFUHj-jEEJ98HuRw14Jqg?w=462&h=63)

注意：如果这个用户组中存在用户的话，则该用户组是无法直接删除的，如果需要删除的话，则可以先将组内的成员删除掉或者移动到别的组，然后才可以删除当前的用户组。



------

**特别说明：**在Linux中只有超级管理员权限才能对用户和用户组进行设置，其他的用户一律没有权限设置。



------

# **第七章：****文件/文件夹属性设置**

# **一.不同用户之间的切换**

上一章介绍了用户和用户组，没有介绍不同用户之间的切换，这里介绍一下su命令，用来切换用户，其实很简单，命令时【su 用户名】，之前一直都是在root用户下操作，你是root用户，可以切换到任何用户不需要密码，但普通用户切换到其他用户或者root用户，需要输入该用户的密码【有密码的话】。当从root切换到普通用户后，再想切换到root用户时，输入命令【su root】是需要输入密码，如果不想输入密码，可以输入【exit】，免去输入密码的过程。

![img](https://docimg8.docs.qq.com/image/cMBIvzdOVc72o3npQ0QC2A?w=563&h=102)

# **二.权限介绍**

权限设置主要是针对用户和用户组对于文件/文件夹的一个操作限制，只有有权限才能进行相应的设置，没有权限则设置不了。在Linux中如何去查看一个文件/文件夹的权限呢？这可以通过命令【ls -l】来查看权限的信息。

例如：使用ls查看当前工作路径下的文件夹/文件权限信息。

![img](https://docimg10.docs.qq.com/image/XL4RieVSVXoNagPKc0mT2A?w=681&h=521)

上述图中红色的区域就是权限的组成情况。

权限信息中的字符分别表示什么意思：

![img](https://qqadapt.qpic.cn/txdocpic/0/7d3c4611f4d74cd21afcdad7cdc8e785/0?_type=png&w=877&h=386)

![img](https://qqadapt.qpic.cn/txdocpic/0/b92fd1bd0827b6bd22a9c6582eda8bc7/0?_type=png&w=451&h=200)

第0个字符：表示文档的类型，d表示是目录，-表示是文件；

第1~3个字符：表示文件所有者的权限情况（u表示，user）；

第4~6个字符：表示所有者同组的组内成员的权限情况（g表示，group）；

第7~9个字符：表示除上述两类人员的其他用户的权限情况（o表示，other）；

# **三.修改权限**

## **1.通过字符形式设置权限**

命令：chmod

语法：#chmod 权限组成信息 需要操作的对象（文件夹/文件）

需要注意，如果操作的对象是文件夹，则需要加上-r参数，表示递归赋予权限。

权限的组成信息，将语法进行拆分：

第一个情况：针对单个对象（ugo）的拆分

​	给某个组成部分添加读权限：#chmod u+r,g+r,o+r 需要操作的文件/文件夹。

我首先创建一个RNASeq-Counts.txt文件，



```
[root@VM-0-2-centos ~]# touch RNASeq-Counts.txt
[root@VM-0-2-centos ~]# ls -l
total 8
drwxr-xr-x 3 root root 4096 Oct 27 20:41 BioInfoData
-rw-r--r-- 1 root root    0 Oct 27 20:25 bioinfonotes.txt
-rw-r--r-- 1 root root 1371 Oct 31 13:32 passwd
-rw-r--r-- 1 root root    0 Nov  5 20:12 RNASeq-Counts.txt
```





RNASeq-Counts.txt文件对于组合其他用户没有w权限，尝试设置一下。



```
[root@VM-0-2-centos ~]# chmod g+w o+w RNASeq-Counts.txt
chmod: cannot access ‘o+w’: No such file or directory
[root@VM-0-2-centos ~]# 
```





o+w没有发生改变，是因为我没有在中间加","号。换个文件改一下。



```
[root@VM-0-2-centos ~]# chmod g+w,o+w RNASeq-Counts.txt
[root@VM-0-2-centos ~]# ls -l
total 8
drwxr-xr-x 3 root root 4096 Oct 27 20:41 BioInfoData
-rw-r--r-- 1 root root    0 Oct 27 20:25 bioinfonotes.txt
-rw-r--r-- 1 root root 1371 Oct 31 13:32 passwd
-rw-rw-rw- 1 root root    0 Nov  5 20:12 RNASeq-Counts.txt
[root@VM-0-2-centos ~]# 
```





切换到普通用户[yunsen]，在普通用户家目录下创建RNASeq-Counts.txt 文件。



```
[root@VM-0-2-centos ~]# su yunsen
[yunsen@VM-0-2-centos root]$ cd ~
[yunsen@VM-0-2-centos ~]$ touch RNASeq-Counts.txt
[yunsen@VM-0-2-centos ~]$ ls -l
total 0
-rw-rw-r-- 1 yunsen yunsen 0 Nov  5 20:21 RNASeq-Counts.txt
```





![img](https://docimg10.docs.qq.com/image/sWxpvf_8fTZJ3Q02dbqCvg?w=675&h=171)

给其他用户添加w权限，用普通用户操作，切换到root用户，查看没有问题。

![img](https://docimg5.docs.qq.com/image/_RkvOVvHL36hGqjqOU7KhQ?w=702&h=328)

再给用户组和其他人添加x权限，能正常添加。修改root家目录下的文件就没有权限。

![img](https://docimg7.docs.qq.com/image/hzL2eGBBJUbXyVuYJ7sVUQ?w=721&h=213)

第二个情况：设置全部的组成部分：

​	可以使用下面的这个语法：

​	#chmod a+r 文件		（表示给全部的组成部分添加读权限）

​	#chmod a-r 文件		（表示给全部的组成部分删减读权限）

​	#chmod a=rwx 文件	（表示给全部的组成部分权限设置成刻度可行可执行）

其中a表示全部（ugo组合）

![img](https://docimg10.docs.qq.com/image/ve7tGv-Bb-ZyBXK6kK-tXQ?w=755&h=195)

## **2.通过数字的形式来设置权限**

在Linux权限体系中支持使用数字的形式来表示权限的信息，比如说777表示全部的权限。

- 4表示读权限
- 2表示写权限
- 1表示执行权限

例如：如果说我想把RNASeq-Counts.txt 这个文件的权限设置成所有者拥有全部权限，同组用户拥有读写权限，其他用户拥有读权限，则数字形式该写成？

全部权限=读+写+执行=4+2+1=7

读写权限=读+写=4+2=6

读权限=4

所以最终的权限数字应该是764。

![img](https://docimg2.docs.qq.com/image/UHGt3AK8j3SIenMxXc_5LQ?w=693&h=200)

# **四.更改文件属性**

## **1.chgrp更改文件数组**

语法：chgrp [-R] 属组名 文件名

参数选项

-R：递归更改文件属组，就是在更改某个目录文件的属组时，如果加上-R的参数，那么该目录下的所有文件的属组都会更改。

![img](https://docimg9.docs.qq.com/image/loxhISxv98PzJx1cWWmzrw?w=803&h=351)

## **2.chown更改文件属主**

chown：更改文件属主，也可以同时更改文件属组

语法：



```
chown [-R] 属主名 文件名
chown [-R] 属主名：属组名 文件名
```





![img](https://docimg2.docs.qq.com/image/cpy0XvFfA3x4ndgY4FfKIg?w=789&h=334)



------

**友情提示：**在以后实际工作不要出现一个奇葩的权限：-wx。不要出现类似这样的权限，原因是读权限是最基本的，而你如果想写入，则必须先打开文件。

# **第八章：文件系统与文件压缩**

# **一.Linux的文件系统**

文件系统就是操作系统（比如windows）管理和存储文件的软件机构。文件系统指文件存在的物理空间。通俗地说，没有文件系统，系统就不知道该怎么读取硬盘。文件系统的种类有很多，每一种文件系统的结构，逻辑，存取速度，灵活性，安全性，大小，等等都不一样。文件系统可以被使用在磁带，移动硬盘，闪存等地方。在Linux系统中，每个分区都是一个文件系统，都有自己的目录层次结构。Linux的最重要特征之一就是支持多种文件系统，这样它更加灵活，并可以和许多其它种操作系统共存。Virtual File System（虚拟文件系统）使得Linux可以支持多个不同的文件系统。由于系统已将Linux文件系统的所有细节进行了转换，所以Linux核心的其它部分及系统中运行的程序将看到统一的文件系统。Linux的虚拟文件系统允许用户同时能透明地安装许多不同的文件系统。虚拟文件系统是为Linux用户提供快速且高效的文件访问服务而设计的。总之，文件系统的类别有很多，也很复杂，又想弄明白文件系统的原理，需要学习的东西有很多，这里我只介绍Linux中几种文件系统格式。

随着Linux的不断发展，它所支持的文件格式系统也在迅速扩充。特别是Linux 2.4内核正式推出后，出现了大量新的文件系统，其中包括日志文件系统ext3、ReiserFS、XFSJFS和其它文件系统。Linux系统核心可以支持十多种文件系统类型：JFS、 ReiserFS、ext、ext2、ext3、ISO9660、XFS、Minx、MSDOS、UMSDOS、VFAT、NTFS、HPFS、NFS、 SMB、SysV、PROC等。

文件系统指文件存在的物理空间。在Linux系统中，每个分区都是一个文件系统，都有自己的目录层次结构。Linux的最重要特征之一就是支持多种文件系统，这样它更加灵活，并可以和许多其它种操作系统共存。Virtual File System（虚拟文件系统）使得Linux可以支持多个不同的文件系统。由于系统已将Linux文件系统的所有细节进行了转换，所以Linux核心的其它部分及系统中运行的程序将看到统一的文件系统。Linux的虚拟文件系统允许用户同时能透明地安装许多不同的文件系统。虚拟文件系统是为Linux用户提供快速且高效的文件访问服务而设计的。

随着Linux的不断发展，它所支持的文件格式系统也在迅速扩充。特别是Linux 2.4内核正式推出后，出现了大量新的文件系统，其中包括日志文件系统ext3、ReiserFS、XFSJFS和其它文件系统。Linux系统核心可以支持十多种文件系统类型：JFS、 ReiserFS、ext、ext2、ext3、ISO9660、XFS、Minx、MSDOS、UMSDOS、VFAT、NTFS、HPFS、NFS、 SMB、SysV、PROC等。

下面介绍Linux下几个最常用的文件系统，其中包括ext、ext2、ext3、JFS、XFS、ReiserFS等。

## **1.ext**

ext是第一个专门为开发的Linux的文件系统类型，叫做扩展文件系统。它是1992年4月完成的，对Linux早期的发展产生了重要作用。但是，由于其在稳定性、速度和兼容性上存在许多缺陷，现在已经很少使用了。

## **2.ext2**

ext2是为解决ext文件系统的缺陷而设计的可扩展的、高性能的文件系统，它又被称为二级扩展文件系统。ext2是1993年发布的，设计者是Rey Card。它是Linux文件系统类型中使用最多的格式，并且在速度和CPU利用率上较为突出，是GNU/Linux系统中标准的文件系统。它存取文件的性能极好，对于中、小型的文件更显示出优势，这主要得益于其簇快取层的优良设计。ext2可以支持256字节的长文件名，其单一文件大小和文件系统本身的容量上限与文件系统本身的簇大小有关。在常见的Intel x86兼容处理器的系统中，簇最大为4KB，单一文件大小上限为2048GB, 而文件系统的容量上限为6384GB。尽管Linux可以支持种类繁多的文件系统，但是2000年以前几乎所有的Linux发行版都使用ext2作为默认的文件系统。　

ext2也有一些问题。由于它的设计者主要考虑的是文件系统性能方面的问题，而在写入文件内容的同时，并没有写入文件的meta- data（和文件有关的信息，例如权限、所有者及创建和访问时间）。换句话说，Linux先写入文件的内容，然后等到有空的时候才写入文件的meta- data。如果出现写入文件内容之后，但在写入文件的meta-data之前系统突然断电，就可能造成文件系统就会处于不一致的状态。在一个有大量文件操作的系统中，出现这种情况会导致很严重的后果。另外，由于目前Linux的 2.4内核所能使用的单一分割区最大只有2048GB，尽管文件系统的容量上限为6384G，但是实际上能使用的文件系统容量最多也只有2048GB。

## **3.ext3**

在讲解ext3、JFS、XFS、ReiserFS日志格式文件系统之前，先介绍一些日志式文件系统基础。

日志式文件系统起源于Oracle、Sybase等大型数据库。由于数据库操作往往是由多个相关的、相互依赖的子操作组成，任何一个子操作的失败都意味着整个操作的无效性，对数据库数据的任何修改都要恢复到操作以前的状态。Linux日志式文件系统就是由此发展而来的。日志文件系统通过增加一个叫做日志的、新的数据结构来解决这个“fsck”问题。这个日志是位于磁盘上的结构。在对元数据做任何改变以前，文件系统驱动程序会向日志中写入一个条目，这个条目描述了它将要做些什么，所以日志文件具有可伸缩性和健壮性。在分区中保存日志记录文件好处是：文件系统写操作首先是对记录文件进行操作，若整个写操作由于某种原因(如系统掉电)而中断，则在下次系统启动时就会读日志记录文件的内容，恢复到没有完成的写操作，这个过程一般只需要两三分钟时间。

ext3是由开放资源社区开发的日志文件系统，早期主要开发人员是Stephen Tweedie。ext3被设计成是ext2的升级版本，尽可能方便用户从ext2向ext3迁移。ext3在ext2的基础上加入了记录元数据的日志功能，努力保持向前和向后的兼容性，也就是在保有目前ext2的格式之下再加上日志功能。和ext2相比，ext3提供了更佳的安全性，这就是数据日志和元数据日志之间的不同。ext3是一种日志式文件系统，日志式文件系统的优越性在于由于文件系统都有快取层参与运作，如不使用时必须将文件系统卸下，以便将快取层的资料写回磁盘中。因此，每当系统要关机时，必须将其所有的文件系统全部卸下后才能进行关机。如果在文件系统尚未卸下前就关机 (如停电)，那么重开机后就会造成文件系统的资料不一致，故这时必须做文件系统的重整工作，将不一致与错误的地方修复。然而，这个过程是相当耗时的，特别是容量大的文件系统不能百分之百保证所有的资料都不会流失，特别在大型的服务器上可能会出现问题。除了与ext2兼容之外，ext3还通过共享ext2的元数据格式继承了ext2的其它优点。比如，ext3用户可以使用一个稳固的fsck工具。由于ext3基于ext2的代码，所以它的磁盘格式和ext2 的相同，这意味着一个干净卸装的ext3文件系统可以作为ext2文件系统毫无问题地重新挂装。如果现在使用的是ext2文件系统，并且对数据安全性要求很高，这里建议考虑升级使用ext3。

ext3最大的缺点是，它没有现代文件系统所具有的、能提高文件数据处理速度和解压的高性能。此外，使用ext3文件系统要注意硬盘限额问题，在这个问题解决之前,不推荐在重要的企业应用上采用ext3＋Disk Quota（磁盘配额）。  

## **4.JFS** 

JFS是一种提供日志的字节级文件系统。该文件系统主要是为满足服务器（从单处理器系统到高级多处理器和群集系统）的高吞吐量和可靠性需求而设计、开发的。JFS文件系统是为面向事务的高性能系统而开发的。在IBM的AIX系统上，JFS已经过较长时间的测试，结果表明它是可靠、快速和容易使用的。 2000年2月，IBM宣布在一个开放资源许可证下移植Linux版本的JFS文件系统。JFS也是一个有大量用户安装使用的企业级文件系统，具有可伸缩性和健壮性。与非日志文件系统相比，它的突出优点是快速重启能力，JFS能够在几秒或几分钟内就把文件系统恢复到一致状态。虽然JFS主要是为满足服务器（从单处理器系统到高级多处理器和群集系统）的高吞吐量和可靠性需求而设计的，但还可以用于想得到高性能和可靠性的客户机配置，因为在系统崩溃时JFS能提供快速文件系统重启时间，所以它是因特网文件服务器的关键技术。使用数据库日志处理技术，JFS能在几秒或几分钟之内把文件系统恢复到一致状态。而在非日志文件系统中，文件恢复可能花费几小时或几天。

JFS的缺点是，使用JFS日志文件系统性能上会有一定损失，系统资源占用的比率也偏高，因为当它保存一个日志时，系统需要写许多数据。

## **5.ReiserFS**

ReiserFS的第一次公开亮相是在1997年7月23日，Hans Reiser把他的基于平衡树结构的ReiserFS文件系统在网上公布。ReiserFS 3.6.x（作为Linux 2.4一部分的版本）是由Hans Reiser和他的Namesys开发组共同开发设计的。SuSE Linux也对它的发展起了重大的帮助。Hans和他的组员们相信最好的文件系统是能够有助于创建独立的共享环境或命名空间的文件系统，应用程序可以在其中更直接、有效和有力地相互作用。为了实现这一目标，文件系统就应该满足使用者对性能和功能方面的需要。那样使用者就能够继续直接地使用文件系统，而不必建造运行在文件系统之上（如数据库之类）的特殊目的层。ReiserFS 使用了特殊的、优化的平衡树（每个文件系统一个）来组织所有的文件系统数据，这为其自身提供了非常不错的性能改进，也能够减轻文件系统设计上的人为约束。另一个使用平衡树的好处就是，ReiserFS 能够像其它大多数的下一代文件系统一样，根据需要动态地分配索引节，而不必在文件系统创建时建立固定的索引节。这有助于文件系统更灵活地适应面临的各种存储需要，同时提供附加的空间有效率。

ReiserFS被看作是一个更加激进和现代的文件系统。传统的Unix文件系统是按磁盘块来进行空间分配的，对于目录和文件等的查找使用了简单的线性查找。这些设计在当时是合适的，但随着磁盘容量的增大和应用需求的增加，传统文件系统在存储效率、速度和功能上已显得落后。在 ReiserFS的下一个版本-Reiser 4，将提供了对事务的支持。ReiserFS突出的地方还在于其设计上着眼于实现一些未来的插件程序，这些插件程序可以提供访问控制列表、超级链接，以及一些其它非常不错的功能。在http://www.namesys.com/v4/v4.html中，有Reiser 4的介绍和性能测试。

ReiserFS一个最受批评的缺点是，每升级一个版本都将要将磁盘重新格式化一次，而且它的安全性能和稳定性与ext3相比有一定的差距。因为 ReiserFS文件系统还不能正确处理超长的文件目录，如果创建一个超过768字符的文件目录，并使用ls或其它echo命令，将有可能导致系统挂起。在http://www.namesys.com/ ;网站可以了解关于ReiserFS的更多信息。

## **6.XFS**

XFS是一种非常优秀的日志文件系统，它是由SGI于20世纪90年代初开发的。XFS推出后被业界称为先进的、最具可升级性的文件系统技术。它是一个全 64位、快速、稳固的日志文件系统，多年用于SGI的IRIX操作系统。当SGI决定支持Linux社区时，它将关键的基本架构技术授权于Linux，以开放资源形式发布了他们自己拥有的XFS的源代码，并开始进行移植。此项工作进展得很快，目前已进入beta版阶段。作为一个64位文件系统，XFS可以支持超大数量的文件（9000×1GB），可在大型2D和3D数据方面提供显著的性能。XFS有能力预测其它文件系统薄弱环节，同时提供了在不妨碍性能的情况下增强可靠性和快速的事故恢复。

XFS可为Linux和开放资源社区带来如下新特性：

◆可升级性 XFS被设计成可升级，以面对大多数的存储容量和I/O存储需求；可处理大型文件和包含巨大数量文件的大型目录，以满足21世纪快速增长的磁盘需求。 XFS有能力动态地为文件分配索引空间，使系统形成高效支持大数量文件的能力。在它的支持下，用户可使用的文件远远大于现在最大的文件系统。

◆优秀的I/O 性能典型的现代服务器使用大型的条带式磁盘阵列，以提供达数GB/秒的总带宽。XFS可以很好地满足I/O请求的大小和并发I/O请求的数量。XFS可作为 root文件系统，并被LILO支持，也可以在NFS服务器上使用，并支持软件磁盘阵列（RAID）和逻辑卷管理器（Logical Volume Manager,LVM）。SGI最新发布的XFS为1.0.1版，在http://oss.sgi.com/projects/XFS/ ;可以下载它。

由于XFS比较复杂，实施起来有一些难度（包括人员培训等），所以目前XFS主要应用于Linux企业应用的高端。

## **7.ext4**

第4个扩展文件系统，是下一代的日志文件系统，它与上一代文件系统ext3是向后兼容的。ext4 在性能、伸缩性和可靠性方面进行了大量改，支持 1 EB 的文件系统。ext4 是由 Theodore Tso（ext3 的维护者）领导的开发团队实现的，并引入到 2.6.19 内核中。Ubuntu9.04开始支持Ext4文件系统。

参考：https://www.cnblogs.com/luoahong/p/6242058.html 

# **二.文件解压缩相关命令**

## **1.概述**

在Linux下面有相当多的压缩命令可以运行，这些压缩命令可以让我们更方便地从网络上面下载容量较大的文件。此外，我们知道在Linux下面，扩展名没有什么特殊的意义。 不过，针对这些压缩命令所产生的压缩文件，为了方便记忆，还是会有一些特殊的命名方式，就让我们来看看吧！

什么是文件压缩呢？我们稍微谈一谈它的原理，目前我们使用的计算机系统中都是使用所谓的字节单位来计量。不过，事实上，计算机最小的计量单位应该是bit才对，此外，我们也知道 1字节=8比特(1Byte=8bit),但是如果今天我们只是记录一个数字，即1这个数字，它会如何记录？假设一个字节可以看成下面的模样：

![img](https://qqadapt.qpic.cn/txdocpic/0/94f49c0da9f7a31017a3382b0f36a9b2/0?_type=png&w=1030&h=206)

由于 1Byte=8bit，所以每个字节当中会有8个空格，而每个空格只可以是0、1

由于我们记录的数字是1，考虑计算机所谓的二进制，如此一来，1会在最右边占据1个位，而其他的7个位将会自动地被填上0。如下图所示：

![img](https://qqadapt.qpic.cn/txdocpic/0/b8466317ff05d16f3b13c994d84631a1/0?_type=png&w=918&h=222)

你看看，其实在这样的例子中，那7个位应该是空的才对。不过，为了要满足目前我们的操作系统数据的读写，所以就会将该数据转为字节的形式来记录。而一些聪明的计算机工程师就利用一些复杂的计算方式，将这些没有使用到的空间【丢】出来，以让文件占用的空间变小，这就是压缩的技术。

另一种压缩技术也很有趣，它是将重复的数据进行统计记录。举例来说，如果你的数据为【111······】共有100个1时，那么压缩技术会记录为【100个1】而不是真的有100个1的位存在。这样也能够精简文件记录的容量，非常有趣吧！

简单地说，你可以将它想成，其实文件里面有相当多的空间存在，并不是完全填满的，而压缩技术就是将这些空间填满，以让整个文件占用的容量下降。不过，这些压缩过的文件并无法直接被我们的操作系统所使用，因此，若要使用这些被压缩过的文件数据，则必须将它还原回未压缩前的模样，那就是所谓的解压缩。而至于压缩后与压缩的文件所占用的磁盘空间大小，就可以被称为是压缩比。

这个压缩与解压缩的操作有什么好处呢？最大的好处就是压缩过的文件容量变小了，所以你的硬盘无形之中就可以容纳更多的数据。此外，在一些网络数据的传输中，也会由于数据量的降低，好让网络带宽可以用来做更多的工作，而不是老卡在一些大型文件传输上面。

## **2.Linux系统常见压缩命令**

在Linux的环境中，压缩文件的扩展名大多是: *.tar、*.tar.gz、*.gz、*.Z、*.bz2、*.xz。为什么会有这样的扩展名？不是说Linux的扩展名没有什么作用吗？

这是因为Linux支持的压缩命令非常多，且不同的命令所用的压缩技术并不相同，当然彼此之间可能就无法互通/解压缩文件。所以，当你下载到某个文件时，自然就需要知道该文件是由哪种压缩命令所制作出来的，好用来对照对照着解压缩，也就是说，虽然Linux文件的属性基本上是与文件名没有绝对关系的，但是为了帮助我们人类小小的脑袋，所以适当的扩展名还是必要的，下面我们就列出几个常见的压缩文件扩展名:

*.gz         gzip程序压缩的文件

*.bz2        bzip2程序压缩的文件

*.xz         xz程序压缩的文件

*.zip        zip程序压缩的文件

*.Z          compress程序压缩的文件

*.tar        tar程序打包的文件，并没有压缩过

*.tar.gz     tar程序打包的文件，并且经过gzip的压缩

*.tar.bz2    tar程序打包的文件，并且经过bzip2的压缩

*.tar.xz     tar程序打包的文件，并且经过xz的压缩

Linux常见的压缩命令就是gzip、bzip2以及最新的xz，至于compress已经不流行了。为了支持windows常见的zip，其实Linux也早就有zip命令了。gzip是由GNU计划所开发出来的压缩命令，该命令支持已经替换了compress。后台GNU又开发出了bzip2及xz这几个压缩比更好的压缩命令。不过，这些命令通常仅能针对一个文件来压缩与解压缩，如此一来，每次压缩与解压缩都要一大堆文件，岂不烦人？此时，这个所谓的【打包软件,tar】就显得很重要。

这个tar可以将很多文件打包成一个文件，甚至是目录也可以这么玩。不过，单纯的tar功能仅仅是打包而已，即将很多文件结合为一个文件，事实上，它并没有提供压缩的功能，后台，GNU计划中，将整个tar与压缩的功能结合在一起，如此一来，提供用户更方便且更强大的压缩与打包功能，下面我们就来谈一谈这些在Linux下面基本的压缩命令。案列文件我上传人的基因组注释文件，下载地址:https://www.gencodegenes.org/human/ 

![img](https://docimg3.docs.qq.com/image/9rT-21GT7iOTN6JXSqZz9g?w=1898&h=848)

下载后利用FileZilla软件上传到服务器，我这里上传到/root/BioInfoData 目录中，下载后可以直接上传，我是为了本教程，先解压后再上传的文件。

![img](https://docimg1.docs.qq.com/image/DS65ffUnr-fU1cpBiDzbNg?w=1900&h=616)

### **（1）gzip**

gzip可以说是应用最广的压缩命令了，目前gzip可以解开compress、zip和gzip等软件所压缩的文件，至于gzip所建立的压缩文件为*.gz，让我们来看看这个命令的语法:

gzip [-cdtvn] 文件名

选项与参数：

- -c: 将压缩的数据输出到屏幕上，可通过数据流重定向来处理;
- -d: 解压缩的参数;
- -t: 可以用来检验一个压缩文件的一致性，看看文件有无错误;
- -v: 可以显示出原文件/压缩文件的压缩比等信息;
- -n: n为数字的意思,代表压缩等级，-1最快，但压缩比最差，-9最慢，但是压缩比最好，默认是-6。

在/root/BioInfoData/gencode.v35lift37.annotation.gtf/目录下有一个快1.6G的gtf文件。就是前面上传的文件.

然后我们利用gzip来压缩这个文件，命令如下：



```
gzip -v /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf 
```





![img](https://docimg6.docs.qq.com/image/566Ydcqv4MNDId3Th3Z18w?w=1895&h=72)

我们可以看见压缩比为96.2%，我们查看一下目录下的文件。

![img](https://docimg1.docs.qq.com/image/3lg3eA-xgGwuYtPkUpSKdA?w=929&h=105)

压缩前是1.6G，压缩后的文件是59M，可见压缩文件是多么的节省存储空间，此外，压缩后原始文件将不存在，压缩后的文件名是原来文件名加上.gz。

相反，我们可以通过-d参数解压压缩文件。



```
gzip -d /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf.gz
```





![img](https://docimg3.docs.qq.com/image/OoMqwMYQdb7xPkdbTJImow?w=1315&h=125)

同样，解压后原始的压缩文件也将被删除。如果想保留原始文件，我们可以通过-c参数与>的使用解决这个问题。-c参数是将压缩的数据输出到屏幕上，>将原本输出到屏幕上的数据转成输出到文件。



```
gzip -c /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf.gz > /root/BioInfoData/human.v33.annotation.gtf.gz/gencode.v35lift37.annotation.gtf
```





### **（2）bzip2**

若说gzip是为了替换compress并提供更好的压缩比而成立的，那么bzip2则是为了替换gzip并提供更加的压缩比而来。bzip2真是很不错的东西，这玩意的压缩比竟然比gzip还要好，至于bzip2的用法几乎与gzip相同,看看下面的用法吧!

bzip2 [-cdkzvn] 文件名

选项与参数：

- -c: 将压缩的数据输出到屏幕上，可通过数据流重定向来处理;
- -d: 解压缩的参数;
- -k: 保留原始文件，而不是删除原始文件；
- -z: 压缩的参数(默认值，可以不加)；
- -v: 可以显示出原文件/压缩文件的压缩比等信息;
- -n: n为数字的意思,代表压缩等级，-1最快，但压缩比最差，-9最慢，但是压缩比最好，默认是-6

![img](https://qqadapt.qpic.cn/txdocpic/0/e5d07a60757247590265d73e048a01cd/0?_type=png&w=1064&h=165)

bzip2压缩于gzip差不多，就是文件后缀名不一样，bzip2压缩比比gzip好，但时间更长。

![img](https://docimg7.docs.qq.com/image/Edi6nUg5peKBx7EoFCZ2RQ?w=1297&h=152)

### **（3）xz**

虽然bzip2已经具有很棒的压缩比，不过显然某些自由软件开发者还不满足，因此后来还推出了xz这个压缩比更高的软件。这个软件的用法也跟gzip/bzip2几乎一模一样，那我们就来看一看。

xz [-cdtlkn] 文件名

选项与参数：

- -c: 将压缩的数据输出到屏幕上，可通过数据流重定向来处理;
- -d: 解压缩的参数;
- -k: 保留原始文件，而不是删除原始文件；
- -l: 列出压缩文件的相关信息；
- -t: 测试压缩文件的完整性，看看有没有错误;
- -z: 压缩的参数(默认值，可以不加)；
- -n: n为数字的意思,代表压缩等级，-1最快，但压缩比最差，-9最慢，但是压缩比最好，默认是-6

我们继续压缩文件。



```
xz -k /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf 
```





可以看见，xz压缩比又比bzip2好，但时间同样长。

这三个压缩命令，参数都差不多，所以会一个就会3个。我们可以查看压缩前后的信息。



```
 xz -l /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf.xz
```





## **3.打包命令——tar**

前面谈到的命令大多仅能针对单一文件来进行压缩，虽然gzip、bzip2、xz也能够针对目录来进行压缩，不过，这几个命令对目录的压缩指的是将目录内的所有文件【分别】进行压缩的操作。而不像在Windows的系统，可以使用类似WinRAR这一类的压缩软件来将好多数据包成一个文件的样式。

这种将多个文件或目录包成一个大文件的命令功能，我们可以称它是一种打包命令，那Linux有没有这种打包命令？有，那就是大名鼎鼎的tar，tar可以将多个目录或文件打包成一个大文件，同时还可以通过gzip、bzip2、xz的支持，将该文件同时进行压缩。更有趣的是，由于tar的使用太广泛了，目前Windows的WinRAR也支持.tar.gz文件名的解压缩。

tar的选项与参数特别多，我们只讲几个常用的选项，更多选项您可以自行man tar查询。

- tar [-z|-j|-J] [cv] [-f 待建立的新文件名] filename... <== 打包与压缩。
- tar [-z|-j|-J] [cv] [-f 既有的tar文件名]  <== 查看文件名
- tar [-z|-j|-J] [xv] [-f 既有的tar文件名]  <== 解压缩

选项与参数:

- -c: 建立打包文件，可搭配-v来查看过程中被打包的文件名(filename);
- -t: 查看打包文件的内容含有那些文件名，重点在查看【文件名】；
- -x: 解包或解压缩功能，可以搭配-C(大写)在特定目录解压，特别留意的是，-c、-t、-x不可同时出现在一串命令行中；
- -z: 通过gzip的支持进行压缩/解压缩: 此时文件名最好为*.tar.gz；
- -j: 通过bzip2的支持进行压缩/解压缩：此时文件名最好为*.tar.bz2;
- -J: 通过xz的支持进行压缩/解压缩: 此时文件名最好为 *.tar.xz，特别留意，-z、-j、-J不可以同时出现在一串命令行中；
- -v: 在压缩/解压缩的过程中，将正在处理的文件名显示出来;
- -f filename: -f后面要立刻接要被处理的文件名,建议-f单独写一个选项(比较不会忘记)。
- -C 目录: 这个选项用在解压缩，若要在特定目录解压缩，可以使用这个选项
- -p(小写): 保留备份数据的原本权限与属性，常用于备份(-c)重要的配置文件；
- -P(大写): 保留绝对路径，亦即允许备份数据中含有根目录存在之意。

将/root/BioInfoData/gencode.v35lift37.annotation.gtf文件夹下的所以文件复制到新创建的temp目录中。



```
mkdir temp
cp /root/BioInfoData/gencode.v35lift37.annotation.gtf/* ./temp
```





![img](https://docimg7.docs.qq.com/image/cDkGhJVAAiFa5uwUFBMGtA?w=965&h=148)

如果文件大可以考虑删除一些大文件。



```
time tar -zpcv -f ./temp.tar.gz ./temp
```





![img](https://docimg9.docs.qq.com/image/iSdoQjvJODeAHCG9T8Xt-g?w=829&h=399)

# **第九章：文本操作神器**

# **一.常见查看文件命令**

## **1.cat 与tac命令**

cat 命令用于连接文件并打印到标准输出设备上。

语法格式:cat [-AbeEnstTuv] [--help] [--version] fileName

参数说明：

- -n 或 --number：由 1 开始对所有输出的行数编号。
- -b 或 --number-nonblank：和 -n 相似，只不过对于空白行不编号。
- -s 或 --squeeze-blank：当遇到有连续两行以上的空白行，就代换为一行的空白行。
- -v 或 --show-nonprinting：使用 ^ 和 M- 符号，除了 LFD 和 TAB 之外。
- -E 或 --show-ends : 在每行结束处显示 $。
- -T 或 --show-tabs: 将 TAB 字符显示为 ^I。
- -A, --show-all：等价于 -vET。
- -e：等价于"-vE"选项；
- -t：等价于"-vT"选项；

![img](https://docimg5.docs.qq.com/image/7szgC14BNvZ-TnbLA1IYCA?w=1107&h=674)

tac的功能是将文件从最后一行开始倒过来将内容数据输出到屏幕上。我们可以发现，tac实际上是cat反过来写。

![img](https://docimg4.docs.qq.com/image/KqYRX5CT9CSMxNtai-rr0Q?w=1102&h=674)

## **2.head与tail命令**

head和tail通常使用在只需要读取文件的前几行或者后几行的情况下使用。

head 命令查看文件头部， -n 选项可以指定查看前几行。

![img](https://docimg10.docs.qq.com/image/RfRGKOvuhUunbO2iUcVsQQ?w=778&h=126)

tail 命令查看文件尾部， -n 选项可以指定查看后几行。

![img](https://docimg7.docs.qq.com/image/xOJ1Aqzjn2YQB5QW-t4EVg?w=765&h=144)

## **3.more与less命令**

more的功能是将文件从第一行开始，根据输出窗口的大小，适当的输出文件内容。当一页无法全部输出时，可以用“回车键”向下翻行，或者使用“空格键”向下翻页。退出查看页面，请按“q”键。



```
more /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf
```





![img](https://docimg6.docs.qq.com/image/8EL8N3hvjNaDx8vAumFwzw?w=1901&h=716)

less的功能和more相似，但是使用more无法向前翻页，只能向后翻。less可以使用【pageup】和【pagedown】键进行前翻页和后翻页，这样看起来更方便。less 命令用来查阅文档，功能更为强大。



```
less /root/BioInfoData/gencode.v35lift37.annotation.gtf/gencode.v35lift37.annotation.gtf
```





参考：https://www.cnblogs.com/machangwei-8/p/9570550.html 

## **4.paste命令**

用来将多个文件的内容合并，与 cut 命令完成的功能刚好相反。

具体用法：

paste [-s][-d <间隔字符>][--help][--version][文件...]

参数：

- -d, --delimiters=列表   改用指定列表里的字符替代制表分隔符
- -s, --serial 不使用平行的行目输出模式，而是每个文件占用一行
- --help            显示此帮助信息并退出
- --version          显示版本信息并退出

首先确保两个文件行数相同。paste指令会把每个文件以列对列的方式，一列列地加以合并将每个指定文件里的每一行整合到对应一行里写到标准输出，之间用制表符分隔。如果没有指定文件，或指定文件为"-"，程序将从标准输入读取数据。 paste 连接文件时，除非指定 -d 选项，否则默认用 空格 或 tab键 分隔文本。



```
# touch exp1
# touch exp2
```





创建2个文件，exp1和exp2，并自己输入类似的数据。

![img](https://docimg6.docs.qq.com/image/xIeY_i2OTVUYw1rJP7GwNQ?w=569&h=260)



```
paste ./temp/info1.txt ./temp/info2.txt
```





![img](https://docimg9.docs.qq.com/image/n8P6J5UjuFRWP2cMM16iKg?w=713&h=145)

## **5.cut命令**

cut是一个选取命令，就是将一段数据经过分析，取出我们想要的。一般来说，选取信息通常是针对“行”来进行分析的，并不是整篇信息分析的。

其语法格式为：



```
cut  [-bn] [file] 或 cut [-c] [file]  或  cut [-df] [file]
```





主要参数

- -b ：以字节为单位进行分割。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志。
- -c ：以字符为单位进行分割。
- -d ：自定义分隔符，默认为制表符。
- -f ：与-d一起使用，指定显示哪个区域。
- -n ：取消分割多字节字符。仅和 -b 标志一起使用。如果字符的最后一个字节落在由 -b 标志的 List 参数指示的<br />范围之内，该字符将被写出；否则，该字符将被排除。

cut命令主要是接受三个定位方法：

第一，字节（bytes），用选项-b

第二，字符（characters），用选项-c

第三，域（fields），用选项-f

案例：

![img](https://docimg4.docs.qq.com/image/tNul40c46-eM1NyHEvz_9w?w=596&h=144)

其实cut的-d选项的默认间隔符就是制表符，所以当你就是要使用制表符的时候，完全就可以省略-d选项，而直接用－f来取域就可以了。

![img](https://qqadapt.qpic.cn/txdocpic/0/ed91908b9cc17326fdebd50f8a687a5c/0?_type=png&w=1005&h=122)

参考：https://blog.csdn.net/zsf8701/article/details/7718680 

# **二.文本处理的2大神器**

关于文本操作命令，前面已经介绍了一部分，这里介绍处理文本的三大神器。

## **1.grep 匹配**

grep：一种强大的文本搜索工具，能使用正则表达式匹配模式搜索文本，并把匹配的行打印出来。正则表达式是对字符串操作的一种逻辑公式，就是用事先定义好的一些特定字符、及这些特定字符的组合，组成一个“规则字符串”，这个“规则字符串”用来表达对字符串的一种过滤逻辑。grep 处理速度非常之快，尽量使用这个命令处理文本。**不了解正则表达式，需要去补充一下知识**。

知道正则表达式以后，我们就更加容易掌握grep，语法格式如下： 

grep [options] pattern file

常用参数：

- -v 反向选择，即输出没有没有匹配的行
- -n 显示匹配成功的行所在的行号
- -c 统计匹配成功的行的数量
- -w 完全匹配
- -o 只输出匹配的内容
- -f 从文件中读取pattern
- -e 指定多个匹配模式

其他参数：

-    -a 或 --text : 不要忽略二进制的数据。
-   -A<显示行数> 或 --after-context=<显示行数> : 除了显示符合范本样式的那一列之外，并显示该行之后的内容。
-   -b 或 --byte-offset : 在显示符合样式的那一行之前，标示出该行第一个字符的编号。
-   -B<显示行数> 或 --before-context=<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前的内容。
-   -c 或 --count : 计算符合样式的列数。
-   -C<显示行数> 或 --context=<显示行数>或-<显示行数> : 除了显示符合样式的那一行之外，并显示该行之前后的内容。
-   -d <动作> 或 --directories=<动作> : 当指定要查找的是目录而非文件时，必须使用这项参数，否则grep指令将回报信息并停止动作。
-   -e<范本样式> 或 --regexp=<范本样式> : 指定字符串做为查找文件内容的样式。
-   -E 或 --extended-regexp : 将样式为延伸的正则表达式来使用。
-   -f<规则文件> 或 --file=<规则文件> : 指定规则文件，其内容含有一个或多个规则样式，让grep查找符合规则条件的文件内容，格式为每行一个规则样式。
-   -F 或 --fixed-regexp : 将样式视为固定字符串的列表。
-   -G 或 --basic-regexp : 将样式视为普通的表示法来使用。
-   -h 或 --no-filename : 在显示符合样式的那一行之前，不标示该行所属的文件名称。
-   -H 或 --with-filename : 在显示符合样式的那一行之前，表示该行所属的文件名称。
-   -i 或 --ignore-case : 忽略字符大小写的差别。
-   -l 或 --file-with-matches : 列出文件内容符合指定的样式的文件名称。
-   -L 或 --files-without-match : 列出文件内容不符合指定的样式的文件名称。
-   -n 或 --line-number : 在显示符合样式的那一行之前，标示出该行的列数编号。
-   -o 或 --only-matching : 只显示匹配PATTERN 部分。
-   -q 或 --quiet或--silent : 不显示任何信息。
-   -r 或 --recursive : 此参数的效果和指定"-d recurse"参数相同。
-   -s 或 --no-messages : 不显示错误信息。
-   -v 或 --revert-match : 显示不包含匹配文本的所有行。
-   -V 或 --version : 显示版本信息。
-   -w 或 --word-regexp : 只显示全字符合的列。
-   -x --line-regexp : 只显示全列符合的列。
-   -y : 此参数的效果和指定"-i"参数相同。 

继续用上面的文件演示。在info1.txt文件中查找Bio

![img](https://docimg7.docs.qq.com/image/mgOcthFUa3gMcvLAZd6pAQ?w=575&h=69)

我们搜索“Bio”。搜索出来的结果会标红。

查看一下gtf文件内容的前6行：



```
head -6 ./temp/gencode.v35lift37.annotation.gtf
```





![img](https://docimg7.docs.qq.com/image/Jh1xJr1SvJAp9u1lxuACxA?w=1896&h=219)

关于gtf文件可以参考文章：[生信中常见的数据文件格式 ](https://mp.weixin.qq.com/s/ZcBGBOVzZwVpVQFLspZR7g)

我们上面搜索的gene，把含有gene字母的字符串也搜索出来啦,比如：gene_id，假如我们只希望出现gene_id这个单词的结果，那就加上-w参数.



```
grep -wc gene_id ./temp/gencode.v35lift37.annotation.gtf
```





![img](https://docimg7.docs.qq.com/image/T3evTpD9QiOn_85GnmCRyA?w=1901&h=390)

可以看到gene就是唯一的精确匹配结果。载加上-c这个参数，返回匹配的结果行数。



```
grep -wc gene_id ./temp/gencode.v35lift37.annotation.gtf
```





查找匹配结果反选：



```
grep -v gene_id ./temp/gencode.v35lift37.annotation.gtf
```





![img](https://docimg6.docs.qq.com/image/vNDhh3JIWodARWmk-EbUzg?w=1491&h=167)

我再演示一下正则表达式的检索模式,我们检索一下以B开头的行。

![img](https://docimg4.docs.qq.com/image/yzccPfE0pi8SnygmjtQH9A?w=604&h=82)

要怎么匹配，就按照正则表达式书写匹配模式就行啦。

## **2.sed流编辑器**

sed 是一种在线编辑器，它一次处理一行内容。处理时，把当前处理的行存储在临时缓冲区中，称为“模式空间”（pattern space），接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕。接着处理下一行，这样不断重复，直到文件末尾。文件内容并没有 改变，除非你使用重定向存储输出。sed主要用来自动编辑一个或多个文件；简化对文件的反复操作；编写转换程序等。

### **（1）sed命令的格式**

sed 选项 '动作' 文件名 (【sed [-opitons] 'script' file(s)】

cat 文件名 | sed 选项 '动作'

选项：

- -n ：只显示被修改的行的内容
- -e ：直接在命令列模式上进行 sed 的动作编辑；
- -f ：直接将 sed 的动作写在一个文件内， -f filename 则可以运行 filename 内的 sed 动作；
- -r ：sed 的动作支持的是延伸型正规表示法的语法。(默认是基础正规表示法语法)
- -i ：直接修改读取的文件内容，而不是输出到终端。

动作：匹配模式 '/pattern/ command'

- a：在指定行后新增一行或多行内容
- c：替换指定行的内容
- d：删除指定行的内容
- i ：在指定行之前 插入一行或多行内容
- s：替换指定内容，【格式】 ： s/pattern/replacement/[flags]，【flags】 数字：新文本替换第几处模式匹配的文本g（global） ： 新文本将替换所有匹配到的文本
- p：（print）打印
- w：（write）
- r：（read）
- = ：打印行号
- y： 转换

### **（2）删除行内容**

删除第4行的内容



```
sed "4d" ./temp/info1.txt
```





![img](https://docimg2.docs.qq.com/image/xE1AakW7_FxMtYGaHC35Gg?w=691&h=348)

删除第2-4行的内容



```
sed '2,4d' ./temp/info1.txt
```





删除第3行到最后一行的内容



```
sed '3,$d' ./temp/info1.txt
```





![img](https://docimg4.docs.qq.com/image/pusLkLSe-prPSc-ED8CeUQ?w=586&h=147)

在第2行后新增内容



```
sed '2a YunSen' ./temp/info1.txt
```





![img](https://docimg10.docs.qq.com/image/HPrpARcUUAIzwbYbojXlDw?w=655&h=170)

在第3行前插入内容



```
 sed '3i YunSen' ./temp/info1.txt
```





![img](https://docimg4.docs.qq.com/image/HdUj41dIiPwJ61xTE4v47Q?w=641&h=171)

把第3行的内容替换为Student



```
sed '3c Student' ./temp/info1.txt
```





![img](https://docimg10.docs.qq.com/image/C_sy38HmCZMLz4hqkld6Hg?w=652&h=259)

### **（3）搜索指定内容**

搜索含有Med的行



```
sed -n '/Bio/p' ./temp/info1.txt
```





搜索并删除指定内容



```
sed '/root/d' ./temp/info1.txt
```





![img](https://docimg9.docs.qq.com/image/wVtJ4O5AdRpS-KwRHCAk9w?w=636&h=177)

### **（4）替换指定内容**

默认只替换每行中模式首次匹配的内容



```
sed 's/yunsen/'YunSen'/' ./temp/info1.txt
```





![img](https://docimg7.docs.qq.com/image/0GNqDzVQFCTkYCtUjiUNEA?w=730&h=152)

g标记可以使sed执行全局替换



```
sed 's/o/'O'/g' ./temp/info1.txt
```





![img](https://docimg8.docs.qq.com/image/tT8tQtzlKPVu-7tNSsE2IA?w=643&h=144)

g标记可以使sed替换第N次即以后出现的匹配



```
sed 's/o/O/2g' ./temp/info1.txt
```





![img](https://docimg1.docs.qq.com/image/hjfadFRjUB5Gzs79zcw_4w?w=634&h=150)

### **（5）直接操作文件内容(危险动作)**

直接删除文件内容



```
sed -i '3d' ./temp/info1.txt
```





直接替换文件内容



```
sed -i 's/yunsen/YunSen/g' ./temp/info1.txt
```





（6）在sed中使用正则表达式

搜索并删除空行



```
sed '/^$/d' ./temp/info1.txt
```





参考文章：https://www.cnblogs.com/lfjn/p/11455970.html 



------

除了上面2 个工具外，还有一个awk工具，awk是一个强大的文本分析工具，相对于grep的查找，sed的编辑，awk在其对数据分析并生成报告时，显得尤为强大。简单来说awk就是把文件逐行的读入，以空格为默认分隔符将每行切片，切开的部分再进行各种分析处理。这个工具后面再介绍。 

# **第十章：****Linux的运行模式与网卡设置**

# **一.Linux的运行模式**

单用户、多用户、单任务、多任务。

单用户：是指操作系统一般只能由一个人同时进行登录；

多用户：是指操作系统可以允许由多个人同时进行登录；

单任务：是指操作系统只能同时处理一个任务；

多任务：是指操作系统可以同时处理多个任务；

Windows属于单用户、多任务的操作系统；（mstsc是windows系统的远程工具）

Linux属于多用户、多任务的操作系统；

在Linux中存在运行模式一说，运行模式也就是Linux的运行方式。运行模式一共有7种，可以从运行模式文件中查看到具体的信息，运行模式的文件名叫做inittab，位置位于/etc/inittab。

打开inittab文件：



```
vim /etc/inittab
```





![img](https://qqadapt.qpic.cn/txdocpic/0/74e3c16eceb8c30521f998fec82dd4b1/0?_type=png&w=992&h=351)

云服务和本地装的Linux，这个文件的内容还不一样。

## **1. Linux 系统启动过程**

linux启动时我们会看到许多启动信息。

Linux系统的启动过程并不是大家想象中的那么复杂，其过程可以分为5个阶段：

- 内核的引导。
- 运行 init。
- 系统初始化。
- 建立终端 。
- 用户登录系统。

### **（1）内核引导**

当计算机打开电源后，首先是BIOS开机自检，按照BIOS中设置的启动设备（通常是硬盘）来启动。

操作系统接管硬件以后，首先读入 /boot 目录下的内核文件。

![img](https://qqadapt.qpic.cn/txdocpic/0/dcfab5e339d3b7b8551461d47fbb2a4a/0?_type=png&w=602&h=135)

### **（2）运行init**

init 进程是系统所有进程的起点，你可以把它比拟成系统所有进程的老祖宗，没有这个进程，系统中任何进程都不会启动。

init 程序首先是需要读取配置文件 /etc/inittab。

![img](https://qqadapt.qpic.cn/txdocpic/0/f9b7cce82f127e983ad41b123efbecfc/0?_type=png&w=596&h=131)

**运行级别:**

许多程序需要开机启动。它们在Windows叫做"服务"（service），在Linux就叫做"守护进程"（daemon）。init进程的一大任务，就是去运行这些开机启动的程序。但是，不同的场合需要启动不同的程序，比如用作服务器时，需要启动Apache，用作桌面就不需要。Linux允许为不同的场合，分配不同的开机启动程序，这就叫做"运行级别"（runlevel）。也就是说，启动时根据"运行级别"，确定要运行哪些程序。

![img](https://qqadapt.qpic.cn/txdocpic/0/99f3f1c43c41a3287b02c021d8416455/0?_type=png&w=589&h=114)

Linux系统有7个运行级别(runlevel)：

- 运行级别0：系统停机状态，系统默认运行级别不能设为0，否则不能正常启动
- 运行级别1：单用户工作状态，root权限，用于系统维护，禁止远程登陆
- 运行级别2：多用户状态(没有NFS)
- 运行级别3：完全的多用户状态(有NFS)，登陆后进入控制台命令行模式
- 运行级别4：系统未使用，保留
- 运行级别5：X11控制台，登陆后进入图形GUI模式
- 运行级别6：系统正常关闭并重启，默认运行级别不能设为6，否则不能正常启动

### **（3）系统初始化**

在init的配置文件中有这么一行： si::sysinit:/etc/rc.d/rc.sysinit　它调用执了/etc/rc.d/rc.sysinit，而rc.sysinit是一个bash shell的脚本，它主要是完成一些系统初始化的工作，rc.sysinit是每一个运行级别都要首先运行的重要脚本。

它主要完成的工作有：激活交换分区，检查磁盘，加载硬件模块以及其它一些需要优先执行任务。



```
l5:5:wait:/etc/rc.d/rc 5
```





这一行表示以5为参数运行/etc/rc.d/rc，/etc/rc.d/rc是一个Shell脚本，它接受5作为参数，去执行/etc/rc.d/rc5.d/目录下的所有的rc启动脚本，/etc/rc.d/rc5.d/目录中的这些启动脚本实际上都是一些连接文件，而不是真正的rc启动脚本，真正的rc启动脚本实际上都是放在/etc/rc.d/init.d/目录下。而这些rc启动脚本有着类似的用法，它们一般能接受start、stop、restart、status等参数。

/etc/rc.d/rc5.d/中的rc启动脚本通常是K或S开头的连接文件，对于以 S 开头的启动脚本，将以start参数来运行。而如果发现存在相应的脚本也存在K打头的连接，而且已经处于运行态了(以/var/lock/subsys/下的文件作为标志)，则将首先以stop为参数停止这些已经启动了的守护进程，然后再重新运行。这样做是为了保证是当init改变运行级别时，所有相关的守护进程都将重启。至于在每个运行级中将运行哪些守护进程，用户可以通过chkconfig或setup中的"System Services"来自行设定。

![img](https://qqadapt.qpic.cn/txdocpic/0/2b4fdb9721ee8487aacf2fa5daaaebe2/0?_type=png&w=592&h=206)

### **（4）建立终端**

rc执行完毕后，返回init。这时基本系统环境已经设置好了，各种守护进程也已经启动了。

init接下来会打开6个终端，以便用户登录系统。在inittab中的以下6行就是定义了6个终端：

1:2345:respawn:/sbin/mingetty tty1

2:2345:respawn:/sbin/mingetty tty2

3:2345:respawn:/sbin/mingetty tty3

4:2345:respawn:/sbin/mingetty tty4

5:2345:respawn:/sbin/mingetty tty5

6:2345:respawn:/sbin/mingetty tty6

从上面可以看出在2、3、4、5的运行级别中都将以respawn方式运行mingetty程序，mingetty程序能打开终端、设置模式。

同时它会显示一个文本登录界面，这个界面就是我们经常看到的登录界面，在这个登录界面中会提示用户输入用户名，而用户输入的用户将作为参数传给login程序来验证用户的身份。

### **（5）用户登录系统**

一般来说，用户的登录方式有三种：

- 命令行登录
- ssh登录
- 图形界面登录

![img](https://qqadapt.qpic.cn/txdocpic/0/e4ef996f7d4261fd4bee045a9aaaca7a/0?_type=png&w=599&h=215)

对于运行级别为5的图形方式用户来说，他们的登录是通过一个图形化的登录界面。登录成功后可以直接进入 KDE、Gnome 等窗口管理器。

而本文主要讲的还是文本方式登录的情况：当我们看到mingetty的登录界面时，我们就可以输入用户名和密码来登录系统了。

Linux 的账号验证程序是 login，login 会接收 mingetty 传来的用户名作为用户名参数。

然后 login 会对用户名进行分析：如果用户名不是 root，且存在 /etc/nologin 文件，login 将输出 nologin 文件的内容，然后退出。

这通常用来系统维护时防止非root用户登录。只有/etc/securetty中登记了的终端才允许 root 用户登录，如果不存在这个文件，则 root 用户可以在任何终端上登录。

/etc/usertty文件用于对用户作出附加访问限制，如果不存在这个文件，则没有其他限制。

### **（6）图形模式与文字模式的切换方式**

Linux预设提供了六个命令窗口终端机让我们来登录。

默认我们登录的就是第一个窗口，也就是tty1，这个六个窗口分别为tty1,tty2 … tty6，你可以按下Ctrl + Alt + F1 ~ F6 来切换它们。如果你安装了图形界面，默认情况下是进入图形界面的，此时你就可以按Ctrl + Alt + F1 ~ F6来进入其中一个命令窗口界面。当你进入命令窗口界面后再返回图形界面只要按下Ctrl + Alt + F7 就回来了。如果你用的vmware 虚拟机，命令窗口切换的快捷键为 Alt + Space + F1~F6. 如果你在图形界面下请按Alt + Shift + Ctrl + F1~F6 切换至命令窗口。

![img](https://qqadapt.qpic.cn/txdocpic/0/175263c5197daa552075f450942a2d4e/0?_type=png&w=603&h=237)

# **二.网卡设置（重点）**

在实际开发的时候Linux服务器/windows服务器的网卡不要随便的禁用，一旦禁用，远程终端连接立马会断开，一但断开就会连接不上。

## **1.网卡配置文件的位置**

在Linux中网卡不像windows系统中那样以图标的形式进行配置，在命令行中存在单独的配置文件的，配置文件的位置在/etc/sysconfig/network-scripts/

![img](https://docimg5.docs.qq.com/image/TKDixL-hJ_9s5ERnoSfL5g?w=907&h=444)

每个网卡都对应着一个配置文件。例如ifcfg-eth0对应着eth0这个网卡，ifcfg-lo对应着lo网卡：

![img](https://docimg6.docs.qq.com/image/9oL58TjYBsJRu_tP6JcYXA?w=795&h=469)

## **2.禁用/启用网卡**

禁用网卡：#ifdown 设备名称

例如禁用eth0这块网卡，则输入#ifdown eth0，然后按下回车就可以。

启用网卡：#ifup 设备名称

例如启用eth0这块网卡，则输入#ifup eth0，然后按下回车就可以。

在实际工作的时候千万不要随意禁用网卡。

# **第十一章：云硬盘的管理**

# **一.云硬盘的挂载**

我们购买服务器的时候，给的硬盘容量是比较少的，我们的基因组数据，单细胞测序数据都是很大的，所以我们是需要单独去买硬盘用于存储数据，在Windows系统，相当于你把一个U盘或者移动硬盘插到USB接口，系统就会自动识别，在电脑上就会显示，但在Linux系统中，我们需要自己挂载。这里的话我是购买的腾讯云硬盘。你用阿里的服务器，就购买阿里的云硬盘，不要跨平台，而且，同一平台也还要注意，购买的云硬盘仅支持同可用区挂载：弹性云盘可在同可用区的实例之间自由挂载、卸载，不支持跨可用区操作，也就是说你购买的服务器和硬盘要在同一个区，我的服务器是在北京1区，所以购买的云硬盘最好就是在北京一区。

在个人控制台页面的云硬盘窗口，点击新建。

![img](https://qqadapt.qpic.cn/txdocpic/0/442f78d882bd8f0882d282d0fdcd4511/0?_type=png&w=1917&h=709)

会让我们选择购买的地区，选择和服务器一个地区。SSD云硬盘比高性能云硬盘贵2~3倍。一般我们也就选择高性能硬盘，容量，你可以根据自己的需求选择，100G/1个月/35元。

![img](https://qqadapt.qpic.cn/txdocpic/0/7e8053c24a17c21068b9efdf64aa9c9a/0?_type=png&w=785&h=885)

我这里演示的话，就购买了一个10G的，一个月，付款后，返回云硬盘窗口，就会看见一个多一个硬盘，而且显示未挂载。所以我们接下来需要进行挂载。

![img](https://qqadapt.qpic.cn/txdocpic/0/d5f5063d14ea7f440bad42c36cf7c82a/0?_type=png&w=1918&h=396)

在右侧有个更多，里面就有个挂载选项。

![img](https://qqadapt.qpic.cn/txdocpic/0/f2a1600a14b51dec7f922b15f3c5a595/0?_type=png&w=1643&h=459)

点击挂载后，会让我们选择挂载到那个服务器上，这里只有一个服务器，就默认给我选择了。在挂载选项可以根据自己选择，显示付费是因为我购买的云硬盘只是一个月，也就是2020年7月27日到期，而我的服务器2021年4月2日才到期，挂载到服务器上，如果需要和服务器同时间到期，那就选择对其实例到期时间，所以会付费，也可以选择到期后按月到期付费，或者直接挂载。

![img](https://qqadapt.qpic.cn/txdocpic/0/5fe4a73122353c7c4264b34dc06bb675/0?_type=png&w=681&h=721)

我这里演示的话就选择直接挂载了。学习的时候，可以这样，但后期自己需要分析数据的时候，最好还是同步服务器，后者到期自动续费。

![img](https://qqadapt.qpic.cn/txdocpic/0/93b68f31d44dc5d1db512054564cd132/0?_type=png&w=685&h=709)

点击下一步。

![img](https://qqadapt.qpic.cn/txdocpic/0/20066d31d93e385a9cae5cc7c409c059/0?_type=png&w=686&h=336)

点击开始挂载。然后就可以看到状态显示已挂载。

![img](https://qqadapt.qpic.cn/txdocpic/0/13fc2017549a19d7d7752038fc39895a/0?_type=png&w=1900&h=370)

还可以创建快照，这个对于硬盘到期后没有续费，后面又想用，又想恢复之前的数据很重要。

![img](https://qqadapt.qpic.cn/txdocpic/0/66a621d69118c0102dbd297aa1a6165d/0?_type=png&w=1643&h=658)

创建快照后，快照总大小处就会显示大小，因为该购买的硬盘，里面什么数据都没有，所以是0。

![img](https://qqadapt.qpic.cn/txdocpic/0/ad0f5deb8f561c63f26b86d322337d6f/0?_type=png&w=1614&h=233)

如果我们内存不够用了，可以继续扩容，这就是云硬盘的好处。

![img](https://qqadapt.qpic.cn/txdocpic/0/48a22c6115dad7cf4c9e42b196d0b3db/0?_type=png&w=1641&h=364)

不过在扩容前对云硬盘制作快照，防止因误操作造成文件系统损坏，为了防止数据丢失，硬盘只可扩容不可缩。

![img](https://qqadapt.qpic.cn/txdocpic/0/39d67eb1071eb2232da67c3581fcc4a8/0?_type=png&w=990&h=509)

# **二.查看云硬盘**

以root身份登录 Linux 云服务器。输入：fdisk -l 命令。返回信息类似如下图，表示当前的云服务器有两块磁盘，“/dev/vda” 是系统盘，“/dev/vdb” 是新增数据盘，也就是我刚刚购买挂载的硬盘。

![img](https://qqadapt.qpic.cn/txdocpic/0/21bfda2110e783d9ebf7f2b31b426678/0?_type=png&w=894&h=383)

你以为这样就可以直接使用该硬盘了吗？不是的，还需要进行初始化等设置，我们尝试创建一个文件，发现会报错，dev是Device(设备)的缩写, 该目录下存放的是Linux的外部设备，在Linux中访问设备的方式和访问文件的方式是相同的。所以我们是不能直接这么用的，还需要设置挂载点，这就得先去了解文件Linux的文件系统。

![img](https://qqadapt.qpic.cn/txdocpic/0/c3500e1492b1324474dc8bcda3362f4f/0?_type=png&w=987&h=88)

# **四.云硬盘的管理**

我们需要根据您实际使用场景选择初始化方式：

若整块硬盘只呈现为一个独立的分区（即不存在多个逻辑盘，如 vdb1 和 vdb2 ），腾讯云强烈建议不使用分区，直接在裸设备上构建文件系统。

若整块硬盘需要呈现为多个逻辑分区（即存在多个逻辑盘），需要先进行分区操作，再在分区上构建文件系统。

关于硬盘分区，我们还是需要去掌握的，但我自己觉得，在云服务器上，在购买云硬盘的时候就可以选择购买几块硬盘，那样就不用自己分区了，但是最多只能挂载20个云硬盘，所以超过这个后，数据量大，我们只能扩容，方便管理还是需要分区的。

## **1.在裸设备上构建文件系统**

以 root 用户身份登录 Linux 云服务器。

设备名称，可以通过命令lsblk（list block devices）来获取：

![img](https://qqadapt.qpic.cn/txdocpic/0/fcf24af5d1b6ebf7e85506373d2b6e60/0?_type=png&w=568&h=176)

也可以通过下面命令查看



```
fdisk -l
```







![img](https://qqadapt.qpic.cn/txdocpic/0/7243e70fb692c69a9ae425ff1db0d4b9/0?_type=png&w=876&h=425)

前面硬盘挂载的时候，我就提到了“/dev/vda” 是系统盘，“/dev/vdb” 是新增数据盘，也就是我刚刚购买挂载的硬盘。

执行以下命令，对 “/dev/vdb” 裸设备直接创建文件系统格式。

mkfs -t <文件系统格式> /dev/vdb

这里的文件系统格式，就是我前面介绍的系统格式，不同文件系统支持的分区大小不同，根据实际需求合理选择文件系统。不是很了解，就用ext4。ext4 在性能、伸缩性和可靠性方面进行了大量改，支持 1 EB 的文件系统。





```
mkfs -t ext4 /dev/vdb
```





输入上面命令后，出现下面这样的信息，表示没有错误。

![img](https://qqadapt.qpic.cn/txdocpic/0/090b39b8e8459887b3dcaa545d06bff9/0?_type=png&w=997&h=539)

新建挂载点。所谓光盘挂载，可以理解成将光盘创建一个快捷方式。在windows下也有类似这样的过程（盘符的分配），但linux下必须的手动进行光盘/USB外接设备的挂载，只有挂载之后才能使用该外接设备中的文件/文件夹。挂载点就是指将这个设备放到什么地方去，挂载点就是一个目录。一般情况有个习惯，在实际使用的时候习惯于将外接设备挂载到/mnt目录下，比如说可以在mnt目录下创建一个dvd目录，然后可将光盘挂载到/mnt/dvd上，我这里就直接挂载到根目录(/)下。其实就是我们在根目录下创建一个文件夹data，文件名可以更改，自己认识就行，有点像Windows的CDEF盘。data表示用来存储数据的。

mkdir /data

执行mount命令，将新建分区挂载至新建的挂载点。

命令：mount

语法：mount [参数] 设备的名称 挂载点/挂载位置。



```
mount /dev/vdb /data
```







![img](https://qqadapt.qpic.cn/txdocpic/0/ac6b77c3db1eab609d1e9f820c4df926/0?_type=png&w=831&h=75)

这样我们就挂载好硬盘了，可以通过下面命令查看挂载情况。



```
df -TH
```







![img](https://qqadapt.qpic.cn/txdocpic/0/f9918f2f24c271b12092b751331e1a83/0?_type=png&w=891&h=237)

这里的Type就是我们说的文件系统类型，我们设置的ext4，系统盘是ext3。

我们也可以通过lsblk命令以树枝的方式查看。

![img](https://qqadapt.qpic.cn/txdocpic/0/9af5ad0e0b2a46caa47a0b6fa8935de0/0?_type=png&w=798&h=171)

我们尝试在data下创建一个文件，这没有问题了，你可以大data这个文件夹理解成Windows下的D盘或者F盘。

![img](https://qqadapt.qpic.cn/txdocpic/0/34f007e23581cee97f7dd215f983d4c1/0?_type=png&w=878&h=144)

关于这部分可参考官方文档：https://cloud.tencent.com/document/product/362/6734

## **2.Linux磁盘管理常用三个命令**

Linux磁盘管理好坏直接关系到整个系统的性能问题。

Linux磁盘管理常用三个命令为df、du和fdisk。

df：列出文件系统的整体磁盘使用量

du：检查磁盘空间使用量

fdisk：用于磁盘分区

df 以磁盘分区为单位查看文件系统，可以获取硬盘被占用了多少空间，目前还剩下多少空间等信息。

例如，我们使用df -h命令来查看磁盘信息， -h 选项为根据大小适当显示：

![img](https://qqadapt.qpic.cn/txdocpic/0/bd7b9fb8b224743a498d85e915cd5502/0?_type=png&w=747&h=240)

显示内容参数说明：

Filesystem：文件系统

Size： 分区大小

Used： 已使用容量

Avail： 还可以使用的容量

Use%： 已用百分比

Mounted on： 挂载点　

du 的英文原义为 disk usage，含义为显示磁盘空间的使用情况，用于查看当前目录的总大小。

![img](https://qqadapt.qpic.cn/txdocpic/0/fe30caf0b74339940c8ed17137c038ae/0?_type=png&w=835&h=77)

显示指定文件所占空间：

![img](https://qqadapt.qpic.cn/txdocpic/0/27d2436e6afc5a9187fda7d60baa6210/0?_type=png&w=735&h=78)

方便阅读的格式显示test目录所占空间情况：

![img](https://qqadapt.qpic.cn/txdocpic/0/c0a3022abe2f651495009fe6efc142c3/0?_type=png&w=797&h=80)

du 命令常用参数：

-s：对每个Names参数只给出占用的数据块总数。

-a：递归地显示指定目录中各文件及子目录中各文件占用的数据块数。若既不指定-s，也不指定-a，则只显示Names中的每一个目录及其中的各子目录所占的磁盘块数。

-b：以字节为单位列出磁盘空间使用情况（系统默认以k字节为单位）。

-k：以1024字节为单位列出磁盘空间使用情况。

-c：最后再加上一个总计（系统默认设置）。

-l：计算所有的文件大小，对硬链接文件，则计算多次。

-x：跳过在不同文件系统上的目录不予统计。

-h：以K，M，G为单位，提高信息的可读性。

相关命令：

df -hl：查看磁盘剩余空间

df -h：查看每个根路径的分区大小

du -sh [目录名]：返回该目录的大小

du -sm [文件夹]：返回该文件夹总M数

du -h [目录名]：查看指定文件夹下的所有文件大小（包含子文件夹）

fdisk 是 Linux 的磁盘分区表操作工具。

语法：

fdisk [-l] 装置名称

-l ：输出后面接的装置所有的分区内容。若仅有 fdisk -l 时， 则系统将会把整个系统内能够搜寻到的装置的分区均列出来。这个我们前面已经用过啦。

![img](https://qqadapt.qpic.cn/txdocpic/0/7ecfd64cc2ee6e46d2e626e7b1ba3000/0?_type=png&w=860&h=191)

## **3.硬盘的卸载**

我们前面介绍硬盘的挂载，使用的是mount命令，那么卸载用的是 umount 命令。语法如下：

umount [-fn] 装置文件名或挂载点

选项与参数：

-f ：强制卸除！可用在类似网络文件系统 (NFS) 无法读取到的情况下；

-n ：不升级 /etc/mtab 情况下卸除。

我们卸载前面挂载的云硬盘。再看看之间创建的文件MedBioInfoCloud.txt文件已经不存在了。

![img](https://qqadapt.qpic.cn/txdocpic/0/a1910f4fc95b1034b725665e08264ca0/0?_type=png&w=836&h=102)

## **4.硬盘的分区**

我前面已经卸载了硬盘，我们查看硬盘设备。

![img](https://qqadapt.qpic.cn/txdocpic/0/7363ddb5ae9b91cf8a888b5b657f530a/0?_type=png&w=843&h=416)

硬盘的分区也是以fdisk命令来操作的，执行以下命令，进入 fdisk 分区工具，开始对新增数据盘执行分区操作。以我购买的云硬盘/dev/vdb为例：



```
fdisk /dev/vdb
```







![img](https://qqadapt.qpic.cn/txdocpic/0/4582f24afd008a5bc26b9dc96588aa6a/0?_type=png&w=842&h=237)

我们输入m，可以查看所有命令，创建分区就是输入n。

![img](https://qqadapt.qpic.cn/txdocpic/0/3ead478c4f2ee532233291bc41b33bc9/0?_type=png&w=810&h=683)

输入n，按 Enter，开始新建分区。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/21bbf367676e9f51b54c8b986dfadbf5/0?_type=png&w=769&h=126)

表示磁盘有两种分区类型：

【p】表示主要分区。

【e】表示延伸分区。

这里，我们先创建一个主分区，后面介绍扩展分区的时候在进一步介绍他们之间的区别。输入p，按 Enter，开始创建一个主分区。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/09f8f169b1dfb6d0538ba3cb2e712aa1/0?_type=png&w=702&h=54)

【Partition number】表示主分区编号，可以选择1-4。

以选择分区编号1为例，输入主分区编号1，按 Enter。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/e857f0733c243ea9526c0f46fef835f2/0?_type=png&w=790&h=49)

【First sector】表示初始磁柱区域，可以选择2048 - 20971519，默认为2048。

以选择默认初始磁柱编号2048为例，按 Enter。关于磁柱编号，可能还需要去了解硬盘的结构，如果不是太懂，你可以看成一个区间，根据你的硬盘大小决定，我购买的是10G，你就把10G这个量分配到2048 - 20971519这个区间，5G的范围大概就是10485759这个位置，我们分区都是重最左侧开始的，所以选2048。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/5312bc32a37d4786f69f97f78fa55f2c/0?_type=png&w=1082&h=53)

【Last sector】表示截止磁柱区域，可以选择2048 - 20971519，默认为20971519。我们说了5G的范围大概就是10485759这个位置，所以选择截止磁柱编号10485759为例，表示硬盘上2048 -10485759为我们将要设置的一个分区，按 Enter。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/463a3b135c37da195e17038921f6e447/0?_type=png&w=989&h=99)

表示分区完成，即为5GB的数据盘新建了1个分区。

输入p，按 Enter，查看新建分区的详细信息。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/8a84b2c950813ddac09a2796b455b3fa/0?_type=png&w=891&h=304)

表示新建分区/dev/vdb1的详细信息。

若上述分区操作有误，请输入q，退出 fdisk 分区工具，之前的分区结果将不会被保留。我们这里不输入q，继续输入n继续分区，因为我们的硬盘是10G的内存，我们前面已经分了5G，还有5G。所以我们继续按照上面操作执行一遍。2048-10485759我们已经设置分区为vdb1了，那么设置第二个分区的时候，这块硬盘的开始位置就不是2018啦，而是10485760，而是上一个分区的结束位置。

![img](https://qqadapt.qpic.cn/txdocpic/0/1721b381219a73232bfc317055d91587/0?_type=png&w=964&h=267)

我们输入p，可看见2个分区了，一个vdb1，一个vdb2。

![img](https://qqadapt.qpic.cn/txdocpic/0/3ae6899ded5788f7332f1016d68c6866/0?_type=png&w=886&h=330)

输入w，按 Enter，将分区结果写入分区表中。

回显信息类似如下图，表示分区创建完成。

![img](https://qqadapt.qpic.cn/txdocpic/0/b84b1d1f37aba993c2eccd49a2ffccca/0?_type=png&w=889&h=145)

然后我们执行以下命令，将新的分区表变更同步至操作系统。

partprobe

输入上面这个命令，可能会有如下警告信息。不用管。

![img](https://qqadapt.qpic.cn/txdocpic/0/dec538fce258fe902b74dbbf44654ef2/0?_type=png&w=1239&h=51)

我们可以继续通过fdisk -l命令查看

![img](https://qqadapt.qpic.cn/txdocpic/0/5b123ad49dbb57241147060c54a745de/0?_type=png&w=975&h=536)

lsblk命令查看

![img](https://qqadapt.qpic.cn/txdocpic/0/ddc9de22b780874ffd17b5027f3137fc/0?_type=png&w=907&h=212)

接下来我们就可以将/dev/vdb1 和/dev/vdb2 挂载到特定的挂载点。

创建挂载点

![img](https://qqadapt.qpic.cn/txdocpic/0/eed1060b9dc8c4ce0de9e2b59f5b7258/0?_type=png&w=920&h=78)

执行下面2行命令

mkfs -t ext4 /dev/vdb1

mkfs -t ext4 /dev/vdb2

然后分别挂载到2个挂载点上就可以啦。

![img](https://qqadapt.qpic.cn/txdocpic/0/ff9c5030ed908038d63538ecd16fe223/0?_type=png&w=849&h=75)

看一下挂载结果：

![img](https://qqadapt.qpic.cn/txdocpic/0/7b7d8f0428bdfdc6179beb968c69b801/0?_type=png&w=955&h=254)

![img](https://qqadapt.qpic.cn/txdocpic/0/7374d5ae196a5619018781e06746610f/0?_type=png&w=929&h=259)

## **5.删除分区**

我们前面输入命令fdisk /dev/vdb 后输入n，创建一个新的分区，我们前面创建了2个分区，我们可以删除这2个分区。

![img](https://qqadapt.qpic.cn/txdocpic/0/c0bc0440cc32c013c7073b0d6a5a9c26/0?_type=png&w=898&h=221)

删除分区输入的是d，然后会提示输入分区编号，这里提示的是1,2，因为我们只有2个分区，所以只显示这2个数，如果有3个分区，那就是1,2,3，最多是4，因为我们前面创建分区时，第一次不就是1-4，第二次是2-4吗？也就是说，一块硬盘最多可以分4个区。我们这里输入2，表示删除第二个分区，也就是/dev/vdb2。

![img](https://qqadapt.qpic.cn/txdocpic/0/491c0211fe4981d286a010d348914d9d/0?_type=png&w=748&h=126)

提示分区已经被删除，我们输入w保存退出，检查一下看看。发现已经只有vdb1啦。

![img](https://qqadapt.qpic.cn/txdocpic/0/9848923de8ca78830c7f06a2783e5b04/0?_type=png&w=964&h=648)

## **6.扩展分区与逻辑分区**

linux分区不同于windows，linux下硬盘设备名为（IDE硬盘为hdx（x为从a—d）因为IDE硬盘最多四个，SCSI，SATA，USB硬盘为sdx（x为a—z）），硬盘主分区最多为4个，所以我们前面分区的时候只能输入1~4的那一步，就是说明最多能分2个分区，准确来说，就是主分区和扩展分区加起来最多4个，但有时候你想分超过4个分区怎么办？所以我先介绍硬盘的基本概念。

一个硬盘主分区至少有1个，最多4个，扩展分区可以没有，最多1个。且主分区+扩展分区总共不能超过4个。逻辑分区可以有若干个。

在windows下激活的主分区是硬盘的启动分区，他是独立的，也是硬盘的第一个分区，正常分的话就是C区。 在linux下主分区和逻辑分区都可以用来放系统，引导os开机，grub会兼容windows系统开机启动。分出主分区后，其余的部分可以分成扩展分区，一般是剩下的部分全部分成扩展分区，也可以不全分，那剩的部分就浪费了。但扩展分区是不能直接用的，他是以逻辑分区的方式来使用的，所以说扩展分区可分成若干逻辑分区。他们的关系是包含的关系，所有的逻辑分区都是扩展分区的一部分。在linux中第一块硬盘分区为hda分区，主分区编号为hda1-4，逻辑分区从5开始。硬盘的容量=主分区的容量+扩展分区的容量，扩展分区的容量=各个逻辑分区的容量之和，主分区也可成为“引导分区”，会被操作系统和主板认定为这个硬盘的第一个分区。所以C盘永远都是排在所有磁盘分区的第一的位置上。MBR（主引导记录）的分区表（主分区表）只能存放4个分区，如果要分更多的分区的话就要一个扩展分区表（EBR），扩展分区表放在一个系统ID为0x05的主分区上，这个主分区就是扩展分区，扩展分区能可以分若干个分区，每个分区都是个逻辑分区。

关于硬盘的扩展分区创建，和主分区差不多。我们前面输入下面命令时。



```
fdisk /dev/vdb
```







![img](https://qqadapt.qpic.cn/txdocpic/0/4582f24afd008a5bc26b9dc96588aa6a/0?_type=png&w=842&h=237)

输入n，按 Enter，开始新建分区。

回显信息类似如下图：

![img](https://qqadapt.qpic.cn/txdocpic/0/21bbf367676e9f51b54c8b986dfadbf5/0?_type=png&w=769&h=126)

表示磁盘有两种分区类型：

【p】表示主要分区。

【e】表示延伸分区。

我们前面创建分区，输入p，按 Enter，延伸分区的话，输入e，按 Enter，后面的操作几乎一样。

![img](https://qqadapt.qpic.cn/txdocpic/0/0625e0a7a07461f566c5bc2524e49f94/0?_type=png&w=1038&h=679)

我们利用fdisk -l命令查看一下，新创建的vdb2就是扩展分区。

![img](https://qqadapt.qpic.cn/txdocpic/0/7902d3c1c3d46d1e78f9cbdef4a64b30/0?_type=png&w=869&h=536)

尝试挂载vdb2是挂载不成功的。vdb2是扩展分区，我们只能在vdb2的基础上创建逻辑分区。

![img](https://qqadapt.qpic.cn/txdocpic/0/517ba9fd94740e849fcd66a8431fb89e/0?_type=png&w=900&h=169)

我们需要创建逻辑分区。我们前面10G的内存分成了2个区，一个主分区vdb1，一个扩展区vdb2，可能我们会觉得，扩展分区可分成若干逻辑分区，所以创建逻辑分区会用vdb2这个设备名称，当我们执行fdisk /dev/vdb2命令后，再输入n发现不行。

![img](https://qqadapt.qpic.cn/txdocpic/0/61ab4e7d034a2c51a73b3e15e1285f71/0?_type=png&w=881&h=334)

其实我们创建逻辑分区，还是得用vdb这个设备名称。

![img](https://qqadapt.qpic.cn/txdocpic/0/406c383ff2b131d7107174adfed69ad7/0?_type=png&w=868&h=201)

然后我们输入n，就会提示是创建一个主分区还是逻辑分区，可能你会觉得前面我们输入n的时候出现的是p和e，没有l，这里又没有e。原因是，刚开始的的时候，我们的的硬盘还没有分区，就一块，也就是只有一个主分区，我们在进行分区的时候，硬盘没有扩展分区，由于逻辑分区是利用扩展分区创建的，所以就不会出现"l logical"这个选项，后面我们删除vdb2这个主分区，重新创建为扩展分区，我们说了扩展分区只能有一个，所以现在输入n，由于有扩展分区存在，所以就不会有e这个选项，而且我们看到，逻辑分区是从5开始的。

![img](https://qqadapt.qpic.cn/txdocpic/0/f290e422002ea211fd47c33843228cc0/0?_type=png&w=836&h=135)

我们输入l，创建逻辑分区，后面的First sector和Last sector与前面分主分区的一样，直接回车的话就是选择默认的值，这里我就是选择默认的值。

![img](https://qqadapt.qpic.cn/txdocpic/0/55717d25cf120da8638338e4d768b6b9/0?_type=png&w=876&h=315)

最后输入w保存。

![img](https://qqadapt.qpic.cn/txdocpic/0/b8d9706d85f153c0aa0995ee26a648d0/0?_type=png&w=721&h=126)

然后我们查看一下，就多了个vdb5。

![img](https://qqadapt.qpic.cn/txdocpic/0/55a944578fb4326c2dfbc88a33013028/0?_type=png&w=994&h=563)

后面，就是把硬盘挂载到相应目录下就可以啦。

![img](https://qqadapt.qpic.cn/txdocpic/0/b6ca01719fd77209a9a476f0c62b09c1/0?_type=png&w=989&h=561)

再查看一下挂载结果。

![img](https://qqadapt.qpic.cn/txdocpic/0/daa5ac5fea877d6c7483b666f63e6cd9/0?_type=png&w=849&h=263)

最后:Linux系统硬盘分区管理是很复杂的，上面这些也就是简单的分区应用而已，真正要做好管理的话，还需要学习很多东西。

# **第十二章：文件的查找**

查看文件类型：file ~/.bashrc

命令与文件查找：

脚本文件的查找：which [-a] command

查找文件：whereis命令或者locate命令，比find命令快速。locate查找的是/var/lib/mlocate里面的数据，需要updatedb更新。



```
[root@VM-0-2-centos ~]# cd /lib/modules/$(uname -r)/kernel
```





![img](https://docimg1.docs.qq.com/image/OoxOe-UDkzL1HiHnkRvYaQ?w=900&h=421)