from django import forms

from . import models


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = models.UserRegistration
        fields = ['user_no','name', 'profile_pic', 'mobile','email', 'id_card','created_date']
