from django import forms

from tweets.models import User, Tweet


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["text"]
