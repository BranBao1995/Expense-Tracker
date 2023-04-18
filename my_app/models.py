from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Model fields validations are not run automatically unless Django Moodel Form is used
# Model fields validations are app-side validations not DB-side validations
# Can also implement DB-side validations


class User(AbstractUser):
    pass



class Expense(models.Model):
    # max_length is required for models.CharField
    # model fields can use the 'validators=[]' argument
    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    date = models.DateField() 
    amount = models.IntegerField(validators=[MinValueValidator(0)]) 
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):

        return f"{self.title}"    
