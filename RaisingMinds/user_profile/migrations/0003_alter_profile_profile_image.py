# Generated by Django 4.2.4 on 2023-11-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_profile_forget_password_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='profile_images/defalt_profile_image.jpg', upload_to='profile_images'),
        ),
    ]