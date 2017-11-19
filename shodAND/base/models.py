from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    creation_date = models.DateTimeField('date created')
    modification_date = models.DateTimeField('date modified')

class Port(models.Model):
    port = models.IntegerField()
    creation_date = models.DateTimeField('date created')
    modification_date = models.DateTimeField('date modified')

class Scan(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE)
    ports = models.ManyToManyField(Port, on_delete=models.CASCADE)
    creation_date = models.DateTimeField('date created')
    modification_date = models.DateTimeField('date modified')
