---
title: Git实例
---

# Git实例

## git init/add/status/diff/commit/status/add/commit/log/diff

### 初始化仓库

```
$ cd ./github
$ mkdir notes
$ cd notes
$ git init
Initialized empty Git repository in ./.git/
```

### 添加一个文件

```
$ touch markdown_learn.md
$ vim markdown_learn.md
$ cat markdown_learn.md
# Markdown Note
# Grammar
`#`: title

[](): add link

![](): add image
```

### 查看状态

```
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	markdown_learn.md

nothing added to commit but untracked files present (use "git add" to track)
```

### 添加文件到暂存区

```
$ git add markdown_learn.md
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   markdown_learn.md
```

### 再添加一篇文件

```
$ touch git_learn.md
$ vim git_learn.md
$ cat git_learn.md
# Git Note
# About Git
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

# Git Commands
`git add <file>`
`git commit -m "<msg>"`
```

### 查看状态

```
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   markdown_learn.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	git_learn.md
```

### 修改文件

```
$ vim markdown_learn.md
# Markdown Note
# Grammar
`#`: title

[](): add link

![](): add image

**bold_text**

*italic_text*
```

### 再次查看状态

```
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   markdown_learn.md

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   markdown_learn.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	git_learn.md
```

### 添加gitignore

我们希望一次添加这两个文件，在这之前先创建`.gitignore`：

```
$ touch .gitignore
$ echo ".DS_Store" >> .gitignore

$ git add .
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   .gitignore
	new file:   git_learn.md
	new file:   markdown_learn.md
```

### 提交

```
$ git commit -m "add two notes"
[main (root-commit) bdf79c8] add two notes
 3 files changed, 19 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 git_learn.md
 create mode 100644 markdown_learn.md
```

### 查看状态

```
$ git status
On branch main
nothing to commit, working tree clean
```

### 添加和提交

```
$ vim git_learn.md
$ cat git_learn.md
# Git Note
# About Git
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

# Git Commands
`git add <file>`
`git commit -m "<msg>"`
`git status`

$ git add .
$ git commit -m "add new git commands"
[main c874462] add new git commands
 1 file changed, 1 insertion(+)
```

### 查看log

```
$ git log
commit c874462dba874eb098a4445f8ff6a15b2e381fc7 (HEAD -> main)
Author: yxj <564197835@qq.com>
Date:   Thu May 20 20:42:43 2021 +0800

    add new git commands

commit bdf79c8b45ebdd1e7644d0a19b47b8c4cba84f9a
Author: yxj <564197835@qq.com>
Date:   Thu May 20 20:40:03 2021 +0800

    add two notes
```

### 比较差异

比较两次commit的差异（其中前面有加号的是第二次提交添加的，剩下的信息并不那么重要）：

```
$ git diff bdf79c c87446
diff --git a/git_learn.md b/git_learn.md
index 575b88e..1b60d22 100644
--- a/git_learn.md
+++ b/git_learn.md
@@ -5,3 +5,4 @@ Git is a free and open source distributed version control system designed to han
 # Git Commands
 `git add <file>`
 `git commit -m "<msg>"`
+`git status`
```

## git restore

`git restore` 是 Git 2.23 引入的命令，专门用来“撤销改动”，把 `git checkout -- <file>` 和 `git reset HEAD <file>` 这两件容易混淆的事情拆成了两个清晰的参数。

**（1）撤销工作区的修改**（把文件恢复成最近一次 commit 的样子）：

```
$ git status
modified:   git_learn.md
$ git restore git_learn.md
$ git status
nothing to commit, working tree clean
```

⚠️ 这一步会**直接丢弃**你还没提交的改动，且不可恢复，执行前请确认。

**（2）把已 `git add` 的文件撤出暂存区**（文件内容不变，只是不再被跟踪为“待提交”）：

```
$ git add git_learn.md
$ git restore --staged git_learn.md
$ git status
 Changes not staged for commit:
   modified:   git_learn.md
```

**（3）两条一起用**：既撤出暂存区，又丢弃工作区改动，等于把这个文件彻底还原：

```
$ git restore --staged --worktree git_learn.md
```

| 想做的事 | 旧写法 | 新写法 |
| --- | --- | --- |
| 撤销工作区改动 | `git checkout -- <file>` | `git restore <file>` |
| 撤出暂存区 | `git reset HEAD <file>` | `git restore --staged <file>` |
| 两者都撤销 | `git checkout HEAD -- <file>` | `git restore -SW <file>` |

> `git restore` 只管**文件**；想移动分支指针、撤销整次提交，用 `git reset`。

## git branch/switch

### 新建仓库并初始化

```
$ cd ~/Desktop
$ mkdir teamwork
$ cd teamwork
$ git init
```

### 添加文件在main分支至少有一次commit

```
$ touch README.md
$ echo  'This is our teamwork!'  >> README.md
$ cat README.md
This is our teamwork!
$ git add README.md
$ git commit -m "add README"
[main (root-commit) 605051f] add README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

### 在sayHello分支上写代码

```
$ git branch -c sayHello
$ git switch sayHello
Switched to branch 'sayHello'
$ touch sayHello.swift
$ vim sayHello.swift
$ cat sayHello.swift
func sayHello(name: String) {
    print("Hello, \(name).")
}
$ git add sayHello.swift
$ git commit -m "add func sayHello"
[sayHello e30ff7a] add func sayHello
 1 file changed, 3 insertions(+)
 create mode 100644 sayHello.swift
```

### 回到main分支进行合并

```
$ git switch main
Switched to branch 'main'
$ git merge sayHello
Updating 605051f..e30ff7a
Fast-forward
 sayHello.swift | 3 +++
 1 file changed, 3 insertions(+)
 create mode 100644 sayHello.swift
$ git log
 Untracked files:
commit e30ff7a9797f9577b056c91cdbc46b37bff71168 (HEAD -> main, sayHello)
Author: yxj <564197835@qq.com>
Date:   Fri May 21 18:37:09 2021 +0800

    add func sayHello

commit 605051f10e676b477d5f101dca5828cf34165ab6
Author: yxj <564197835@qq.com>
Date:   Fri May 21 18:30:57 2021 +0800

    add README
```

### 在goodMorning分支上写代码

同上述`在sayHello分支上写代码`的内容，之后也是回到`main分支`进行合并

## 向GitHub上的开源项目提交代码

给别人的仓库贡献代码，不能直接往人家仓库里推，标准流程是 **Fork → Clone → 新建分支 → 提交 → Push → Pull Request**。

### （1）Fork 仓库

在目标项目页面右上角点 **Fork**，GitHub 会在你自己的账号下复制一份完整仓库，比如 `https://github.com/<你的用户名>/<项目名>`。

### （2）克隆自己那份

```
$ git clone git@github.com:<你的用户名>/<项目名>.git
$ cd <项目名>
```

### （3）关联上游仓库，方便后续同步

```
$ git remote add upstream https://github.com/<原作者>/<项目名>.git
$ git remote -v
origin    git@github.com:<你的用户名>/<项目名>.git (fetch)
origin    git@github.com:<你的用户名>/<项目名>.git (push)
upstream  https://github.com/<原作者>/<项目名>.git (fetch)
upstream  https://github.com/<原作者>/<项目名>.git (push)
```

### （4）从最新代码开一个分支

不要直接在 `main` 上改，一个功能（或一个 bug 修复）对应一个分支：

```
$ git switch main
$ git fetch upstream
$ git merge upstream/main       # 或者 git reset --hard upstream/main
$ git switch -c fix-typo-readme
```

### （5）改代码并提交

```
$ vim README.md
$ git add README.md
$ git commit -m "docs: fix typo in README"
```

提交信息的通行写法是 `<type>: <说明>`，常用 type 有 `feat`（新功能）、`fix`（修复）、`docs`（文档）、`refactor`（重构）、`test`（测试）、`chore`（杂项）。

### （6）推到自己仓库

```
$ git push -u origin fix-typo-readme
```

### （7）发起 Pull Request

回到自己仓库的 GitHub 页面，会出现黄色的 **Compare & pull request** 按钮；点进去写清“改了什么、为什么改”，选择正确的目标分支（通常是上游仓库的 `main`），提交即可。

### （8）按评审意见修改

评审让你改时，**不需要**关掉 PR 重新来一遍——只要在同一个分支上继续 commit 并 `git push`，PR 会自动更新。

```
$ vim README.md
$ git add README.md
$ git commit -m "docs: address review comments"
$ git push
```

### （9）合并后清理

PR 被合并之后，可以删掉本地和远程的功能分支：

```
$ git switch main
$ git fetch upstream && git merge upstream/main
$ git branch -d fix-typo-readme
$ git push origin --delete fix-typo-readme
```

> 小提示：如果只是改错别字、补文档这类小改动，也可以在 GitHub 网页上直接编辑文件，网页会**自动帮你 Fork 并开分支**，然后一步跳到发起 PR，不需要碰命令行。
