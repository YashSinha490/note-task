# Generated by Django 3.1.3 on 2020-11-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtask', '0005_auto_20201124_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='time',
            field=models.TimeField(blank=True, default='16:06:55'),
        ),
    ]
