from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import VideoServiceUserCreationForm, VideoServiceUserChangeForm
from .models import VideoServiceUser


class VideoServiceUserAdmin(UserAdmin):
    add_form = VideoServiceUserCreationForm
    form = VideoServiceUserChangeForm
    model = VideoServiceUser
    list_display = ['email', 'username', 'phone_number']


admin.site.register(VideoServiceUser, VideoServiceUserAdmin)
