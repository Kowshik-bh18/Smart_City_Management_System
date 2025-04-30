from django import forms
from .models import *

class GridForm(forms.ModelForm):
    class Meta:
        model = Grid
        fields = ['name', 'region', 'capacity_mw', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity_mw': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class SubstationForm(forms.ModelForm):
    class Meta:
        model = Substation
        fields = ['name', 'grid', 'location', 'capacity_mw']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'grid': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity_mw': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
        }


class TransformerForm(forms.ModelForm):
    class Meta:
        model = Transformer
        fields = ['substation', 'identifier', 'capacity_kva', 'status']
        widgets = {
            'substation': forms.Select(attrs={'class': 'form-control'}),
            'identifier': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity_kva': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['user', 'address', 'meter_number', 'connected_transformer']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-textarea'}),
            'meter_number': forms.TextInput(attrs={'class': 'form-input'}),
            'connected_transformer': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }

class ElectricityUsageForm(forms.ModelForm):
    class Meta:
        model = ElectricityUsage
        fields = ['consumer', 'reading_date', 'units_consumed', 'cost']
        widgets = {
            'reading_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'units_consumed': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['consumer', 'issue_date', 'due_date', 'total_units', 'amount_due', 'is_paid']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'total_units': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'amount_due': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'is_paid': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['bill', 'amount_paid', 'payment_method']

        widgets = {
            'bill': forms.Select(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'payment_method': forms.Select(attrs={'class': 'form-select'}),
        }

class OutageReportForm(forms.ModelForm):
    class Meta:
        model = OutageReport
        fields = ['location',  'description', 'latitude', 'longitude', 'resolved']

    widgets = {
            'latitude': forms.HiddenInput(attrs={'id': 'id_latitude'}),
            'longitude': forms.HiddenInput(attrs={'id': 'id_longitude'}),
        }



class OutageFeedbackForm(forms.Form):
    is_resolved = forms.BooleanField(
        label="Has this outage been resolved?",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        label="Additional feedback (optional)"
    )