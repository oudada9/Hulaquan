from django.db import models


class UserInfo(models.Model):
    '''用户表'''
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=128)

    class Mate:
        models = 'user'


class Article(models.Model):
    '''文章表'''
    categroy_choices = [
        (1, '资讯'),
        (2, '公司动态'),
        (3, '分享'),
        (4, '答疑'),
        (5, '其他'),
    ]
    categroy = models.IntegerField(verbose_name='分类', choices=categroy_choices)
    title = models.CharField(verbose_name='标题', max_length=32)
    image = models.CharField(verbose_name='图片路径', max_length=128)
    summary = models.CharField(verbose_name='简介', max_length=255)

    comment_count = models.IntegerField(verbose_name='评论数', default=0)
    read_count = models.IntegerField(verbose_name='浏览数', default=0)

    author = models.ForeignKey(verbose_name='作者', to=UserInfo, on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Mate:
        models = 'Article'


class ArticleDetail(models.Model):
    article = models.OneToOneField(verbose_name='文章表', to='Article', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='内容')

    class Mate:
        models = 'ArticleDetail'


class Comment(models.Model):
    '''评论表'''
    article = models.ForeignKey(verbose_name='文章', to="Article", on_delete=models.CASCADE)
    content = models.TextField(verbose_name='评论')
    user = models.ForeignKey(verbose_name='评论者', to='UserInfo', on_delete=models.CASCADE)
    parent = models.ForeignKey(verbose_name='回复', to='self', null=True, blank=True, on_delete=models.CASCADE)  # to='self'是给自己做关联，也可以写成to='Comment'

    class Mate:
        models = 'Comment'
