# Generated by Django 2.2 on 2022-10-15 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="report",
            name="comment",
            field=models.CharField(default="", max_length=100),
        ),
    ]