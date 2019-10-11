from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        # admin 显示用
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    # 外键 blog_type是一个对象
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        '''文章排序处理'''
        ordering = ['-create_time']