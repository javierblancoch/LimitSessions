from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	description = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.username

class UserAcces(models.Model):
	user  = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
	session_key = models.CharField(max_length=32, null=True, blank=True)
	datetime = models.DateTimeField(auto_now=False)

	def __str__(self):
		return str(self.id)