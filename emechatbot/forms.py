from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(label='You', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Type your emergency message...',
    }))
