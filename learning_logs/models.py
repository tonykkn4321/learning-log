from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """用戶學習的主題。"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """返回模型的字符串表示。"""
        return self.text

class Entry(models.Model):
    """學到的有關某個主題的具體知識。"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        """返回模型的字符串表示。"""
        return f"{self.text[:50]}..."