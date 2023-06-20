from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'app/recipes_home.html')