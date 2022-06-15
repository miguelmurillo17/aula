from django.db import models
from viewflow.models import Process
import datetime
from django.db.models.deletion import CASCADE

# Create your models here.
class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

class Profesor(models.Model):
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    curp = models.CharField(max_length=18,unique=True)
    fechaNacimiento = models.DateField()
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def nombreCompleto(self):
        cadena = '{0} {1} {2}'
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

    def __str__(self):
        return self.nombreCompleto()

class Grupo(models.Model):
    nombre = models.CharField(max_length=4)
    año_inicio_generacion = models.IntegerField(null=False, blank=False, default=datetime.date.today().year)

    def aliasGrupo(self):
        cadena = '{0} - generación {1}'
        return cadena.format(self.nombre, self.año_inicio_generacion)
    
    def __str__(self):
        return self.aliasGrupo()

class Alumno(models.Model):
    generos = [
        ('f','Femenino'),
        ('m','Masculino')
    ]

    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombre = models.CharField(max_length = 35)
    curp = models.CharField(max_length=18,unique=True)
    fechaNacimiento = models.DateField()
    genero = models.CharField(max_length=9,choices=generos,null=False,blank=False)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE,default=1)
    #usuario = models.ForeignKey(User,on_delete=models.CASCADE,default=1)

    def nombreCompleto(self):
        cadena = '{0} {1} {2}'
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.nombre)

    def __str__(self):
        return self.nombreCompleto()

class Area(models.Model):
    nombre = models.CharField(max_length = 35)

    def __str__(self):
        return self.nombre

class EjeTematico(models.Model):
    nombre = models.CharField(max_length = 50)
    area = models.ForeignKey(Area, null=False, blank=False, default=1, on_delete=models.CASCADE)

    def nombreCompuesto(self):
        cadena = '{0}: {1}'
        return cadena.format(self.area, self.nombre)

    def __str__(self):
        return self.nombreCompuesto()

class Pregunta(models.Model):
    ejeTematico = models.ForeignKey(EjeTematico, null=False, blank=False, default=1, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length = 300, null=False, blank=False)
    opcionA = models.CharField(max_length = 100 , null=False, blank=False)
    opcionB = models.CharField(max_length = 100, null=False, blank=False)
    opcionC = models.CharField(max_length = 100, null=False, blank=False)
    opcionD = models.CharField(max_length = 100, null=False, blank=False)
    opciones = (('A','A'),('B','B'),('C','C'),('D','D'))
    opcionCorrecta = models.CharField(max_length=1, choices=opciones, null=False, blank=False)

    def __str__(self):
        return self.pregunta

class EvaluacionProcess(Process):
    preguntas = [
        ('1','1'),
        ('3','3'),
        ('5','5')
    ]
    
    text = models.CharField(max_length=20)
    aprobado =  models.BooleanField(default=False)
    #fecha = models.DateField()
    #ejeTematico = models.ForeignKey(EjeTematico, null=False, blank=False, default=1, on_delete=models.CASCADE)
    #grupo = models.ForeignKey(Grupo,null=False,blank=False,default=1,on_delete=CASCADE)
    #cantidadPreguntas = models.CharField(max_length=9,choices=preguntas,null=False,blank=False)


"""
class EvaluacionProcess(Process):
    preguntas = [
        ('1','1'),
        ('3','3'),
        ('5','5')
    ]
    fecha = models.DateField()
    grupo = models.ForeignKey(Grupo,null=False,blank=False,default=1,on_delete=models.CASCADE)
    ejeTematico = models.ForeignKey(EjeTematico, null=False, blank=False, default=1, on_delete=models.CASCADE)
    cantidadPreguntas = models.CharField(max_length=9,choices=preguntas,null=False,blank=False)
    comentarios = models.CharField(max_length=20)
    aprobado =  models.BooleanField(default=False)

class Evaluacion(models.Model):
    grupo = models.ForeignKey(Grupo, null=False, blank=False, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField(null=False, blank=True)
    fechaFin = models.DateTimeField(null=False)
    codigoAcceso = models.CharField(max_length=10, null=False, blank=False, default='123456789$')

    def __str__(self):
        cadena = '{0} - {1} - {2}'
        return cadena.format(self.grupo, self.area, self.fechaInicio)


# Capturas:
class RespuestaEvaluacion(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, null=False, blank=False, on_delete=models.CASCADE)
    pregunta = models.ForeignKey(Pregunta, null=False, blank=False, on_delete=models.CASCADE)
    respuestaAlumno = models.CharField(max_length = 1 , null=False, blank=False)


# Configuraciones:

#class Grupo_alumno(models.Model):
#    alumno = models.ForeignKey(Alumno, null=False, blank=False, on_delete=models.CASCADE)
#    grupo = models.ForeignKey(Grupo, null=False, blank=False, on_delete=models.CASCADE)
#    #creacion = models.DateTimeField(auto_now_add=True, blank=True)
#    #actualizacion = models.DateTimeField(auto_now=True)

#    def __str__(self):
#        return self.grupo
"""
