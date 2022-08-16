# Generated by Django 4.0.5 on 2022-08-04 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('dni', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apPat', models.CharField(max_length=20)),
                ('apMat', models.CharField(max_length=20)),
                ('telf', models.CharField(max_length=6)),
                ('edad', models.IntegerField()),
                ('dir', models.CharField(max_length=30)),
                ('fechNac', models.DateField()),
                ('medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Medico.medico')),
            ],
        ),
    ]
