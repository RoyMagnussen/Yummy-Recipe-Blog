from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe

# Create your views here.


@login_required(login_url='/')
def home(request):
    recipes = Recipe.objects.all()

    context = {
        'title': 'Home',
        'recipes': recipes,
    }

    return render(request, 'blog/home.html', context)
