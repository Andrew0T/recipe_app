from django.urls import path
from .views import recipe_home, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
  path('', recipe_home),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]
