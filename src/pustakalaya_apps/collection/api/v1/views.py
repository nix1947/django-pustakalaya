from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import CollectionSerializer
from pustakalaya_apps.collection.models import Collection
from rest_framework import permissions
from rest_framework import renderers

class CollectionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Collection model
    """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer



collection_list = CollectionViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
collection_detail = CollectionViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

