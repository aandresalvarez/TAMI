# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Neonato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('codigo', models.CharField(unique=True, max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(verbose_name=b'date of birth')),
                ('result_path', models.CharField(max_length=200)),
                ('enfermedad_por_neonato', models.ManyToManyField(to='nucleo.Enfermedad')),
                ('lote', models.ForeignKey(to='nucleo.Lote')),
                ('madre', models.ForeignKey(to='nucleo.Madre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Valor_marcadores_de_cada_neonato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valor', models.DecimalField(default=0, max_digits=15, decimal_places=2)),
                ('marcador', models.ForeignKey(to='nucleo.Marcador')),
                ('neonato', models.ForeignKey(to='nucleo.Neonato')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='neonato',
            name='marcadores_por_neonato',
            field=models.ManyToManyField(to='nucleo.Marcador', through='nucleo.Valor_marcadores_de_cada_neonato'),
            preserve_default=True,
        ),
    ]
