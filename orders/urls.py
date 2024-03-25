from django.urls import path
from .views import orders, order, delete_object_function

urlpatterns = [
    path('<int:id>/', order),
    path('delete/<int:orderID>/<int:id>', delete_object_function, name='delete_object'),
    path('', orders)
]