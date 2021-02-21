"""yummy_recipe_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from blog import views as blog_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('home/', include('blog.urls')),
    path('profile/', blog_views.profile_page, name='profile_page'),
    path('profile/edit/', account_views.update_user_page, name='update_user'),
    path('profile/my_recipes/', blog_views.personal_recipes, name='personal_recipes'),
    path('profile/liked_recipes/', blog_views.liked_recipes_page, name='liked_recipes'),
    path('profile/liked_recipes/<recipe_id>/remove/', blog_views.remove_liked_recipe, name='remove_liked_recipe'),
    path('recipes/', include('recipes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
