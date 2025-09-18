# 个人网站项目

## 项目概述
这是一个基于Django框架的个人网站项目，包含博客、作品集、简历和聊天功能。

## 功能模块
- **博客系统**：文章发布与展示
- **作品集**：展示个人项目作品
- **简历**：在线简历展示
- **聊天室**：简单的实时聊天功能
- **用户账户**：用户注册与登录

## 技术栈
- Python 3.x
- Django 3.x/4.x
- SQLite 数据库
- HTML5/CSS3/JavaScript
- Django模板系统

## 安装与运行
1. 克隆仓库：
   ```bash
   git clone https://github.com/Tomzhuiowewie/personal_site.git
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 迁移数据库：
   ```bash
   python manage.py migrate
   ```
4. 运行开发服务器：
   ```bash
   python manage.py runserver
   ```
5. 访问 http://localhost:8000

## 项目结构
```
personal_site/
├── apps/                # 各功能应用
│   ├── accounts/        # 用户账户管理
│   ├── blog/            # 博客系统
│   ├── chat/            # 聊天功能
│   ├── portfolio/       # 作品集
│   └── resume/          # 简历
├── personal_site/       # 项目主配置
├── static/              # 静态文件
│   ├── css/
│   └── js/
└── templates/           # 模板文件
    ├── base.html        # 基础模板
    ├── home.html        # 首页
    └── ...              # 其他页面模板
```

## 贡献指南
欢迎提交Pull Request或Issue报告问题。

## 许可证
MIT License
