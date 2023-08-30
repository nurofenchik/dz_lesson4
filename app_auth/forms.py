from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name' , 'last_name' ,'password1', 'password2']
    def username_clean(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("User Already Exist")
        return username

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        return last_name
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    def save(self, commit=True , **extra_fields):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['first_name'],
            self.cleaned_data['last_name'],
            )
        return user



