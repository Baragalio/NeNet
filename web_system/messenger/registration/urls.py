"""
from django.urls import path
from .views import Registration
urlpatterns = [
    path('registration/', Registration.as_view, name="registration"),
]
"""