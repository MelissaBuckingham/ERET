# Generated by Django 5.1.2 on 2024-11-08 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]