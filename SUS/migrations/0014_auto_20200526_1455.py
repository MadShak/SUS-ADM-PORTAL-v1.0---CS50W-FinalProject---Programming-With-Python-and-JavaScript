# Generated by Django 3.0.5 on 2020-05-26 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SUS', '0013_patient_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
