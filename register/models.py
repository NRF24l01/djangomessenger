from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField()
    username = models.TextField(max_length=25)
    pasw = models.TextField(null=None)
    name = models.TextField(max_length=50)
    image = models.ImageField(upload_to="images/profile", null=None)
    state = models.TextField()
    reg_link = models.TextField()
