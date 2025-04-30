from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WaterSource(models.Model):
    SOURCE_TYPE_CHOICES = [
        ('River', 'River'),
        ('Reservoir', 'Reservoir'),
        ('Borewell', 'Borewell'),
        ('Lake', 'Lake'),
    ]

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.FloatField(help_text="Maximum capacity in liters")
    type = models.CharField(max_length=20, choices=SOURCE_TYPE_CHOICES)
    status = models.CharField(max_length=20, default='Active', choices=[('Active', 'Active'), ('Under Maintenance', 'Under Maintenance')])
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.type}"

class WaterConsumption(models.Model):
    zone = models.CharField(max_length=100)
    date = models.DateField()
    residential_usage = models.FloatField(default=0.0, help_text="Water usage in liters for residential areas")
    commercial_usage = models.FloatField(default=0.0, help_text="Water usage in liters for commercial areas")
    industrial_usage = models.FloatField(default=0.0, help_text="Water usage in liters for industrial areas")

    def total_usage(self):
        return self.residential_usage + self.commercial_usage + self.industrial_usage

    def __str__(self):
        return f"Water Consumption in {self.zone} on {self.date}"
class LeakageReport(models.Model):
    user = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='leak_reports/', null=True, blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')])
    latitude = models.FloatField(default= None)
    longitude = models.FloatField(default= None)
    def __str__(self):
        return f"Leakage reported at {self.location} on {self.date_reported.strftime('%Y-%m-%d')}"

class WaterQualityCheck(models.Model):
    source = models.ForeignKey(WaterSource, on_delete=models.CASCADE)
    date = models.DateField()
    ph_level = models.FloatField(help_text="PH level of the water")
    contaminants_detected = models.TextField(null=True, blank=True, help_text="List of contaminants detected")
    remarks = models.TextField(null=True, blank=True, help_text="Additional remarks or comments")

    def __str__(self):
        return f"Quality check for {self.source.name} on {self.date}"
