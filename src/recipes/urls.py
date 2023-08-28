from django.urls import path
<<<<<<< Updated upstream
from .views import recipe_home, RecipeListView, RecipeDetailView, searches
=======
from .views import recipe_home, RecipeListView, RecipeDetailView, search_view, create_view, edit_view
>>>>>>> Stashed changes

app_name = 'recipes'

urlpatterns = [
  path('', recipe_home, name='home'),
  path('list/', RecipeListView.as_view(), name='list'),
  path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
<<<<<<< Updated upstream
  path('searches', searches, name='searches'),
=======
  path('searches', search_view, name='searches'),
  path('create', create_view, name='create'),
  path('edit_recipe', edit_view, name='edit_recipe'),

>>>>>>> Stashed changes
]
