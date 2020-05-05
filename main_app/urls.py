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

    path('accounts/signup', views.signup, name='signup'),
    # path('profile/<int:favorite_id>/delete/',
    #      views.delete_favorite, name='delete_favorite'),
]
