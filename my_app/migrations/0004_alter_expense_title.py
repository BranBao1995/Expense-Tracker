# Generated by Django 4.1.7 on 2023-03-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_expense_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]