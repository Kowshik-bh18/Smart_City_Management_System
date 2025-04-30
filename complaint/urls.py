from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='complaint'
urlpatterns = [
    path('', views.image_list, name='image_list'),
    path('upload/', views.image_upload, name='image_upload'),
    path('<int:pk>/edit/', views.image_edit, name='image_edit'),
    path('<int:pk>/delete/', views.image_delete, name='image_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)