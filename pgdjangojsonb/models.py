from django.db import models
from django.contrib.postgres.fields import JSONField


class Profile(models.Model):
    name = models.CharField(max_length=200)
    preferences = JSONField()

    def __str__(self):
        return self.name
