# Generated by Django 3.0.5 on 2020-09-02 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_doctors_info_mou_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mon', models.BooleanField()),
                ('tue', models.BooleanField()),
                ('wed', models.BooleanField()),
                ('thu', models.BooleanField()),
                ('fri', models.BooleanField()),
                ('sat', models.BooleanField()),
                ('sun', models.BooleanField()),
                ('from_time', models.CharField(max_length=50)),
                ('to_time', models.CharField(max_length=50)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctors_info')),
            ],
        ),
    ]