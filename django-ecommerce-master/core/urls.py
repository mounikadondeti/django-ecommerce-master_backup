from django.contrib.auth import admin
from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    AdminLoginView
)
from .import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.SearchPage, name='search_result'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),

    path('login/', AdminLoginView.as_view(), name='login'),
    path('adminurl/', views.siteurl, name='url'),
    path('chart/', views.charts, name='chart'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user/', views.user, name='user'),
    path('product/', views.AdminProduct, name='product'),
    path('AdminOrder/', views.AdminOrder, name='AdminOrder'),
    path('update_product/<str:pk>', views.updateProduct, name="update_product"),
    path('delete_product/<str:pk>', views.deleteproduct, name="delete_product"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
