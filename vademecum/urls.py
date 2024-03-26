from django.urls import path
from .views import index, register

urlpatterns = [
    path('register/', register, name='register'),
    path('', index)
]