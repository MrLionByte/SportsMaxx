# Generated by Django 5.0.4 on 2024-04-24 12:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product_app", "0007_product_color_image_product_variant_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product_sizes_variants",
            name="product_quantity",
            field=models.PositiveIntegerField(
                default=0, validators=[django.core.validators.MaxValueValidator(10000)]
            ),
        ),
    ]
