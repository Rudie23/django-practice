# Generated by Django 4.2.1 on 2023-06-11 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
