# Generated by Django 4.2.5 on 2023-12-02 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrador', '0013_recetas_equipomedico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
