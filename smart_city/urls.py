from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('waste_management/',include('waste_management.urls')),
    path('road/',include('road.urls')),
    path('water_management/',include('water_management.urls')),
    path('electricity/',include('electricity.urls')),
    path('complaint/',include('complaint.urls')),
    path('mapif/', include('mapdata.urls')),
    path('chat/', include('emechatbot.urls')),

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
