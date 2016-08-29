Quick Start
==========
.. |help| image:: _static/help.png

依赖
--------------------

* `Python 2.7+ <http://www.python.org/>`_
* `PIP <https://pip.pypa.io/en/stable/>`_


安装
--------------------

该项目托管在我们的PYPI私有仓库, 所以你可以通过PIP来快速安装，
PIP使用细节可以参照 `PIP使用指南
<http://confluence.newegg.org/display/DFIS/PIP>`_.

通过以下命令快速安装recipe：

::

  pip --trusted-host scmesos06 install -i http://scmesos06/simple recipe



查看帮助
---------

成功安装Recipe之后，你可以在命令行执行如下命令，获取帮助信息：

::

  recipe -h
  recipe --help

或者你可以通过以下命令行查看某个具体子命令使用规则，以create命令为例：

::

   recipe create -h
   recipe create --help


命令执行结果如下：
|help|

创建项目
---------------

1. 创建Git仓库
+++++++++++++

首先，你需要在trgit2代码托管仓库上创建一个git仓库，记录下git仓库地址， 例如：http://trgit2/dfis/demo.git


2. 生成项目
++++++++++++++

然后，你只需要执行如下命令，就可以快速创建项目：

::

  recipe create demo

通过该命令会默认使用python.flask项目模板，并且在当前工作目录下生成名为demo的项目

现在我们提供了多种项目模板，你可以添加参数 ``--template`` 来切换使用的项目, 使用方式如下：

::

	recipe create --template python.lib demo

你可以通过 ``list`` 命令来查看有哪些可用的模板，详细使用请参考 `查看模板`_ 。

3. 创建Jenkins CI Jobs
++++++++++++++

接下来是在Jenkins上创建持续集成相关Jobs，我们可以通过使用 ``deploy`` 命令就可以轻松完成命令如下：

::

  recipe deploy --template python.flask --repo http://trgit2/dfis/demo.git demo

它会创建一系列Jenkins jobs，并且把http://trgit2/dfis/demo.git仓库的develop分支作为VCS源。


.. attention::
	实际上，创建项目和创建Jenkins Job是可以一步完成的，你只需要在使用 ``create`` 命令时，添加 ``--deploy``
	参数， 命令如下：

	::

		recipe create --repo http://trgit2/dfis/demo.git --deploy demo


4. GIT 设置
++++++++++++++

因为我们的recipe已经创建了demo文件夹，所以 ``git clone`` 已经不在适用，所以你可以参照下面命令初始化本地git仓库：

::

	cd demo
	git init
	git config core.autocrlf false
	git remote add origin http://trgit2/dfis/demo.git
	git add --all
	git commit -a -m 'init'
	git push origin master

.. attention::
	禁用autocrlf非常重要， 因为我们项目中包含了用于CI流程的shell脚本， ``LF`` 不能被替换成 ``CRLF``。


查看模板
---------------

Recipe 提供了多种项目模板，你可以通过 list参数来查看所有可用的模板：

::

  recipe list


查看版本信息
---------------

你可以通过version子命令来检查项目版本：

::

	recipe version


