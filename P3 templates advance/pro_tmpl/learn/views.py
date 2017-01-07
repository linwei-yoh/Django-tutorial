# -*- coding: utf-8 -*-
from django.shortcuts import render


# Create your views here.
 
def home(request):
    # 基本字符串传递
    strval = u'字符串变量传递测试'
    # 基本for循环和list内容显示  
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # 字典内容显示
    info_dict = {'site': u'AL的site', 'content': u'各种测试'}
    
    return render(request,'learn/home.html',{'strkey':strval,'listkey':TutorialList,'infokey':info_dict})
 
