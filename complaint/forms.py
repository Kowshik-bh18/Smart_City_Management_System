from django import forms
from .models import LocationImage

class LocationImageForm(forms.ModelForm):
    class Meta:
        model = LocationImage
        fields = ['image', 'latitude', 'longitude']
        widgets = {
            'latitude': forms.HiddenInput(attrs={'id': 'id_latitude'}),
            'longitude': forms.HiddenInput(attrs={'id': 'id_longitude'}),
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user is not None:
            instance.user = user  # set the user programmatically
        if commit:
            instance.save()
        return instance
