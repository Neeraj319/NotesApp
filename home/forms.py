from django import forms
from .models import Notes
from django_summernote.fields import SummernoteTextFormField


class NotesForm(forms.Form):
    title = forms.CharField()
    content = SummernoteTextFormField()
