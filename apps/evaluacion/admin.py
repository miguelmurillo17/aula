from django.contrib import admin

# Register your models here.
from .models import (
    Profesor,
    Grupo,
    Alumno,
    Area,
    EjeTematico,
    Pregunta,
    #EvaluacionProcess,
)

admin.site.register(Profesor)
admin.site.register(Grupo)
admin.site.register(Alumno)
admin.site.register(Area)
admin.site.register(EjeTematico)
admin.site.register(Pregunta)
#admin.site.register(EvaluacionProcess)