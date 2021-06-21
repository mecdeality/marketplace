from rest_framework.generics import ListAPIView

from .serializers import ItemSerializer
from ..models import Item


class ItemListAPIView(ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()