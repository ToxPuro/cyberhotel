from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
    path('receipt/<int:receipt_id>/', views.receipt, name='receipt'),
    path('hotel/<int:hotel_id>/', views.hotel, name='hotel')
    
    
]