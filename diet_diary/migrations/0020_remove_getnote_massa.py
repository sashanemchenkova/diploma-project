# Generated by Django 4.2.2 on 2023-07-31 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0019_alter_getnote_massa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getnote',
            name='massa',
        ),
    ]
