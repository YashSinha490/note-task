# Generated by Django 3.1.3 on 2020-12-03 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtask', '0008_auto_20201128_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='date',
            field=models.DateField(blank=True, default='2020-12-03'),
        ),
        migrations.AlterField(
            model_name='addtask',
            name='time',
            field=models.TimeField(blank=True, default='18:26:28'),
        ),
    ]
