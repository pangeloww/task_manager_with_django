from django import forms
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError

from accounts.models import User


class CreateAccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(render_value=True))
    repeat_password = forms.CharField(widget=forms.PasswordInput(render_value=True))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'repeat_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        repeat_password = cleaned_data.get("repeat_password")

        if password and repeat_password and password != repeat_password:
            raise ValidationError("Passwords do not match. Please enter the same password in both fields.")

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.password = make_password(password)  # Hash the password
        if commit:
            user.save()
        return user


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    field_order = ['email', 'password']


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
