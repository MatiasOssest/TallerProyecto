# Generated by Django 3.2.4 on 2021-06-03 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='longitud',
        ),
    ]