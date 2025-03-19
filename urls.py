from django.urls import path
from .views import product_form

urlpatterns = [
    path("", product_form, name="product_form"),
]
