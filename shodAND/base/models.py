from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Host(models.Model):
    hostname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200, unique=True)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now)
    modification_date = models.DateTimeField('date modified', default=datetime.datetime.now)

    def __str__(self):
        return f"{self.ip}"

    def __repr__(self):
        return f"<Host {self.ip}>"

    class Meta:
        ordering = ['ip']


class Port(models.Model):
    port = models.IntegerField(
        unique=True,
        validators=[
            MaxValueValidator(65535),
            MinValueValidator(1)
        ]
    )
    privileged = models.BooleanField(default=False, editable=False)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now)
    modification_date = models.DateTimeField('date modified', default=datetime.datetime.now)

    def __str__(self):
        return f"{self.port}"

    def __repr__(self):
        return f"<Port {self.port}>"

    def save(self, *args, **kwargs):
        self.privileged = True if self.port < 1024 else False
        super(Port, self).save(*args, **kwargs)

    class Meta:
        ordering = ['port']


class Scan(models.Model):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, unique_for_date="creation_date")
    ports = models.ManyToManyField(Port)
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now)
    modification_date = models.DateTimeField('date modified', default=datetime.datetime.now)

    def __str__(self):
        return f"{self.host} [{self.ports}]"

    def __repr__(self):
        return f"<Scan {self.host} [{self.ports}]>"

    class Meta:
        ordering = ['host', 'creation_date']
