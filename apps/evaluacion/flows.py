from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView

from .models import HelloWorldProcess
from .models import EvaluacionProcess
#from .views import IniciarEvaluacionView
from viewflow import frontend


@frontend.register
class HelloWorldFlow(Flow):
    process_class = HelloWorldProcess

    start = (
        flow.Start(
            CreateProcessView,
            fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_hello_world_request
        ).Next(this.end)
    )

    end = flow.End()

    def send_hello_world_request(self, activation):
        print(activation.process.text)


@frontend.register
class EvaluacionFlow(Flow):
    process_class = EvaluacionProcess

    inicio = (
        flow.Start(
            CreateProcessView,
            fields=['text']
        ).Permission(
            auto_create=True
        ).Next(this.resolver_evaluacion)
    )

    resolver_evaluacion = (
        flow.View(
            UpdateProcessView,
            fields = ["text"]
        ).Permission(
            auto_create=True
        ).Next(this.ver_resultados)
    )

    ver_resultados = (
        flow.View(
            UpdateProcessView,
            fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.fin)
    )

    fin = flow.End()
