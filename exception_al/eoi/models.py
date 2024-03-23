from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Eoi(models.Model):

    TYPE_CHOICES = (
        ('Organise', 'Organise'),
        ('Attend', 'Attend'),
        ('Mentor', 'Mentor'),
    )


    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey('User', on_delete=models.CASCADE)
    # workshop = models.ForeignKey('Workshop', on_delete=models.CASCADE)
    # eoi_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    comment = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return f"Registration {self.id} for Workshop {self.workshop_id} by User {self.user_id}"

# test
# class Eoi(models.Model):
#     user = models.CharField(max_length=200)
#     workshop = models.TextField()
#     eoi_type = models.IntegerField()
#     comment = models.URLField()
   
    
