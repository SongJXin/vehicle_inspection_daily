# Generated by Django 2.2.5 on 2019-09-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20190917_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles_record',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='vehicles_record',
            name='vehicle_type',
            field=models.IntegerField(max_length=50),
        ),
    ]
