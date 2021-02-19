from django.forms.models import ModelForm
from django.forms.fields import CharField, IntegerField, FileField
from .models import Recipe


class RecipeCreationForm(ModelForm):
    """
    A form for creating recipes.

    Args:
        ModelForm (class): The standard form class provide by Django. Can be found here: `django.forms.models`
    """
    
    name = CharField(required=True, label='Recipe name')
    servings = IntegerField(required=True, label='Servings')
    prep_time = IntegerField(required=True, label='Prep Time (Minutes)')
    cook_time = IntegerField(required=True, label='Cook Time (Minutes)')
    categories = CharField(required=True, label='Categories (Separate with comma)')
    image = FileField(required=False, label='Image')
    

    class Meta:
        model = Recipe
        fields = ('name', 'image', 'ingredients', 'steps',
                  'categories', 'servings', 'prep_time', 'cook_time',)

    def __init__(self, *args, **kwargs):
        super(RecipeCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control form-control-lg border-0'

    def save(self):
        return super(RecipeCreationForm, self).save()
