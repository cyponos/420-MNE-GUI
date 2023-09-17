from django.urls import path
from . import views

urlpatterns = [
    path('upload_file', views.upload_file, name='upload_file'),
    path('', views.home, name='home'),
    path('file_list/', views.file_list, name='file_list')
]