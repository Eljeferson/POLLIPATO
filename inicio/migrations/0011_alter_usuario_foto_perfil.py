# Generated by Django 4.1.7 on 2024-03-12 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0010_alter_usuario_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, null=True, upload_to='perfil/'),
        ),
    ]
