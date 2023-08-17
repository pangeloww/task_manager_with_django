from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from .validators import validate_unique_email, validate_name

# Create your models here.
class AppUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'

    objects = AppUserManager()
    first_name = models.CharField(
        max_length=30,
        validators=[validate_name]
    )
    last_name = models.CharField(
        max_length=30,
        validators=[validate_name]
    )
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        validators=[validate_unique_email]
    )
    is_staff = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        default=timezone.now,
    )

