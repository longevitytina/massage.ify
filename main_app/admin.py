from django.contrib import admin
from .models import Technique, Profile, Playlist, PlaylistTechnique, Following


# class Favorites(admin.ModelAdmin):
#     list_display = ('user', 'technique')


# Register your models here.
admin.site.register(Technique)
admin.site.register(Profile)
admin.site.register(Playlist)
admin.site.register(PlaylistTechnique)
admin.site.register(Following)


admin.site.site_header = "Massage.ify Admin"
