from django.db import models
from viewflow.models import Process

AVAILABLE_STATUS = (
    ('todo', 'To do'),
    ('pending', 'Pending'),
    ('wip', 'Work in progress'),
    ('done', 'Done'),
)

class ScanProcess(Process):
    """ Simple scan model """
    result = models.CharField(max_length=150)
    status = models.CharField(
        max_length=20,
        choices=AVAILABLE_STATUS,
        default="todo",
    )
    error = models.BooleanField(default=False)

