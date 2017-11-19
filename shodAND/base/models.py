from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    modification_date = models.DateTimeField('date modified')
