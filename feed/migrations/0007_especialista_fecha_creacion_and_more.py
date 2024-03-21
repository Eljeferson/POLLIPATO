# Generated by Django 4.1.7 on 2024-03-13 03:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_remove_publicacion_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialista',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='publicacionefimero',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
