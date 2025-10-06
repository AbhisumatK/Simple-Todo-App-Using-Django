from django.db import models

class Todomodel(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)