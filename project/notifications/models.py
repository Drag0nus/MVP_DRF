from django.db import models

from users.models import User

# Create your models here.


class Notification(models.Model):
    text = models.CharField(max_length=300, default='',
                            help_text='Notification text')
    notification_date = models.DateTimeField(help_text='Date of notification', default='')
    user_notified = models.ForeignKey(User, on_delete=models.CASCADE)



