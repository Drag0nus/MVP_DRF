# 1. While user updated (patch), update weather field. https://openweathermap.org/current
# 2. Create Notification model, (id, text, date, user_id). While new user created,
# send gratz in 30 days
# 3. periodically tasks. Each 12h, create Notification object with text='SLAVA UKRAINI"
from celery.schedules import crontab

from django_app.celery_app import app
from django.utils import timezone

from notifications.models import Notification
from users.models import User


@app.task()
def congratz_after_30days(pk):
    # user = User.objects.get(pk=pk)
    notification_text = 'Congratulations being 30 days in this shitty site...Stay on!'
    notification = Notification(user_notified_id=pk,
                                notification_date=timezone.now(),
                                text=notification_text)
    notification.save()
    return notification_text


# minute=0, hour='*/12'


@app.task
def slava_ukr_notification():
    users = User.objects.all()
    for user in users:
        notification = Notification(user_notified=user,
                                    notification_date=timezone.now(),
                                    text='СЛАВА УКРАЇНІ!!!')
        notification.save()
    return 'PERIODIC TASK!'


""""
apply_async(eta=datetime.combine(new_time.today(), day_info.time_open) + relativedelta(hours=-3, minutes=10), args=[company.id, company.phone])
user_info_sms.delay(str(request.user.phone), send_message)

"""
