# Generated by Django 4.2.2 on 2023-06-15 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0006_lesson_vimeo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='vimeo_id',
            field=models.CharField(max_length=36),
        ),
    ]
