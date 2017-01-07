from django.shortcuts import render


# Create your views here.
# 主页显示
def home(request):
    # 在templates中增加了一层文件夹 以APP名字命名 因此改变了调用路径
    return render(request, 'learn/home.html')
