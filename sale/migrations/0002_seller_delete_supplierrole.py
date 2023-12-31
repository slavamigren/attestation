# Generated by Django 4.2.4 on 2023-08-29 23:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='название юр лица')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=70, null=True, verbose_name='улица')),
                ('house', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='номер дома')),
                ('type', models.CharField(choices=[('factory', 'factory'), ('retail', 'retail'), ('seller', 'seller')], default='factory', max_length=7, verbose_name='типа продавца')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время создания')),
                ('debt', models.DecimalField(decimal_places=2, default=0, max_digits=11, verbose_name='задолженность')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.seller', verbose_name='поставщик продукции')),
            ],
            options={
                'verbose_name': 'продавец',
                'verbose_name_plural': 'продавцы',
                'ordering': ('title', 'type'),
            },
        ),
        migrations.DeleteModel(
            name='SupplierRole',
        ),
    ]
