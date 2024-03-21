# Generated by Django 4.1.7 on 2024-03-11 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_delete_publicacion'),
        ('feed', '0003_remove_especialista_datos_especialista_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inicio.usuario'),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='foto/'),
        ),
    ]