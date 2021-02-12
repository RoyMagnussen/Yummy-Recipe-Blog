from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('signup/', views.sign_up, name='sign_up'),
    path('signup/payment/', views.payment, name='payment'),
    path('signup/complete/', views.sign_up_complete, name='sign_up_complete'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('reset_password_sent/', views.reset_password_sent, name='reset_password_sent'),
    path('reset_password/<uidb64>/<token>/', views.reset_password_change_password, name='reset_password_send'),
    path('resest_password_confirm/', views.reset_password_confirm, name='reset_password_confirm'),
]