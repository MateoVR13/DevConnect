# Generated by Django 4.2.6 on 2023-11-09 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdevconnect', '0005_alter_proyecto_archivo_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='project_upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
