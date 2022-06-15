'''
from django import forms
from django_superform import SuperModelForm, InlineFormSetField
from material import Layout, Row

from .models import(
    Profesor,
    Grupo,
    Alumno,
    Area,
    EjeTematico,
    Pregunta,
    EvaluacionProcess,
)

class IniciarEvaluacionForm(SuperModelForm):
    class Meta:
        model = EvaluacionProcess
        fields = [
            'fecha',
            'grupo',
            'ejeTematico',
            'cantidadPreguntas'
        ]
'''