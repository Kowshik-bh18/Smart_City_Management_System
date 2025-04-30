from django import forms
from .models import *

class WasteBinForm(forms.ModelForm):
    class Meta:
        model = WasteBin
        fields = ['location', 'zone', 'bin_type', 'capacity_kg', 'current_fill_kg']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter zone'}),
            'bin_type': forms.Select(attrs={'class': 'form-select'}),
            'capacity_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Capacity in kg'}),
            'current_fill_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Current fill in kg'}),
        }
from django import forms
from .models import CollectionSchedule

class CollectionScheduleForm(forms.ModelForm):
    class Meta:
        model = CollectionSchedule
        fields = ['bin', 'collection_date', 'collected']
        widgets = {
            'bin': forms.Select(attrs={'class': 'form-select'}),
            'collection_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'collected': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CollectionScheduleForm(forms.ModelForm):
    class Meta:
        model = CollectionSchedule
        fields = ['bin', 'collection_date', 'collected']
        widgets = {
            'bin': forms.Select(attrs={'class': 'form-select'}),
            'collection_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'collected': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BinSensorDataForm(forms.ModelForm):
    class Meta:
        model = BinSensorData
        fields = ['bin', 'fill_percentage']



class WasteComplaintForm(forms.ModelForm):
    class Meta:
        model = WasteComplaint
        fields = ['location', 'description', 'image', 'status']

        widgets = {
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter complaint location'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the issue',
                'rows': 4
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

from django import forms
from .models import WasteTypeRecord

class WasteTypeRecordForm(forms.ModelForm):
    class Meta:
        model = WasteTypeRecord
        fields = ['zone', 'date', 'recyclable_weight', 'non_recyclable_weight']
        widgets = {
            'zone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Zone'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'recyclable_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight in kg'}),
            'non_recyclable_weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight in kg'}),
        }

class WasteAnalyticsForm(forms.ModelForm):
    class Meta:
        model = WasteAnalytics
        fields = [
            'zone',
            'month',
            'total_waste_kg',
            'collection_efficiency',
            'complaints_resolved',
            'complaints_total',
        ]
        widgets = {
            'zone': forms.TextInput(attrs={'class': 'form-control'}),
            'month': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., April 2025'}),
            'total_waste_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'collection_efficiency': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'complaints_resolved': forms.NumberInput(attrs={'class': 'form-control'}),
            'complaints_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }

