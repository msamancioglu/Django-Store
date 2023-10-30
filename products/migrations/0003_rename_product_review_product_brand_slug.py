# Generated by Django 4.2.5 on 2023-10-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_product_slug_product_tags_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='Product',
            new_name='product',
        ),
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]