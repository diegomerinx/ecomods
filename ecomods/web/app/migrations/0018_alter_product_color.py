# Generated by Django 5.1.1 on 2024-11-18 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(default='blue', max_length=255),
        ),
    ]
