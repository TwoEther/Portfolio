# Generated by Django 4.1.1 on 2022-12-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_post_proj_stack"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="image4",
            field=models.ImageField(null=True, upload_to="post/images"),
        ),
        migrations.AddField(
            model_name="post",
            name="image5",
            field=models.ImageField(null=True, upload_to="post/images"),
        ),
    ]
