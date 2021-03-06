from django.conf.urls import url
from . import author_views

urlpatterns = [

    # /authors/<author_name>/<author_id>


    url(
        r'^(?P<author_name>.*)/books/$',
        author_views.author_books,
        name="books"

    ),
    url(
        r'^(?P<author_name>.*)/(?P<pk>\b[0-9A-Fa-f]{8}\b(-\b[0-9A-Fa-f]{4}\b){3}-\b[0-9A-Fa-f]{12}\b)/$',
        author_views.AuthorDetail.as_view(),
        name="author_detail"

    ),



    url(
        r'^$',
        author_views.author_list,
        name="author_list"

    ),

]
