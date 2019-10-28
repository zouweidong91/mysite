# mysite
个人博客

# 执行命令
## 创建项目和app
* django-admin startproject mysite
* python manage.py startapp blog

## 初始化数据库和创建超级管理员
```
后台管理http://127.0.0.1:8000/admin 密码 123456  用户名 zwd
修改settings文件:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blog',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '3306'
        }
    }
    blog 加入 INSTALLED_APPS中 
安装mysqlclient
    whl文件下载地址：
        https://pypi.org/project/mysqlclient/#files
    pip install 
    C:\Users\70756\Downloads\mysqlclient-1.4.4-cp36-cp36m-win_amd64.whl

创建mysql数据库
    create database blog;
```
* python manage.py makemigrations  # 迁移文件
* python manage.py migrate   # 同步数据库
* python manage.py createsuperuser # 创建超级管理员
* python manage.py runserver 8000 # 启动本地服务 默认8000端口
* python manage.py shell  # 命令行模式
    from blog.models import Blog
    blog = Blog()
    blog.title = 'XXX'
    blog.save()
    此时数据便保存至数据库

    命令行下巧用  dir(var)  help(function)

* shift + f5 强制刷新
## 部署命令
* pip freeze > requirements.txt
* pip install -r requirements.txt


# setting  文件配置方法  查找
pypi python  搜索相关包 ckeditor