from django import forms

class login_form(forms.Form):
    Username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-2','placeholder':'Enter Your Username Here'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2','placeholder':'Enter Your Password Here'}))



































