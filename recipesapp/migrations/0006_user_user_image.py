# Generated by Django 5.1.2 on 2024-11-05 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0005_recipe_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(null=True, upload_to='img/users/'),
        ),
    ]