# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20141029_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140)),
                ('resumen', models.CharField(max_length=500)),
                ('imagen', models.ImageField(upload_to=b'media/')),
                ('contenido', models.TextField()),
                ('archivo', models.FileField(upload_to=b'media/')),
                ('date', models.DateField(default=datetime.date(2014, 11, 22))),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='campos',
            name='imagen_dos',
            field=models.ImageField(upload_to=b'media/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campos',
            name='imagen_ppal',
            field=models.ImageField(upload_to=b'media/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campos',
            name='imagen_uno',
            field=models.ImageField(upload_to=b'media/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campos',
            name='img_des_dos',
            field=models.ImageField(upload_to=b'media/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campos',
            name='img_des_tres',
            field=models.ImageField(upload_to=b'media/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='campos',
            name='img_des_uno',
            field=models.ImageField(upload_to=b'media/'),
            preserve_default=True,
        ),
    ]
