from django.contrib import admin
from .models import Jar, User, Log
# Register your models here.

admin.site.register(Jar)
admin.site.register(User)
admin.site.register(Log)