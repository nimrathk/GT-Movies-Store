# models.py
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    security_question = models.CharField(max_length=50)
    security_answer = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
