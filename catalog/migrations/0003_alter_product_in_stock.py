# Generated by Django 5.0.8 on 2024-09-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_product_in_stock_alter_product_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="in_stock",
            field=models.BooleanField(default=True, verbose_name="в наличии"),
        ),
    ]
