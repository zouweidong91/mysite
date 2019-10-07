# mysite
个人博客

# 执行命令
## 创建项目和app
* django-admin startproject mysite
* python manage.py startapp blog

## 初始化数据库和创建超级管理员
```
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
* python manage.py runserver # 启动本地服务


## 部署命令
* pip freeze > requirements.txt
* pip install -r requirements.txt