# Generated by Django 2.2.6 on 2019-12-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0008_auto_20191218_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='photo_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
