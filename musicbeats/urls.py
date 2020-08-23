from django.urls import path
from . import views

urlpatterns = [
    path('songs/', views.songs, name='songs'),
    path('songs/<int:id>', views.songpost, name='songpost'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout_user', views.logout_user, name='logout_user'),
    path('watchlater', views.watchlater, name='watchlater'),
    path('history', views.history, name='history'),
    path('c/<str:channel>', views.channel, name='channel'),
    path('upload', views.upload, name='upload'),
]
