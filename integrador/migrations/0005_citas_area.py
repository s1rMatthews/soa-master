# Generated by Django 4.2.5 on 2023-10-01 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrador', '0004_alter_medicos_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='integrador.especialidad'),
        ),
    ]
