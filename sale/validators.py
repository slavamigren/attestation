from rest_framework.serializers import ValidationError


class SellerValidator:
    """
    Валидирует:
    - завод не может закупать ни у кого
    - завод не может быть должником
    - дебеторская задолженность не может быть установлена без наличия поставщика
    """
    def __call__(self, seller):
        if seller.get('type', None) == 'factory':
            if seller.get('supplier', None):
                raise ValidationError('Завод не может закупать товары для реализации')
            if seller.get('debt', None):
                raise ValidationError('Завод не может быть должником по закупкам')
        else:
            if seller.get('debt', None) and not seller.get('seller', None):
                raise ValidationError('Задолженность не может быть установлена без контрагента')
