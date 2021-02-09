from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signup/payment/', views.payment, name='payment'),
    path('signup/complete/', views.sign_up_complete, name='sign_up_complete'),
]