from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Note

def main(request):
    all_notes = Note.objects.all()
    return render(request, 'noting.html', 
    {'all_items': all_notes})# render the Database as a dictionary to be used in templates

def temp(request):
    return HttpResponse("This is a temporary view for this Page")

def addNote(request):
    new_item = Note(title=request.POST['title'], desc=request.POST['desc'], quad=request.POST['quad'])# creating the Note
    new_item.save()# saving the note
    return HttpResponseRedirect('/noting/')

def deleteNote(request, Note_id):
    del_item = Note.objects.get(id = Note_id)
    del_item.delete()
    return HttpResponseRedirect('/noting/')
