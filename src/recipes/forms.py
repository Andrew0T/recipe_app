from django import forms	#import django forms
from django.forms import ModelForm
from .models import Recipe, TYPE_CHOICES

CHART__CHOICES = (			#specify choices as a tuple
	('#1', 'Bar chart'),	# when user selects "Bar chart", it is stored as "#1"
	('#2', 'Pie chart'),
	('#3', 'Line chart')
	)

#define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):	
	name= forms.CharField(max_length=120)
	chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class CreateRecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields = ('name','ingredients','cooking_time','type','instructions','pic')


class EditRecipeForm(ModelForm):
  class Meta:
    model = Recipe
    fields = ('name','ingredients','cooking_time','type','instructions','pic')

