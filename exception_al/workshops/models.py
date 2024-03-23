from django.db import models
from django.contrib.auth.models import User # This is the default user model that comes with Django


# Create your models here.
# This is the model for the workshops
# It has the following fields:


class Workshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='workshop_images/', blank=True)
    category = models.CharField(max_length=255)
    planned_date = models.DateField()
    closing_date = models.DateField()
    attendee_target = models.PositiveIntegerField()
    mentor_target = models.PositiveIntegerField()
    support_target = models.PositiveIntegerField()
    est_cost = models.DecimalField(max_digits=10, decimal_places=2)
    materials = models.TextField(blank=True)
    is_open = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
