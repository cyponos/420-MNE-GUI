from django.urls import path
from . import views

urlpatterns = [
    path('upload_file', views.upload_file, name='upload_file'),
    path('', views.home, name='home'),
    path('file_list/', views.file_list, name='file_list'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('view/<int:eeg_data_id>/', views.view_data, name='view_data'),
    path('filter_data/<int:eeg_data_id>/', views.filter_data, name='filter_data'),
    path('graph/<int:eeg_data_id>/', views.make_graph, name='graph_data'),
    path('apply_ica_preprocessing/<int:eeg_data_id>/', views.apply_ica_preprocessing, name='apply_ica_preprocessing'),
    path('individual_channels/<int:eeg_data_id>/', views.make_channel_graph, name='individual_channels'),

]
