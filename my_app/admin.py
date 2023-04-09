from django.contrib import admin
from my_app.models import Expense, User

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, User, ExpenseAdmin)