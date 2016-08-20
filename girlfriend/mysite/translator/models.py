from django.db import models
from datetime import datetime

# Create your models here.

class user_input(models.Model):
	content = models.CharField(max_length=100)

	def __str__(self):
		return self.content

