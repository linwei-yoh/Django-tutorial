1.传递一个基本的字符串到网页上
在render中，以字典的形式传递参数，在模板上 以{{字典的key}}的格式获取内容

2.列表内容的传递，以及 for循环的使用

3.在模板中各段内容间的多个空行无意义，1个即可。不是所见所得形式，换行需要额外操作。

4.字典内容的显示

5.条件判断 与 forloop的使用

{% for item in List %}
    {{ item }}，   			','也是显示内容的一部分
{% endfor %}

{% for item in List %}
    {{ item }}{% if not forloop.last %},{% endif %}    ','是包括在if判断中的如果不符合条件就不执行
{% endfor %}

forloop.counter		索引从 1 开始算
forloop.counter0	索引从 0 开始算
forloop.revcounter	索引从最大长度到 1
forloop.revcounter0	索引从最大长度到 0
forloop.first		当遍历的元素为第一项时为真
forloop.last		当遍历的元素为最后一项时为真
forloop.parentloop	用在嵌套的 for 循环中，获取上一层 for 循环的 forloop

6.当列表可能为空值时用for empty
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>抱歉，列表为空</li>
{% endfor %}
</ul>