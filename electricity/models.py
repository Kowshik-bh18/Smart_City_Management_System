from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Grid(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    capacity_mw = models.FloatField()  # Maximum capacity in megawatts
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Maintenance', 'Maintenance')])

    def __str__(self):
        return self.name


class Substation(models.Model):
    name = models.CharField(max_length=100)
    grid = models.ForeignKey(Grid, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    capacity_mw = models.FloatField()

    def __str__(self):
        return self.name


class Transformer(models.Model):
    substation = models.ForeignKey(Substation, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=100)
    capacity_kva = models.FloatField()
    status = models.CharField(max_length=50, choices=[('Operational', 'Operational'), ('Faulty', 'Faulty')])

    def __str__(self):
        return self.identifier


class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    meter_number = models.CharField(max_length=100, unique=True)
    connected_transformer = models.ForeignKey(Transformer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username


class ElectricityUsage(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    reading_date = models.DateField()
    units_consumed = models.FloatField(help_text="In kWh")
    cost = models.FloatField()

    def __str__(self):
        return f"{self.consumer.user.username} - {self.reading_date}"


class Bill(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField()
    total_units = models.FloatField()
    amount_due = models.FloatField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Bill #{self.id} - {self.consumer.user.username}"


class Payment(models.Model):
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount_paid = models.FloatField()
    payment_method = models.CharField(max_length=50, choices=[
        ('Credit Card', 'Credit Card'),
        ('UPI', 'UPI'),
        ('Cash', 'Cash'),
        ('Online Banking', 'Online Banking')
    ])

    def __str__(self):
        return f"Payment for Bill #{self.bill.id}"


class OutageReport(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='user_outage_reports')
    location = models.CharField(max_length=255)
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='reported_outage_reports')
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    reported_at = models.DateTimeField(default=timezone.now)  # Define default value
    resolved = models.BooleanField(default=False)

    last_notification_sent = models.DateTimeField(null=True, blank=True)
    feedback_requested = models.BooleanField(default=False)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Outage at {self.location}"
    
    def mark_as_resolved(self):
        self.resolved = True
        self.resolved_at = timezone.now()
        self.save()
    
    def should_request_feedback(self):
        """Check if we should send a feedback notification"""
        if self.resolved:
            return False
            
        if self.feedback_requested:
            # Already requested feedback and waiting for response
            return False
            
        if not self.last_notification_sent:
            # First notification should be sent 10 days after creation
            return (timezone.now() - self.reported_at).days >= 10
        else:
            # Subsequent notifications every 10 days
            return (timezone.now() - self.last_notification_sent).days >= 10
        
class OutageFeedbackNotification(models.Model):
    outage_report = models.ForeignKey(OutageReport, on_delete=models.CASCADE, related_name='notifications')
    sent_at = models.DateTimeField(auto_now_add=True)
    feedback_provided = models.BooleanField(default=False)
    issue_resolved = models.BooleanField(null=True, blank=True)
    feedback_text = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Notification for outage at {self.outage_report.location}"


class MaintenanceLog(models.Model):
    transformer = models.ForeignKey(Transformer, on_delete=models.CASCADE)
    date = models.DateField()
    technician_name = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f"Maintenance - {self.transformer.identifier} - {self.date}"
