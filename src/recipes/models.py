from django.db import models
type_choices =(
  ('breakfast', 'Breakfast'),
  ('drink', 'Drink'),
  ('lunch', 'Lunch'),
  ('snack','Snack'),
  ('tea', 'Tea'),
)
# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=255, help_text="You must use a comma to separate the ingredients.")
    cooking_time = models.PositiveIntegerField(help_text="In minutes")
    type = models.CharField(max_length=20, choices=type_choices, default="br")
    instructions = models.TextField()

    def __str__(self):
      return str(self.name)



