# Generated by Django 4.2.2 on 2023-07-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet_diary', '0005_gender_delete_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
    ]