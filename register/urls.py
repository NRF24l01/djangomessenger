from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello'),
    path('mail_sender/', views.register_sistem, name='check_mail_sender'),
]