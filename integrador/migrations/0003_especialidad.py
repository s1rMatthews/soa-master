# Generated by Django 4.2.5 on 2023-10-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrador', '0002_remove_pacientes_paciente_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
