from django.urls import path
from . import views
app_name='road'
urlpatterns = [
    path('',views.index,name='index'),
    path('roads/', views.road_list, name='road_list'),
    path('roads/create/', views.road_create, name='road_create'),
    path('roads/update/<int:pk>/', views.road_update, name='road_update'),
    path('roads/delete/<int:pk>/', views.road_delete, name='road_delete'),
    path('traffic-incidents/', views.traffic_incident_list, name='traffic_incident_list'),
    path('traffic-incidents/create/', views.traffic_incident_create, name='traffic_incident_create'),
    path('traffic-incidents/<int:pk>/edit/', views.traffic_incident_update, name='traffic_incident_update'),
    path('traffic-incidents/<int:pk>/delete/', views.traffic_incident_delete, name='traffic_incident_delete'),
    path('road-maintenance/', views.road_maintenance_list, name='road_maintenance_list'),
    path('road-maintenance/create/', views.road_maintenance_create, name='road_maintenance_create'),
    path('road-maintenance/<int:pk>/update/', views.road_maintenance_update, name='road_maintenance_update'),
    path('road-maintenance/<int:pk>/delete/', views.road_maintenance_delete, name='road_maintenance_delete'),
]
