from django.db import models

from accounts.models import User


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('started', 'Start'),
        ('finished', 'Finished'),
    ]
    title = models.CharField(max_length=50)
    description = models.TextField()
    choices = models.CharField(max_length=20, choices=STATUS_CHOICES, default='started')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
