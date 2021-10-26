# Generated by Django 3.2.8 on 2021-10-18 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pers_nombre', models.CharField(max_length=50)),
                ('pers_ap_paterno', models.CharField(max_length=50)),
                ('pers_ap_matenor', models.CharField(max_length=50)),
                ('pers_dni', models.CharField(max_length=8)),
                ('pers_fnacimiento', models.DateField()),
                ('pers_estado_civil', models.CharField(max_length=50)),
                ('pers_sexo', models.CharField(max_length=2)),
                ('pers_telefono', models.CharField(max_length=9)),
                ('pers_correo', models.EmailField(max_length=50)),
                ('pers_direccion', models.CharField(max_length=50)),
                ('pers_nacionalidad', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]