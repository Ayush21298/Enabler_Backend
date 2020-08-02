from django.db import models
from django.utils import timezone

from utils import *

# Create your models here.
class Video(models.Model):
	url = models.CharField(max_length=128, null=True)
	file = models.FileField(upload_to=get_upload_path_video, blank=True, null=True)
	title = models.CharField(max_length=64, null=True)
	description = models.TextField(max_length=64, null=True)
	author = models.CharField(max_length=64, null=True)
	uploader = models.CharField(max_length=64, null=True)
	approved = models.BooleanField(default=False)
	timestamp = models.DateTimeField(default=timezone.now, null=True)

	def __str__(self):
		return self.url
