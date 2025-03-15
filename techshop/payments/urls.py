from django.urls import path
from .views import create_order, verify_payment

urlpatterns = [
    path('create_order/<int:course_id>/', create_order, name='create_order'),
    path('verify_payment/', verify_payment, name='verify_payment'),
]
