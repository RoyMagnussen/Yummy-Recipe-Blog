from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from accounts.models import Account

# Create your views here.


@login_required(login_url='/')
def home(request):
    recipes = Recipe.objects.all()

    context = {
        'title': 'Home',
        'recipes': recipes,
    }

    return render(request, 'blog/home.html', context)


@login_required(login_url='/')
def profile_page(request) -> render:
    user = Account.objects.get(username=request.user.username)
    context = {
        'title': 'Profile',
        'user': user,
    }

    return render(request, 'blog/profile_page.html', context)
