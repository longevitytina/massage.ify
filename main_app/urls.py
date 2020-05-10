from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('techniques/', views.techniques_list, name='techniques_list'),

    path('techniques/<int:profile_id>/assoc_technique/<int:technique_id>/',
         views.assoc_technique, name='assoc_technique'),

    path('techniques/<int:technique_id>/detail',
         views.technique_detail, name='technique_detail'),
    path('profile/', views.profile, name='profile'),
    path('profile/new', views.new_playlist, name='new_playlist'),

    path('profile/playlist/<int:playlist_id>/detail',
         views.playlist_detail, name='playlist_detail'),

    path('profile/<int:playlist_technique_id>/edit',
         views.edit_playlist_item, name='edit_playlist_item'),

    path('profile/<int:technique_id>/add',
         views.assoc_playlist_item, name='assoc_playlist_item'),

    path('accounts/signup', views.signup, name='signup'),

    path('profile/<int:technique_id>/delete_favorites/',
         views.delete_favorite, name='delete_favorite'),

    path('profile/<int:playlist_id>/delete_playlist/',
         views.delete_playlist, name='delete_playlist'),

    path('profile/<int:playlist_technique_id>/delete_playlist_technique/',
         views.delete_playlist_technique, name='delete_playlist_technique'),
]
