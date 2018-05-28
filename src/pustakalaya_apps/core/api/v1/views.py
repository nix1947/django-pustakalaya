from rest_framework import viewsets
from .serializers import (
    BiographySerializer,
    KeyWordSerializer,
    EducationLevelSerializer,
    LanguageSerializer,
    LicenseTypeSerializer,
    PublisherSerializer,
    SponsorSerializer,
)

from pustakalaya_apps.core.models import (
    Biography,
    Keyword,
    Language,
    Publisher,
    EducationLevel,
    Sponsor,
    LicenseType,
)

class BiographyViewSet(viewsets.ModelViewSet):
    """
    Endpoint to CRUD Authors
    """
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer



biography_list = BiographyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

biography_detail = BiographyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


class KeywordViewSet(viewsets.ModelViewSet):
    """
     Keyword endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for keyword
    """
    queryset = Keyword.objects.all()
    serializer_class = KeyWordSerializer

keyword_list = KeywordViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

keyword_detail = KeywordViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



class LanguageViewSet(viewsets.ModelViewSet):
    """
    Language endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Language links
    """
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


language_list = LanguageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

language_detail = LanguageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


class PublisherViewSet(viewsets.ModelViewSet):
    """
    Publisher endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for publisher links
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


publisher_list = PublisherViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

publisher_detail = PublisherViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



class EducationLevelViewSet(viewsets.ModelViewSet):
    """
     Education Level endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Education Level 
    """
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer


educationlevel_list = EducationLevelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

educationlevel_detail = EducationLevelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})





class SponsorViewSet(viewsets.ModelViewSet):
    """
     sponsors endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for sponsors
    """
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer


sponsor_list = SponsorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

sponsor_detail = SponsorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


class LicenseTypeViewSet(viewsets.ModelViewSet):
    """
     Licese type endpoint to  `list`, `create`, `retrieve`,
    `update` and `destroy` actions for LicenseType
    """
    queryset = LicenseType.objects.all()
    serializer_class = LicenseTypeSerializer


licensetype_list = LicenseTypeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

licensetype_detail = LicenseTypeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})



