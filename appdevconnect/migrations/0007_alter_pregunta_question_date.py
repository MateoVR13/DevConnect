# Generated by Django 4.2.7 on 2023-11-09 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdevconnect', '0006_alter_proyecto_project_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='question_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]