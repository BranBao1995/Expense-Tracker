from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my_app.models import Expense, User

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Expense, ExpenseAdmin)

admin.site.register(User, UserAdmin)