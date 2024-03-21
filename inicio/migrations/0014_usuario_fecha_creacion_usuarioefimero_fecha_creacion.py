# Generated by Django 4.1.7 on 2024-03-13 03:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0013_alter_usuarioefimero_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='usuarioefimero',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]