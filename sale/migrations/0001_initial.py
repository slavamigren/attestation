# Generated by Django 4.2.4 on 2023-08-29 20:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='продукт')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='модель')),
                ('date', models.DateField(blank=True, null=True, verbose_name='дата выхода')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('title', 'date'),
            },
        ),
        migrations.CreateModel(
            name='SupplierRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='название юр лица')),
                ('email', models.EmailField(max_length=50, verbose_name='email')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='страна')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=70, null=True, verbose_name='улица')),
                ('house', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='номер дома')),
                ('type', models.PositiveSmallIntegerField(choices=[('0', 'factory'), ('1', 'retail'), ('2', 'seller')], default='0', verbose_name='типа продавца')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='время создания')),
                ('exp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sale.supplierrole', verbose_name='')),
            ],
            options={
                'verbose_name': 'контакты',
                'verbose_name_plural': 'контакты',
                'ordering': ('title', 'type'),
            },
        ),
    ]
