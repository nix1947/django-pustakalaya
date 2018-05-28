from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import (
    DocumentSerializer,
    DocumentFileSerializer,
    DocumentLinkInfoSerializer,
    DocumentSeriesSerializer,
    DocumentIdentifierSerializer
)
from pustakalaya_apps.document.models import (
    Document,
    DocumentFileUpload,
    DocumentLinkInfo,
    DocumentSeries,
    DocumentIdentifier
)

@api_view(['GET', "POST"])
def document_lists(request, format=None):
    """
    Endpoint to get list of documents and 
    to create a document
    """
    
    if request.method == 'GET':
        pagination_class = PageNumberPagination 
        paginator = PageNumberPagination()
        paginator.page_size = 1
        documents = Document.objects.all()
        page = paginator.paginate_queryset(documents, request)
        serializer = DocumentSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def document_detail(request, pk, format=None):
    """
    API endpoint to retrive and update a document. 
    """
    try:
        document = Document.objects.get(pk=pk)
    except Document.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DocumentSerializer(document, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        document.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DocumentFileUploadViewSet(viewsets.ModelViewSet):
    """
     Document Fileupload endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Document Files 
    """
    queryset = DocumentFileUpload.objects.all()
    serializer_class = DocumentFileSerializer


documentfile_list = DocumentFileUploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

documentfile_detail = DocumentFileUploadViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


class DocumentLinkInfoViewSet(viewsets.ModelViewSet):
    """
     Document DocumentLinkInfo endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for document links
    """
    queryset = DocumentLinkInfo.objects.all()
    serializer_class = DocumentLinkInfoSerializer


documentlinkinfo_list = DocumentLinkInfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

documentlinkinfo_detail = DocumentLinkInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



class DocumentSeriesViewSet(viewsets.ModelViewSet):
    """
    DocumentSeries endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for  DocumentSeries
    """
    queryset = DocumentSeries.objects.all()
    serializer_class = DocumentSerializer


documentseries_list = DocumentSeriesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

documentseries_detail = DocumentSeriesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

# DocumentIdentifierSerializer viewsets
class DocumentIdentifierViewSet(viewsets.ModelViewSet):
    """
    DocumentIdentifier endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for  DocumentIdentifier
    """
    queryset = DocumentIdentifier.objects.all()
    serializer_class = DocumentIdentifierSerializer


documentIdentifier_list = DocumentSeriesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

documentIdentifier_detail = DocumentSeriesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
