from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = "{}__iexact".format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    user_type = (
        ('Member', 'Member'),
        ("Librarian", 'Librarian')
    )
    role = models.CharField(choices=user_type, max_length=20, default="mem")
    objects = CustomUserManager()

    def tokens(self):
        tokens = RefreshToken.for_user(self)
        return {"refresh": str(tokens), "access": str(tokens.access_token)}
