from django.contrib import admin

from .models import Profile, location

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(location, LocationAdmin)