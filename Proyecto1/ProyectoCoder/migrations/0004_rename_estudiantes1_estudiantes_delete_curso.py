# Generated by Django 4.1 on 2022-10-01 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoCoder', '0003_rename_estudiantes_estudiantes1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='estudiantes1',
            new_name='estudiantes',
        ),
        migrations.DeleteModel(
            name='curso',
        ),
    ]
