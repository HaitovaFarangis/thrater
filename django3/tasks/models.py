from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length = 100 )
    description = models.TextField(null = True, blank = True)
    due_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now = True)
    image = models.ImageField()
    
    class Meta:
        db_table = 'tasks'
        managed = True
        verbose_name = 'Zadach'
        verbose_name_plural = 'Zadachi'


# Create your models here.
