# Generated by Django 5.0.6 on 2024-07-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPost', '0002_remove_userpost_title_userpost_post_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_bio',
            field=models.TextField(default=''),
        ),
    ]
