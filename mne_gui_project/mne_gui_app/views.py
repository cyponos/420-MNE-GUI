from django.shortcuts import render, redirect
from .forms import EEGDataUploadForm
from .models import UploadedFile

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
    files = UploadedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})