# Generated by Django 3.0.7 on 2022-11-18 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_style',
            field=models.CharField(max_length=100),
        ),
    ]
