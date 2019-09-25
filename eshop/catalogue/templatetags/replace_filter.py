from django import template

register = template.Library()

def replace(valor):
	return str(valor).replace(',','.')

def nuevo_precio(cantidad, precio):
	return cantidad*precio

def checkout(cantidad, envio):
	return cantidad + envio

register.filter('replace',replace)
register.filter('precio', nuevo_precio)
register.filter('checkout',checkout)