# Generated by Django 4.2.2 on 2023-07-11 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0009_goals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goals',
            new_name='Goal',
        ),
    ]
