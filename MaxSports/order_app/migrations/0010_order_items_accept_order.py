# Generated by Django 5.0.4 on 2024-05-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order_app", "0009_order_items_cancel_return_confirm_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order_items",
            name="accept_order",
            field=models.BooleanField(default=False),
        ),
    ]
