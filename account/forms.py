from django import forms
from django.contrib.auth import get_user_model
from .models import Profile


User = get_user_model()


class EditAccountForm(forms.Form):

    class Meta:
        model = User
        fields = ['username', 'email', 'user']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date', 'phone_number', 'photo')
