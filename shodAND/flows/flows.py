from viewflow import flow, frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import ScanProcess

@frontend.register
class ScanFlow(Flow):
    process_class = ScanProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["command"]
        ).Permission(
            auto_create=True
        #).Assign(
        #    lambda process: process.created_by
        ).Next(this.planify)
    )

    planify = (
        flow.View(
            UpdateProcessView,
            fields=["state"]
        ).Permission(
            auto_create=True
        ).Next(this.check_execution)
    )

    check_execution = (
        flow.If(lambda activation: activation.process.state == "done")
        .Then(this.execute)
        .Else(this.wait_for_execution)
    )


    wait_for_execution = (
        flow.If(lambda activation: activation.process.state == "done")
        .Then(this.check_execution)
        .Else(this.check_execution)
    )

    execute = (
        flow.Handler(
            this.dispatch_job
        ).Next(this.end)
    )

    end = flow.End()

    def dispatch_job(self, activation):
        print(activation.process.command, activation.process.state)

