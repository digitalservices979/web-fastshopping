from django.test import TestCase
from carton.cart import Cart
# Create your tests here.

class Carro(TestCase):
	def setUp(self):
		cart = Cart(request.session)
		productos = list(cart.products)

	def prueba(self):
		if len(productos)==0:
			print('Lista vacia')
		else:
			print('Lista no vacia')