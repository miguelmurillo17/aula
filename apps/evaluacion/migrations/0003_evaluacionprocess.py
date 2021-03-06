# Generated by Django 3.2.11 on 2022-01-11 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewflow', '0008_jsonfield_and_artifact'),
        ('evaluacion', '0002_alumno_area_ejetematico_grupo_pregunta_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionProcess',
            fields=[
                ('process_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='viewflow.process')),
                ('titulo', models.CharField(max_length=20)),
                ('aprobado', models.BooleanField(default=False)),
                ('fecha', models.DateField()),
                ('cantidadPreguntas', models.CharField(choices=[('1', '1'), ('3', '3'), ('5', '5')], max_length=9)),
                ('ejeTematico', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='evaluacion.ejetematico')),
                ('grupo', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='evaluacion.grupo')),
            ],
            options={
                'abstract': False,
            },
            bases=('viewflow.process',),
        ),
    ]
