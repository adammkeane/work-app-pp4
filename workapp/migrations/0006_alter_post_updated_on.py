# Generated by Django 3.2.18 on 2023-03-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0005_auto_20230314_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]