from django.db import models
from django.conf import settings

# Create your models here.
class Blog(models.Model):
	imagen = models.ImageField(upload_to='products', verbose_name='Imagen')
	titulo = models.CharField(max_length=100, verbose_name='Título')
	descripcion = models.TextField(verbose_name='Descripcion')
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
	fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de creación')
	class Meta:
		verbose_name='Blog'
		verbose_name_plural ='Blogs'
	def __str__(self):
		return self.titulo