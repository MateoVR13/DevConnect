from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    question_title = models.CharField(max_length=50)
    question_topic = models.CharField(max_length=30)
    question_language = models.CharField(max_length=20)
    question_body = models.TextField()
    question_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Respuesta(models.Model):
    answer_body = models.TextField()
    answer_date = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Proyecto(models.Model):
    preview_image = models.URLField(blank=True)
    project_title = models.CharField(max_length=50)
    project_language = models.CharField(max_length=20)
    project_topic = models.CharField(max_length=30)
    project_description = models.TextField()
    project_upload_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    archivo_content = models.URLField(blank=True)
    
