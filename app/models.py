from django.db import models


class User(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    hbtn_id = models.PositiveIntegerField()
    hbtn_key = models.TextField()
    hbtn_auth = models.TextField()
    hbtn_password = models.TextField()
    phone = models.PositiveIntegerField()
    nexmo_key = models.TextField()
    nexmo_secret = models.TextField()
    cohort = models.TextField()
