import mne.io
from django.shortcuts import render, redirect
from .forms import EEGDataUploadForm
from .models import UploadedFile
from django . shortcuts import get_object_or_404
from .models import EEGData
import os, tempfile



def view_data(request, eeg_data_id):
    eeg_data = get_object_or_404(EEGData, pk=eeg_data_id)
    edf_fileName = eeg_data.edf_file.path
    raw = mne.io.read_raw_edf(edf_fileName)

    fig = raw.plot()

    raw_data_head = raw.to_data_frame().head()

    context = {'raw_data_head': raw_data_head}

    return render(request, 'view.html', context)
def upload_file(request):
    if request.method == 'POST':
        form = EEGDataUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = EEGDataUploadForm()
    return render(request, 'upload_file.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def file_list(request):
    files = EEGData.objects.all()
    return render(request, 'file_list.html', {'uploaded_files': files})

def delete_file(request, file_id):
    file_to_delete = get_object_or_404(EEGData, pk=file_id)
    if request.method == "POST":
        file_to_delete.eeg_file.delete()
        file_to_delete.delete()
    return redirect('file_list')