from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import Recipe, Category
from .forms import RecipeCreationForm
from accounts.models import Account

# Create your views here.


@login_required(login_url='/')
def create_recipe(request) -> render:
    """
    Creates the create recipe view.

    Args:
        request (HttpRequest): A HttpRequest class object.

    Returns:
        render: A HttpResponse whose content is filled by the provided template and context.
    """
    if request.method == 'POST':
        form = RecipeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            servings = form.cleaned_data.get('servings')
            prep_time = form.cleaned_data.get('prep_time')
            cook_time = form.cleaned_data.get('cook_time')
            total_time = prep_time + cook_time
            form_categories = form.cleaned_data['categories'].split(',')
            image = form.cleaned_data.get('image')
            ingredients = form.cleaned_data.get('ingredients')
            steps = form.cleaned_data.get('steps')
            author = Account.objects.get(username=request.user.username)
            for category in form_categories:
                if category not in Category.objects.all():
                    Category.objects.create(name=category)

            categories = Category.objects.filter(name__in=form_categories)

            recipe = Recipe.objects.create(name=name, servings=servings, prep_time=prep_time, cook_time=cook_time,
                                           total_time=total_time, image=image, ingredients=ingredients, steps=steps, author=author)

            recipe.category.set(categories)

            return redirect('home')

    user = Account.objects.get(username=request.user.username)
    form = RecipeCreationForm()
    context = {
        'title': 'Create Recipe',
        'form': form,
        'user': user
    }

    return render(request, 'recipes/create_recipe.html', context)
