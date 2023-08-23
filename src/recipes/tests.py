from django.test import TestCase
from .models import Recipe
from .forms import RecipeSearchForm

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
    self.assertEqual(max_length, 120)

  def test_ingredients_name_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('ingredients').max_length
    self.assertEqual(max_length, 300)
  
  def test_cooking_time_max_length(self):
    recipe = Recipe.objects.get(id=1)
    help_text = recipe._meta.get_field('cooking_time').help_text
    self.assertEqual(help_text, 'In minutes')

  def test_type_max_length(self):
    recipe = Recipe.objects.get(id=1)
    max_length = recipe._meta.get_field('type').max_length
    self.assertEqual(max_length, 50)

class RecipeSearchFormTest(TestCase):
  
  def test_form_valid_name(self):
    form = RecipeSearchForm()
    self.assertIn('name', form.as_p())

  def test_form_render_select_chart_type(self):
    form = RecipeSearchForm()
    self.assertIn('chart_type', form.as_p())

  def test_form_valid_data(self):
    form = RecipeSearchForm(
      data={
        'name': 's',
        'chart_type': '#2'})
    self.assertTrue(form.is_valid())

  def test_form_invalid_data(self):
    form = RecipeSearchForm(
      data={
        'cooking_time':'',
        'chart_type': ''})
    self.assertFalse(form.is_valid())
    