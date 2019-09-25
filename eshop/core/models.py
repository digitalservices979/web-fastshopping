from django.db import models

# Create your models here.

class Mensajes(models.Model):
	nombre = models.CharField(max_length=100, verbose_name='Persona')
	asunto = models.CharField(max_length=100, verbose_name='Asunto')
	mensaje = models.TextField(verbose_name='Mensaje')
	correo = models.EmailField(max_length=254, verbose_name='Correo')
	class Meta:
		verbose_name = 'Mensaje'
		verbose_name_plural = 'Mensajes'
	def __str__(self):
		return self.asunto