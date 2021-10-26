# Generated by Django 3.2.8 on 2021-10-18 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracto_fecha', models.DateField()),
                ('tracto_horas', models.CharField(max_length=50)),
                ('tracto_tipo', models.CharField(max_length=50)),
                ('tracto_socio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socio.socio')),
            ],
            options={
                'verbose_name': 'Tracto',
                'verbose_name_plural': 'Tractos',
            },
        ),
    ]
