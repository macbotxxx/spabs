# Generated by Django 4.2.13 on 2024-08-04 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_jobenrollment_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobenrollment',
            name='completed_enrollment',
            field=models.BooleanField(default=False, help_text='this indicates if the enrollment process has been confirmed if the payment is completed', null=True, verbose_name='Enrollment Completed'),
        ),
        migrations.AddField(
            model_name='jobenrollment',
            name='identification_number',
            field=models.CharField(max_length=150, null=True, verbose_name='Identification Number'),
        ),
        migrations.AddField(
            model_name='jobenrollment',
            name='referee_phone_number',
            field=models.CharField(max_length=100, null=True, verbose_name='Referee Phone Number'),
        ),
    ]