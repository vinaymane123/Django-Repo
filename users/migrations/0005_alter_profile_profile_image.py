# Generated by Django 3.2.7 on 2021-10-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_social_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='user-default.png', null=True, upload_to='static/images/profiles/'),
        ),
    ]
