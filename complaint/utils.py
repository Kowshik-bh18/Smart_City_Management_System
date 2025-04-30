# utils.py
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from .models import OutageReport, OutageFeedbackNotification

def create_outage_feedback_notification(outage_report):
    """Create a feedback notification for an outage report and send email"""
    notification = OutageFeedbackNotification.objects.create(outage_report=outage_report)
    
    # Update outage report to reflect notification sent
    outage_report.last_notification_sent = timezone.now()
    outage_report.feedback_requested = True
    outage_report.save()
    
    # Generate feedback URL
    feedback_url = f"{settings.SITE_URL}{reverse('outage_feedback', kwargs={'outage_id': outage_report.id})}"
    
    # Send email notification
    send_mail(
        subject=f"Service Outage Feedback Request: {outage_report.location}",
        message=f"""
        Hello {outage_report.user.get_full_name() or outage_report.user.username},
        
        We're following up on your reported outage at: "{outage_report.location}"
        
        Has this service outage been resolved? Please click the link below to provide feedback:
        {feedback_url}
        
        Thank you for helping improve our city's services!
        """,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[outage_report.user.email],
        fail_silently=False,
    )
    
    return notification

def process_outage_feedback(outage_report, is_resolved, feedback_text=None):
    """Process user feedback on an outage report"""
    # Update latest notification
    latest_notification = outage_report.notifications.latest('sent_at')
    latest_notification.feedback_provided = True
    latest_notification.issue_resolved = is_resolved
    latest_notification.feedback_text = feedback_text
    latest_notification.save()
    
    # Update outage report status
    outage_report.feedback_requested = False
    
    if is_resolved:
        outage_report.mark_as_resolved()
    else:
        # Reset notification tracking for next cycle
        outage_report.save()
        
    return outage_report