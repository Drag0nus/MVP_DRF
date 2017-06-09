from django.db import models
from django.utils import timezone

from users.models import User

# Create your models here.


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    # creator = models.(max_length=300, default='None')
    task_description = models.TextField(verbose_name='Task Description',
                                        default='No Description')
    start_date = models.DateTimeField(auto_now_add=True)
    expired_date = models.DateTimeField(verbose_name='Expiration time',
                                        default=timezone.now)
    is_done = models.BooleanField(default='False')


