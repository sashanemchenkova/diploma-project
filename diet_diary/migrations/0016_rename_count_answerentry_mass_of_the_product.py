# Generated by Django 4.2.2 on 2023-07-15 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0015_answerentry_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answerentry',
            old_name='count',
            new_name='mass_of_the_product',
        ),
    ]