from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from sale.models import Seller
from sale.serializers import SellerSerializer, SellerCreateSerializer, SellerUpdateSerializer


class SellerSet(ModelViewSet):
    """
    Контроллер модели Seller
    """
    queryset = Seller.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ('country',)
    default_serializer = SellerSerializer
    serializers = {
        'create': SellerCreateSerializer,
        'update': SellerUpdateSerializer,
        'partial_update': SellerUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)
