# Generated by Django 5.1.7 on 2025-03-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividimos_app', '0002_evento_invitado_aporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='pais',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
