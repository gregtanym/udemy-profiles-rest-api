from django.contrib import admin
from profiles_api import models

# Register your models here. so that django knows you want to display these models in the admin interface
admin.site.register(models.UserProfile)
