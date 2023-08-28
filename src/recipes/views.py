from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe
<<<<<<< Updated upstream
from .forms import RecipeSearchForm
=======
from .forms import RecipeSearchForm, CreateRecipeForm, EditRecipeForm
>>>>>>> Stashed changes
import pandas as pd
from .utils import get_recipename_from_id, get_chart

# Create your views here.
def recipe_home(request):
  return render(request, 'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin, ListView):
  model = Recipe
  template_name = 'recipes/main.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
  model = Recipe
  template_name = 'recipes/detail.html'

@login_required
def searches(request):
	form = RecipeSearchForm(request.POST or None)
	recipes_df=None
	chart = None

	if request.method =='POST':
		name = request.POST.get('name')
		chart_type = request.POST.get('chart_type')

		qs = Recipe.objects.filter(name=name)		
		if qs:
			recipes_df=pd.DataFrame(qs.values())	
			recipes_df['id']=recipes_df['id'].apply(get_recipename_from_id)
			chart=get_chart(chart_type, recipes_df, labels=recipes_df['cooking_time'].values)			
			recipes_df=recipes_df.to_html()

	context={
			'form': form,
			'recipes_df': recipes_df,
			'chart': chart
<<<<<<< Updated upstream
			}

	return render(request, 'recipes/searches.html', context)
=======
			}			

	return render(request, 'recipes/searches.html', context)

@ login_required
def create_view(request):
	form = CreateRecipeForm(request.POST, request.FILES)
	create_recipe_form = form
	name = None
	ingredients = None
	cooking_time = None
	type = None
	instructions = None
	pic = None

	if request.method == 'POST':

		if form.is_valid():
				name = form.cleaned_data.get('name'),
				pic = form.cleaned_data.get('pic')
				recipe = Recipe.objects.create(
						name = request.POST.get('name'),
						ingredients = request.POST.get('ingredients'),
						cooking_time = request.POST.get('cooking_time'),
						type = request.POST.get('type'),
						instructions= request.POST.get('instructions'),
						pic = request.POST.get('pic')
				)
	
				recipe.save()

		else:
				print('Error...sorry something went wrong!!!')

	context = {
			'create_recipe_form': create_recipe_form,
			'name': name,
			'ingredients': ingredients,
			'cooking_time': cooking_time,
			'type': type,
			'instructions': instructions,
			'pic': pic,}

	return render(request, 'recipes/create.html', context)

@ login_required
def edit_view(request):
	form = EditRecipeForm(request.POST, request.FILES)
	edit_recipe_form = form
	name = None
	ingredients = None
	cooking_time = None
	type = None
	instructions = None
	pic = None

	if request.method == 'POST':

		if form.is_valid():
				name = form.cleaned_data.get('name'),
				pic = form.cleaned_data.get('pic')
				recipe = Recipe.objects.all(
						name = request.POST.get('name'),
						ingredients = request.POST.get('ingredients'),
						cooking_time = request.POST.get('cooking_time'),
						type = request.POST.get('type'),
						instructions= request.POST.get('instructions'),
						pic = request.POST.get('pic')
				)
	
				recipe.save()

		else:
				print('Error...sorry something went wrong!!!')

	context = {
			'edit_recipe_form': edit_recipe_form,
			'name': name,
			'ingredients': ingredients,
			'cooking_time': cooking_time,
			'type': type,
			'instructions': instructions,
			'pic': pic,
	}

	return render(request, 'recipes/edit_recipe.html', context)

>>>>>>> Stashed changes
