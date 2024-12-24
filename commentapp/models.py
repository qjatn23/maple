from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

from articleapp.models import Article


# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='comment')
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # 유효성 검사: 내용이 비어 있지 않은지 확인
        if not self.content.strip():
            raise ValidationError('댓글 내용은 비어 있을 수 없습니다.')
        super().save(*args, **kwargs)
