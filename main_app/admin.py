from django.contrib import admin
from .models import Technique, Profile


# class Favorites(admin.ModelAdmin):
#     list_display = ('user', 'technique')


# Register your models here.
admin.site.register(Technique)
admin.site.register(Profile)


admin.site.site_header = "Massage.ify Admin"
