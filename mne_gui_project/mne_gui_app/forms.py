from django import forms
from .models import EEGData

class EEGDataUploadForm(forms.ModelForm):
    class Meta:
        model = EEGData
        fields = ['eeg_file']