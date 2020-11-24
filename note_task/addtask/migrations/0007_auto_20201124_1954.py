# Generated by Django 3.1.3 on 2020-11-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addtask', '0006_auto_20201124_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addtask',
            name='body',
        ),
        migrations.AddField(
            model_name='addtask',
            name='notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='addtask',
            name='time',
            field=models.TimeField(blank=True, default='19:54:50'),
        ),
    ]
