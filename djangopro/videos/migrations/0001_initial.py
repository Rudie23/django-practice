# Generated by Django 4.2.1 on 2023-06-07 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36)),
                ('slug', models.SlugField(max_length=36)),
                ('vimeo_id', models.CharField(max_length=36)),
                ('creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
