# Generated by Django 5.0.6 on 2024-07-07 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPost', '0003_userprofile_user_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='post_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
