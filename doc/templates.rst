Templates
=======================
.. |flask| image:: _static/python.flask.png
.. |lib| image:: _static/python.lib.png

Recipe是根据项目模板来构建项目骨架和Jenkins Job，不同项目模板应对不同场景使用。

doc
-----------------------------

该模板还未完成

python.flask
-----------------------------

该模板用于生成web应用骨架，使用Python Flask框架，并添加用于Jenkins的CI文件夹，
用于测试的test文件夹，用于书写文档的doc文件夹，以及项目文件夹。 生成的项目是完整的
可运行的程序， 可以直接执行 ``python run.py`` 运行程序。

下面生成名为demo的项目，目录结构如下：

|flask|

python.lib
------------------------------

该模板用于生成Python Lib 的骨架，包含Jenkins的CI文件夹，用于测试的test文件夹，用于文档
的doc文件夹，项目文件，还有一些必要的资源文件.

下面生成名为demo的项目，目录结构如下：

|lib|