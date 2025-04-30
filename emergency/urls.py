from django.urls import path
from . import views
app_name=''
urlpatterns = [
    path("\home",views.index,name="home-page"),
]
