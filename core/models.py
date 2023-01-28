from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['email']


