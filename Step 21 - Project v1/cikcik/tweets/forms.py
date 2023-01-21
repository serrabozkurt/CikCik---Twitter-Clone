from django import forms

from tweets.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]
