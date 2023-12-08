from django.urls import include, path
from . import views

urlpatterns = [
    path('chat/<int:chat_number>', views.chatrender, name='regren'),
]