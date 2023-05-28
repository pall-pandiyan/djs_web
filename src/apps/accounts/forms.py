from django import forms


class LoginForm(forms.Form):
    """
    A Simple Login Form.

    Developer: Pall Pandiyan.S
    """
    username = forms.CharField(label=None, max_length=20, min_length=5,strip=True)
    password = forms.CharField(label=None, max_length=20, min_length=8)
