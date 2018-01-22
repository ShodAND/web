from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from django.contrib import messages

from .models import ScanProcess
from .tasks import perform_scan 

from base.models import Scan, Host, Port



@frontend.register
class ScanFlow(Flow):
    process_class = ScanProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["host", "ports"]
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

        host = activation.process.host
        ports = activation.process.ports.all()

        new_scan = Scan(host=host)
        new_scan.save()
        new_scan.ports.add(*ports)

        perform_scan.delay(new_scan.id)
        print ("Task dispatched!")

