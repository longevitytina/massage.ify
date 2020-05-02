from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('techniques/', views.techniques_list, name='techniques_list'),
    path('techniques/<int:technique_id>/detail',
         views.technique_detail, name='technique_detail'),
    path('profile/', views.profile, name='profile'),
]
