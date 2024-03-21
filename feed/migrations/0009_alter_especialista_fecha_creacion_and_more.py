# Generated by Django 4.1.7 on 2024-03-13 04:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_alter_especialista_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialista',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publicacionefimero',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
