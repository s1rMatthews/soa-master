# Generated by Django 4.2.5 on 2023-11-18 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrador', '0007_salaoperaciones_delete_cirugias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('dni', models.PositiveIntegerField()),
                ('celp', models.PositiveIntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Enfermeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('dni', models.PositiveIntegerField()),
                ('celp', models.PositiveIntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrador.especialidad')),
            ],
        ),
    ]
