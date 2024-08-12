from django import forms
from .models import Event
class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"
        widgets = {
            'initial_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'final_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }