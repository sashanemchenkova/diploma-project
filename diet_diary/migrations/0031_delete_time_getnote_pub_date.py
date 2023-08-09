# Generated by Django 4.2.2 on 2023-08-03 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0030_time_remove_profile_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Time',
        ),
        migrations.AddField(
            model_name='getnote',
            name='pub_date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='created at'),
            preserve_default=False,
        ),
    ]
