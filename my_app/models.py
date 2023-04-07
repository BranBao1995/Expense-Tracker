from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.

# Model fields validations are not run automatically unless Django Moodel Form is used
# Model fields validations are app-side validations not DB-side validations
# Can also implement DB-side validations

class Expense(models.Model):
    # max_length is required for models.CharField
    # model fields can use the 'validators=[]' argument
    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    date = models.DateField() 
    amount = models.IntegerField(validators=[MinValueValidator(0)]) 
    description = models.TextField()

    def __str__(self):

        return f"{self.title}"    
