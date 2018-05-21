
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
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


# All API v1 based urls goes here. 
urlpatterns = [
    # Retrive the list of documents
    url(r'^documents/$', document_lists),
    # Retrive the single document i
    url(r'^documents/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', document_detail),

    # Audio url 
    url(r'^audios/$', AudioList.as_view()),
    url(r'^audios/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', AudioDetail.as_view()),

    # Video url
    #  # Audio url 
    url(r'^videos/$', VideoList.as_view()),
    url(r'^videos/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', VideoDetail.as_view()), 
    
]

urlpatterns = format_suffix_patterns(urlpatterns)


