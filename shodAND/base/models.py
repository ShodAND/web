from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class ShodANDModel(models.Model):
    """
    Default ShodAND Model

    Integrate default fields:
    - creation_date
    - modification_date

    Also update modification_date at every save()
    """
    creation_date = models.DateTimeField('date created', default=datetime.datetime.now)
    modification_date = models.DateTimeField('date modified', default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        self.modification_date = datetime.datetime.now()
        super(ShodANDModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Host(ShodANDModel):
    hostname = models.CharField(max_length=200)
    ip = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.ip}"

    def __repr__(self):
        return f"<Host {self.ip}>"

    class Meta:
        ordering = ['ip']


class Port(ShodANDModel):
    port = models.IntegerField(
        unique=True,
        validators=[
            MaxValueValidator(65535),
            MinValueValidator(1)
        ]
    )
    privileged = models.BooleanField(default=False, editable=False)
    label = models.CharField(max_length=200, editable=False)

    def __str__(self):
        return f"{self.port}"

    def __repr__(self):
        return f"<Port {self.port}>"

    def save(self, *args, **kwargs):
        self.privileged = True if self.port < 1024 else False
        super(Port, self).save(*args, **kwargs)

    class Meta:
        ordering = ['port']


class Scan(ShodANDModel):
    host = models.ForeignKey(Host, on_delete=models.CASCADE, unique_for_date="creation_date")
    ports = models.ManyToManyField(Port)

    def __str__(self):
        return f"{self.host} [{self.ports}]"

    def __repr__(self):
        return f"<Scan {self.host} [{self.ports}]>"

    class Meta:
        ordering = ['host', 'creation_date']
