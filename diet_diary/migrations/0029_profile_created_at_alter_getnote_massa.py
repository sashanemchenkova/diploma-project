# Generated by Django 4.2.2 on 2023-08-03 07:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0028_remove_getnote_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='getnote',
            name='massa',
            field=models.FloatField(default=100.0),
        ),
    ]
