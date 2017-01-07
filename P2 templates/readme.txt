1.模板的使用 INSTALLED_APPS,render ,templates

2.建立数据库表
	python manage.py syncdb 
	# Django 1.9.x 以及上要用
	python manage.py migrate

3.模板的查找机制
假如我们每个app的templates中都有一个 index.html，当我们在views.py中使用的时候，直接写一个 render(request, 'index.html')，Django 能不能找到当前 app 的 templates 文件夹中的 index.html 文件夹呢?
答案是不一定能，有可能找错

Django 模板查找机制： Django 查找模板的过程是在每个 app 的 templates 文件夹中找（而不只是当前 app 中的代码只在当前的 app 的 templates 文件夹中找）。各个 app 的 templates 形成一个文件夹列表，Django 遍历这个列表，一个个文件夹进行查找，当在某一个文件夹找到的时候就停止，所有的都遍历完了还找不到指定的模板的时候就是 Template Not Found （过程类似于Python找包）。这样设计有利当然也有弊，有利是的地方是一个app可以用另一个app的模板文件，弊是有可能会找错了。所以我们使用的时候在 templates 中建立一个 app 同名的文件夹，这样就好了。

这就需要把每个app中的 templates 文件夹中再建一个 app 的名称，仅和该app相关的模板放在 app/templates/app/ 目录下面。

而此时模板的使用就变成了"app/index.html" 这样的格式 ，而不是原先的直接index.html

3.模板的extend include block使用 
在模板文件中，注释掉的内容依旧有效？
extend 页面的继承关系和对象的继承作用类似，没被重写的block将直接执行父页面。

