from django.db import models

# Create your models here.

class TestingDocker(models.Model):
    name = models.CharField(max_length=20, null=True)
    profile_picture = models.ImageField(
        upload_to="picture", blank=True, null=True
    )