from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, viewsets
from pustakalaya_apps.audio.models import (
    Audio,
    AudioFileUpload,
    AudioLinkInfo
)
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    AudioSerializers,
    AudioFileSerializer,
    AudioLinkInfoSerializer
)


class AudioList(APIView):
    """
    List all audio, or create a new audio.
    """
    def get(self, request, format=None):
        pagination_class = PageNumberPagination 
        paginator = PageNumberPagination()
        paginator.page_size = 1
        audios = Audio.objects.all()
        page = paginator.paginate_queryset(audios, request)
        serializer = AudioSerializers(page, many=True)
        return paginator.get_paginated_response(serializer.data)
        

    def post(self, request, format=None):   
        serializer = AudioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AudioDetail(APIView):
    """
    Retrieve, update or delete a Audio instance.
    """
    def get_object(self, pk):
        try:
            return Audio.objects.get(pk=pk)
        except Audio.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        audio = self.get_object(pk)
        serializer = AudioSerializers(audio)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        audio = self.get_object(pk)
        serializer = AudioSerializers(audio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        audio = self.get_object(pk)
        audio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

 
class AudioFileUploadViewSet(viewsets.ModelViewSet):
    """
     Audio Fileupload endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Audio Files 
    """
    queryset = AudioFileUpload.objects.all()
    serializer_class = AudioFileSerializer


audiofile_list = AudioFileUploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
audiofile_detail = AudioFileUploadViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


class AudioLinkInfoViewSet(viewsets.ModelViewSet):
    """
     Audio AudioLinkInfo endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Audio links
    """
    queryset = AudioLinkInfo.objects.all()
    serializer_class = AudioLinkInfoSerializer


audiolinkinfo_list = AudioLinkInfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

audiolinkinfo_detail = AudioLinkInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



