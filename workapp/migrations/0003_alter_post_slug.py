# Generated by Django 3.2.18 on 2023-03-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0002_auto_20230309_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=105, unique=True),
        ),
    ]
