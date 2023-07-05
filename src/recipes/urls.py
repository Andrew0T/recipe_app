from django.urls import path
from .views import recipe_home, RecipeListView, RecipeDetailView, searches

app_name = 'recipes'

urlpatterns = [
  path('', recipe_home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
  path('searches', searches, name='searches'),
]
