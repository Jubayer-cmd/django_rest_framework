from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("products/", views.product_list, name="products"),
    path("product/<int:pk>/", views.product, name="product"),
    path("register/", views.register, name="register"),
    path("login/", obtain_auth_token, name="login"),
]
