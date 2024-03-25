from django.db import models
from django.contrib.auth.models import AbstractUser

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name
    
class Interest(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, unique=True, null=False, blank=False, verbose_name='username')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256, unique=True, verbose_name='email')
    biography = models.TextField()
    profile_image = models.URLField()
    skills = models.ManyToManyField(Skill, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)

    def __str__(self):
        return self.username
    
    def delete (self, *args, **kwargs):
        print (f"User {self.username} is about to be deleted.")
        super().delete(*args, **kwargs)

