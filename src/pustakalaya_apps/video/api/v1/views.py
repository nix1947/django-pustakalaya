from pustakalaya_apps.video.models import (
    Video,
    VideoFileUpload
)
from .serializers import (
    VideoSerializers,
    VideoFileSerializer
)
from rest_framework import mixins
from rest_framework import generics, viewsets



class VideoList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VideoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





class VideoFileUploadViewSet(viewsets.ModelViewSet):
    """
     Document Fileupload endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Document Files 
    """
    queryset = VideoFileUpload.objects.all()
    serializer_class = VideoFileSerializer



videofile_list = VideoFileUploadViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

videofile_detail = VideoFileUploadViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})




