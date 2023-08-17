from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_name(value):
    if not value.isalpha():
        raise ValidationError(
            _("Name should only contain alphabetic characters."),
            code='invalid_name'
        )

def validate_unique_email(value):
    from .models import User  # Import User model to avoid circular imports
    existing_users = User.objects.filter(email=value)
    if existing_users.exists():
        raise ValidationError(
            _("A user with this email address already exists."),
            code='unique_email'
        )