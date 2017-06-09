from django_app.celery_app import app
from users.models import User
from users.serializers import UserSerializer
from django.utils import timezone
import requests


@app.task()
def make_file(trigger=None):
    if trigger:
        test_file = open('./test-file.txt', 'w')
        test_file.write('Sup, bro! Its task')
        return 'DONE!!!!'


@app.task()
def get_weather(pk, trigger=None):
    if trigger:
        API_KEY = 'b04f1e40353fbbe233b4b8a84ccc625e'
        user = User.objects.get(pk=pk)
        print(user)
        request = 'http://samples.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (user.city, API_KEY)
        print(request)
        result = requests.get(request).json()
        user.weather = '%s, %s, %s' % (user.city, result['main']['temp'], timezone.now())
        print(user.weather)
        user.save()
        return 'FIELD HAS BEEN UPDATED!'



# requests
