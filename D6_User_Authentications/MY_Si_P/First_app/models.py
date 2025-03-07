from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    F_ID=models.URLField(blank=True)
    profile_P=models.ImageField(upload_to="Profile_pic",blank=True)
    def __str__(self):
        return self.user.username
