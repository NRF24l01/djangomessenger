from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.TextField()
    username = models.TextField(max_length=25)
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to="images/profile")
    state = models.TextField()
