# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermedad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=200)),
                ('sigla', models.CharField(max_length=200)),
                ('Descripcion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dou', models.DateTimeField(blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Madre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=200)),
                ('apellido', models.CharField(unique=True, max_length=200)),
                ('dob', models.DateTimeField(verbose_name=b'date of birth')),
                ('email', models.EmailField(max_length=70, blank=True)),
                ('Observaciones', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Marcador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=200)),
                ('percentil_superior', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('percentil_inferior', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='enfermedad',
            name='marcadores_por_enfermedad',
            field=models.ManyToManyField(to='nucleo.Marcador'),
            preserve_default=True,
        ),
    ]
