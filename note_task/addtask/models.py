from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class AddTask(models.Model):
    taskName = models.CharField(max_length = 200)
    date = models.DateField(default = datetime.today().strftime('%Y-%m-%d'),blank=True)
    time = models.TimeField(default = datetime.now().strftime('%H:%M:%S'), blank=True)
    notes = models.CharField(max_length = 500, blank = True, null = True)
    '''user = models.ForeignKey(User, default = None, on_delete = )'''


    def __str__(self):
        return self.taskName
