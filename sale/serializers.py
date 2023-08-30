from rest_framework import serializers
from sale.models import Seller
from sale.validators import SellerValidator


class SellerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для просмотра списка и отдельных объектов Seller
    """
    class Meta:
        model = Seller
        fields = '__all__'


class SellerCreateSerializer(serializers.ModelSerializer):
    """
    Сериализотор для заведения нового объекта Seller
    """
    class Meta:
        model = Seller
        fields = '__all__'
        validators = [SellerValidator()]


class SellerUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления объекта Seller.
    Поле debt исключено из обновляемых по API
    """
    class Meta:
        model = Seller
        # exclude = ('debt',)
        fields = '__all__'
        validators = [SellerValidator()]

    def validate_supplier(self, value):
        """Валидирует присвоение полю supplier собственного id"""
        if self.instance == value:
            raise serializers.ValidationError('Продавец не может закупать сам у себя')
        return value

    def validate_debt(self, value):
        """Запрещает изменение debt по API"""
        raise serializers.ValidationError('Задолженность не может быть изменена по API')
