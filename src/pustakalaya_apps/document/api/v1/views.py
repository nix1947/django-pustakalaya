from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import DocumentSerializer
from pustakalaya_apps.document.models import Document

@api_view(['GET', "POST"])
def document_lists(request, format=None):
    """
    Return list of documents
    """
    if request.method == 'GET':
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents,many=True)
        return Response(serializer.data)
    

    elif request.method == 'POST':
        serializer = DocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def document_detail(request, pk, format=None):
    """
    Retrieve document 
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