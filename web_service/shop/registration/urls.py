from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    #path('', login_required(views.edit), name="settings")
]

