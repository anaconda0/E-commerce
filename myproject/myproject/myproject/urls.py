"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myapp.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'specifications', SpecificationViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/<int:user_id>/addresses/', UserAddressesView.as_view(), name='user-addresses'),
    path('users/<int:user_id>/orders/', UserOrdersView.as_view(), name='user-orders'),
    path('product/<int:product_id>/users/', UsersByProductView.as_view(), name='user-by-product'),
    path('users/<int:user_id>/cart/', UserCartView.as_view(), name='user-cart'),
    path('order/<int:order_id>/address/', OrderAddressView.as_view(), name='order-address'),
    path('address/<int:address_id>/orders/', OrdersInAddressView.as_view(), name='orders-in-address'),

]
