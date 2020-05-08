from django.contrib import admin
from .models import Technique, Profile, Playlist, PlaylistTechnique, Following


class ProfileA(admin.ModelAdmin):
    list_display = ('user',)


class FollowingA(admin.ModelAdmin):
    list_display = ('from_user', 'to_user')


class PlaylistTechA(admin.ModelAdmin):
    list_display = ('playlist', 'technique')


# Register your models here.
admin.site.register(Technique)
admin.site.register(Profile, ProfileA)
admin.site.register(Playlist)
admin.site.register(PlaylistTechnique, PlaylistTechA)
admin.site.register(Following, FollowingA)


admin.site.site_header = "Massage.ify Admin"
