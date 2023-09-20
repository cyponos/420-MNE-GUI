from django.db import models

# Create your models here.
class EEGData(models.Model):
    eeg_file = models.FileField(upload_to='eeg_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class React(models.Model):
	name = models.CharField(max_length=30)
	detail = models.CharField(max_length=500)
