# Generated by Django 4.2.7 on 2023-11-21 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_collection_options_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
