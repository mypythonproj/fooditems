# Generated by Django 2.2 on 2023-02-06 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categ',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
