from django.shortcuts import render
from django.utils import timezone
from .models import BlogPost

def blog_list_view(request):
    # Sample blog posts
    posts = [
        {
            'title': 'Django入门指南',
            'content': 'Django是一个高级Python Web框架，鼓励快速开发和简洁实用的设计...',
            'created_at': timezone.now(),
            'tags': 'django, python, web开发',
            'author': {'username': 'admin'}
        },
        {
            'title': 'React核心概念解析',
            'content': 'React是一个用于构建用户界面的JavaScript库...',
            'created_at': timezone.now(),
            'tags': 'react, javascript, 前端',
            'author': {'username': 'admin'}
        }
    ]
    return render(request, 'blog/list.html', {'posts': posts})

def blog_detail_view(request, pk=None):  # Make pk optional
    # Sample blog post detail
    post = {
        'title': 'Django入门指南',
        'content': '''
        <h2>什么是Django？</h2>
        <p>Django是一个高级Python Web框架，鼓励快速开发和简洁实用的设计。</p>
        
        <h2>主要特性</h2>
        <ul>
            <li>强大的ORM系统</li>
            <li>自动生成管理后台</li>
            <li>完善的文档</li>
            <li>活跃的社区</li>
        </ul>
        
        <h2>安装Django</h2>
        <pre><code>pip install django</code></pre>
        ''',
        'created_at': timezone.now(),
        'tags': 'django, python, web开发',
        'author': {'username': 'admin'}
    }
    return render(request, 'blog/detail.html', {'post': post})
