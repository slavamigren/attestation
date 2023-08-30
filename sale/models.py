from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


NULLABLE = {'blank': True, 'null': True}


class SupplierType(models.TextChoices):
    FACTORY = 'factory', _('factory')
    RETAIL = 'retail', _('retail')
    SELLER = 'seller', _('seller')


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='продукт')
    model = models.CharField(max_length=100, **NULLABLE, verbose_name='модель')
    date = models.DateField(**NULLABLE, verbose_name='дата выхода')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title', 'date', )

    def __str__(self):
        return f'{self.title}, модель {self.model}, дата выхода {self.date}'


class Seller(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='название юр лица')
    email = models.EmailField(max_length=50, verbose_name='email')
    country = models.CharField(max_length=50, **NULLABLE, verbose_name='страна')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='город')
    street = models.CharField(max_length=70, **NULLABLE, verbose_name='улица')
    house = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='номер дома')
    type = models.CharField(
        max_length=7,
        choices=SupplierType.choices,
        default=SupplierType.FACTORY,
        verbose_name='типа продавца'
    )
    time = models.DateTimeField(default=timezone.now, verbose_name='время создания')
    supplier = models.ForeignKey(
        'Seller',
        **NULLABLE,
        on_delete=models.SET_NULL,
        verbose_name='поставщик продукции',
    )
    debt = models.DecimalField(max_digits=11, decimal_places=2, default=0, verbose_name='задолженность')
    products = models.ManyToManyField(Product, blank=True, verbose_name='продукты')

    class Meta:
        verbose_name = 'продавец'
        verbose_name_plural = 'продавцы'
        ordering = ('title', 'type')

    def __str__(self):
        return f'Продавец {self.title}'
