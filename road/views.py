from django.shortcuts import render,HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Road
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'road/index.html')


def road_list(request):
    roads = Road.objects.all()
    return render(request, 'road/road_list.html', {'roads': roads})

# Create View
def road_create(request):
    if request.method == 'POST':
        form = RoadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Road added successfully!')
            return redirect('road:road_list')
    else:
        form = RoadForm()
    return render(request, 'road/road_form.html', {'form': form})

# Update View
def road_update(request, pk):
    road = get_object_or_404(Road, pk=pk)
    if request.method == 'POST':
        form = RoadForm(request.POST, instance=road)
        if form.is_valid():
            form.save()
            messages.success(request, 'Road details updated!')
            return redirect('road:road_list')
    else:
        form = RoadForm(instance=road)
    return render(request, 'road/road_form.html', {'form': form})

# Delete View
def road_delete(request, pk):
    road = get_object_or_404(Road, pk=pk)
    if request.method == 'POST':
        road.delete()
        messages.success(request, 'Road deleted successfully!')
        return redirect('road:road_list')
    return render(request, 'road/road_confirm_delete.html', {'road': road})

from django.shortcuts import render, redirect
from .models import TrafficIncident
from .forms import TrafficIncidentForm

def traffic_incident_list(request):
    incidents = None
    if request.user.is_superuser:
        # If the user is a superuser, show all incidents
        incidents = TrafficIncident.objects.all()
    else:
        # If the user is not a superuser, show only their own incidents
        incidents = TrafficIncident.objects.filter(user=request.user)
    
    return render(request, 'road/traffic_incident_list.html', {'incidents': incidents})

def traffic_incident_create(request):
    if request.method == 'POST':
        form = TrafficIncidentForm(request.POST)
        if form.is_valid():
            creating = form.save(commit=False)
            creating.user = request.user
            creating.save()  # Save the instance to the database
            return redirect('road:traffic_incident_list')
    else:
        form = TrafficIncidentForm()
    
    return render(request, 'road/traffic_incident_form.html', {'form': form})


def traffic_incident_update(request, pk):
    incident = get_object_or_404(TrafficIncident, pk=pk)
    if request.method == 'POST':
        form = TrafficIncidentForm(request.POST, instance=incident)
        if form.is_valid():
            form.save()
            return redirect('road:traffic_incident_list')
    else:
        form = TrafficIncidentForm(instance=incident)
    return render(request, 'road/traffic_incident_form.html', {'form': form})

def traffic_incident_delete(request, pk):
    incident = get_object_or_404(TrafficIncident, pk=pk)
    if request.method == 'POST':
        incident.delete()
        return redirect('road:traffic_incident_list')
    return render(request, 'road/traffic_incident_confirm_delete.html', {'incident': incident})


def road_maintenance_list(request):
    maintenances = RoadMaintenance.objects.all()
    return render(request, 'road/road_maintenance_list.html', {'maintenances': maintenances})

# Create View
def road_maintenance_create(request):
    if request.method == 'POST':
        form = RoadMaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('road:road_maintenance_list')
    else:
        form = RoadMaintenanceForm()
    return render(request, 'road/road_maintenance_form.html', {'form': form})

# Update View
def road_maintenance_update(request, pk):
    maintenance = get_object_or_404(RoadMaintenance, pk=pk)
    if request.method == 'POST':
        form = RoadMaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect('road:road_maintenance_list')
    else:
        form = RoadMaintenanceForm(instance=maintenance)
    return render(request, 'road/road_maintenance_form.html', {'form': form})

# Delete View
def road_maintenance_delete(request, pk):
    maintenance = get_object_or_404(RoadMaintenance, pk=pk)
    if request.method == 'POST':
        maintenance.delete()
        return redirect('road:road_maintenance_list')
    return render(request, 'road/road_maintenance_confirm_delete.html', {'maintenance': maintenance})