# management/commands/send_outage_feedback_requests.py
from django.core.management.base import BaseCommand
from .models import OutageReport
from .utils import create_outage_feedback_notification

class Command(BaseCommand):
    help = 'Send feedback request notifications for outage reports'

    def handle(self, *args, **options):
        # Get all unresolved outage reports that need feedback requests
        outages_to_notify = []
        for outage in OutageReport.objects.filter(resolved=False):
            if outage.should_request_feedback():
                outages_to_notify.append(outage)
        
        # Send notifications
        notification_count = 0
        for outage in outages_to_notify:
            create_outage_feedback_notification(outage)
            notification_count += 1
            
        self.stdout.write(self.style.SUCCESS(
            f'Successfully sent {notification_count} outage feedback request notifications'
        ))