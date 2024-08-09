from django.shortcuts import render

# Create your views here.
# important note u should render the home html instead of the base html and you should render the child instead of the parent template
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html', {})

def projects(request):
    return render(request, 'projects.html' , {})

def resume(request):
    return render(request, 'resume.html' , {})
    