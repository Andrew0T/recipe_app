from django.urls import path
from .views import recipe_home, RecipeListView, RecipeDetailView, search_view, create_view

app_name = 'recipes'

urlpatterns = [
  path('', recipe_home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('searches', search_view, name='searches'),
  path('create', create_view, name='create'),

]
