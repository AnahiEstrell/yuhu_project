from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
import os
import uuid

EXTENSION_ALLOWED = ['.jpg', '.png', '.jpeg']


def user_image_file_path(instance, filename):
    """Generate a file path for image user"""
    extension = os.path.splitext(filename)[1]
    if extension.lower() not in EXTENSION_ALLOWED:
        raise ValidationError(f'Invalid extension: {extension}')
    filename = f'{uuid.uuid4()}{extension}'

    return os.path.join('uploads', 'user', filename)


class UserManager(BaseUserManager):
    """Manager for the user"""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""

        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return and new super user"""

        superuser = self.create_user(email, password)
        superuser.is_active = True
        superuser.is_superuser = True
        superuser.save(using=self._db)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """Users in the systems"""

    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=255)
    primer_apellido = models.CharField(max_length=255)
    segundo_apellido = models.CharField(max_length=255)
    imagen = models.ImageField(null=True, upload_to=user_image_file_path)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        ordering = ['email']

    def __str__(self):
        return self.email
