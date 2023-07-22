from django.contrib import admin
from .models import VSUser, VSVideo, VSComment
# Register your models here.

admin.register(VSVideo)
admin.register(VSUser)
admin.register(VSComment)
