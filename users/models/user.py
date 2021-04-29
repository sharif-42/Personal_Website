import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext_lazy as _

from commons.constant import GENDER_CHOICES


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    uuid = models.UUIDField(
        verbose_name=_('unique identifier'),
        help_text=_('Must be unique'),
        default=uuid.uuid4,
        editable=False
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('First name'),
        help_text=_('User first name'),
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('Last name'),
        help_text=_('User first name'),
        blank=True
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name=_('Contact number'),
        help_text=_('User contact number'),
        blank=True,
    )
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        help_text=_("User's Gender."),
    )

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # blocking related fields
    is_blocked = models.BooleanField(default=False)
    # common fields
    join_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return str(self.first_name) + ' ' + str(self.last_name)
        return str(self.email)
