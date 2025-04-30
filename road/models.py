from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Road(models.Model):
    ROAD_TYPE_CHOICES = [
        ('Highway', 'Highway'),
        ('Street', 'Street'),
        ('Alley', 'Alley'),
        ('Avenue', 'Avenue'),
    ]
    name = models.CharField(max_length=255)
    road_type = models.CharField(max_length=20, choices=ROAD_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    condition = models.CharField(max_length=50, default='Good')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class TrafficIncident(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ('Accident', 'Accident'),
        ('Roadwork', 'Roadwork'),
        ('Obstacle', 'Obstacle'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPE_CHOICES)
    
    latitude = models.FloatField(null=True, blank=True)  # Set both to allow null and blank values
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=[('Minor', 'Minor'), ('Major', 'Major')])
    date_reported = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.incident_type} on {self.road.name}"
    

class RoadMaintenance(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    road = models.ForeignKey(Road, on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField()

    def __str__(self):
        return f"Maintenance on {self.road.name}"