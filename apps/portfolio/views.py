from django.shortcuts import render
from .models import PortfolioProject

def portfolio_view(request):
    # Sample portfolio projects
    projects = [
        {
            'name': '智能家居系统',
            'description': '基于物联网的智能家居控制系统，支持手机远程操控',
            'link': '#',
            'github': '#'
        },
        {
            'name': '在线教育平台',
            'description': '全功能在线学习管理系统，支持视频直播和互动',
            'link': '#',
            'github': '#'
        },
        {
            'name': '健康监测APP',
            'description': '移动端健康数据追踪应用，集成多种健康指标分析',
            'link': '#',
            'github': '#'
        }
    ]
    return render(request, 'portfolio/list.html', {'projects': projects})
