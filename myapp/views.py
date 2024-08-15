from django.shortcuts import render
from .forms import Contactforms
from django import forms



# Create your views here.
# important note u should render the home html instead of the base html and you should render the child instead of the parent template

def home(request):
   
    return render(request, 'home.html',{})

# ensure to have form.save to save the data to the database
def contact(request):
   
    if request.method == 'POST':
       form = Contactforms(request.POST or None)
       if form.is_valid():
           form.save()
           return render(request,'success.html',{})
    else:
        form = Contactforms()
    return render(request, 'contact.html',{'form':form})   

def projects(request):
    return render(request, 'projects.html' , {})

def resume(request):
    return render(request, 'resume.html' , {})
    

