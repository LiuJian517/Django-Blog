from django.shortcuts import render, render_to_response

# Create your views here.
from Blog.models import *
from Blog.forms import CommentForm
from django.http import Http404,HttpResponse

import json


def get_blogs(request):
    blogs = Blog.objects.all().order_by('-created')
    return render_to_response('blog-list.html', {'blogs': blogs})

def get_json(request):
    data = {}
    data['name'] = "liujian"
    data['age'] = 25
    return HttpResponse(json.dumps(data),content_type = "application/json")

def get_details(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    # 使用render_to_response的话就无法对表单进行验证了，所以还是需要使用render方法。
    # 如果去掉模板中的{% csrf_token %} 用于防跨域请求。就可以了
    return render(request, 'blog_details.html', ctx)
