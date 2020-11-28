# Generated by Django 3.1.3 on 2020-11-27 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addtask', '0007_auto_20201124_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='addtask',
            name='date',
            field=models.DateField(blank=True, default='2020-11-28'),
        ),
        migrations.AlterField(
            model_name='addtask',
            name='time',
            field=models.TimeField(blank=True, default='00:05:04'),
        ),
    ]