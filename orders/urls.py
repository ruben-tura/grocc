from django.urls import path
from .views import orders, order

urlpatterns = [
    path('<int:id>/', order),
    path('', orders)
]