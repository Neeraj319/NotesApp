from django.contrib import admin
from django.urls import path
from .views import index, View_Notes, edit, Delete_note

urlpatterns = [
    path('', index, name='home'),
    path('notes/', View_Notes.as_view(), name='show_notes'),
    path('edit/<str:slug>', edit, name='edit'),
    path('delete/<str:slug>', Delete_note.as_view(), name='delete'),
]
