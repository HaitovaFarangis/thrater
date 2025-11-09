from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    duration = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Movie'
        managed = True
    
    
    
class Performance(models.Model):
    movie = models.ForeignKey( Movie,on_delete=models.CASCADE  )
    hall = models.CharField(max_length=50)
    time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.hall
    
    class Meta:
        db_table = 'Performance'
        managed = True
    
# Create your models here.
