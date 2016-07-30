# Recipe
该项目用于创建统一风格的项目骨架，并加入必要资源文件及文件夹， 同时创建持续集成相关的Jenkins Task。
主要目的是规范开发流程，规范开发风格，减少手工的、重复的工作量。

## 为什么取名为Recipe
我们希望只要你告诉我们项目类型，我们就可以烹饪出你需要的项目， 就像菜谱一样。

## Prerequisites
- [Python 2.7+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)

## Install

该项目托管在我们的[PYPI私有仓库](https://scmesos06), 所以你可以通过PIP来开速安装， PIP使用细节可以参照[这里](http://confluence.newegg.org/display/DFIS/PIP).

通过以下命令快速安装recipe：
```shell
pip --trusted-host scmesos06 install -i https://scmesos06/simple recipe

```

## QuickStart

成功安装Recipe之后，你可以在命令行执行如下命令，获取帮助信息：

```shell
recipe -h

```

### 创建项目

你只需要执行如下命令，就可以快速创建项目：
```shell
recipe startproject demo
```

该命令会完成两件事情：
 - 默认使用python.flask项目模板，在当前工作目录下生成名为demo的项目
 - 默认jenkins上创建一系列用于持续相关task

