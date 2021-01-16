from django.shortcuts import render #to render pages with dictionary of database
from django.http import HttpResponse, HttpResponseRedirect #Returning or Redirecting Http response
from .models import Note #model to workon
from django.views import View #to create Classbased views
from django.contrib.auth.decorators import login_required #to check whether the user is logged-in or not

@login_required #login is required to access this view
def main(request):
    all_notes = Note.objects.filter(author = request.user) #returns all objects in the mentioned database
    return render(request, 'noting.html', 
    {'all_items': all_notes}) #render the Database as a dictionary to be used in templates

def temp(request):
    return render(request, 'home.html')

def addNote(request):
    new_item = Note(
        title=request.POST['title'], 
        desc=request.POST['desc'], 
        quad=request.POST['quad'],
        author=request.user) #getting current logged-in user
    new_item.save() #saving the note in the database
    return HttpResponseRedirect('/noting/') #redirecting to /noting

def deleteNote(request, Note_id):
    del_item = Note.objects.get(id = Note_id) #get the id of the note to be deleted
    del_item.delete() #delete the note from the database
    return HttpResponseRedirect('/noting/') #redirect to /noting
