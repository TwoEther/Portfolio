# Generated by Django 4.1.1 on 2022-12-15 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0005_post_proj_end_post_proj_start"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="head_image",
            field=models.ImageField(null=True, upload_to="post/images"),
        ),
    ]
