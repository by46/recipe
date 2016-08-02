Quickstart
==========
Prerequisites
-------------
* Python 2.7+

* pip

Install
-------
该项目托管在我们的PYPI私有仓库, 所以你可以通过PIP来开速安装，
PIP使用细节可以参照 `PIP使用指南
<http://confluence.newegg.org/display/DFIS/PIP>`_.

通过以下命令快速安装recipe：

::

  pip --trusted-host scmesos06 install -i https://scmesos06/simple recipe



Use
----
查看帮助
```````

成功安装Recipe之后，你可以在命令行执行如下命令，获取帮助信息：

::

  recipe -help

创建项目
```````
你只需要执行如下命令，就可以快速创建项目（默认为python项目）：

::

  recipe startproject <project_name>

* project_name: 这是你需要创建的项目名称
该命令会做两件事：

* 默认使用python.flask项目模板，在当前工作目录下生成名为<project_name>的项目
* 默认jenkins上创建一系列用于持续相关task

当然，你也可以选择使用带参数的命令在创建项目时改变一些默认设置：

::

  recipe startproject -t <flask_name> -r <repository_address> <project_name>

* flask_name: 这是需要创建项目的类型.eg：python.flask

* repository_address: 项目的git仓库地址.在创建项目之前，我们建议先创建项目的git仓库，便于recipe创建jenkins上一系列用于持续相关task。
查看模板
````````
你可以通过 list参数来查看所有的模板：

::

  recipe list

