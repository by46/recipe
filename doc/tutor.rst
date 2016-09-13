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

.. attention::
	这里我们使用demo用于演示，但是你不应该使用该名称，我们建议你参考 `Application 命名规范 <misc.html>`_


2. 生成Application
++++++++++++++

使用下列命令快速生成Application：

::

  recipe create --init-repo demo


3. 启动持续集成
+++++++++++++++++

使用 ``deploy`` 命令初始化持续集成流程：

::

  recipe deploy --repo http://trgit2/dfis/demo.git demo


Jenkins会从http://trgit2/dfis/demo.git的develop分支拉取代码，执行持续集成过程。


4. 同步代码
++++++++++++++

在生成Application时，Recipe已经创建了本地GIT仓库，并且已经为你预先创建了master， develop， feature-doc(用于书写项目文档)三个分支，
所以只需要简单的设置远端GIT仓库地址，并同步master， develop，feature-doc分支代码到trgit2。

所以你可以参照下面命令设置git仓库：

::

	cd demo
	git config core.autocrlf false
	git remote add origin http://trgit2/dfis/demo.git
	git push --all origin

.. attention::
	禁用autocrlf非常重要， 因为我们项目中包含了用于持续集成过程的shell脚本， ``LF`` 不能被替换成 ``CRLF``。

	Application第一次初始化时，会比较耗时，可能需要等待5-10分钟，请你耐性等待。


5. 验证
++++++++++++++
当一切就绪之后，我们已经部署GDEV和GQC两个环境，你可以通过访问下列url验证application。

GDEV
*******************************
http://SCMESOS02/demo/version

GQC
*******************************
http://S1QDFIS02/demo/version


.. attention::
	如果你的项目名称中带有 :code:`连接号(-)` , 会被替换为下划线(_)，例如项目名为dfis-mq-distributor
	那么服务地址为： http://SCMESOS02/dfis_mq_distributor/version.
