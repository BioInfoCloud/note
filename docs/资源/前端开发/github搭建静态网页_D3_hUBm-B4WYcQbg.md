# github搭建静态网页

<font style="color:rgb(24, 25, 28);">Material for MkDocs官方文档</font>

[https://www.mkdocs.org/getting-started/](https://www.mkdocs.org/getting-started/)  
<font style="color:rgb(24, 25, 28);">https://squidfunk.github.io/mkdocs-material/getting-started/</font>  
<font style="color:rgb(24, 25, 28);">GitHub Pages 简介</font>  
<font style="color:rgb(24, 25, 28);">https://yang-xijie.github.io/BLOG/</font>Markdown<font style="color:rgb(24, 25, 28);">/github-pages/ </font>  
<font style="color:rgb(24, 25, 28);">mdBook构建示例</font>  
<font style="color:rgb(24, 25, 28);">https://yang-xijie.github.io/BLOG/Markdown/mdbook-site/</font>  
<font style="color:rgb(24, 25, 28);">mdBook官方文档</font>  
<font style="color:rgb(24, 25, 28);">https://rust-lang.github.io/mdBook/</font>  
<font style="color:rgb(24, 25, 28);">MkDocs构建示例</font>  
<font style="color:rgb(24, 25, 28);">https://yang-xijie.github.io/BLOG/Markdown/mkdocs-site</font>

<font style="color:rgb(24, 25, 28);"></font>

# <font style="color:rgb(24, 25, 28);">1.安装MKdocs</font>
[https://www.mkdocs.org/user-guide/installation/](https://www.mkdocs.org/user-guide/installation/)

```r
pip install mkdocs
```

# 2.<font style="color:rgb(68, 68, 68);">Creating a new project</font>
```r
mkdocs new bioinfocloud
cd bioinfocloud
```

![1664599059098-129b629f-28eb-4a0a-a681-b473ffc28200.png](./img/D3_hUBm-B4WYcQbg/1664599059098-129b629f-28eb-4a0a-a681-b473ffc28200-667607.png)

<font style="color:rgb(73, 80, 87);">There's a single configuration file named</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(51, 51, 51);">mkdocs.yml</font><font style="color:rgb(73, 80, 87);">, and a folder named</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(51, 51, 51);">docs</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(73, 80, 87);">that will contain your documentation source files (</font><font style="color:rgb(51, 51, 51);">docs</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(73, 80, 87);">is the default value for the</font><font style="color:rgb(73, 80, 87);"> </font>[docs_dir](https://www.mkdocs.org/user-guide/configuration/#docs_dir)<font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(73, 80, 87);">configuration setting). Right now the</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(51, 51, 51);">docs</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(73, 80, 87);">folder just contains a single documentation page, named</font><font style="color:rgb(73, 80, 87);"> </font><font style="color:rgb(51, 51, 51);">index.md</font><font style="color:rgb(73, 80, 87);">.</font>

<font style="color:rgb(73, 80, 87);">MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it. Make sure you're in the same directory as the </font><font style="color:rgb(51, 51, 51);">mkdocs.yml</font><font style="color:rgb(73, 80, 87);"> configuration file, and then start the server by running the </font><font style="color:rgb(51, 51, 51);">mkdocs serve</font><font style="color:rgb(73, 80, 87);"> command:</font>

```r
mkdocs serve
```



**<font style="color:rgb(42, 43, 46);">现在尝试编辑配置文件:mkdocs.yml。将site_name设置更改为BioInfoCloud并保存文件。</font>**

```r
site_name: BioInfoCloud
site_url: https://example.com/
```

3.

```r
mkdir .github
cd .github
mkdir workflows
cd workflows
```

在workflows目录下创建一个yml文件，文件名自定义，文件内容为：

```r
name: publish site
on: # 在什么时候触发工作流
  push: # 在从本地main分支被push到GitHub仓库时
    branches:
      - main
  pull_request: # 在main分支合并别人提的pr时
    branches:
      - main
jobs: # 工作流的具体内容
  deploy:
    runs-on: ubuntu-latest # 创建一个新的云端虚拟机 使用最新Ubuntu系统
    steps:
      - uses: actions/checkout@v2 # 先checkout到main分支
      - uses: actions/setup-python@v2 # 再安装Python3和相关环境
        with:
          python-version: 3.x
      - run: pip install mkdocs-material # 使用pip包管理工具安装mkdocs-material
      - run: mkdocs gh-deploy --force # 使用mkdocs-material部署gh-pages分支
```

Adding pages

Now add a second page to your documentation:

```r
curl 'https://jaspervdj.be/lorem-markdownum/markdown.txt' > docs/about.md
```

# <font style="color:rgba(0, 0, 0, 0.87);">3.Git and GitHub</font>[¶](https://yang-xijie.github.io/BLOG/Markdown/mkdocs-site/#git-and-github)
```r
$ git init
$ git add .
$ git commit -m "init"
```

**<font style="color:rgba(0, 0, 0, 0.87);">GitHub - New Repository</font>**[**¶**](https://yang-xijie.github.io/BLOG/Markdown/mkdocs-site/#github-new-repository)

<font style="color:rgba(0, 0, 0, 0.87);">GitHub > New Repository</font>

<font style="color:rgba(0, 0, 0, 0.87);">GitHub > Repository > Settings > Actions > General ></font>

+ <font style="color:rgba(0, 0, 0, 0.87);">Actions permissions: Allow all actions and reusable workflows</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">Workflow permissions: Read and write permissions</font>
+ <font style="color:rgba(0, 0, 0, 0.87);">Click Save</font>

设置Page

![1664630874491-42193745-9385-44c6-892c-1766c0a75fcd.png](./img/D3_hUBm-B4WYcQbg/1664630874491-42193745-9385-44c6-892c-1766c0a75fcd-767741.png)

```r
$ git remote add origin git@github.com:BioInfoCloud/bioinfocloud.git # change to your github repo
$ git branch -M main
$ git push -u origin main
```





# 4.主题
[https://squidfunk.github.io/mkdocs-material/getting-started/](https://squidfunk.github.io/mkdocs-material/getting-started/)

```r
pip install mkdocs-material
git clone https://github.com/squidfunk/mkdocs-material.git
pip install -e mkdocs-material
```

5.其他发布平台

[https://www.netlify.com/](https://www.netlify.com/)



> 更新: 2022-10-02 09:45:12  
> 原文: <https://www.yuque.com/doublehelix/bioinfonotes/lf2277>