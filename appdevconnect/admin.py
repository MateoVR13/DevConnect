from django.contrib import admin

from .models import Usuario, Pregunta, Respuesta, Proyecto, Archivo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Pregunta)
admin.site.register(Respuesta)
admin.site.register(Proyecto)
admin.site.register(Archivo)
