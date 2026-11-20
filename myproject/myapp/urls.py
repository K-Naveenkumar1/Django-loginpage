from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register, name='register'),
    path('products/', views.products, name='products'),
    path('login/', views.login_page, name='login'),

]