from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
# /?a=1&b=2
def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# /1/2/
def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

# 将app放入INSTALLED_APPS中后，调用index() 就会通过render渲染app路径下templates中的 名为"home.html"的文件
def index(request):
    return render(request, "home.html")

# 两种url的适配器 就是转化一种格式的url到另外一种格式，
def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
