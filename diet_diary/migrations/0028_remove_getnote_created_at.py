# Generated by Django 4.2.2 on 2023-08-02 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0027_delete_timestampmixin_getnote_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='getnote',
            name='created_at',
        ),
    ]
