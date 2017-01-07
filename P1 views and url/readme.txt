1.Django 的视图和网址设置

2.通过url 以两种方式传递参数 在网页上做加减

3.页面渲染 render reverse的使用
render方法是用于渲染模板，调用该方法会获得使用INSTALLED_APPS 下app中的templates中的文件。

reverse方法是为了动态的获得url.
例如:
	reverse('add2', args=(4,5)) -> '/add/4/5/'
网页模板中：
	不带参数的：
	{% url 'name' %}
	带参数的：参数可以是变量名
	{% url 'name' 参数 %}
	<a href="{% url 'add2' 4 5 %}">link</a>
在url参数的输入格式发生变化后，只要url的name保持不变，就算更改url的正则表达式，依旧能获得正确路径。
但是不适用于参数数量发生变化的情况（暂时看来）
