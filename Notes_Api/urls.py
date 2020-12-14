from django.contrib import admin
from django.urls import path, include
from .views import ShowUserNotes, NotesDetailsView, Login_API_View
urlpatterns = [
    path('UsersNotes/', ShowUserNotes.as_view(),),
    path('Note/<int:id>', NotesDetailsView.as_view(),),
    path('login/', Login_API_View.as_view())
]
