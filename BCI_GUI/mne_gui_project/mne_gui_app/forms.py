from django import forms
from .models import EEGData

class EEGDataUploadForm(forms.ModelForm):
    class Meta:
        model = EEGData
        fields = ['eeg_file']

    def clean_eeg_file(self):
        eeg_file = self.cleaned_data['eeg_file']
        if not eeg_file.name.endswith('.edf'):
            raise forms.ValidationError('Only edf files are allowed. Please choose another file.')
        return eeg_file
