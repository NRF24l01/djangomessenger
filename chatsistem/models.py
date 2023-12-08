from django.db import models
from django.db.models import Model, AutoField, IntegerField, TextField, DateTimeField


# Create your models here.
class Messages(Model):
    id = AutoField(primary_key=True)
    user_id = IntegerField()
    chat_id = IntegerField()
    datetimer = DateTimeField(auto_now_add=True)
    message_text = TextField()


class Chats(Model):
    id = AutoField(primary_key=True)
    members = TextField()
    name = TextField(max_length=45)
    description = TextField(max_length=150)
    invite = TextField(max_length=15)
