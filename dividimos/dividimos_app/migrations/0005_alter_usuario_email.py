# Generated by Django 5.1.7 on 2025-04-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividimos_app', '0004_aporte_precio_mercaderia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
