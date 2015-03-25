"""
Definition of models.
"""

from django.db import models

class Twitte(models.Model):
    twitter_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200, unique=True)
    text = models.CharField(max_length=200)
    created_at = models.CharField(max_length=200)
    user_followers_count = models.IntegerField()
    user_profile_image_url = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')
