from django.urls import path
from .views import ProductListView, ProductDetailView, CartTemplateView, add_cart, remove_total_cart, update, CheckoutTemplateView
urlpatterns = [
	path('lista-de-ropa/', ProductListView.as_view(), name='product_list'),
	path('<slug:slug_product>/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
	path('productos/', CartTemplateView.as_view(), name='product_cart'),
	path('agregar/', add_cart, name='agregar'),
	path('eliminar/', remove_total_cart,name='eliminar'),
	path('actualizar/', update, name='actualizar'),
	path('checkout/', CheckoutTemplateView.as_view(), name='checkout'),
]