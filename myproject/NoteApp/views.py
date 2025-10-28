from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NotesForm



def get_all_notes(request):
    notes = Notes.objects.all() 
    return render(request, "NoteApp/All_notes.html", {"notes": notes})



def create_notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all_notes")
    else:
        form = NotesForm()
    return render(request, "NoteApp/notes.html", {"form": form})



def update_notes(request, pk):
    note = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("all_notes")
    else:
        form = NotesForm(instance=note)
    return render(request, "NoteApp/notes.html", {"form": form})



def delete_note(request, pk):
    form = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
        form.delete()
        return redirect("all_notes")
    return render(request, "NoteApp/note_delete.html", {"form": form})

