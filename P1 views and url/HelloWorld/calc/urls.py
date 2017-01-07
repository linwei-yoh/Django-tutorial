from django.conf.urls import url

from calc import views

urlpatterns = [
    # 将类似2_3/ 的url传递给old_add2_redirect方法 通过reverse 和重定向方法获得add2的url格式
    url(r'(\d+)_(\d+)/$', views.old_add2_redirect),
    url(r'(\d+)/(\d+)/$', views.add2, name='add2'),
    url(r'^$', views.add, name='add'),
]
