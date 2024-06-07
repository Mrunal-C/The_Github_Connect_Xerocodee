
from django.db import models

class Repository(models.Model):
    owner = models.CharField(max_length=100)
    repo_name = models.CharField(max_length=100)
    repo_description = models.TextField(blank=True)
    repo_url = models.URLField()
    is_private = models.BooleanField()
    repo_description = models.CharField(max_length=255, null=True, blank=True)
