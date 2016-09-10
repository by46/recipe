temp
===================

.. |help| image:: _static/help.png

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

通过该命令会默认使用python.flask项目模板，并且在当前工作目录下生成名为demo的项目

现在我们提供了多种项目模板，你可以添加参数 ``--template`` 来切换使用的项目, 使用方式如下：

::

	recipe create --template python.lib demo

你可以通过 ``list`` 命令来查看有哪些可用的模板，详细使用请参考 `查看模板`_ 。