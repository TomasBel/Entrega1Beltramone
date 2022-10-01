# Generated by Django 4.1 on 2022-09-30 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('camada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='entregable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fechaDeEntrega', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('profesion', models.CharField(max_length=60)),
            ],
        ),
    ]