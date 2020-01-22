# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from notes.models import Note
from notes.forms import NoteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def index_view(request):
    notes = Note.objects.all().order_by('-timestamp')
    #notes = Note.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'notes/index.html', {'notes': notes})


@login_required(login_url='/login')
def add_note(request):
    id = request.GET.get('id', None)
    if id is not None:
        note = get_object_or_404(Note, id=id)
    else:
        note = None

    if request.method == 'POST':  #DELETE
        if request.POST.get('control') == 'delete':
            note.delete()
            messages.add_message(request, messages.INFO, 'Note Deleted!')
            return HttpResponseRedirect(reverse('notes:index'))

        form = NoteForm(request.POST, instance=note)  #ADD/EDIT
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Note Added!')
            return HttpResponseRedirect(reverse('notes:index'))

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/addnote.html', {'form': form, 'note': note})

