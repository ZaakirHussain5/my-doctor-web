# Generated by Django 3.0.5 on 2020-08-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Doctor', models.CharField(max_length=25, null=True)),
                ('Consultations_count', models.IntegerField()),
                ('Total_amt', models.IntegerField()),
                ('Comm_amt', models.IntegerField()),
                ('Amount_payable', models.IntegerField()),
                ('created_at', models.IntegerField()),
                ('created_by', models.CharField(max_length=25, null=True)),
                ('Last_modied', models.DateTimeField(auto_now_add=True)),
                ('Modified_by', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
