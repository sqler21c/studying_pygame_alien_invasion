from django.db import models

# Create your models here.

class Topic(models.Model):
    """사용자가 배우는 주제

    Args:
        models (_type_): _description_
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """객체의 문자열 표현을 반환합니다."""
        return self.text
    