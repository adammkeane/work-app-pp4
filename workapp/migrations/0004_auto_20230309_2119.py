# Generated by Django 3.2.18 on 2023-03-09 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=55, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
