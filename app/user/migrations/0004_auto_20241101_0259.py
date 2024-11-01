# Generated by Django 4.0.10 on 2024-11-01 02:59

from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_initial_user(apps, schema_editor):

    User = apps.get_model('user', 'User')

    initial_user_data = {
        'email': 'admin@gmail.com',
        'password': make_password('admin'),
        'nombre': 'Admin',
        'primer_apellido': 'Example',
        'segundo_apellido': 'User',
        'is_active': True,
        'is_superuser': True,
    }

    User.objects.create(**initial_user_data)


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_id'),
    ]

    operations = [
        migrations.RunPython(create_initial_user),
    ]
