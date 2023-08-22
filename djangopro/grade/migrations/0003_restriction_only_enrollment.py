# Generated by Django 4.2.2 on 2023-06-26 21:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('grade', '0002_creation_enrollment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment',
            options={'ordering': ['grade', 'date']},
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('user', 'grade')},
        ),
    ]