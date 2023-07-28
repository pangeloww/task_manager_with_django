from django.db import models


# Create your models here.
class GatheredEmailsFromBulletin(models.Model):
    email = models.EmailField()
