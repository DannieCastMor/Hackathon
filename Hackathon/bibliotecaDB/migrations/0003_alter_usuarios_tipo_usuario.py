# Generated by Django 3.2.8 on 2021-12-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotecaDB', '0002_alter_usuarios_tipo_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='tipo_usuario',
            field=models.BooleanField(),
        ),
    ]
