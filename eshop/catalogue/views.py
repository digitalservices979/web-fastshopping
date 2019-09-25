from django.shortcuts import render
from django.shortcuts import get_object_or_404
import json
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from carton.cart import Cart
from .models import Product, Category, Brand, Color
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class ProductListView(ListView):
	model = Product
	template_name = 'catalogue/category.html'
	paginate_by = 12
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['categoria'] = Category.objects.all()
		context['marca'] = Brand.objects.all()
		context['color'] = Color.objects.all()
		return context

	def get_queryset(self):
		#Rehacer el if >:v
		try:
			self.categoria = Category.objects.get(name_category=self.request.GET.get('categoria'))
		except Exception as e:
			self.categoria = False
		try:
			self.marca =  Brand.objects.get(name_brand=self.request.GET.get('marca'))
		except Exception as e:
			self.marca = False
		try:
			self.color =  Color.objects.get(name_color=self.request.GET.get('color'))
		except Exception as e:
			self.color = False

		if self.categoria:
			if self.marca:
				if self.color:
					if Product.objects.filter(category_product=self.categoria,brand_product = self.marca, color_product = self.color).count() < 6:
						return Product.objects.filter(category_product=self.categoria)
					else:	
						return Product.objects.filter(category_product=self.categoria,brand_product = self.marca, color_product = self.color)
				else:
					return Product.objects.filter(category_product=self.categoria,brand_product = self.marca)
			elif self.color:
					return Product.objects.filter(category_product=self.categoria, color_product = self.color)					
			else:
				return Product.objects.filter(category_product=self.categoria)		
		elif self.marca:
			if self.color:
				return Product.objects.filter(brand_product = self.marca, color_product = self.color)
			else:
				return Product.objects.filter(brand_product = self.marca)
		elif self.color:
			return Product.objects.filter(color_product = self.color)
		else:
			return Product.objects.all()

class ProductDetailView(DetailView):
	model = Product
	template_name = 'catalogue/single-product.html'

class CartTemplateView(TemplateView):
	template_name = 'catalogue/cart.html'
	def get(self,request,*args,**kwargs):
		cart = Cart(request.session)
		context = {'cart':cart.items,'total':cart.total}
		return render(request,self.template_name, context)

@csrf_exempt
def add_cart(request):
	if request.is_ajax():
		if request.method == 'POST':
			cart = Cart(request.session)
			producto = Product.objects.get(id=request.POST.get('id'))
			cart.add(producto,price=producto.price)
			return HttpResponse('Agregado')

@csrf_exempt
def remove_total_cart(request):
	if request.is_ajax():
		if request.method == 'POST':
			cart = Cart(request.session)
			producto = Product.objects.get(id=request.POST.get('id'))
			cart.remove(producto)
			return HttpResponse('Eliminado')

@csrf_exempt
def update(request):
	if request.is_ajax():
		if request.method == 'POST':
			cart = Cart(request.session)
			producto = Product.objects.get(id=request.POST.get('id'))
			new_cantidad = request.POST.get('valor')
			cart.set_quantity(producto,quantity=new_cantidad)
			return HttpResponse('Actualizado')

class CheckoutTemplateView(TemplateView):
	template_name = 'catalogue/checkout.html'
	def get(self,request,*args,**kwargs):
		context = super().get_context_data(**kwargs)
		cart = Cart(request.session)
		lista_enviada = []
		enviar = ""
		for a in range(len(cart.products)):
			enviar = enviar + str(cart.products[a].id) + ","

		paypal_dict = {
			"business" : 'qwer_jv16@outlook.com',
			"amount" : cart.total,
			"item_name": "Pago total",
			"return" : request.build_absolute_uri(reverse('home')),
			"cancel_return" : request.build_absolute_uri(reverse('product_list')),
			"custom": enviar,
			"rm":2,
		}
		print(enviar)
		form = PayPalPaymentsForm(initial=paypal_dict)
		context = {'producto':cart.items, 'total': cart.total, 'form':form}
		return render(request,self.template_name, context) 