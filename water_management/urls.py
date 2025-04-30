from django.urls import path
from . import views

app_name='water_management'
urlpatterns = [
    path('',views.index,name='index'),
     path('water_sources/', views.water_source_list, name='water_source_list'),
    path('water_sources/create/', views.water_source_create, name='water_source_create'),
    path('water_sources/update/<int:pk>/', views.water_source_update, name='water_source_update'),
    path('water_sources/delete/<int:pk>/', views.water_source_delete, name='water_source_delete'),
    path('water_consumption/', views.water_consumption_list, name='water_consumption_list'),
    path('water_consumption/create/', views.water_consumption_create, name='water_consumption_create'),
    path('water_consumption/<int:pk>/update/', views.water_consumption_update, name='water_consumption_update'),
    path('water_consumption/<int:pk>/delete/', views.water_consumption_delete, name='water_consumption_delete'),
     path('leakages/', views.leakage_report_list, name='leakage_report_list'),
    path('leakages/create/', views.leakage_report_create, name='leakage_report_create'),
    path('leakages/<int:pk>/update/', views.leakage_report_update, name='leakage_report_update'),
    path('leakages/<int:pk>/delete/', views.leakage_report_delete, name='leakage_report_delete'),
    path('quality-checks/', views.water_quality_check_list, name='water_quality_check_list'),
    path('quality-checks/create/', views.water_quality_check_create, name='water_quality_check_create'),
    path('quality-checks/<int:pk>/update/', views.water_quality_check_update, name='water_quality_check_update'),
    path('quality-checks/<int:pk>/delete/', views.water_quality_check_delete, name='water_quality_check_delete'),
]
