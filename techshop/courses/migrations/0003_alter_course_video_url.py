# Generated by Django 5.1.2 on 2025-03-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
