import mne.io
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import EEGDataUploadForm
from .models import UploadedFile
from django . shortcuts import get_object_or_404
from .models import EEGData
from django.urls import reverse
import os, tempfile
from django.conf import settings
import matplotlib.pyplot as plt
import io
import base64
import json
import pandas as pd
import numpy as np
import plotly.graph_objs as go


def filter_data(request, eeg_data_id):
    if request.method == 'POST':
        high_range = float(request.POST.get('high_range', 20.0))
        low_range = float(request.POST.get('low_range', 0.5))

        eeg_data = get_object_or_404(EEGData, pk=eeg_data_id)
        eeg_file_name = eeg_data.eeg_file.path

        raw = mne.io.read_raw_edf(eeg_file_name, preload=True)
        raw.filter(low_range, high_range)

        filtered_data = raw.to_data_frame()

        time_data = filtered_data['time'].tolist()

        eeg_channels_data = filtered_data.drop(columns='time').to_dict(orient='list')

        filtered_data_dict = {
            'time': time_data,
            **eeg_channels_data
        }

        context = {
            'filtered_data': json.dumps(filtered_data_dict),
        }

        return render(request, 'filtered_data.html', context)
    else:
        return render(request, 'filter_form.html')
def view_data(request, eeg_data_id):
    eeg_data = get_object_or_404(EEGData, pk=eeg_data_id)
    eeg_file_name = eeg_data.eeg_file.path

    raw = mne.io.read_raw_edf(eeg_file_name)

    raw_data_head = raw.to_data_frame().head()

    print(raw_data_head)

    fig = raw.plot()

    temp_dir = tempfile.mkdtemp()
    temp_plot_file = os.path.join(temp_dir, 'eeg_plot.png')
    fig.savefig(temp_plot_file)

    plot_file_name = f'{eeg_data_id}_plot.png'

    plot_file_path = os.path.join(settings.MEDIA_ROOT, plot_file_name)

    fig.savefig(plot_file_path)

    context = {'raw_data_head': raw_data_head,
               'plot_file_name': plot_file_name,
               'eeg_data_id' : eeg_data_id
               }
    print(f'plot_file_path: {plot_file_path}')
    print(f'MEDIA_URL: {settings.MEDIA_URL}')

    return render(request, 'view.html', context)

def make_graph(request, eeg_data_id):
    eeg_data = get_object_or_404(EEGData, pk=eeg_data_id)
    eeg_file_name = eeg_data.eeg_file.path

    raw = mne.io.read_raw_edf(eeg_file_name)
    eeg_data = raw.to_data_frame()

    channel_names = eeg_data.columns.tolist()
    eeg_data_dict = {
        'x': eeg_data.index.tolist(),
    }

    for channel_name in channel_names:
        eeg_data_dict[channel_name] = eeg_data[channel_name].tolist()

    eeg_data_json = json.dumps(eeg_data_dict)

    context = {
        'eeg_data_json': eeg_data_json,
        'channel_names': channel_names,
        'raw_data_head': raw.to_data_frame().head(),
    }

    return render(request, 'graph.html', context)

def make_channel_graph(request, eeg_data_id):
    eeg_data = get_object_or_404(EEGData, pk=eeg_data_id)
    eeg_file_name = eeg_data.eeg_file.path

    raw = mne.io.read_raw_edf(eeg_file_name)
    eeg_data = raw.to_data_frame()

    channel_names = eeg_data.columns.tolist()
    eeg_data_dict = {
        'x': eeg_data.index.tolist(),
    }

    for channel_name in channel_names:
        eeg_data_dict[channel_name] = eeg_data[channel_name].tolist()

    eeg_data_json = json.dumps(eeg_data_dict)

    context = {
        'eeg_data_json': eeg_data_json,
        'channel_names': channel_names,
        'raw_data_head': raw.to_data_frame().head(),
    }

    return render(request, 'individual_channels.html', context)

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

def apply_ica_preprocessing(request, eeg_data_id):
    eeg_data = get_object_or_404(EEGData, pk=eeg_data_id)
    eeg_file_name = eeg_data.eeg_file.path

    raw = mne.io.read_raw_edf(eeg_file_name, preload=True)

    ica = mne.preprocessing.ICA(n_components=20, random_state=97)
    ica.fit(raw)
    ica.apply(raw)
    eeg_data = raw.to_data_frame()

    channel_names = eeg_data.columns.tolist()
    eeg_data_dict = {
        'x': eeg_data.index.tolist(),
    }

    for channel_name in channel_names:
        eeg_data_dict[channel_name] = eeg_data[channel_name].tolist()

    eeg_data_ica_json = json.dumps(eeg_data_dict)

    return JsonResponse({'message': 'ICA preprocessing applied successfully', 'eeg_data_ica_json': eeg_data_ica_json})

