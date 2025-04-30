from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(WasteBin)
admin.site.register(CollectionSchedule)
admin.site.register(WasteComplaint)
admin.site.register(BinSensorData)
admin.site.register(WasteTypeRecord)
admin.site.register(WasteAnalytics)