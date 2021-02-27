from recipes.forms import RecipeCreationForm
from django.test import TestCase

# Create your tests here.


class TestRecipeCreationForm(TestCase):
    def test_recipe_prep_time_is_required(self):
        form = RecipeCreationForm({'total_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_recipe_servings_is_required(self):
        form = RecipeCreationForm({'servings': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('servings', form.errors.keys())
        self.assertEqual(form.errors['servings'][0], 'This field is required.')

    def test_recipe_prep_time_is_required(self):
        form = RecipeCreationForm({'prep_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('prep_time', form.errors.keys())
        self.assertEqual(form.errors['prep_time']
                         [0], 'This field is required.')

    def test_recipe_cook_time_is_required(self):
        form = RecipeCreationForm({'cook_time': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('cook_time', form.errors.keys())
        self.assertEqual(form.errors['cook_time']
                         [0], 'This field is required.')

    def test_recipe_categories_is_required(self):
        form = RecipeCreationForm({'categories': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('categories', form.errors.keys())
        self.assertEqual(form.errors['categories']
                         [0], 'This field is required.')

    def test_recipe_ingredients_are_required(self):
        form = RecipeCreationForm({'ingredients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(form.errors['ingredients']
                         [0], 'This field is required.')

    def test_recipe_steps_are_required(self):
        form = RecipeCreationForm({'steps': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('steps', form.errors.keys())
        self.assertEqual(form.errors['steps'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_meta_class(self):
        form = RecipeCreationForm()
        self.assertEqual(form.Meta.fields, [
                         'name', 'image', 'ingredients', 'steps', 'categories', 'servings', 'prep_time', 'cook_time'])
