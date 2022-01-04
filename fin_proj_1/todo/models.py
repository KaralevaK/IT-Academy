from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.http import request
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE, null=True, blank=True, name='user')
    title = models.CharField('title', max_length=200)
    description = models.TextField('description', blank=False)
    complete = models.BooleanField('complete', default=False)
    created = models.DateTimeField('created', auto_now_add=True)
    deadline = models.DateField('deadline', null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    
