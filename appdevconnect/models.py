from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    birth_date = models.DateField()
    institution = models.CharField(max_length=60)

class Pregunta(models.Model):
    question_title = models.CharField(max_length=50)
    question_topic = models.CharField(max_length=30)
    question_language = models.CharField(max_length=20)
    question_body = models.TextField()
    question_date = models.DateField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Respuesta(models.Model):
    answer_body = models.TextField()
    answer_date = models.DateField()
    question = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Proyecto(models.Model):
    project_title = models.CharField(max_length=50)
    project_language = models.CharField(max_length=20)
    project_topic = models.CharField(max_length=30)
    project_description = models.TextField()
    project_upload_date = models.DateField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    archivo_content = models.BinaryField()
