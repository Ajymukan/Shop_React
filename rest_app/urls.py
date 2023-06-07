from django.urls import path , include
from . import views

urlpatterns = [
    path('productsList/',views.ProductsAPIlist.as_view(), name='productsList'),
    path('brandList/',views.BrandAPIlist.as_view(), name='brandList'),

    path('cartList/',views.CartAPIlist.as_view(), name='cartList'),
    path('cartList/<int:pk>/',views.CartList.as_view(), name='cartList'),

    path('orderList/',views.OrderAPIlist.as_view(), name='orderList'),
    path('orderList/<int:pk>/',views.OrderList.as_view(), name='orderList'),

    path('commentList/',views.CommentAPIlist.as_view(), name='commentList'),
    path('commentList/<int:pk>/',views.CommentList.as_view(), name='commentList'),

]