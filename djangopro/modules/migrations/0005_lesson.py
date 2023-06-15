# Generated by Django 4.2.2 on 2023-06-15 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_unique_slug_and_not_null'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modules.module')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
