# Generated by Django 3.0.5 on 2020-08-14 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_health_info',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patient_health_info',
            name='weight',
        ),
    ]
