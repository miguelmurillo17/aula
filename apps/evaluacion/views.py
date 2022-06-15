from django.shortcuts import render
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from .forms import (IniciarEvaluacionForm)

# Create your views here.
class IniciarEvaluacionView(CreateProcessView):
    from_class = IniciarEvaluacionForm
