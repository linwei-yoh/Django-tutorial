1.ģ���ʹ�� INSTALLED_APPS,render ,templates

2.�������ݿ��
	python manage.py syncdb 
	# Django 1.9.x �Լ���Ҫ��
	python manage.py migrate

3.ģ��Ĳ��һ���
��������ÿ��app��templates�ж���һ�� index.html����������views.py��ʹ�õ�ʱ��ֱ��дһ�� render(request, 'index.html')��Django �ܲ����ҵ���ǰ app �� templates �ļ����е� index.html �ļ�����?
���ǲ�һ���ܣ��п����Ҵ�

Django ģ����һ��ƣ� Django ����ģ��Ĺ�������ÿ�� app �� templates �ļ������ң�����ֻ�ǵ�ǰ app �еĴ���ֻ�ڵ�ǰ�� app �� templates �ļ������ң������� app �� templates �γ�һ���ļ����б�Django ��������б�һ�����ļ��н��в��ң�����ĳһ���ļ����ҵ���ʱ���ֹͣ�����еĶ��������˻��Ҳ���ָ����ģ���ʱ����� Template Not Found ������������Python�Ұ������������������ȻҲ�бף������ǵĵط���һ��app��������һ��app��ģ���ļ��������п��ܻ��Ҵ��ˡ���������ʹ�õ�ʱ���� templates �н���һ�� app ͬ�����ļ��У������ͺ��ˡ�

�����Ҫ��ÿ��app�е� templates �ļ������ٽ�һ�� app �����ƣ����͸�app��ص�ģ����� app/templates/app/ Ŀ¼���档

����ʱģ���ʹ�þͱ����"app/index.html" �����ĸ�ʽ ��������ԭ�ȵ�ֱ��index.html

3.ģ���extend include blockʹ�� 
��ģ���ļ��У�ע�͵�������������Ч��
extend ҳ��ļ̳й�ϵ�Ͷ���ļ̳��������ƣ�û����д��block��ֱ��ִ�и�ҳ�档

