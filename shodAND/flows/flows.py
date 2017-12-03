from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import ScanProcess

class HelloWorldFlow(Flow):
    process_class = ScanProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.planify)
    )

    planify = (
        flow.View(
            UpdateProcessView,
            fields=["status"]
        ).Permission(
            auto_create=True
        ).Next(this.check_execution)
    )

    check_execution = (
        flow.If(lambda activation: activation.process.status)
        .Then(this.execute)
        .Else(this.end)
    )

    execute = (
        flow.Handler(
            this.dispatch_job
        ).Next(this.end)
    )

    end = flow.End()

    def dispatch_job(self, activation):
        print(activation.process.command)

