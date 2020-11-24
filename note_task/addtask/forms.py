from django import forms
from .models import AddTask

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ('taskName', 'date', 'time', 'notes')

        widgets = {
            'taskName': forms.TextInput(attrs={'type':"text", 'class':"task__name_input", 'placeholder':"task name"}),
            'date': forms.TextInput(attrs={'type':"text", 'class':"date__input", 'placeholder':"DD/MM/YYYY", 'value':"12/20/2020"}),
            'time': forms.TextInput(attrs={'type':"text", 'class':"time__input", 'placeholder':"HH:MM", 'value':'06:30'}),
            'notes': forms.TextInput(attrs={'type':"text", 'class':"notes__input", 'placeholder':"Notes"}),
        }
