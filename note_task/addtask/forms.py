from django import forms
from addtask.models import AddTask

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ('taskName', 'date', 'time')

        widgets = {
            'taskName': forms.TextInput(attrs={'class' : 'add__taskname', 'placeholder' : "Task Name"}),
            'date': forms.TextInput(attrs={'placeholder' : "Add Date", 'class' : "add__taskdate"}),
            'time': forms.TextInput(attrs={'placeholder' : "Add Time", 'class' : "add__tasktime"}),
        }
