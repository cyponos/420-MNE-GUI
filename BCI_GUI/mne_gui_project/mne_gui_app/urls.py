from django.urls import path
from mne_gui_app.views import *
from . import views

urlpatterns = [

    path('', views.ReactView.as_view(), name="react-view"),
    path('upload_file', views.upload_file, name='upload_file'),
    path('file_list/', views.file_list, name='file_list'),
    path('<int:pk>/', views.ReactView.as_view(), name='react-delete'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('view/<int:eeg_data_id>/', views.view_data, name='view_data'),
]