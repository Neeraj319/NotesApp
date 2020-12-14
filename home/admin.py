from django.contrib import admin
from .models import Notes
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Notes)
class NotesAdmin(SummernoteModelAdmin):
    list_display = ['title', ]
    summernote_fields = ['content', ]
