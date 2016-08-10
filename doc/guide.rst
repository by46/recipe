User Guide
================

当然，你也可以选择使用带参数的命令在创建项目时改变一些默认设置：

::

  recipe startproject -t <flask_name> -r <repository_address> <project_name>

* flask_name: 这是需要创建项目的类型.eg：python.flask

* repository_address: 项目的git仓库地址.在创建项目之前，我们建议先创建项目的git仓库，便于recipe创建jenkins上一系列用于持续相关task。