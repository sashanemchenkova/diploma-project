# Generated by Django 4.2.2 on 2023-07-10 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0007_product_massa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='massa',
        ),
    ]