# Generated by Django 5.1.4 on 2024-12-11 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("preferences", "0008_tag_remove_post_tags_alter_user_preferences_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tag",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelTable(
            name="tag",
            table="tag",
        ),
    ]
