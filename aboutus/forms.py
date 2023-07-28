from django import forms
from django.core.validators import EmailValidator

from aboutus.models import GatheredEmailsFromBulletin


class BulletinEmailForm(forms.ModelForm):
    class Meta:
        model = GatheredEmailsFromBulletin
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'})
        }
        labels = {
            'email': 'Email address'
        }

    email = forms.EmailField(max_length=30, validators=[EmailValidator])
