from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Grid)
admin.site.register(Substation)
admin.site.register(Transformer)
admin.site.register(Consumer)
admin.site.register(ElectricityUsage)
admin.site.register(Bill)
admin.site.register(Payment)
admin.site.register(OutageReport)
admin.site.register(MaintenanceLog)




@admin.register(OutageFeedbackNotification)
class OutageFeedbackNotificationAdmin(admin.ModelAdmin):
    list_display = ['outage_report', 'sent_at', 'feedback_provided', 'issue_resolved']
    list_filter = ['feedback_provided', 'issue_resolved']
    search_fields = ['outage_report__location', 'outage_report__user__username']