from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my_app.models import Expense, User

# Register your models here.

# Customize admin area
class ExpenseAdmin(admin.ModelAdmin):
    fields = (('title', 'date'), 'amount', 'description', 'author') # customize fields in the detail page
    list_display = ('title', 'date', 'amount') # add columns on the main model page.
    list_filter = ('title', 'date', 'amount') # add custom filter
    ordering = ('-date',) # order by date, from newest to oldest. Remove '-' if you want to order by date from oldest to newest.
    search_fields = ('title', 'date')

admin.site.register(Expense, ExpenseAdmin)

admin.site.register(User, UserAdmin)