from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'water_management/index.html')


def water_source_list(request):
    water_sources = WaterSource.objects.all()
    return render(request, 'water_management/water_source_list.html', {'water_sources': water_sources})

# Create View
def water_source_create(request):
    if request.method == 'POST':
        form = WaterSourceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Water Source created successfully!')
            return redirect('water_management:water_source_list')
    else:
        form = WaterSourceForm()
    return render(request, 'water_management/water_source_form.html', {'form': form})

# Update View
def water_source_update(request, pk):
    water_source = get_object_or_404(WaterSource, pk=pk)
    if request.method == 'POST':
        form = WaterSourceForm(request.POST, instance=water_source)
        if form.is_valid():
            form.save()
            messages.success(request, 'Water Source updated successfully!')
            return redirect('water_management:water_source_list')
    else:
        form = WaterSourceForm(instance=water_source)
    return render(request, 'water_management/water_source_form.html', {'form': form})

# Delete View
def water_source_delete(request, pk):
    water_source = get_object_or_404(WaterSource, pk=pk)
    if request.method == 'POST':
        water_source.delete()
        messages.success(request, 'Water Source deleted successfully!')
        return redirect('water_management:water_source_list')
    return render(request, 'water_management/water_source_confirm_delete.html', {'water_source': water_source})


def water_consumption_create(request):
    if request.method == 'POST':
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Water Consumption record created successfully.")
            return redirect('water_management:water_consumption_list')
    else:
        form = WaterConsumptionForm()
    return render(request, 'water_management/water_consumption_form.html', {'form': form})


def water_consumption_list(request):
    water_consumptions = WaterConsumption.objects.all()
    return render(request, 'water_management/water_consumption_list.html', {'water_consumptions': water_consumptions})


def water_consumption_update(request, pk):
    water_consumption = get_object_or_404(WaterConsumption, pk=pk)
    
    if request.method == 'POST':
        form = WaterConsumptionForm(request.POST, instance=water_consumption)
        if form.is_valid():
            form.save()
            messages.success(request, "Water Consumption record updated successfully.")
            return redirect('water_management:water_consumption_list')
    else:
        form = WaterConsumptionForm(instance=water_consumption)
    
    return render(request, 'water_management/water_consumption_form.html', {'form': form})


def water_consumption_delete(request, pk):
    water_consumption = get_object_or_404(WaterConsumption, pk=pk)
    water_consumption.delete()
    messages.success(request, "Water Consumption record deleted successfully.")
    return redirect('water_management:water_consumption_list')



def leakage_report_list(request):
    if(request.user.is_superuser):
        reports = LeakageReport.objects.all().order_by('-date_reported')
    else:
        reports = LeakageReport.objects.filter(user = request.user).order_by('-date_reported')
    return render(request, 'water_management/leakage_report_list.html', {'reports': reports})

# Create View
def leakage_report_create(request):
    if request.method == 'POST':
        form = LeakageReportForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('water_management:leakage_report_list')
    else:
        form = LeakageReportForm()
    return render(request, 'water_management/leakage_report_form.html', {'form': form, 'title': 'Report Leakage'})

# Update View
def leakage_report_update(request, pk):
    report = get_object_or_404(LeakageReport, pk=pk)
    if request.method == 'POST':
        form = LeakageReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('water_management:leakage_report_list')
    else:
        form = LeakageReportForm(instance=report)
    return render(request, 'water_management/leakage_report_form.html', {'form': form, 'title': 'Update Report'})

# Delete View
def leakage_report_delete(request, pk):
    report = get_object_or_404(LeakageReport, pk=pk)
    if request.method == 'POST':
        report.delete()
        return redirect('water_management:leakage_report_list')
    return render(request, 'water_management/leakage_report_confirm_delete.html', {'report': report})

def water_quality_check_list(request):
    checks = WaterQualityCheck.objects.all()
    return render(request, 'water_management/water_quality_check_list.html', {'checks': checks})

# CREATE view
def water_quality_check_create(request):
    if request.method == 'POST':
        form = WaterQualityCheckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('water_management:water_quality_check_list')
    else:
        form = WaterQualityCheckForm()
    return render(request, 'water_management/water_quality_check_form.html', {'form': form, 'title': 'Add Water Quality Check'})

# UPDATE view
def water_quality_check_update(request, pk):
    check = get_object_or_404(WaterQualityCheck, pk=pk)
    if request.method == 'POST':
        form = WaterQualityCheckForm(request.POST, instance=check)
        if form.is_valid():
            form.save()
            return redirect('water_management:water_quality_check_list')
    else:
        form = WaterQualityCheckForm(instance=check)
    return render(request, 'water_management/water_quality_check_form.html', {'form': form, 'title': 'Update Water Quality Check'})

# DELETE view
def water_quality_check_delete(request, pk):
    check = get_object_or_404(WaterQualityCheck, pk=pk)
    if request.method == 'POST':
        check.delete()
        return redirect('water_management:water_quality_check_list')
    return render(request, 'water_management/water_quality_check_confirm_delete.html', {'check': check})




