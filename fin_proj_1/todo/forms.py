# from django.db.models.fields import BooleanField, DateTimeField
from datetime import datetime
from django.core.exceptions import ValidationError
from django.forms.widgets import Textarea
from .models import Task
from django.forms import ModelForm, TextInput, DateInput

class TaskForm(ModelForm):
    
    
    class Meta:

        model = Task
        fields = ['title','description', 'deadline']
        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Title'}),
            'description': Textarea(attrs={
                'class':'form-control',
                'placeholder':'Description'}),

            'deadline': DateInput(attrs={
                'class':'form-control',
                'placeholder':'Deadline yyyy-mm-dd'}),
        }

    def clean_deadline(self):

        user_deadline = self.cleaned_data['deadline']
        if user_deadline and user_deadline < datetime.today().date():
            raise ValidationError ("Deadline sould be today and later")
        return user_deadline    

    
