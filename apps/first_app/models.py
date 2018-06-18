from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<user: {} | {}, {}, {}, {}>".format(self.id, self.first_name, self.last_name, self.email)