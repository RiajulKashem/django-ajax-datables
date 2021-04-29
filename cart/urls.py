from django.urls import path

from cart.views import Home, OrderListAPIView

app_name = 'cart'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('order-list/', OrderListAPIView.as_view(), name='order_list'),
]
