# Generated by Django 5.1.4 on 2024-12-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("preferences", "0010_rename_tags_name_tag_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="preferences",
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="tags",
            field=models.JSONField(blank=True, null=True),
        ),
    ]