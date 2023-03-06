from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator,EmailValidator

# Create your models here.


class Expense(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now=True) 
    amount = models.IntegerField(validators=[MinValueValidator(0)]) 
    description = models.TextField()

