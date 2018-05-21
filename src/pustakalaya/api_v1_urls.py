
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from pustakalaya_apps.document.api.v1 import views
# All API v1 based urls goes here. 
urlpatterns = [
    # Retrive the list of documents
    url(r'^documents/$', views.document_lists),
    # Retrive the single document i
    url(r'^documents/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$', views.document_detail),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)


