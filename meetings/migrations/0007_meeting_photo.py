# Generated by Django 2.2.6 on 2019-12-18 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0006_auto_20191201_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
