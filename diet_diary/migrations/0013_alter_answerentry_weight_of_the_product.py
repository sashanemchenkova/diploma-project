# Generated by Django 4.2.2 on 2023-07-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0012_alter_answerentry_weight_of_the_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerentry',
            name='weight_of_the_product',
            field=models.IntegerField(default=0),
        ),
    ]