from django.db import models
from django.contrib.auth import get_user_model

class Workshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='workshop_images', blank=True, null=True)
    category = models.CharField(max_length=255)
    planned_date = models.DateField(null=True, blank=True)
    closing_date = models.DateField()
    attendee_target = models.PositiveIntegerField()
    mentor_target = models.PositiveIntegerField()
    support_target = models.PositiveIntegerField(null=True, blank=True)
    est_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    materials = models.TextField(blank=True, null=True)
    is_open = models.BooleanField(default=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
