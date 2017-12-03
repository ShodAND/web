from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from django.contrib import messages

from .models import ScanProcess
from .tasks import perform_scan 

@frontend.register
class ScanFlow(Flow):
    process_class = ScanProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["command"]
        ).Permission(
            auto_create=True
        ).Next(this.send)
    )

    send = (
        flow.Handler(
            this.trigger_scan
        ).Next(this.end)
    )

    end = flow.End()

    def trigger_scan(self, activation):
        #messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')

        print ("Triggering celery task")
        perform_scan.delay(activation.process.command)
        print ("Task dispatched!")
