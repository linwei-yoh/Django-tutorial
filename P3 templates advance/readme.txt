1.����һ���������ַ�������ҳ��
��render�У����ֵ����ʽ���ݲ�������ģ���� ��{{�ֵ��key}}�ĸ�ʽ��ȡ����

2.�б����ݵĴ��ݣ��Լ� forѭ����ʹ��

3.��ģ���и������ݼ�Ķ�����������壬1�����ɡ���������������ʽ��������Ҫ���������

4.�ֵ����ݵ���ʾ

5.�����ж� �� forloop��ʹ��

{% for item in List %}
    {{ item }}��   			','Ҳ����ʾ���ݵ�һ����
{% endfor %}

{% for item in List %}
    {{ item }}{% if not forloop.last %},{% endif %}    ','�ǰ�����if�ж��е���������������Ͳ�ִ��
{% endfor %}

forloop.counter		������ 1 ��ʼ��
forloop.counter0	������ 0 ��ʼ��
forloop.revcounter	��������󳤶ȵ� 1
forloop.revcounter0	��������󳤶ȵ� 0
forloop.first		��������Ԫ��Ϊ��һ��ʱΪ��
forloop.last		��������Ԫ��Ϊ���һ��ʱΪ��
forloop.parentloop	����Ƕ�׵� for ѭ���У���ȡ��һ�� for ѭ���� forloop

6.���б����Ϊ��ֵʱ��for empty
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% empty %}
    <li>��Ǹ���б�Ϊ��</li>
{% endfor %}
</ul>