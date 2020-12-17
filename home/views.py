from django.urls import reverse_lazy
from django.shortcuts import render, HttpResponse, redirect
from .models import Notes
from django.views.generic import ListView, DeleteView, View
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm

# def home_page(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     return render(request, 'home.html')


@login_required
def index(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            note = Notes(title=title, content=content, user=request.user)
            note.save()
            print('created')
        return redirect('show_notes')
    return render(request, 'index.html', {'context': form})


class View_Notes(LoginRequiredMixin, ListView):
    context_object_name = 'Notes'
    template_name = 'notes.html'

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user).order_by('-date_created')


@login_required
def edit(request, slug):
    note = Notes.objects.get(slug=slug)

    if request.user == note.user:
        form = NotesForm({'title': note.title, 'content': note.content})
        if request.method == 'POST':
            form = NotesForm(request.POST)
            if form.is_valid():

                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                note.title = title
                note.content = content
                note.user = request.user
                note.save()
                print('updated')
                return redirect('show_notes')
        context = {
            "notes": note,
            'context': form
        }
    else:
        return redirect('show_notes')
    return render(request, 'edit_notes.html', context)


class Delete_note(LoginRequiredMixin, View):
    model = Notes
    template_name = 'delete_notes.html'
    success_url = reverse_lazy('show_notes')

    def post(self, request, slug):
        note = Notes.objects.get(slug=slug)

        if request.user == note.user:
            note.delete()
            return redirect('show_notes')
        else:
            return redirect('show_notes')

    def get(self, request, slug):
        note = Notes.objects.get(slug=slug)
        if request.user == note.user:

            return render(request, 'delete_notes.html', context={'notes': note})
        else:
            return redirect('show_notes')
