from django import forms
from .models import *

class WaterSourceForm(forms.ModelForm):
    class Meta:
        model = WaterSource
        fields = ['name', 'location', 'capacity', 'type', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }


class WaterConsumptionForm(forms.ModelForm):
    class Meta:
        model = WaterConsumption
        fields = ['zone', 'date', 'residential_usage', 'commercial_usage', 'industrial_usage']
        widgets = {
            'zone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'residential_usage': forms.NumberInput(attrs={'class': 'form-control'}),
            'commercial_usage': forms.NumberInput(attrs={'class': 'form-control'}),
            'industrial_usage': forms.NumberInput(attrs={'class': 'form-control'}),
        }


from django import forms
from .models import LeakageReport

class LeakageReportForm(forms.ModelForm):
    class Meta:
        model = LeakageReport
        fields = ['location', 'description', 'image', 'status', 'latitude', 'longitude']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }



class WaterQualityCheckForm(forms.ModelForm):
    class Meta:
        model = WaterQualityCheck
        fields = ['source', 'date', 'ph_level', 'contaminants_detected', 'remarks']
        widgets = {
            'source': forms.Select(attrs={'class': 'form-select'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'ph_level': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'contaminants_detected': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }