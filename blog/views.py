from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from recipes.models import LikedRecipe, Recipe
from accounts.models import Account

# Create your views here.


@login_required(login_url='/')
def home(request):
    recipes = Recipe.objects.all()
    user = Account.objects.get(username=request.user.username)

    context = {
        'title': 'Home',
        'recipes': recipes,
        'user': user,
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


@login_required(login_url='/')
def personal_recipes(request) ->render:
    """
    Renders the personal recipes page.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse whose content is filled by the provided template and context.
    """
    user = Account.objects.get(username=request.user.username)
    recipes = Recipe.objects.all().filter(author=user)
    context = {
        'title': 'My Recipes',
        'user': user,
        'recipes': recipes
    }
    
    return render(request, 'blog/personal_recipes.html', context)

@login_required(login_url='/')
def liked_recipes_page(request) ->render:
    """
    Renders the liked recipes page.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse whose content is filled by the provided template and context.
    """
    user = Account.objects.get(username=request.user.username)
    recipes = LikedRecipe.objects.all().filter(liked_by=user)
    context = {
        'title': 'Liked Recipes',
        'user': user,
        'recipes': recipes,
    }
    
    return render(request, 'blog/liked_recipes.html', context)


@login_required(login_url='/')
def remove_liked_recipe(request, recipe_id) -> redirect:
    """
    Finds the recipe from the liked recipes table where the recipe Id matches the provided Id and the `liked_by` field matches the currently logged in user.

    Args:
        request (HttpRequest): A HttpRequest class object. 
        recipe_id (int): The Id of the recipe that needs to be removed.

    Returns:
        redirect: Redirects the user to the provided url name.
    """
    user = Account.objects.get(username=request.user.username)
    recipe = Recipe.objects.get(id=recipe_id)
    LikedRecipe.objects.get(recipe=recipe, liked_by=user).delete()
    messages.success(request, 'The recipe has successfully been removed.')
    return redirect('liked_recipes')