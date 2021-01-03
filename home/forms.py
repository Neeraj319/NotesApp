from django import forms
from .models import Notes
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NotesForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=CKEditorUploadingWidget(), required=False)
