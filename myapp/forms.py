from django import forms
from .models import Contact
from django import forms

class Contactforms(forms.ModelForm):
    full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fullname'}), required=True)
    email_address = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=True)
    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone number'}), required=True)
    message = forms.CharField(label="", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'}), required=True)

    class Meta:
        model = Contact
        fields = ['full_name', 'email_address', 'phone_number','message']
