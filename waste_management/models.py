
from django.db import models
from django.contrib.auth.models import User

# 1. Waste Collection Points (Bins across the city)
class WasteBin(models.Model):
    BIN_TYPE_CHOICES = [
        ('Recyclable', 'Recyclable'),
        ('Non-Recyclable', 'Non-Recyclable'),
    ]
    
    location = models.CharField(max_length=255)
    zone = models.CharField(max_length=100)
    bin_type = models.CharField(max_length=20, choices=BIN_TYPE_CHOICES)
    capacity_kg = models.FloatField(help_text="Maximum bin capacity in kilograms")
    current_fill_kg = models.FloatField(default=0.0)
    last_collected = models.DateTimeField(null=True, blank=True)

    def is_full(self):
        return self.current_fill_kg >= self.capacity_kg

    def __str__(self):
        return f"{self.zone} - {self.bin_type} Bin at {self.location}"

# 2. Garbage Collection Schedule
class CollectionSchedule(models.Model):
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    collection_date = models.DateField()
    collected = models.BooleanField(default=False)

    def __str__(self):
        return f"Scheduled for {self.collection_date} - {'Collected' if self.collected else 'Pending'}"

# 3. Citizen Waste Complaints
class WasteComplaint(models.Model):
    COMPLAINT_STATUS = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='waste_complaints/', null=True, blank=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=COMPLAINT_STATUS, default='Pending')

    def __str__(self):
        return f"Complaint by {self.user.username} - {self.status}"

# 4. Smart Bin Monitoring (can be simulated)
class BinSensorData(models.Model):
    bin = models.ForeignKey(WasteBin, on_delete=models.CASCADE)
    fill_percentage = models.IntegerField(help_text="e.g., 75 means 75% full")
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bin} - {self.fill_percentage}% at {self.recorded_at.strftime('%Y-%m-%d %H:%M')}"

# 5. Recyclable vs Non-Recyclable Tracking
class WasteTypeRecord(models.Model):
    zone = models.CharField(max_length=100)
    date = models.DateField()
    recyclable_weight = models.FloatField(default=0.0)
    non_recyclable_weight = models.FloatField(default=0.0)

    def total_weight(self):
        return self.recyclable_weight + self.non_recyclable_weight

    def __str__(self):
        return f"{self.zone} on {self.date}"

# 6. Analytics Data (optional, or aggregate from above models)
class WasteAnalytics(models.Model):
    zone = models.CharField(max_length=100)
    month = models.CharField(max_length=20)  # e.g., "April 2025"
    total_waste_kg = models.FloatField()
    collection_efficiency = models.FloatField(help_text="Percentage of scheduled bins collected")
    complaints_resolved = models.IntegerField()
    complaints_total = models.IntegerField()

    def complaint_resolution_rate(self):
        return (self.complaints_resolved / self.complaints_total) * 100 if self.complaints_total > 0 else 0

    def __str__(self):
        return f"Analytics for {self.zone} - {self.month}"
