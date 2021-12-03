# Generated by Django 3.2.8 on 2021-12-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='libros',
            fields=[
                ('codigo_ISBN', models.CharField(max_length=40, primary_key='codigo_ISBN', serialize=False)),
                ('nombre_libro', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('login', models.CharField(max_length=40, primary_key='login', serialize=False)),
                ('contrasena', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('tipo_usuario', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('codigo_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecaDB.libros')),
                ('login_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotecaDB.usuarios')),
            ],
        ),
    ]
