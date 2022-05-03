from django.db import models

# Create your models here.

#!Task Model
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.title)