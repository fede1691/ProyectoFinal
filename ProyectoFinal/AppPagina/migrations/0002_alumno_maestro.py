# Generated by Django 4.0 on 2021-12-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPagina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.IntegerField()),
                ('nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.IntegerField()),
                ('nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], default='H', max_length=2)),
                ('titulo', models.CharField(choices=[('Lic', 'Licenciatura'), ('M', 'Maestria'), ('D', 'Doctorado')], default='Lic', max_length=12)),
            ],
        ),
    ]
