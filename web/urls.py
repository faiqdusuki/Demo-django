from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.login, name="login"),
	#path('cart/', views.cart, name="cart"),


]
