# Generated by Django 3.0.5 on 2020-08-30 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0002_auto_20200814_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_id', models.CharField(max_length=15, unique=True)),
                ('full_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=25)),
                ('dob', models.CharField(max_length=25, null=True)),
                ('age', models.IntegerField(null=True)),
                ('blood_group', models.CharField(max_length=5)),
                ('rel_type', models.CharField(max_length=25, null=True)),
                ('relation', models.CharField(max_length=32, null=True)),
                ('ph_no', models.CharField(max_length=15)),
                ('s_ph_no', models.CharField(max_length=15, null=True)),
                ('pref_lang', models.CharField(max_length=25, null=True)),
                ('street_address', models.CharField(max_length=200, null=True)),
                ('locality', models.CharField(max_length=25, null=True)),
                ('city', models.CharField(max_length=32, null=True)),
                ('pincode', models.CharField(max_length=10, null=True)),
                ('medical_history', models.CharField(max_length=1000, null=True)),
                ('other_history', models.CharField(max_length=100, null=True)),
                ('groups', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.FileField(max_length=355, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='patient_health_info',
        ),
    ]
