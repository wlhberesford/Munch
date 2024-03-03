from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	#set to 100 for testing
	content = models.TextField()
	#size not set to allow for long descriptions
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	#^ deletes post since post's author is linked and will delete if author is gone
	#if this is changed any way at all, remember to make migrations
	#python manage.py makemigrations
	#haven't tested yet

	def __str__(self):
		return self.title

