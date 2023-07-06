# Generated by Django 4.2.2 on 2023-07-03 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Drink', 'Drink'), ('Lunch', 'Lunch'), ('Snack', 'Snack'), ('Tea', 'Tea'), ('Dinner', 'Dinner')], max_length=50),
        ),
    ]