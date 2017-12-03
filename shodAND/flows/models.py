from django.db import models
from viewflow.models import Process
#from base.models import Scan

AVAILABLE_STATUS = (
    ('todo', 'To do'),
    ('pending', 'Pending'),
    ('wip', 'Work in progress'),
    ('done', 'Done'),
)

#class ScanProcess(Scan, Process):
class ScanProcess(Process):
    """ Simple scan model """
    command = models.CharField(max_length=150)
    result = models.CharField(max_length=150)
    state = models.CharField(
        max_length=20,
        choices=AVAILABLE_STATUS,
        default="todo",
    )
    error = models.BooleanField(default=False)

