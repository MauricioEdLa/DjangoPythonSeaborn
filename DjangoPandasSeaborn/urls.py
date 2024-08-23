from django.contrib import admin
from django.urls import path
from visualizations.views import upload_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
]