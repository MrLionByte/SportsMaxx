# Generated by Django 5.0.4 on 2024-05-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_user_address_full_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="file",
        ),
        migrations.AddField(
            model_name="image",
            name="image",
            field=models.ImageField(default="ook", upload_to="images/"),
        ),
    ]
