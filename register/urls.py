from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.render_register, name='regren'),
    path('mail_sender/', views.register_sistem, name='check_mail_sender'),
    path('login/', views.render_login, name='logren'),
    path('login/cheker/', views.login_user, name='logus'),
]