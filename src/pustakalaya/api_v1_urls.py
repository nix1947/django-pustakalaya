
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from pustakalaya_apps import (
    collection,
    document,
    audio,
    video
)
from rest_framework.urlpatterns import format_suffix_patterns
from pustakalaya.views import api_v1_root_view
from pustakalaya_apps.document.api.v1.views import (
    document_lists,
    document_detail,
)

from pustakalaya_apps.audio.api.v1.views import (
    AudioList,
    AudioDetail
)

from pustakalaya_apps.video.api.v1.views import (
    VideoList,
    VideoDetail
)

from pustakalaya_apps.collection.api.v1.views import (
    collection_list,
    collection_detail
)

# All API v1 based urls goes here. 
urlpatterns = [
    # Entry point for urls 
    url(r'^$',api_v1_root_view, name="api_v1"),
    
    # Retrive the list of documents
    url(r'^documents/$', document_lists, name="document_list"),
    # Retrive the single document i
    url(
        r'^documents/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',      
        document_detail,
          name="document_detail"
    ),

    # Audio url 
    url(
        r'^audios/$', 
        AudioList.as_view(),
        name="audio_list"
        ),
    url(
        r'^audios/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
        AudioDetail.as_view(),
        name="audio_detail"

        ),

    # Video url
    #  # Audio url 
    url(
        r'^videos/$', 
        VideoList.as_view(),
        name="video_list"
        ),
    url(
        r'^videos/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',
         VideoDetail.as_view(),
         name="video_detail"
         ),   
]

urlpatterns = format_suffix_patterns(urlpatterns)

# Define a viewsets for collections 
router = DefaultRouter()
router.register(r'collections', collection.api.v1.views.CollectionViewSet)

# routers for documentfileupload
router.register(r'documentfileuploads', document.api.v1.views.DocumentFileUploadViewSet)

# router for audiofileupload
router.register(r'audiofileuploads', audio.api.v1.views.AudioFileUploadViewSet)

# router for video fileupload
router.register(r'videofileuploads', video.api.v1.views.VideoFileUploadViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns += [
    url(r'^', include(router.urls))
]


# Endpoints for api .
schema_view = get_schema_view(title='Pustakalaya API')

urlpatterns += [
    url(r'^schema/$', schema_view),
]
