from django.db import models

class UserRoleChoice(models.IntegerChoices):
    READER = 0, 'Reader'
    BLOGGER = 1, 'Blogger'