# Generated by Django 3.2.8 on 2021-10-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tractor_codigo', models.CharField(max_length=50)),
                ('tractor_marca', models.CharField(max_length=50)),
                ('tractor_modelo', models.CharField(max_length=50)),
                ('tractor_potencia', models.CharField(max_length=50)),
                ('tractor_velocidad', models.CharField(max_length=50)),
                ('tractor_articulacion', models.CharField(max_length=50)),
                ('tractor_estado', models.CharField(max_length=2)),
                ('tractor_created', models.DateField(auto_now_add=True)),
                ('tractor_updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Tractor',
                'verbose_name_plural': 'Tractores',
            },
        ),
    ]
