# Generated by Django 5.1.4 on 2024-12-09 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("preferences", "0002_user_interaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interaction",
            name="interaction_time",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="interaction",
            name="interaction_type",
            field=models.CharField(max_length=50),
        ),
    ]
