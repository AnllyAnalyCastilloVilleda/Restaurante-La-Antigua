# Generated by Django 5.0.4 on 2024-05-05 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='tipo',
            field=models.CharField(choices=[(1, 'Comida'), (2, 'Bebida'), (3, 'Postre')], max_length=10),
        ),
    ]
