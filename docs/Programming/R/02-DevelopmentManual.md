![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658125901289-76527173-1bf0-4ddb-a050-569e11659913.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=1125&id=ub5c8804a&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1406&originWidth=1820&originalType=binary&ratio=1&rotation=0&showTitle=false&size=763918&status=error&style=none&taskId=uba288409-37b1-4bbf-807e-ccacd3008fa&title=&width=1456)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658125918742-33f28a9c-00f9-4736-9638-d85ed2c7bf8a.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=1125&id=u901c5b1d&margin=%5Bobject%20Object%5D&name=image.png&originHeight=1406&originWidth=1820&originalType=binary&ratio=1&rotation=0&showTitle=false&size=760643&status=error&style=none&taskId=u346d877d-4fd3-4dd4-a9a9-72da5351c72&title=&width=1456)

一个R包本质上就是一系列函数的集合，通过调用R包的函数从而实现相应的功能。R包开发对R语言编程能力提升有极大帮助，更能方便理解他人编写的包，而不仅仅调参。
```r
install.packages("usethis") 
```
或者
```r
# install.packages("devtools") 
devtools::install_github("r-lib/usethis") 
```
相关函数：[https://usethis.r-lib.org/reference/index.html](https://usethis.r-lib.org/reference/index.html)
# **一.创建一个R包**
Rstudio中点击File - New Project - New Directory - R Package - 给自己R包取名和选择包地址，确定即可。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108473539-1f51f674-502f-485a-9d21-58a7064bcc72.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=uf7d56e74&margin=%5Bobject%20Object%5D&originHeight=382&originWidth=531&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=uf510c6a3-1d1e-49a3-a92d-e33fbdb9bdf&title=)
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108473624-728a1087-17bc-4a88-a83d-5e6364b8340a.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u7ef78d94&margin=%5Bobject%20Object%5D&originHeight=384&originWidth=532&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u10e07513-5b54-42fc-bc8b-60cae47202c&title=)
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108473609-d2e1897b-8177-4dc4-acf1-063e6a8180c9.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u557d619b&margin=%5Bobject%20Object%5D&originHeight=380&originWidth=527&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u6427bcd4-af3c-474c-916f-ec0d25ca594&title=)
通过代码创建
```r
devtools::create("F:/Rpkgs/YunSen") 
```
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108473599-c51aebfb-7085-4359-a057-93c15fb4c136.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u3c9d64e3&margin=%5Bobject%20Object%5D&originHeight=277&originWidth=683&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u66944d74-8bda-405b-9f64-c54a60e1586&title=)
在包的文件下会生成5个文件和一个R文件夹
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108473690-55e14901-1fe8-440e-b3c5-db77186391c4.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u27ff1e71&margin=%5Bobject%20Object%5D&originHeight=357&originWidth=1071&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u4567c1b1-4785-45fc-8099-94bcb78f92a&title=)
在RStudio中也可以看见。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108474594-f342d743-6fcf-4ad5-bb97-2635028c8f83.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u4037d8cf&margin=%5Bobject%20Object%5D&originHeight=1039&originWidth=1920&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u93c7c017-f039-4be7-9d97-d9ab7f76e94&title=)
R(存放R代码的地方)
DESCRIPTION(R包的相关描述)
NAMESPACE(用来规定可以调用的R函数功能,如果这里没有写明，即是R文件夹里面有相关函数功能也不能在之后调用)
.gitignore和.Rbuildgnore
# **二.创建R脚本**
R脚本是存放在R这个文件夹下，但我们通常usethis工具创建。自动在R文件夹下生成脚本文件。
```r
usethis::use_r("getSamInfo") 
```
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108474743-ccbf8223-59a1-47e7-b4ba-9985a66a67ff.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u7a624b76&margin=%5Bobject%20Object%5D&originHeight=1026&originWidth=1920&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u17e74a56-cf17-49b1-82f1-e11de77fa2e&title=)
开始写脚本，代码一般全是函数。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108474904-42410253-4f42-4340-9ffe-81863e1e9efe.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=uc9e00e8b&margin=%5Bobject%20Object%5D&originHeight=1039&originWidth=1920&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u68091290-ffe4-49c8-85d2-5f53f2b6165&title=)
写好脚本，我们要测试一下这个函数能否正常工作，首先使用load_all()函数加载包，它大致模拟了用library()安装和加载包时的情况。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108474854-6d4f0b1c-eb6b-489a-bf7d-8c8001f2d7e6.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u043ad57a&margin=%5Bobject%20Object%5D&originHeight=204&originWidth=728&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u689226de-c78a-409c-beb5-5d7837e2d8a&title=)
当我们把所有函数都写好后，利用devtools::check()自动检查构建和检查源代码包。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108474891-a893c2fd-429a-4197-a3e2-2e17defda93f.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u1e81a344&margin=%5Bobject%20Object%5D&originHeight=475&originWidth=1212&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u31e812ac-8289-4546-bfda-bc4295d1565&title=)
0个错误，1个警告，0个注意。可以看见警告内容是没有许可协议，如果不给其他人用，自己用的话，可以忽略许可协议。
怎么生成许可协议？？首先就得介绍一下DESCRIPTION文件
# **三.编写DESCRIPTION文件**
DESCRIPTION文件的作用是存储包中重要的元数据，当创建包时，就默认生成了DESCRIPTION文件，默认已经有一些内容。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108475723-299c29ce-bb4d-4d40-a900-dd855309ea1d.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u6fcd916f&margin=%5Bobject%20Object%5D&originHeight=506&originWidth=1219&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=uc675da0b-937b-4a2f-a47c-be4bbe28096&title=)
Package：包的名字
Title: 包的介绍，这里的内容就是Rstudio中Packages面板下各种包的描述
Version: 0.0.0.9000(版本号,版本号存在一定规范。这里只是一个简单的R包开发教程，不需理会)
Author: 作者信息
Description: 包的描述
License: 许可证(包的公共许可，开源程序的特色)
Encoding: UTF-8(编码方式)
LazyData: true(R包内置数据时选中)
先修改作者信息。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108476042-2eaeea09-50e3-4d45-9a1d-0d084506d268.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u4d186b2d&margin=%5Bobject%20Object%5D&originHeight=480&originWidth=1015&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u9c33c1c4-1105-4378-8c2a-2986682b30c&title=)
生成许可协议
```r
usethis::use_mit_license("Yun Sen") 
```
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108476031-334c41c0-6546-40bc-8689-198f85624189.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u4e7f0303&margin=%5Bobject%20Object%5D&originHeight=153&originWidth=936&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u789b8e61-c02f-44bb-82ab-4cfa31427a4&title=)
然后我们就会看见DESCRIPTION文件里的License处发生了变化
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108476276-35995e4e-45c3-4198-a677-05805335115c.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=uee2f4fb5&margin=%5Bobject%20Object%5D&originHeight=445&originWidth=802&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u3de09539-71a2-4fbe-8ab1-b12873884d4&title=)
同时在包目录下会生成2个文件。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108476393-e63db304-1bdd-428e-b051-ed9e9f299f5d.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u8b4af6f9&margin=%5Bobject%20Object%5D&originHeight=275&originWidth=679&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u9603c6bd-8c93-45ea-b5d6-39a7399c338&title=)
# **四.写函数帮助文档**
R 函数的帮助文档也是 R Package 的重要组成部分。函数文档以特殊的标记格式放在 man/*.Rd 文件中，但是我们不需要掌握这种特殊标记语法，我们只需要撰写特殊格式的注释，然后 roxygen2 就会将其转换成 *.Rd 文件。
将鼠标光标放在指定的函数体内，在 RStudio 中使用 Ctrl + Shift + Alt + R 或依次点击 Code -> Insert Roxygen Skeleton，就能够产生特殊格式的注释框架。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108477174-2b91cfba-38d4-437e-8882-f19fbc7f2c35.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u6a418137&margin=%5Bobject%20Object%5D&originHeight=703&originWidth=506&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u7161181e-1e18-4a2b-b971-2aa57a3e29f&title=)
然后会自动在该脚本前面生成默认的常见参数，都是以@开始的，这些我们可以称为标签
@param 函数参数
@return 说明本函数返回值
@importFrom 包名 函数名 函数名
@export（不添加，这个函数就不显示也就不能直接使用）
@examples提供示例代码
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108477261-ec6d0fc0-eeb8-4fb4-8d89-b47873c2e470.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=ufcd6e43b&margin=%5Bobject%20Object%5D&originHeight=414&originWidth=1057&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u828d393c-45c1-40d7-86be-9e96d4f5bbc&title=)
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658376743349-52be6cdf-0538-4df8-a00b-671f96decc14.png#clientId=u9c60cf61-0ec4-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=445&id=u918a90da&margin=%5Bobject%20Object%5D&name=image.png&originHeight=329&originWidth=553&originalType=binary&ratio=1&rotation=0&showTitle=false&size=224350&status=error&style=none&taskId=u2608b9f6-7458-42fc-942d-186ee6fb4d0&title=&width=748.4000244140625)
开始写参数介绍。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108478976-ae94855d-770c-4e2e-93be-031952d31ec0.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=ubce28dbe&margin=%5Bobject%20Object%5D&originHeight=486&originWidth=1225&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=ueb76c071-1abd-495e-abc5-4dcc2e40a7a&title=)
document()函数生成帮助文档，执行devtools::document()后，会生成一个man文件夹，man文件夹下会生成相应的Rd文件，文件名就是函数名。
```r
devtools::document() 
```
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108479226-5bb30a5e-4dc2-4621-92e2-8f8f77c6dcfc.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u1e71176c&margin=%5Bobject%20Object%5D&originHeight=1026&originWidth=1920&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u1e25f84c-cc82-4f0a-aa26-6b00825fb9f&title=)
然后我们就可以像平时一样通过问号?getSamInfo查看帮助文档了。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108479203-97d37cc6-acb7-45e2-b3f4-5ee4b35aa2f5.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u2c4e09f6&margin=%5Bobject%20Object%5D&originHeight=525&originWidth=674&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u6d61e563-7504-4651-a3d7-76d14233618&title=)
# **五.添加测试代码**
当我们写好一个函数后，需要验证函数是否能正确执行，结果是否正确，需要进行测试。
```r
usethis::use_testthat() 
```
通过usethis::use_testthat()创建测试文件，会生成一个tests文件夹，里面有一个文件夹和一个R脚本。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108479478-903dcfa8-f6cb-4f79-80d9-5c23c0fc23b6.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u241888a8&margin=%5Bobject%20Object%5D&originHeight=148&originWidth=675&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u5988865b-1c30-4f0a-8a26-fe8cc59ca02&title=)
test_check.文件里面的代码如下，就是加载我们自己的包和testthat包，和测试检查我们的包，这里先不管。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108479752-705e0bf5-bcc6-4a52-b82f-95e7f50c9fda.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u4b73d7e7&margin=%5Bobject%20Object%5D&originHeight=189&originWidth=1228&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u4b740065-18a3-49ba-aba0-9a512d9fe67&title=)
我们要测试函数，需要自己创建一个R脚本，这里通过use_test函数创建，参数是包名
```r
usethis::use_test("YunSen") 
```
testthat文件夹下会自动生成测试的R脚本，打开后默认有3行代码。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108480046-45c2a372-bc66-44a6-bd4f-aacf8c071b97.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u297e026e&margin=%5Bobject%20Object%5D&originHeight=754&originWidth=1583&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=uf9710c90-8f40-40b5-8cf5-71eba68277f&title=)
我们主要是通过检查函数运行结果一预期结果的比较。通常会用到下面这些函数，但不是全部。
expect_equal()判断是否相等，它使用all.equal()来检查一个数值在误差内是否相等。expect_identical()精确测试是否相等。
expect_match检测一个字符串向量是否与一个正则表达式匹配。
expect_output()检测打印输出，expect_message()检查信息，expect_warning()检查警告，expect_error()检查错误。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108480079-11cb4ff2-24ee-4cfc-b4c8-2a7bc1c3cf4c.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u6aa867ab&margin=%5Bobject%20Object%5D&originHeight=187&originWidth=1233&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=uf985d409-ca69-4c6f-b4b0-bdd20ab20ce&title=)
然后执行devtools::test()进行检查
```r
devtools::test() 
```
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108480693-bb575335-ba0f-495e-8f20-72442d7ff2ea.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=ufec1e665&margin=%5Bobject%20Object%5D&originHeight=238&originWidth=1181&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u16621f39-98da-4853-bb95-b93ada22c22&title=)
如果这些函数不能满足我们的需要，我们需要用expect_true或者expect_false函数来抓取其他的期望。这里的期望是我自己去构造的，也就是构造一个返回值为true或者false的期望表达式。还有，有时候结果太复杂，不容易通过代码重建，在这种情况下，可以检查结果是否与上次相同，expect_equal_to_reference()会缓存第一次结果，然后将其与随后的运行进行比较。
# **六.依赖包**
如果我们开发包过程中用到一些已有的包，或者其中的某个函数，那么我们需要引入，我们平时使用包是通过library或者source来加载包，但在开发时不能使用这种方式。R有很多种方式来描述这种潜在的依赖关系。通过imports（输入）、suggests（建议）、Depends（依赖）、LinkingTo（链接到）和Enhances（增强）来描述。imports里的包必须被安装，也就是在安装自己包的时候，imports申明的包也会被安装。suggests中的包，我们可以使用他，但不是必须的，比如我们可以退使用建议包中的数据来运行测试，编译使用指南，或者只有一个函数需要这个包，suggests中的包是不会随我们的包的安装而安装的。Depends用来指定特定的R版本，例如Depends：R（>=3.0.1)。LinkingTo用于列出依赖于另一个包中的C或者C++代码。Enhances列出你的包增强了的包，通常，你的包为其他包里的类提供了方法。
我们通过use_package()函数来申明依赖包。
```r
use_package(package, type = "Imports", min_version = NULL) 
```
package 包的名称
type 就是依赖类型，必须是 "Imports", "Depends", "Suggests", "Enhances"或者 "LinkingTo"中的一个，默认"Imports"。
关于TCGA分析的包有很多，我么这里可以用。
```r
usethis::use_package("GDCRNATools",type = "Imports") 
```
我们会看见描述文件会发生更新。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108482532-05e64427-730d-4277-9056-981c3576179c.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u40d63994&margin=%5Bobject%20Object%5D&originHeight=937&originWidth=1222&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=ue185163c-2266-4c5a-b5e1-d102466be60&title=)
use_package()向DESCRIPTION添加了一个CRAN包依赖关系，并提供了一些关于如何最好地使用它的建议。use_dev_package()在一个正在开发的GitHub包上添加了一个版本化的依赖，将repo添加到Remotes，这样它就会从正确的位置自动安装。
我们这里创建一个新的R脚本
```r
usethis::use_r("getTCGAData") 
```
导入非标准计算
```r
usethis::use_tidy_eval() 
```
# **七. 外部数据**
## **1.导出的数据**
包中数据最常用的位置是在data/目录下，数据格式一般是.Rdata。其中包含单个对象和文件的名称相同，使用这个规则最简单的方法是使用：
usethis::use_data() 
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108482539-ca01b82c-c81d-4671-a72b-2ede7bddd1ec.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=uc655244a&margin=%5Bobject%20Object%5D&originHeight=206&originWidth=877&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=ua698a8f7-4170-41f6-9166-2367c009a5d&title=)
会在包的目录下产生一个data文件夹，data目录下就会生成对应的Rda格式的文件。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108482620-89655ff4-5ac0-47c6-9495-c5f185ad8006.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u79e63a50&margin=%5Bobject%20Object%5D&originHeight=424&originWidth=1136&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u504275fc-2fa1-4f53-a37b-897c23800b3&title=)
使用Use_data()可以很容易地以正确的格式保存包数据。我建议您将生成包数据的脚本保存在data-raw中:使用use_data_raw()进行设置。您还需要记录导出的数据集。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108482758-6f34f952-a411-4d11-82c6-62a50a4fbdb1.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u0acf9d2f&margin=%5Bobject%20Object%5D&originHeight=669&originWidth=1150&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=ue92f99c1-239b-4ca1-aeb7-f2e153edd76&title=)
在oneSamID写生成数据的代码，后续也好知道数据的来源，data-raw目录下的代码是不需要打包的。对于数据的描述文档可以使用下面2个标签描述。
#' @format #' @source 
## **2.内部数据**
有时候函数需要预先计算的数据表，如果把这些数据放在data/目录下，这些数据也将会被提供给包的用户，这是不恰当的，正确的做法是把他保存在R、sysdata.Rda。我们在使用usethis::use_data()保存数据的时候，可以加上internal=TRUE来创建文件。
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108482964-1dd512ff-1743-42d9-b626-aefff3e0d6ba.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u6ef7616a&margin=%5Bobject%20Object%5D&originHeight=478&originWidth=736&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=u02832db9-e984-4680-818f-86de0d38d10&title=)
## **3.原始数据**
如果想展示加载/解析原始数据的例子，就将原始文件放在inst/extdata。安装包时，inst/中所有文件和文件夹都会移动到顶层目录，所以它们不能有R/description这样的名字，要引用inst/extdata（无论是否安装）中是文件，使用system.file()。 
![](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658108483440-0eefd13a-e65a-4b4f-8613-ca34390c7a36.png#clientId=ub4751717-1738-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&id=u12f1671f&margin=%5Bobject%20Object%5D&originHeight=151&originWidth=695&originalType=url&ratio=1&rotation=0&showTitle=false&status=error&style=none&taskId=ucfbce8cd-ea79-463b-a496-b46b57f0cec&title=)
BioinfoNotes @use_data_table() √ Adding 'data.table' to Imports field in DESCRIPTION √ Writing 'R/utils-data-table.R' * Run `devtools::document()` 
# 八.Build包
检查包
```r
install.packages("rhub")
rhub::check()
```
![image.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658554701486-0f069424-4e86-48c7-bc16-8a9f857c045c.png#clientId=uba1890bb-b287-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=254&id=u2c0e89fd&margin=%5Bobject%20Object%5D&name=image.png&originHeight=317&originWidth=1145&originalType=binary&ratio=1&rotation=0&showTitle=false&size=60629&status=error&style=none&taskId=uef31bc86-9c84-4d98-a289-f6bd57389a8&title=&width=916)
![1658376818867.png](https://cdn.nlark.com/yuque/0/2022/png/1234840/1658376855521-fb75f62a-7d14-4007-92c4-0b39f252dc79.png#clientId=u9c60cf61-0ec4-4&crop=0&crop=0&crop=1&crop=1&errorMessage=unknown%20error&from=paste&height=283&id=u4c105030&margin=%5Bobject%20Object%5D&name=1658376818867.png&originHeight=354&originWidth=628&originalType=binary&ratio=1&rotation=0&showTitle=false&size=45474&status=error&style=none&taskId=u1bf3bdf9-b462-494d-a4e6-65fcf492e15&title=&width=502.4)
# 九.提交到github
配置git用户：
在git窗口：
```git
# configure the user which will be used by Git
# this should be not an acronym but your full name
git config --global user.name "Firstname Lastname"

# configure the email address
git config --global user.email "your.email@example.org"
```
如果之前登录过账户，切换账户，在push时可能会报403错误，解决办法：
CMD窗口，输入命令：rundll32.exe keymgr.dll,KRShowKeyMgr，出现「存储的用户名和密码」窗口：
![9a62cf938120f09415005df8cc1a6b9.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664374881184-66b51a4c-97ee-47e2-86a0-cf15beb43f29.jpeg#clientId=u295c1c55-5a89-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=406&id=u19205dea&margin=%5Bobject%20Object%5D&name=9a62cf938120f09415005df8cc1a6b9.jpg&originHeight=634&originWidth=564&originalType=binary&ratio=1&rotation=0&showTitle=false&size=52206&status=done&style=none&taskId=ucfe74d96-88f3-4af6-a2ee-de91e559f02&title=&width=360.96)
![1b334a72c3c788943d1538553b380e6.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/1234840/1664374900862-940460f9-d284-4b7b-a268-4e3b2967e68f.jpeg#clientId=u295c1c55-5a89-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=402&id=uee6ae663&margin=%5Bobject%20Object%5D&name=1b334a72c3c788943d1538553b380e6.jpg&originHeight=628&originWidth=1053&originalType=binary&ratio=1&rotation=0&showTitle=false&size=72640&status=done&style=none&taskId=ucab75db9-16b1-43da-9e3d-f188e3142d7&title=&width=673.92)
将 github 相关的条目删除。
然后提交
```r
git remote add origin git@github.com:BioInfoNote/FUNscore.git
git push -u origin master
```
# **十. usethis包**
## **1.use_package()**
use_package()向DESCRIPTION添加了一个CRAN包依赖关系，并提供了一些关于如何最好地使用它的建议。
use_dev_package()添加了一个对正在开发的包的依赖，将dev repo添加到Remotes，这样它就会从正确的位置自动安装。
use_package(package, type = "Imports", min_version = NULL) use_dev_package(package, type = "Imports", remote = NULL) 
package：要依赖的包的名称。
type：依赖类型:必须是 "Imports", "Depends", "Suggests", "Enhances"h或者 "LinkingTo" 之一。匹配不区分大小写。
min_version：还可以为包提供一个最小版本。设置为TRUE以使用当前安装的版本。
remote：默认情况下，插入一个OWNER/REPO GitHub远程服务器。您可以选择提供一个字符串来指定远程，例如。"gitlab::jimhester/covr"，使用远程包支持的任何语法。
## **2.use_import_from()**
use_import_from(package, fun, load = is_interactive()) 
use_import_from()通过将roxygen2 @importFrom标记添加到包级文档(可以使用use_package_doc()创建)来从另一个包中导入函数。从另一个包中导入一个函数允许你在没有命名空间的情况下引用它(例如，fun()而不是package::fun())。use_import_from()也会重新记录命名空间，并重新加载当前包。这能够确保你的开发过程中能够立即获得乐趣。
package：Package name
fun：A vector of function names
load：Logical. Re-load with pkgload::load_all()?
## **3.use_r()**
use_r(name = NULL, open = rlang::is_interactive()) use_test(name = NULL, open = rlang::is_interactive()) 
name：可以使用没有扩展名的名称，也可以使用NULL来根据脚本编辑器中当前打开的文件创建成对的文件。如果R文件是打开的，use_test()将创建/打开相应的测试文件;如果测试文件打开，use_r()将创建/打开相应的R文件。
## **4.use_rmarkdown_template()**
use_rmarkdown_template(   template_name ="Template Name",   template_dir =NULL,   template_description ="A description of the template",   template_create_dir =FALSE) 
## **5.Use_data()**
```r
use_data(...,   internal =FALSE,   overwrite =FALSE,   compress ="bzip2",   version =2) 
```
参数：
internal ：如果为FALSE，则将每个对象保存在data/目录中自己的.rda文件中。这些数据文件绕过通常的导出机制，在加载包时可用(如果LazyData不为TRUE，则通过data()可以使用)。如果为TRUE，则将所有对象存储在单个R/sysdata中.rda文件。此文件中的对象遵循通常的导出规则。请注意，这意味着如果您使用通用 exportPattern() 规则导出所有对象，除了以 .
overwrite : 默认情况下，use_data()不会覆盖现有文件。如果您真的想这样做，请将此设置为TRUE。
**compress : **选择save()使用的压缩类型。应该是"gzip"， "bzip2"，或"xz"之一。
version : 要使用的序列化格式版本。默认的2是从R 1.4.0到3.5.3。版本3从R 3.6.0开始成为默认版本，只能由R版本3.5.0及更高版本读取。
use_data_raw(name = "DATASET", open = rlang::is_interactive()) 
name : 要准备包含在包中的数据集的名称。
open : 打开新创建的文件进行编辑?发生在RStudio，如果适用，或通过utils::file.edit()否则。

library(GDCRNATools)
 samInfo <- gdcParseMetadata(project.id="TCGA-COAD", data.type='RNAseq') 
colnames(samInfo) 
#entity_submitter_id 
#TCGA-5M-AAT5-01A-21R-A41B-07 

编写DESCRIPTION文件
在Rstudio中打开DESCRTION文件,编写包的描述。

相关内容包括：
Package：包的名字
Type: Package(类型)
Title: 包的介绍，这里的内容就是Rstudio中Packages面板下各种包的描述
Version: 0.1.0(版本号,版本号存在一定规范。这里只是一个简单的R包开发教程，不需理会)
Author: 作者
Maintainer: The package maintainer yourself@somewhere.net(包的贡献者名字及邮箱)
Description: 包的描述
License: 许可证(包的公共许可，开源程序的特色。这里也不理会，以GPL-3为协议)
Encoding: UTF-8(编码方式)
LazyData: true(R包内置数据时选中)
Depends : 依赖环境
Imports : 需要使用的包
Suggests: 建议配合使用的包
其他如网址、bug报告地址等内容，这里不涉及。

