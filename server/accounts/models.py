from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager, UserManagerAll

from .constants import UserRoleChoice


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(_("username"), max_length=30, blank=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=30, blank=True)
    is_staff = models.BooleanField(_("staff"), default=True)
    role = models.PositiveSmallIntegerField(choices=UserRoleChoice.choices)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    objects_all = UserManagerAll()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")