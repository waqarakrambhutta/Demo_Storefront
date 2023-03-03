from django.urls import path
from .views import say_hello

urlpatterns = [
    path('sections/',say_hello)
]