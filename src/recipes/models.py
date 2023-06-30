from django.db import models
from django.shortcuts import reverse

type_choices =(
  ('Breakfast', 'Breakfast'),
  ('Drink', 'Drink'),
  ('Lunch', 'Lunch'),
  ('Snack','Snack'),
  ('Tea', 'Tea'),
  ('Dinner', 'Dinner'),
)

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255, help_text="You must use a comma to separate the ingredients.")
    cooking_time = models.PositiveIntegerField(help_text="In minutes")
    type = models.CharField(max_length=50, choices=type_choices)
    instructions = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
      return str(self.name)

    def calculate_difficulty(self):
      ingredients = self.ingredients.split(', ')
      if self.cooking_time < 10 and len(ingredients) < 5:
        difficulty = "Easy"
      elif self.cooking_time < 10 and len(ingredients) >= 5:
        difficulty = "Medium"
      elif self.cooking_time >= 10 and len(ingredients) < 5:
        difficulty = "Intermediate"
      elif self.cooking_time >= 10 and len(ingredients) >= 5:
        difficulty = "Hard"
      return difficulty

    def get_absolute_url(self):
      return reverse ('recipes:detail', kwargs={'pk': self.pk})




