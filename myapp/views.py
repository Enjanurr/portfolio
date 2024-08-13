from django.shortcuts import render
from .forms import Contactforms
from .models import Contact
from django import forms
from django.contrib import messages

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
           messages.success(request,'Succesfully sent')
    else:
        form = Contactforms()
    return render(request, 'contact.html',{'form':form})   
'''def contact(request):
    if request.method == 'POST':
        # Retrieve data from request.POST
        full_name = request.POST.get('full_name')
        email_address = request.POST.get('email_address')
        phone_number = request.POST.get('phone_number', '')  # Default to empty string if not provided
        message = request.POST.get('message')

        # Simple validation (you can add more sophisticated validation here)
        if not full_name or not email_address or not message:
            error_message = "Please fill out all required fields."
            return render(request, 'contact.html', {'error_message': error_message})

        # Save data to the database
        UserProfile.objects.create(
            full_name=full_name,
            email_address=email_address,
            phone_number=phone_number,
            message=message
        )

        # Redirect to a success page or render a success message
         # Replace with your success URL name

    return render(request, 'contact.html')
'''
        
   

def projects(request):
    return render(request, 'projects.html' , {})

def resume(request):
    return render(request, 'resume.html' , {})
    
# This is for the comment
'''
def comment_view(request):
    comments = Comment.objects.all()  # Retrieve all comments
    if request.method == 'POST':
        form = CommentForm(request.POST)  # Bind data from POST request to the form
        
        if form.is_valid():
            form.save()  # Save the form data to the database
            print('success')# return redirect('comment_success')  # Redirect to a success page or another view
    else:
        form = CommentForm()  # Instantiate an empty form for GET requests
    
    return render(request, 'submit_comment.html', {'form': form, 'comments': comments})
        '''
