from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from recipes.models import LikedRecipe, Recipe
from accounts.models import Account
from django.db.models.functions import Lower

# Create your views here.


@login_required(login_url='/')
def home(request) -> render:
    """
    Renders the home page.

    Args:
        request (HttpRequest): A HttpRequest class object

    Returns:
        render: A HttpResponse whose content is filled by the provided template and context.
    """

    recipes = Recipe.objects.all()
    
    sort = None
    direction = None
    current_sorting = None

    if 'sort' in request.GET:
        sortkey = request.GET['sort']
        sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            recipes = recipes.annotate(lower_name=Lower('name'))
        if sortkey == 'time':
            sortkey = 'total_time'
        if sortkey == 'category':
            sortkey = 'category__name'
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        recipes = recipes.order_by(sortkey)
        
    current_sorting = f'{sort}_{direction}'

    if 'q' in request.GET:
        query = request.GET.get('q')
        recipes = Recipe.objects.all().filter(name=query)
    else:
        recipes = Recipe.objects.all()
    user = Account.objects.get(username=request.user.username)

    context = {
        'title': 'Home',
        'recipes': recipes,
        'user': user,
        'current_sorting': current_sorting,
    }

    return render(request, 'blog/home.html', context)


@login_required(login_url='/')
def profile_page(request) -> render:
    """
    Renders the profile page.

    Args:
        request (HttpRequest): A HttpRequest class object

    Returns:
        render: A HttpResponse whose content is filled by the provided template and context.
    """
    user = Account.objects.get(username=request.user.username)
    context = {
        'title': 'Profile',
        'user': user,
    }

    return render(request, 'blog/profile_page.html', context)


@login_required(login_url='/')
def personal_recipes(request) -> render:
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
def liked_recipes_page(request) -> render:
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


@login_required(login_url='/')
def delete_recipe(request, recipe_id) -> redirect:
    """
    Finds the recipe from the personal recipes where the recipe Id matches the provided Id.

    Args:
        request (HttpRequest): A HttpRequest class object.
        recipe_id (int): The Id fo the recipe that needs to be removed.

    Returns:
        redirect: Redirects the user to the provided url name.
    """
    user = Account.objects.get(username=request.user.username)
    Recipe.objects.get(id=recipe_id, author=user).delete()
    messages.success(request, 'The recipe has successfully been removed.')
    return redirect('personal_recipes')


@login_required(login_url='/')
def user_profile(request, username) -> render:
    """
    Renders the user page.

    Args:
        request (HttpRequest): A HttpRequest class object.
        user_id (string): The username of the target user.

    Returns:
        render: A HttpResponse whose content is filled by the provided template and content.
    """
    target_user = Account.objects.get(username=username)
    user = Account.objects.get(username=request.user.username)
    recipes = Recipe.objects.all().filter(author=target_user)
    context = {
        'title': f"{target_user.username}'s Profile",
        'user': user,
        'target_user': target_user,
        'recipes': recipes,
    }

    return render(request, 'blog/user_page.html', context)
