
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from pustakalaya_apps import (
    collection,
    document,
    audio,
    video,
)

from pustakalaya_apps.core.api.v1.views import (
    BiographyViewSet,
    biography_list,
    biography_detail,
    KeywordViewSet,
    EducationLevelViewSet,
    PublisherViewSet,
    SponsorViewSet,
    LicenseTypeViewSet,
    LanguageViewSet   
)

from rest_framework.urlpatterns import format_suffix_patterns
from pustakalaya.views import api_v1_root_view
from pustakalaya_apps.document.api.v1.views import (
    document_lists,
    document_detail,
    DocumentSeriesViewSet,
    DocumentIdentifierViewSet,
)

from pustakalaya_apps.audio.api.v1.views import (
    AudioList,
    AudioDetail
)

from pustakalaya_apps.video.api.v1.views import (
    VideoList,
    VideoDetail,
    VideoSeriesViewSet,
    VideoGenreViewSet
)

from pustakalaya_apps.collection.api.v1.views import (
    collection_list,
    collection_detail
)

# Import core serializers
# from pustakalaya_apps.core.api.v1.views import (

# )

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



# Define a viewsets for collections 
router = DefaultRouter()
router.register(r'collections', collection.api.v1.views.CollectionViewSet)

# routers for documentfileupload
router.register(r'documentfileuploads', document.api.v1.views.DocumentFileUploadViewSet)
router.register(r'documentlinkinfos', document.api.v1.views.DocumentLinkInfoViewSet)


# router for audiofileupload
router.register(r'audiofileuploads', audio.api.v1.views.AudioFileUploadViewSet)
router.register(r'audiolinkinfos', audio.api.v1.views.AudioLinkInfoViewSet)

# router for video fileupload
router.register(r'videofileuploads', video.api.v1.views.VideoFileUploadViewSet)
router.register(r'videolinkinfos', video.api.v1.views.VideoLinkInfoViewSet)

# Document, audio, video author, illustrator, and editor end point
# All authors are saved in same table. 
# So we need to seperate the urlname to avoid confusion to endpoints.


urlpatterns += [
    # URL endpoints for document author
    url(r'^documentauthors/$', biography_list,name="documentauthors_list"),
    url(r'^documentauthors/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
    biography_detail,
    name="documentauthors_detail"
    ),

    # Url endpoint for document editors 
    url(r'^documenteditors/$', biography_list,name="documenteditors_list"),
    url(r'^documenteditors/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
    biography_detail,
    name="documenteditors_detail"
    ),

    # Url endpoint for document illustrators
    url(r'^documentillustrators/$', biography_list,name="documentillustrators_list"),
    url(r'^documentillustrators/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
    biography_detail,
    name="documentillustrators_detail"
    ),

    # url endpoint for audio readby aka audiovoiceartists
    url(r'^audiovoiceartists/$', biography_list,name="audiovoiceartists_list"),
    url(r'^audiovoiceartists/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
    biography_detail,
    name="audiovoiceartists_detail"
    ),

    # url endpoint for video directors
    url(r'^videodirectors/$', biography_list,name="videodirectors_list"),
    url(r'^videodirectors/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
    biography_detail,
    name="videodirectors_detail"
    ),

    # url endpoint for video videoproducers
    url(r'^videoproducers/$', biography_list,name="videoproducers_list"),
    url(r'^videoproducers/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', 
    biography_detail,
    name="videoproducers_detail"
    ),
] 

# Suffix the patterns. 
urlpatterns = format_suffix_patterns(urlpatterns)

# Register these url patterns for core Model apis
# keyword, EducationLevel, Publisher,
router.register(r'keywords', KeywordViewSet)
router.register(r'languages', LanguageViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'educationlevels', EducationLevelViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'licensetypes', LicenseTypeViewSet)

# Video series and genre urls.
router.register(r'videoseries', VideoSeriesViewSet)
router.register(r'videogenres', VideoGenreViewSet) 

# Document series url 
router.register(r'documentseries', DocumentSeriesViewSet) 

# Document indentifier url
router.register(r'documentidentifier', DocumentIdentifierViewSet) 




# The API URLs are now determined automatically by the router.
urlpatterns += [
    url(r'^', include(router.urls))
]

# Endpoints for api .
schema_view = get_schema_view(title='Pustakalaya API')

urlpatterns += [
    url(r'^schema/$', schema_view),
]
