# Generated by Django 4.2.4 on 2023-08-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_seller_delete_supplierrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='products',
            field=models.ManyToManyField(to='sale.product', verbose_name='продукты'),
        ),
    ]