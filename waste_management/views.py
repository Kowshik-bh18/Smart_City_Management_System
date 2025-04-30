from django.shortcuts import render,HttpResponse
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'waste_management/index.html')

from .models import WasteBin
from .forms import WasteBinForm

# 1. List View
def wastebin_list(request):
    bins = WasteBin.objects.all()
    return render(request, 'waste_management/wastebin_list.html', {'bins': bins})


# 2. Create View
def wastebin_create(request):
    if request.method == 'POST':
        form = WasteBinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Waste bin added successfully.")
            return redirect('waste_management:wastebin_list')
    else:
        form = WasteBinForm()
    return render(request, 'waste_management/wastebin_form.html', {'form': form, 'title': 'Add Waste Bin'})


# 3. Update View
def wastebin_update(request, pk):
    bin = get_object_or_404(WasteBin, pk=pk)
    if request.method == 'POST':
        form = WasteBinForm(request.POST, instance=bin)
        if form.is_valid():
            form.save()
            messages.success(request, "Waste bin updated successfully.")
            return redirect('waste_management:wastebin_list')
    else:
        form = WasteBinForm(instance=bin)
    return render(request, 'waste_management/wastebin_form.html', {'form': form, 'title': 'Update Waste Bin'})


# 4. Delete View
def wastebin_delete(request, pk):
    bin = get_object_or_404(WasteBin, pk=pk)
    if request.method == 'POST':
        bin.delete()
        messages.success(request, "Waste bin deleted successfully.")
        return redirect('waste_management:wastebin_list')
    return render(request, 'waste_management/wastebin_confirm_delete.html', {'bin': bin})




def collection_schedule_create(request):
    if request.method == 'POST':
        form = CollectionScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Collection schedule added successfully.")
            return redirect('waste_management:collection_schedule_list')  # Redirect to the list view after saving
    else:
        form = CollectionScheduleForm()
    
    return render(request, 'waste_management/collection_schedule_form.html', {'form': form, 'title': 'Add Collection Schedule'})

def collection_schedule_list(request):
    schedules = CollectionSchedule.objects.all()
    return render(request, 'waste_management/collection_schedule_list.html', {'schedules': schedules})
def collection_schedule_update(request, pk):
    schedule = get_object_or_404(CollectionSchedule, pk=pk)
    if request.method == 'POST':
        form = CollectionScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            messages.success(request, "Collection schedule updated successfully.")
            return redirect('waste_management:collection_schedule_list')
    else:
        form = CollectionScheduleForm(instance=schedule)
    
    return render(request, 'waste_management/collection_schedule_form.html', {'form': form, 'title': 'Update Collection Schedule'})

def collection_schedule_delete(request, pk):
    schedule = get_object_or_404(CollectionSchedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        messages.success(request, "Collection schedule deleted successfully.")
        return redirect('waste_management:collection_schedule_list')
    
    return render(request, 'waste_management/collection_schedule_confirm_delete.html', {'schedule': schedule})


def bin_sensor_data_create(request):
    if request.method == 'POST':
        form = BinSensorDataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bin sensor data added successfully.")
            return redirect('waste_management:bin_sensor_data_list')  # Redirect to the list view after saving
    else:
        form = BinSensorDataForm()
    
    return render(request, 'waste_management/bin_sensor_data_form.html', {'form': form, 'title': 'Add Bin Sensor Data'})


def bin_sensor_data_list(request):
    sensor_data = BinSensorData.objects.all()
    return render(request, 'waste_management/bin_sensor_data_list.html', {'sensor_data': sensor_data})

def bin_sensor_data_update(request, pk):
    sensor_data = get_object_or_404(BinSensorData, pk=pk)
    if request.method == 'POST':
        form = BinSensorDataForm(request.POST, instance=sensor_data)
        if form.is_valid():
            form.save()
            messages.success(request, "Bin sensor data updated successfully.")
            return redirect('waste_management:bin_sensor_data_list')
    else:
        form = BinSensorDataForm(instance=sensor_data)
    
    return render(request, 'waste_management/bin_sensor_data_form.html', {'form': form, 'title': 'Update Bin Sensor Data'})


def bin_sensor_data_delete(request, pk):
    sensor_data = get_object_or_404(BinSensorData, pk=pk)
    if request.method == 'POST':
        sensor_data.delete()
        messages.success(request, "Bin sensor data deleted successfully.")
        return redirect('waste_management:bin_sensor_data_list')
    
    return render(request, 'waste_management/bin_sensor_data_confirm_delete.html', {'sensor_data': sensor_data})


@login_required
def complaint_list(request):
    complaints = None
    if(request.user.is_superuser):
        complaints = WasteComplaint.objects.all()
    else:
        complaints = WasteComplaint.objects.filter(user = request.user)
    return render(request, 'waste_management/complaint_list.html', {'complaints': complaints})

# Create a new complaint
@login_required
def complaint_create(request):
    if request.method == 'POST':
        form = WasteComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            messages.success(request, "Complaint submitted successfully.")
            return redirect('waste_management:complaint_list')
    else:
        form = WasteComplaintForm()
    return render(request, 'waste_management/complaint_form.html', {'form': form})

# Update a complaint
@login_required
def complaint_update(request, pk):
    complaint = get_object_or_404(WasteComplaint, pk=pk, user=request.user)
    if request.method == 'POST':
        form = WasteComplaintForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, "Complaint updated successfully.")
            return redirect('waste_management:complaint_list')
    else:
        form = WasteComplaintForm(instance=complaint)
    return render(request, 'waste_management/complaint_form.html', {'form': form})

# Delete a complaint
@login_required
def complaint_delete(request, pk):
    complaint = get_object_or_404(WasteComplaint, pk=pk, user=request.user)
    if request.method == 'POST':
        complaint.delete()
        messages.success(request, "Complaint deleted successfully.")
        return redirect('waste_management:complaint_list')
    return render(request, 'waste_management/complaint_confirm_delete.html', {'complaint': complaint})


def waste_type_record_list(request):
    records = WasteTypeRecord.objects.all().order_by('-date')
    return render(request, 'waste_management/waste_type_record_list.html', {'records': records})

# Create View
def waste_type_record_create(request):
    if request.method == 'POST':
        form = WasteTypeRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record added successfully!")
            return redirect('waste_management:waste_type_record_list')
    else:
        form = WasteTypeRecordForm()
    return render(request, 'waste_management/waste_type_record_form.html', {'form': form})

# Update View
def waste_type_record_update(request, pk):
    record = get_object_or_404(WasteTypeRecord, pk=pk)
    if request.method == 'POST':
        form = WasteTypeRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('waste_management:waste_type_record_list')
    else:
        form = WasteTypeRecordForm(instance=record)
    return render(request, 'waste_management/waste_type_record_form.html', {'form': form})

# Delete View
def waste_type_record_delete(request, pk):
    record = get_object_or_404(WasteTypeRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('waste_management:waste_type_record_list')
    return render(request, 'waste_management/waste_type_record_confirm_delete.html', {'record': record})


def waste_analytics_list(request):
    analytics = WasteAnalytics.objects.all()
    return render(request, 'waste_management/waste_analytics_list.html', {'analytics': analytics})

# Create View
def waste_analytics_create(request):
    if request.method == 'POST':
        form = WasteAnalyticsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Analytics record created successfully.')
            return redirect('waste_management:waste_analytics_list')
    else:
        form = WasteAnalyticsForm()
    return render(request, 'waste_management/waste_analytics_form.html', {'form': form})

# Update View
def waste_analytics_update(request, pk):
    analytics = get_object_or_404(WasteAnalytics, pk=pk)
    if request.method == 'POST':
        form = WasteAnalyticsForm(request.POST, instance=analytics)
        if form.is_valid():
            form.save()
            messages.success(request, 'Analytics record updated successfully.')
            return redirect('waste_management:waste_analytics_list')
    else:
        form = WasteAnalyticsForm(instance=analytics)
    return render(request, 'waste_management/waste_analytics_form.html', {'form': form})

# Delete View
def waste_analytics_delete(request, pk):
    analytics = get_object_or_404(WasteAnalytics, pk=pk)
    if request.method == 'POST':
        analytics.delete()
        messages.success(request, 'Analytics record deleted successfully.')
        return redirect('waste_management:waste_analytics_list')
    return render(request, 'waste_management/waste_analytics_confirm_delete.html', {'analytics': analytics})