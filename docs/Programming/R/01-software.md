
## 必备
R [https://www.r-project.org/](https://www.r-project.org/)
Rstudio [https://www.rstudio.com/products/rstudio/download/#download](https://www.rstudio.com/products/rstudio/download/#download)
Git [https://git-scm.com/](https://git-scm.com/)
Gitee 或 Github [https://gitee.com/](https://gitee.com/) 或 [https://github.com/](https://github.com/)
## 推荐
CRAN统计
METACRAN [https://www.r-pkg.org/](https://www.r-pkg.org/)
几乎所有R包的源代码/文档在线查看
[https://rdrr.io/](https://rdrr.io/)
阅读英文网页
沙拉查词 [https://saladict.crimx.com/download.html](https://saladict.crimx.com/download.html)
# 01_开发环境
开发环境，除了常规的R和Rstudio安装之外，还需要安装的一些东西

[软件工具软件和工具R包开发](https://www.yuque.com/xiayonghe/dev_r_pack/mtr992)

**Windows**
安装好Rtools，正常的下载安装，推荐用默认选项即可
[https://cran.r-project.org/bin/windows/Rtools/](https://cran.r-project.org/bin/windows/Rtools/)

**MacOS**
安装好Xcode和GNU Fortran compiler
[https://mac.r-project.org/tools/](https://mac.r-project.org/tools/)
●xcode推荐安装方式
打开终端
输入命令
●GNU Fortran compiler 下载地址
**注意区分版本**
[https://github.com/fxcoudert/gfortran-for-macOS/releases](https://github.com/fxcoudert/gfortran-for-macOS/releases)
**Linux**
要看具体发行版
下面的链接有主要的几个发行版的手册
[https://cran.r-project.org/bin/linux/](https://cran.r-project.org/bin/linux/)

xcode-select --install
# 02_开发工具包
除了系统和软件，开发过程中还会用到一些用于开发包的包

**必备**
●devtools 
安装上devtools后基本上其他会用到的也会被一同安上

**建议使用**
●依赖管理 
Packrat [https://rstudio.github.io/packrat/](https://rstudio.github.io/packrat/)
●依赖分析
pkgnet [https://uptake.github.io/pkgnet/](https://uptake.github.io/pkgnet/)

R复制代码

```r
# Install devtools from CRAN
install.packages("devtools")

# Or the development version from GitHub:
# install.packages("devtools")
devtools::install_github("r-lib/devtools")
```

# 03_阅读材料

**基础**
R Packages [https://r-pkgs.org/r.html](https://r-pkgs.org/r.html)
文件名规范 [https://style.tidyverse.org/files.html](https://style.tidyverse.org/files.html)
包中文件规范 [https://style.tidyverse.org/package-files.html](https://style.tidyverse.org/package-files.html)
Devtools cheatsheet [https://github.com/rstudio/cheatsheets/raw/master/package-development.pdf](https://github.com/rstudio/cheatsheets/raw/master/package-development.pdf)
可重复代码怎么写 [https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example](https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example)

**工具**
usethis [https://usethis.r-lib.org/articles/articles/usethis-setup.html](https://usethis.r-lib.org/articles/articles/usethis-setup.html)
devtools [https://devtools.r-lib.org/](https://devtools.r-lib.org/)
testthat [https://testthat.r-lib.org/](https://testthat.r-lib.org/)
roxygen2 [https://roxygen2.r-lib.org/](https://roxygen2.r-lib.org/)

**进阶**
Advanced R [https://adv-r.hadley.nz/index.html](https://adv-r.hadley.nz/index.html)
Writing R Extensions [https://cran.r-project.org/doc/manuals/R-exts.html](https://cran.r-project.org/doc/manuals/R-exts.html)
开发全家桶清单 [https://indrajeetpatil.github.io/awesome-r-pkgtools/](https://indrajeetpatil.github.io/awesome-r-pkgtools/)
R Development Guide [https://forwards.github.io/rdevguide](https://forwards.github.io/rdevguide)

**CRAN规定**
CRAN Repository Policy [https://cran.r-project.org/web/packages/policies.html](https://cran.r-project.org/web/packages/policies.html)

**Bioconductor规定**
package guidelines [https://www.bioconductor.org/developers/package-guidelines/](https://www.bioconductor.org/developers/package-guidelines/)
Package Submission [https://www.bioconductor.org/developers/package-submission/](https://www.bioconductor.org/developers/package-submission/)
guide developers [https://bioconductor.org/developers](https://bioconductor.org/developers/)

**其他推荐**
remotes 
[https://remotes.r-lib.org/articles/dependencies.html](https://remotes.r-lib.org/articles/dependencies.html)

Mastering Software Development in R 
[https://bookdown.org/rdpeng/RProgDA/building-r-packages.html](https://bookdown.org/rdpeng/RProgDA/building-r-packages.html)

为新手准备的现代化 R 包开发流程 
[https://swsoyee.vercel.app/2021/02/writing-r-packages-a-modern-workflow-for-beginners](https://swsoyee.vercel.app/2021/02/writing-r-packages-a-modern-workflow-for-beginners/)

rOpenSci Packages: Development, Maintenance, and Peer Review [https://devguide.ropensci.org/index.html](https://devguide.ropensci.org/index.html)

R Packages 中文 
[https://r-packages-zh-cn.readthedocs.io/zh_CN/latest/](https://r-packages-zh-cn.readthedocs.io/zh_CN/latest/)

Develop an R package for CRAN vs BioConductor
[https://www.biostars.org/p/233043/](https://www.biostars.org/p/233043/)

Git教程
[https://backlog.com/git-tutorial/cn/](https://backlog.com/git-tutorial/cn/)
Happy Git and GitHub for the useR
[https://happygitwithr.com/](https://happygitwithr.com/)

![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1656679617881-047e6037-c02c-4a03-9058-3dc7446e4192.png#clientId=u5eb9f118-a292-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=514&id=ud912dd79&margin=%5Bobject%20Object%5D&name=image.png&originHeight=643&originWidth=1285&originalType=binary&ratio=1&rotation=0&showTitle=false&size=531857&status=done&style=none&taskId=ub422667a-0007-4d09-abfa-6c7650408c9&title=&width=1028)
