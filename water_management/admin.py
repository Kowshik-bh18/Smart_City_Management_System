from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(WaterSource)
admin.site.register(WaterConsumption)
admin.site.register(LeakageReport)
admin.site.register(WaterQualityCheck)
