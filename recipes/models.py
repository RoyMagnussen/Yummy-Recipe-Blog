from django.db.models import Model
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField, IntegerField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Category(Model):
    """
    Category Model to be used with Recipe Model.

    Args:
        Model (class): Base Model Class provided by Django. Can be found here: `django.db.models`
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = CharField(max_length=20, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Recipe(Model):
    """
    Recipe Model for creating recipes.

    Args:
        Model (class): Base Model Class provided by Django. Can be found here: `django.db.models`
    """
    name = CharField(max_length=100, null=False, blank=False)
    image = ImageField()
    ingredients = TextField(null=False, blank=False)
    steps = TextField(null=False, blank=False)
    category = ForeignKey(Category, on_delete=CASCADE)
    servings = IntegerField(null=False, blank=False)
    prep_time = IntegerField(null=False, blank=False)
    cook_time = IntegerField(null=False, blank=False)
    likes = IntegerField(default=0)
    author = ForeignKey(User, on_delete=CASCADE)
    date_created = DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name
