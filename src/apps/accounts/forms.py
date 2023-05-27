from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label=None, max_length=20, min_length=5,strip=True)
    password = forms.CharField(label=None, max_length=20, min_length=8)
