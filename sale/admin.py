from django.contrib import admin
from sale.models import Seller, Product
from django.db.models import QuerySet


@admin.action(description='Очистить задолженность')
def debt_reset(self, request, queryset: QuerySet):
    queryset.update(debt=0)


@admin.register(Seller)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'email', 'type', 'supplier', 'debt')
    list_filter = ('city',)
    list_display_links = ('pk', 'supplier',)
    ordering = ('title',)
    filter_horizontal = ('products', )
    search_fields = ('title',)
    actions = (debt_reset,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'model', 'date')
    list_filter = ('title',)
    search_fields = ('title',)
