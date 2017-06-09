from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email adress')

        user = User(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **kwargs):
        return self.create(email=email, password=password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self.create_user(email=email, password=password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    # username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(choices=(('Male', 'male'), ('Female', 'female'), ('Other', 'other')), max_length=10,
                              default='Other')
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    about = models.TextField(default='')
    avatar = models.ImageField(upload_to="images/",
                               blank=True,
                               default='images/default_avatar.png')

    is_staff = models.BooleanField(default=False,
                                   help_text='Designates whether the users can log into this admin site.', )
    is_active = models.BooleanField('active', default=True)
    weather = models.CharField(help_text='Info about current weather, when user info has been updated',
                               default='',
                               max_length=300)
    city = models.CharField(max_length=100,
                            default='')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def activate(self, commit=True):
        self.is_active = True

        if commit:
            self.save()

    def deactivate(self, commit=True):
        self.is_active = False

    def delete(self, using=None, keep_parents=False):
        raise Exception('Nope! Only destroy!')

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    class Meta:
        ordering = ['date_joined', ]
