# Generated by Django 3.2.12 on 2022-02-17 05:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220217_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='unqiue_number',
            field=models.CharField(default=uuid.uuid4, max_length=36),
        ),
    ]
