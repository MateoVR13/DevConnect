from django.db import models

class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=25)
    name1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20, null=True, blank=True)
    last_name1 = models.CharField(max_length=20)
    last_name2 = models.CharField(max_length=20, null=True, blank=True)
    birth_date = models.DateField()
    institution = models.CharField(max_length=60)

    def __str__(self):
        return self.username

class Pregunta(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_title = models.CharField(max_length=50)
    question_topic = models.CharField(max_length=30)
    question_language = models.CharField(max_length=20)
    question_body = models.TextField()
    question_date = models.DateField()
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    file_content = models.BinaryField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_title

class Respuesta(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer_body = models.TextField()
    answer_date = models.DateField()
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    file_content = models.BinaryField()
    question = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"Respuesta {self.answer_id}"

class Proyecto(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=50)
    project_language = models.CharField(max_length=20)
    project_topic = models.CharField(max_length=30)
    project_description = models.TextField()
    project_upload_date = models.DateField()
    file_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    file_content = models.BinaryField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title

class Archivo(models.Model):
    archivo_id = models.AutoField(primary_key=True)
    archivo_name = models.CharField(max_length=255)
    archivo_type = models.CharField(max_length=50)
    archivo_content = models.BinaryField()
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, null=True)
    respuesta = models.ForeignKey(Respuesta, on_delete=models.CASCADE, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.archivo_name
