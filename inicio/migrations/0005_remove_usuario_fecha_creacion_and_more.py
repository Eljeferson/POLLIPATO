# Generated by Django 4.1.7 on 2024-03-11 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_delete_publicacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_creacion',
        ),
        migrations.RemoveField(
            model_name='usuarioefimero',
            name='fecha_creacion',
        ),
    ]
