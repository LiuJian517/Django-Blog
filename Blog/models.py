# coding:utf8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Catagory(models.Model):
    """
    博客分类
    """
    name = models.CharField('名称',max_length=30)

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField('名称',max_length=16)

    def __str__(self):
        return self.name

class Blog(models.Model):
    """
    博客
    """
    title = models.CharField('标题',max_length=32)
    author = models.CharField('作者',max_length=16)
    content = models.TextField('博客正文')
    created = models.DateTimeField('发布时间',auto_now_add=True)
    catagory = models.ForeignKey(Catagory,verbose_name='分类')
    # ManyToManyField只要在任意一方定义即可
    tags = models.ManyToManyField(Tag,verbose_name='标签')

    def __str__(self):
        '''
        如果定义了unicode()方法但是没有定义str()方法，Django会自动提供一个str()方法调用unicode()方法，
        然后把结果转换为UTF-8编码的字符串对象。
        在实际开发中，建议：只定义unicode()方法，需要的话让Django来处理字符串对象的转换。\
        
        但是python 3.x当中还是使用__str__()方法
        '''
        return self.title

class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog,verbose_name='博客')
    name = models.CharField('称呼',max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容',max_length=240)
    created = models.DateTimeField('发布时间',auto_now_add=True)

    def __str__(self):
        return self.content