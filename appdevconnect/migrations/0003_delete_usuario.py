# Generated by Django 4.2.7 on 2023-11-06 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdevconnect', '0002_alter_pregunta_question_date_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]