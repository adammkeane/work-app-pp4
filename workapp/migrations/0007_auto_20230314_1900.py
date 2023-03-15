# Generated by Django 3.2.18 on 2023-03-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workapp', '0006_alter_post_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='payment_type',
            field=models.IntegerField(choices=[(0, 'Per Hour'), (1, 'Total Payment'), (2, 'Job Dependant')], default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]