from django.test import TestCase
from .models import Recipe

# Create your tests here.
class RecipeModelTest(TestCase):
  
  def setUpTestData():
    Recipe.objects.create(
      name='Tea white',
      ingredients='Water, Tea Leaves, Milk',
      cooking_time=6,
      type='Drink',
      instructions='''Bring water to the boil,
                      then add to the Tea leaves,
                      let it steep for 5 minutes,
                      then add milk to taste.''',
    )

  def test_recipe_name(self):
    recipe = Recipe.objects.get(id=1)
    field_label = recipe._meta.get_field('name').verbose_name
    self.assertEqual(field_label, 'name')

  def test_recipe_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('name').max_length
    self.assertEqual(max_length, 50)

  def test_ingredients_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 255)
  
  def test_cooking_time_max_length(self):
    recipe = Recipe.objects.get(id=1)
    help_text = recipe._meta.get_field('cooking_time').help_text
    self.assertEqual(help_text, 'In minutes')

  def test_type_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('type').max_length
    self.assertEqual(max_length, 20)