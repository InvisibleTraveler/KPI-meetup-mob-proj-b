# Generated by Django 2.2.6 on 2019-12-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0009_meeting_photo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='photo_url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
