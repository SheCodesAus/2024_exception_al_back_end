from django.db import models
from django.contrib.auth import get_user_model
from workshops.models import Workshop

class Eoi(models.Model):
    TYPE_CHOICES = (
        ('Organise', 'Organise'),
        ('Attend', 'Attend'),
        ('Mentor', 'Mentor'),
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='eois')
    eoi_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Attend")
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
