# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_uno', models.CharField(max_length=50)),
                ('menu_dos', models.CharField(max_length=50)),
                ('menu_tres', models.CharField(max_length=50)),
                ('imagen_ppal', models.ImageField(upload_to=b'/media/')),
                ('titulo_uno', models.CharField(max_length=100)),
                ('parrafo_uno', models.CharField(max_length=500)),
                ('imagen_uno', models.ImageField(upload_to=b'/media/')),
                ('frase_uno', models.CharField(max_length=100)),
                ('img_des_uno', models.ImageField(upload_to=b'/media/')),
                ('titulo_des_uno', models.CharField(max_length=50)),
                ('descripcion_uno', models.CharField(max_length=250)),
                ('img_des_dos', models.ImageField(upload_to=b'/media/')),
                ('titulo_des_dos', models.CharField(max_length=50)),
                ('descripcion_dos', models.CharField(max_length=250)),
                ('img_des_tres', models.ImageField(upload_to=b'/media/')),
                ('titulo_des_tres', models.CharField(max_length=50)),
                ('descripcion_tres', models.CharField(max_length=250)),
                ('imagen_dos', models.ImageField(upload_to=b'/media/')),
                ('frase_dos', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('google', models.CharField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Prueba',
        ),
    ]
