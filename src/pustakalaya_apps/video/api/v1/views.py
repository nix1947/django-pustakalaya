from pustakalaya_apps.video.models import (
    Video,
    VideoFileUpload,
    VideoLinkInfo,
    VideoSeries,
    VideoGenre
)
from .serializers import (
    VideoSerializers,
    VideoFileSerializer,
    VideoLinkInfoSerializer,
    VideoGenreSerializer,
    VideoSeriesSerializer
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


class VideoLinkInfoViewSet(viewsets.ModelViewSet):
    """
     Video VideoLinkInfo endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Video links
    """
    queryset = VideoLinkInfo.objects.all()
    serializer_class = VideoLinkInfoSerializer


videolinkinfo_list = VideoLinkInfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

videolinkinfo_detail = VideoLinkInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



# Video series 
class VideoSeriesViewSet(viewsets.ModelViewSet):
    """
     VideoSeries endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Video Series
    """
    queryset = VideoSeries.objects.all()
    serializer_class = VideoSeriesSerializer


videoseries_list = VideoSeriesViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

videoseries_detail = VideoSeriesViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



# Video Genre
class VideoGenreViewSet(viewsets.ModelViewSet):
    """
     VideoGenre endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for VideoGenre
    """
    queryset = VideoGenre.objects.all()
    serializer_class = VideoGenreSerializer


videogenre_list = VideoGenreViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

videogenre_detail = VideoGenreViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
