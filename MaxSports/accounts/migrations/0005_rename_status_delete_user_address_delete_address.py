# Generated by Django 5.0.4 on 2024-05-04 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_user_address_status_delete_alter_image_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user_address",
            old_name="status_delete",
            new_name="delete_address",
        ),
    ]