# Generated by Django 5.0.2 on 2024-09-17 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='article_image',
        ),
    ]
