# Generated by Django 4.1 on 2023-05-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="design",
            name="info",
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
