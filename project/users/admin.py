from django.contrib import admin

from .models import User
from .forms import UserCreationForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    form = UserCreationForm
    list_per_page = 20
    ordering = ['id']
    search_fields = ['email']
    list_display = ['email', 'get_full_name', 'last_login', 'id']
    readonly_fields = ['id', 'date_joined', 'last_login']
    fieldsets = (
        ('User', {
            'fields': ('id', 'password')
        }),
        ('About', {
            'fields': ('first_name', 'last_name')
        }),
        ('Contact', {
            'fields': ('email',)
        }),
        (None, {
            'fields': ('date_joined', 'last_login')
        }),
    )
