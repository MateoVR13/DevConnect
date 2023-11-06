from django.contrib import admin
from django.contrib.auth.models import User
from .models import Pregunta, Respuesta, Proyecto

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(Pregunta)
class PreguntasAdmin(admin.ModelAdmin):
    list_display = ['question_title', 'question_topic', 'question_language', 'question_date', 'user']
    list_filter = ['question_language', 'question_topic']
    search_fields = ['question_title']

@admin.register(Respuesta)
class RespuestasAdmin(admin.ModelAdmin):
    list_display = ['answer_date', 'question', 'user']

@admin.register(Proyecto)
class ProyectosAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'project_language', 'project_topic', 'project_upload_date', 'user']
    list_filter = ['project_language', 'project_topic']
    search_fields = ['project_title']
