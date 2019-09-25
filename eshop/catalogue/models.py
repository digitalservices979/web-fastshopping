from django.db import models
from slugify import slugify

# Create your models here.

class Category(models.Model):
	name_category = models.CharField(max_length=100,verbose_name='Categoría')
	slug_category = models.SlugField()
	class Meta:
		verbose_name = 'Categoría'
		verbose_name_plural = 'Categorías'
	def __str__(self):
		return self.name_category

class Brand(models.Model):
	name_brand = models.CharField(max_length=100,verbose_name='Marca')
	slug_brand = models.SlugField()
	class Meta:
		verbose_name = 'Marca'
		verbose_name_plural = 'Marcas'
	def __str__(self):
		return self.name_brand

class Color(models.Model):
	name_color = models.CharField(max_length=100,verbose_name='Color')
	slug_color = models.SlugField()
	class Meta:
		verbose_name = 'Color'
		verbose_name_plural = 'Colores'
	def __str__(self):
		return self.name_color


class Product(models.Model):
	name_product = models.CharField(max_length=100,verbose_name='Producto')
	image_product1 = models.ImageField(upload_to='products',verbose_name='Imagen Principal')
	image_product2 = models.ImageField(upload_to='products',verbose_name='Primera Imagen')
	image_product3 = models.ImageField(upload_to='products',verbose_name='Segunda Imagen')
	image_product4= models.ImageField(upload_to='products',verbose_name='Tercera Imagen')
	description_product = models.TextField(blank=True, verbose_name='Descripción')
	price = models.DecimalField(max_digits=5,decimal_places=2,verbose_name='Precio')
	stock = models.IntegerField(verbose_name='Cantidad en el inventario')
	slug_product = models.SlugField()
	category_product = models.ForeignKey(Category, on_delete = models.CASCADE,verbose_name='Categoría')
	brand_product = models.ForeignKey(Brand, on_delete = models.CASCADE,verbose_name='Marca')
	color_product = models.ManyToManyField(Color,verbose_name='Colores disponibles')
	product_created = models.DateTimeField(auto_now = True, verbose_name='Fecha de creación')
	product_updated = models.DateTimeField(auto_now_add = True, verbose_name='Fecha de actualización')
	class Meta:
		verbose_name = 'Producto'
		verbose_name_plural = 'Productos'
	def __str__(self):
		return self.name_product
	def save(self,*args,**kwargs):
		self.slug_product = slugify(self.name_product)
		super(Product,self).save(*args,**kwargs)