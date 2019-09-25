from django.contrib import admin
from .models import Mensajes

# Register your models here.

class MensajesAdmin(admin.ModelAdmin):
	readonly_fields = 'nombre','asunto','correo','mensaje'
admin.site.register(Mensajes, MensajesAdmin)