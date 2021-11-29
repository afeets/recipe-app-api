from django.db import models

from django.contrib.auth.models import AbstractBaseUser, \
                                        PermissionsMixin, \
                                        BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError('Users must have an email address')

        """Creates and saves new user, set email to lowercase"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return User


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model supports email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'