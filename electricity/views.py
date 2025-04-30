from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
# Create your views here.
def index(request):
    return render(request,'electricity/index.html')

def grid_list(request):
    grids = Grid.objects.all()
    return render(request, 'electricity/grid_list.html', {'grids': grids})

# Create a new grid
def grid_create(request):
    if request.method == 'POST':
        form = GridForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:grid_list')
    else:
        form = GridForm()
    return render(request, 'electricity/grid_form.html', {'form': form})

# Update an existing grid
def grid_update(request, pk):
    grid = get_object_or_404(Grid, pk=pk)
    if request.method == 'POST':
        form = GridForm(request.POST, instance=grid)
        if form.is_valid():
            form.save()
            return redirect('electricity:grid_list')
    else:
        form = GridForm(instance=grid)
    return render(request, 'electricity/grid_form.html', {'form': form})

# Delete a grid
def grid_delete(request, pk):
    grid = get_object_or_404(Grid, pk=pk)
    if request.method == 'POST':
        grid.delete()
        return redirect('electricity:grid_list')
    return render(request, 'electricity/grid_confirm_delete.html', {'grid': grid})

def substation_list(request):
    substations = Substation.objects.all()
    return render(request, 'electricity/substation_list.html', {'substations': substations})

# Create a new substation
def substation_create(request):
    if request.method == 'POST':
        form = SubstationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:substation_list')
    else:
        form = SubstationForm()
    return render(request, 'electricity/substation_form.html', {'form': form})

# Update a substation
def substation_update(request, pk):
    substation = get_object_or_404(Substation, pk=pk)
    if request.method == 'POST':
        form = SubstationForm(request.POST, instance=substation)
        if form.is_valid():
            form.save()
            return redirect('electricity:substation_list')
    else:
        form = SubstationForm(instance=substation)
    return render(request, 'electricity/substation_form.html', {'form': form})

# Delete a substation
def substation_delete(request, pk):
    substation = get_object_or_404(Substation, pk=pk)
    if request.method == 'POST':
        substation.delete()
        return redirect('electricity:substation_list')
    return render(request, 'electricity/substation_confirm_delete.html', {'substation': substation})


def transformer_list(request):
    transformers = Transformer.objects.all()
    return render(request, 'electricity/transformer_list.html', {'transformers': transformers})

# 🔹 Create a new transformer
def transformer_create(request):
    if request.method == 'POST':
        form = TransformerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:transformer_list')
    else:
        form = TransformerForm()
    return render(request, 'electricity/transformer_form.html', {'form': form, 'title': 'Add Transformer'})

# 🔹 Update an existing transformer
def transformer_update(request, pk):
    transformer = get_object_or_404(Transformer, pk=pk)
    if request.method == 'POST':
        form = TransformerForm(request.POST, instance=transformer)
        if form.is_valid():
            form.save()
            return redirect('electricity:transformer_list')
    else:
        form = TransformerForm(instance=transformer)
    return render(request, 'electricity/transformer_form.html', {'form': form, 'title': 'Edit Transformer'})

# 🔹 Delete a transformer
def transformer_delete(request, pk):
    transformer = get_object_or_404(Transformer, pk=pk)
    if request.method == 'POST':
        transformer.delete()
        return redirect('electricity:transformer_list')
    return render(request, 'electricity/transformer_confirm_delete.html', {'transformer': transformer})

def consumer_create(request):
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:consumer_list')  # Redirect to the list of consumers
    else:
        form = ConsumerForm()
    return render(request, 'electricity/consumer_form.html', {'form': form})

def consumer_list(request):
    consumers = Consumer.objects.all()
    return render(request, 'electricity/consumer_list.html', {'consumers': consumers})


def consumer_update(request, pk):
    consumer = Consumer.objects.get(pk=pk)
    if request.method == 'POST':
        form = ConsumerForm(request.POST, instance=consumer)
        if form.is_valid():
            form.save()
            return redirect('electricity:consumer_list')
    else:
        form = ConsumerForm(instance=consumer)
    return render(request, 'electricity/consumer_form.html', {'form': form})
def consumer_delete(request, pk):
    consumer = Consumer.objects.get(pk=pk)
    if request.method == 'POST':
        consumer.delete()
        return redirect('electricity:consumer_list')
    return render(request, 'electricity/consumer_confirm_delete.html', {'consumer': consumer})

def consumer_detail(request, pk):
    consumer = Consumer.objects.get(pk=pk)
    return render(request, 'electricity/consumer_detail.html', {'consumer': consumer})


def electricity_usage_create(request):
    if request.method == 'POST':
        form = ElectricityUsageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:electricity_usage_list')  # Redirect to the list of electricity usage
    else:
        form = ElectricityUsageForm()
    return render(request, 'electricity/electricity_usage_form.html', {'form': form})

def electricity_usage_list(request):
    electricity_usages = ElectricityUsage.objects.all()
    return render(request, 'electricity/electricity_usage_list.html', {'electricity_usages': electricity_usages})


def electricity_usage_detail(request, pk):
    electricity_usage = ElectricityUsage.objects.get(pk=pk)
    return render(request, 'elctricity/electricity_usage_detail.html', {'electricity_usage': electricity_usage})

def electricity_usage_update(request, pk):
    electricity_usage = ElectricityUsage.objects.get(pk=pk)
    if request.method == 'POST':
        form = ElectricityUsageForm(request.POST, instance=electricity_usage)
        if form.is_valid():
            form.save()
            return redirect('electricity:electricity_usage_list')
    else:
        form = ElectricityUsageForm(instance=electricity_usage)
    return render(request, 'electricity/electricity_usage_form.html', {'form': form})

def electricity_usage_delete(request, pk):
    electricity_usage = ElectricityUsage.objects.get(pk=pk)
    if request.method == 'POST':
        electricity_usage.delete()
        return redirect('electricity:electricity_usage_list')
    return render(request, 'electricity/electricity_usage_confirm_delete.html', {'electricity_usage': electricity_usage})

def electricity_usage_delete(request, pk):
    electricity_usage = ElectricityUsage.objects.get(pk=pk)
    if request.method == 'POST':
        electricity_usage.delete()
        return redirect('electricity:electricity_usage_list')
    return render(request, 'electricity:electricity_usage_confirm_delete.html', {'electricity_usage': electricity_usage})


def bill_create(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('electricity:bill_list')  # Redirect to the list of bills
    else:
        form = BillForm()
    return render(request, 'electricity/bill_form.html', {'form': form})

def bill_list(request):
    bills = None
    if request.user.is_superuser:
        bills = Bill.objects.all()
    else:
        bills = Bill.objects.filter(consumer__user = request.user)
    return render(request, 'electricity/bill_list.html', {'bills': bills})


def bill_detail(request, pk):
    bill = Bill.objects.get(pk=pk)
    return render(request, 'electricity/bill_detail.html', {'bill': bill})
def bill_update(request, pk):
    bill = Bill.objects.get(pk=pk)
    if request.method == 'POST':
        form = BillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            return redirect('electricity:bill_list')
    else:
        form = BillForm(instance=bill)
    return render(request, 'electricity/bill_form.html', {'form': form})

def bill_delete(request, pk):
    bill = Bill.objects.get(pk=pk)
    if request.method == 'POST':
        bill.delete()
        return redirect('electricity:bill_list')
    return render(request, 'electricity/bill_confirm_delete.html', {'bill': bill})


def create_payment(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.bill = bill  # Link the payment to the selected bill
            payment.save()
            return redirect('electricity:payment_list')  # Redirect to the list view after creating
    else:
        form = PaymentForm()

    return render(request, 'electricity/create_payment.html', {'form': form, 'bill': bill})


# views.py
def payment_list(request):
    payments=None
    if request.user.is_superuser:
        payments = Payment.objects.all()  # Fetch all payment records
    else:
        payments = Payment.objects.filter(bill__consumer__user = request.user)
    return render(request, 'electricity/payment_list.html', {'payments': payments})

# views.py
def update_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('electricity:payment_list')  # Redirect to the list view after updating
    else:
        form = PaymentForm(instance=payment)

    return render(request, 'electricity/update_payment.html', {'form': form, 'payment': payment})

# views.py
from django.contrib import messages

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)

    if request.method == 'POST':
        payment.delete()
        messages.success(request, "Payment deleted successfully.")
        return redirect('electricity:payment_list')

    return render(request, 'electricity/delete_payment.html', {'payment': payment})

def create_outage_report(request):
    if request.method == 'POST':
        form = OutageReportForm(request.POST)
        if form.is_valid():
            outage_report = form.save(commit=False)

            # Assign the user to the report
            outage_report.user = request.user
            outage_report.reported_by = request.user

            # (Optional) Fallback in case JS didn't set lat/long
            if not outage_report.latitude or not outage_report.longitude:
                # You could set default values or handle this case
                outage_report.latitude = 0.0
                outage_report.longitude = 0.0

            outage_report.save()
            return redirect('electricity:outage_report_list')
    else:
        form = OutageReportForm()

    return render(request, 'electricity/outage_report_create.html', {
        'form': form,
        'title': 'Create New Outage Report'
    })

# READ View (List all reports)
def outage_report_list(request):
    reports = OutageReport.objects.all()  # Get all outage reports from the database
    return render(request, 'electricity/outage_report_list.html', {'reports': reports, 'title': 'Outage Reports'})

# UPDATE View
def update_outage_report(request, pk):
    report = get_object_or_404(OutageReport, pk=pk)  # Get the report with the given pk
    if request.method == 'POST':
        form = OutageReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()  # Update the existing report
            return redirect('electricity:outage_report_list')  # Redirect to a list view or another page
    else:
        form = OutageReportForm(instance=report)
    return render(request, 'electricity/outage_report_update.html', {'form': form, 'title': 'Update Outage Report'})

# DELETE View
def delete_outage_report(request, pk):
    report = get_object_or_404(OutageReport, pk=pk)  # Get the report with the given pk
    if request.method == 'POST':
        report.delete()  # Delete the report
        return redirect('electricity:outage_report_list')  # Redirect to a list view or another page
    return render(request, 'electricity/outage_report_confirm_delete.html', {'report': report, 'title': 'Delete Outage Report'})


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import OutageReport
from .forms import OutageFeedbackForm
from .utils import process_outage_feedback

@login_required
def outage_feedback(request, outage_id):
    outage = get_object_or_404(OutageReport, id=outage_id, user=request.user)
    
    if request.method == 'POST':
        form = OutageFeedbackForm(request.POST)
        if form.is_valid():
            is_resolved = form.cleaned_data['is_resolved']
            feedback_text = form.cleaned_data['feedback']
            
            process_outage_feedback(outage, is_resolved, feedback_text)
            
            if is_resolved:
                messages.success(request, 'Thank you for confirming this outage has been resolved.')
            else:
                messages.info(request, 'Thank you for your feedback. We\'ll continue monitoring this outage.')
            
            return redirect('my_outage_reports')
    else:
        form = OutageFeedbackForm()
    
    return render(request, 'outages/feedback.html', {
        'outage': outage,
        'form': form
    })

@login_required
def my_outage_reports(request):
    outages = OutageReport.objects.filter(user=request.user).order_by('-reported_at')
    return render(request, 'outages/my_outage_reports.html', {'outages': outages})