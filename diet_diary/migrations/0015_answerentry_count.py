# Generated by Django 4.2.2 on 2023-07-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0014_remove_answerentry_weight_of_the_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='answerentry',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
