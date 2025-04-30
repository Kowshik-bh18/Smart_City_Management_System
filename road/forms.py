from django import forms
from .models import *

class RoadForm(forms.ModelForm):
    class Meta:
        model = Road
        fields = ['name', 'road_type', 'location', 'latitude', 'longitude', 'condition']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'road_type': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TrafficIncidentForm(forms.ModelForm):
    class Meta:
        model = TrafficIncident
        fields = ['road', 'incident_type', 'description', 'severity', 'resolved']
        widgets = {
            'road': forms.Select(attrs={'class': 'form-select'}),
            'incident_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'severity': forms.Select(attrs={'class': 'form-select'}),
            'resolved': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class RoadMaintenanceForm(forms.ModelForm):
    class Meta:
        model = RoadMaintenance
        fields = ['road', 'scheduled_date', 'status', 'description']
        widgets = {
            'road': forms.Select(attrs={'class': 'form-select'}),
            'scheduled_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
