from django.urls import path
from . import views
app_name = 'dashboard'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.logout_view,name='logout')
]
