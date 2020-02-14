from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from material import *
from app.models import AddPost


class SignUpForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(label="Email Address")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Enter password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    receive_news = forms.BooleanField(required=False, label='I want to receive news and notifications')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password1', 'password2'),
                    Fieldset('Personal details',
                             Row('first_name', 'last_name'),
                             'receive_news', 'agree_toc'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class AddPostForm(forms.ModelForm):
    category = forms.CharField(label="Enter category")
    title = forms.CharField(label="Title of Post")
    data = forms.CharField(label="Write a post...", widget=forms.Textarea)

    layout = Layout(Fieldset('',
                             Row('category', ),
                             Row('title', ),
                             Row('data', ), ))

    class Meta:
        model = AddPost
        fields = ('category', 'title', 'data',)
