# Generated by Django 4.2.4 on 2023-08-30 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0004_alter_seller_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='products',
            field=models.ManyToManyField(blank=True, to='sale.product', verbose_name='продукты'),
        ),
    ]