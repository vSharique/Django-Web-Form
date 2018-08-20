from django import forms
from .models import *


class UserForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Enter your Full Name'}), required=True,
                           max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Enter your Date Of Birth'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter your Valid Email'}), required=True,
                             max_length=100)
    ph = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off',
                                                       'pattern': '[0-9]+', 'placeholder': 'Enter 10 Digit Number'}),
                         required=True, max_length=10)

    class Meta():
        model = UserData
        fields = ['name', 'dob', 'email', 'ph']

