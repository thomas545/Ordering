from django.contrib import admin

from .models import UserDetails , Order

admin.site.register(UserDetails)
admin.site.register(Order)