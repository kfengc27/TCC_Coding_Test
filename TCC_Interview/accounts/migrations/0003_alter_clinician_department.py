# Generated by Django 3.2.8 on 2022-02-20 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_clinician_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinician',
            name='department',
            field=models.CharField(choices=[('3', 'Outpatient Department'), ('5', 'Other Department'), ('2', 'Medical Record Department'), ('1', 'Radiology Department'), ('4', 'Inpatient Service')], default='female', max_length=32),
        ),
    ]
