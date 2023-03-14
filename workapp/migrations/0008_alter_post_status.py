# Generated by Django 3.2.18 on 2023-03-14 19:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0007_auto_20230314_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
