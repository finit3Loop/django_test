from django import forms

class PasswordForm(forms.Form):
    your_name = forms.CharField(label='Password', max_length=100)