from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from .models import Mensajes
from catalogue.models import Product

# Create your views here.

@csrf_exempt
def homePageView(request):
	if request.method == 'POST':
		cart_2 = request.POST.get('custom')
		num = ""
		for a in cart_2:
			if a != ',':
				num = num + str(a)
			else:
				prod = Product.objects.get(pk=num)
				print(prod)
				print(num)
				num = ""
		"""
		productos = request.POST.get('custom')
		b = 0
		for var in productos:
			if var != '[':
				if var != ',':
					if var !=' ':
						if var !=']':
							print(productos)
							print(var)							
							prod = Product.objects.get(pk=var)
							if b < 1:
								cant = 0
								c_list = []
								for item in cart.items:
									cant = item.quantity
									print(cant)
									c_list.append(cant)
							c_list.reverse()
							n_stock = prod.stock - c_list.pop()
							Product.objects.filter(pk=var).update(stock=n_stock)
							b = b + 1
		cart.clear()"""
	return render(request,'core/index.html')


class ContactView(TemplateView):
	template_name = 'core/contact.html'

@csrf_exempt
def questions(request):
	ms = Mensajes()
	ms.nombre = request.POST.get('nombre')
	ms.mensaje = request.POST.get('mensaje')
	ms.asunto = request.POST.get('asunto')
	ms.correo = request.POST.get('correo')

	ms.save()
	return render_to_response('core/contact.html')
