# Generated by Django 2.2.5 on 2019-10-03 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20190918_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles_record',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]