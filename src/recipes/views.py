from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeSearchForm
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
			}

	return render(request, 'recipes/searches.html', context)