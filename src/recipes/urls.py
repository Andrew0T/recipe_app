from django.urls import path
from .views import recipe_home
from .views import RecipeListView
from .views import RecipeDetailView

app_name = 'recipes'

urlpatterns = [
  path('', recipe_home),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]
