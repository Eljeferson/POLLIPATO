# Generated by Django 4.1.7 on 2024-03-13 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0012_usuarioefimero_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioefimero',
            name='foto',
            field=models.ImageField(default='incognito.jpg', upload_to='fotos_incognito/'),
        ),
    ]
