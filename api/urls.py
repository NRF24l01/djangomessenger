from django.urls import include, path
from . import views

urlpatterns = [
    path('chat/get_desc', views.get_contack_info, name='get_contact'),
]
