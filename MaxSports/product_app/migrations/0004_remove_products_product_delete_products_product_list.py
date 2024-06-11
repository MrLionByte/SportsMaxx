# Generated by Django 5.0.4 on 2024-04-20 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0003_remove_products_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="products",
            name="product_delete",
        ),
        migrations.AddField(
            model_name="products",
            name="product_list",
            field=models.BooleanField(default=True),
        ),
    ]
