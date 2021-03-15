
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True, null=True)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Comment(models.Model):
    to_chika_post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments',
    )
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    comment = models.CharField(max_length=140, verbose_name='comment')
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        related_name='to_post'
        )

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

'''class ChildComment(models.Model):
    to_chika_post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE,
    )
    to_parent_comment = models.ForeignKey(
        ParentComment, 
        on_delete=models.CASCADE,
        related_name='child_comments',
        null=True
    )
    child_comment = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.child_comment
    def get_absolute_url(self):
        return reverse('post_detail')'''