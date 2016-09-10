Quick Start
==========

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



创建Application
---------------

1. 创建Git仓库
+++++++++++++

首先，你需要在trgit2代码托管仓库上创建一个git仓库，并记录下git仓库地址， 例如：http://trgit2/dfis/demo.git


2. 生成Application
++++++++++++++

使用下列命令快速生成Application：

::

  recipe create --init-repo demo


3. 初始化持续集成流程
+++++++++++++++++

使用 ``deploy`` 命令初始化持续集成流程：

::

  recipe deploy --repo http://trgit2/dfis/demo.git demo


Jenkins会从http://trgit2/dfis/demo.git的develop分支拉取代码，执行持续集成过程。


4. GIT 设置
++++++++++++++

因为我们的recipe已经创建了Application 项目目录，所以 ``git clone`` 已经不在适用，所以你可以参照下面命令设置git仓库：

::

	cd demo
	git config core.autocrlf false
	git remote add origin http://trgit2/dfis/demo.git
	git push --all origin

.. attention::
	禁用autocrlf非常重要， 因为我们项目中包含了用于CI流程的shell脚本， ``LF`` 不能被替换成 ``CRLF``。

	在我们初始化Application时，已经初始化好了本地GIT仓库，并且你预先创建master， develop， feature-doc(用于书写项目文档)三个分支，
	所以只需要简单的设置远端GIT仓库地址，并同步master， develop，feature-doc分支代码到trgit2。

5. GDEV 和 GQC
+++++++++++++++++++



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


