from django.urls import path
from django.contrib.auth.views import auth_logout, logout_then_login, LoginView
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', auth_logout , name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),

]
