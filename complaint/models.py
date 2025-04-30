from django.db import models
from django.contrib.auth.models import User

class LocationImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} @ ({self.latitude}, {self.longitude})"
