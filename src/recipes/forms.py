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

# class CreateRecipeForm(ModelForm):
#   class Meta:
#     model = Recipe
#     fields = ('name','ingredients','cooking_time','type','instructions','pic')

class CreateRecipeForm(forms.Form):
	name = forms.CharField(max_length=120)
	ingredients = forms.CharField(max_length=300, help_text="You must use a comma to separate the ingredients.")
	cooking_time = forms.IntegerField(help_text="In minutes")
	type = forms.ChoiceField(choices=TYPE_CHOICES)
	instructions = forms.CharField(max_length=600)
	pic = forms.ImageField()


class EditRecipeForm(forms.Form):
	name = forms.CharField(max_length=120)
	ingredients = forms.CharField(max_length=300, help_text="You must use a comma to separate the ingredients.")
	cooking_time = forms.IntegerField(help_text="In minutes")
	type = forms.ChoiceField(choices=TYPE_CHOICES)
	instructions = forms.CharField(max_length=600)
	pic = forms.ImageField()


# class EditRecipeForm(forms.ModelForm):
#   class Meta:
#     model = Recipe
#     fields = [
# 						'name',
# 						'ingredients',
# 						'cooking_time',
# 						'type',
# 						'instructions',
# 						'pic',
# 							]
