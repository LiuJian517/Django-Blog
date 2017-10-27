"""MyDjango2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Blog.views import *

'''
一旦其中的一个正则表达式匹配上，Django 将导入并调用给出的视图，它是一个简单的Python 函数（或者一个基于类的视图）。
视图将获得如下参数:
1) 一个HttpRequest 实例。
2) 如果匹配的正则表达式返回了没有命名的组，那么正则表达式匹配的内容将作为位置参数提供给视图。
3) 关键字参数由正则表达式匹配的命名组组成，但是可以被django.conf.urls.url()的可选参数kwargs覆盖。
'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/$',get_blogs),
    # 每个正则表达式前面的'r' 是可选的但是建议加上。它告诉Python 这个字符串是“原始的” —— 字符串中任何字符都不应该转义。
    url(r'^detail/(\d+)/$',get_details ,name='blog_get_detail'),
    url(r'^data/$',get_json),
]
