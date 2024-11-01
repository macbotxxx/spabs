# Generated by Django 4.2.13 on 2024-07-31 01:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_jobportal'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobEnrollment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='The unique identifier of an object.', primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Timestamp when the record was created. The date and time\n            are displayed in the Timezone from where request is made.\n            e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC', verbose_name='Created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Timestamp when the record was modified. The date and\n            time are displayed in the Timezone from where request\n            is made. e.g. 2019-14-29T00:15:09Z for April 29, 2019 0:15:09 UTC\n            ', null=True, verbose_name='Updated')),
                ('names', models.CharField(help_text='this hold the first , last and maiden name', max_length=250, null=True, verbose_name='Full Name')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], help_text='the gender of the applicant is required', max_length=10, null=True, verbose_name='Gender')),
                ('residential_address', models.CharField(help_text='the current residential address of the applicant', max_length=350, null=True, verbose_name='Residential Address')),
                ('state_of_residential', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'Federal Capital Territory'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], help_text='current state of residential is needed', max_length=40, null=True, verbose_name='State Of Residential')),
                ('local_gov_area', models.CharField(help_text='local gov area of the residential state', max_length=100, null=True, verbose_name='Local Gov Area')),
                ('phone_number', models.CharField(help_text='the applicant mobile number will be inputted', max_length=15, null=True, verbose_name='Phone Number')),
                ('date_of_birth', models.DateField(help_text='the applicant date of birth', max_length=25, null=True, verbose_name='Job Title')),
                ('place_of_birth', models.CharField(help_text='input the place of birth', max_length=250, null=True, verbose_name='Place Of Birth')),
                ('state_of_origin', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Adamawa'), ('Akwa Ibom', 'Akwa Ibom'), ('Anambra', 'Anambra'), ('Bauchi', 'Bauchi'), ('Bayelsa', 'Bayelsa'), ('Benue', 'Benue'), ('Borno', 'Borno'), ('Cross River', 'Cross River'), ('Delta', 'Delta'), ('Ebonyi', 'Ebonyi'), ('Edo', 'Edo'), ('Ekiti', 'Ekiti'), ('Enugu', 'Enugu'), ('FCT', 'Federal Capital Territory'), ('Gombe', 'Gombe'), ('Imo', 'Imo'), ('Jigawa', 'Jigawa'), ('Kaduna', 'Kaduna'), ('Kano', 'Kano'), ('Katsina', 'Katsina'), ('Kebbi', 'Kebbi'), ('Kogi', 'Kogi'), ('Kwara', 'Kwara'), ('Lagos', 'Lagos'), ('Nasarawa', 'Nasarawa'), ('Niger', 'Niger'), ('Ogun', 'Ogun'), ('Ondo', 'Ondo'), ('Osun', 'Osun'), ('Oyo', 'Oyo'), ('Plateau', 'Plateau'), ('Rivers', 'Rivers'), ('Sokoto', 'Sokoto'), ('Taraba', 'Taraba'), ('Yobe', 'Yobe'), ('Zamfara', 'Zamfara')], help_text='current state of origin is needed', max_length=40, null=True, verbose_name='State Of Origin')),
                ('means_of_identification', models.CharField(help_text='kindly submit the means of identification which is needed', max_length=40, null=True, verbose_name='Means Of Identification')),
                ('next_of_kin', models.CharField(help_text='the name of next of kin which will be passed by the applicant', max_length=100, null=True, verbose_name='Name Of Next Of Kin')),
                ('referee', models.CharField(help_text='ythe name of the refree and phone number', max_length=100, null=True, verbose_name='Name Of Referee and Phone Number')),
                ('job_categories', models.ForeignKey(help_text='the job categories should be selected by the applicant', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.jobportal', verbose_name='Job Categories')),
            ],
            options={
                'verbose_name': 'Job Enrollment',
                'verbose_name_plural': 'Job Enrollment',
                'ordering': ['-created_date'],
            },
        ),
    ]
