# Generated by Django 3.0.5 on 2020-08-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist_type', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specialist_type',
            old_name='is_acrive',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='specialist_type',
            name='icon',
            field=models.FileField(max_length=355, null=True, upload_to=''),
        ),
    ]
