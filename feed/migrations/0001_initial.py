# Generated by Django 4.1.7 on 2024-03-05 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publicacion', models.CharField(max_length=500)),
                ('foto', models.ImageField(upload_to='foto/')),
            ],
        ),
    ]