# Generated by Django 3.1.5 on 2021-01-22 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtask', '0010_auto_20210123_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtask',
            name='time',
            field=models.TimeField(blank=True, default='00:12:43'),
        ),
    ]
