# Generated by Django 4.2.13 on 2024-08-03 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_jobenrollment_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobenrollment',
            name='passport',
            field=models.ImageField(null=True, upload_to='passport/', verbose_name='Passport'),
        ),
        migrations.AlterField(
            model_name='jobenrollment',
            name='local_gov_area',
            field=models.CharField(choices=[('Abeokuta North', 'Abeokuta North'), ('Abeokuta South', 'Abeokuta South'), ('Ado Odo-ota', 'Ado Odo-ota'), ('Ewekoro', 'Ewekoro'), ('Ifo', 'Ifo'), ('Ijebu East', 'Ijebu East'), ('Ijebu North', 'Ijebu North'), ('Ijebu North East', 'Ijebu North East'), ('Ijebu Ode', 'Ijebu Ode'), ('Ikenne', 'Ikenne'), ('Imeko Afon', 'Imeko Afon'), ('Ipokia', 'Ipokia'), ('Obafemi Owode', 'Obafemi Owode'), ('Odeda', 'Odeda'), ('Odogbolu', 'Odogbolu'), ('Ogun Water Side', 'Ogun Water Side'), ('Remo North', 'Remo North'), ('Sagamu', 'Sagamu'), ('Yewa North', 'Yewa North'), ('Yewa South', 'Yewa South')], max_length=100, null=True, verbose_name='Local Gov Area'),
        ),
        migrations.AlterField(
            model_name='jobenrollment',
            name='means_of_identification',
            field=models.CharField(choices=[('NIN', 'NIN'), ('VOTERS ID CARD', 'VOTERS ID CARD'), ('DRIVERS LICENSE', 'DRIVERS LICENSE'), ('INTERNATIONAL PASSPORT', 'INTERNATIONAL PASSPORT')], max_length=70, null=True, verbose_name='Means Of Identification'),
        ),
    ]
