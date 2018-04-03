import string
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.views.generic.detail import DetailView
from .models import Biography
from django.shortcuts import (
    render,
)


def home(request):
    return render(request, "index.html", {})


class AuthorDetail(DetailView):
    model = Biography

    template_name = "core/author_detail.html"


def author_list(request):
    # hold some data.
    letters = string.ascii_lowercase
    nepali_letters = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऋ', 'ए', 'क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ',
                      'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प', 'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'स',
                      'ष', 'ह']

    #Filter for show all
    letter_exist = False;

    if request.method == "GET":
        query_letter = request.GET.get('letter',None)

        if not query_letter:
            author_list = Biography.objects.all()
        else:
            author_list = Biography.objects.filter(name__startswith=query_letter or query_letter.upper())
            letter_exist = True

        new_list = []
        for item in author_list:
            if item.name:
                new_list.append(item)


        # Paginate the results
        number_per_page = 15
        # Get the page no.

        page_no = request.GET.get('page')

        paginator = Paginator(new_list, number_per_page)
        try:
            authors = paginator.page(page_no)
        except PageNotAnInteger:
            authors = paginator.page(1)
        except EmptyPage:
            authors = paginator.page(paginator.num_pages)

        start_item_count = 0
        # print("pg num= ",page_no)
        if page_no is not None:

            if page_no.isdigit():
                if page_no == 1:
                    start_item_count = 1
                elif int(page_no) > 1:
                    start_item_count = (int(page_no) - 1) * number_per_page
            else:
                start_item_count = 0

    return render(request, "core/author_list.html", {
        "letters": letters,
        "authors": authors,
        "nepali_letters": nepali_letters,
        "page_number_count" : start_item_count,
        "letter_exist":letter_exist
    })


def author_books(request, author_name):
    from pustakalaya_apps.core.utils import list_search_from_elastic
    from pustakalaya_apps.core.utils import  list_search_from_elastic_work
    """
    Query all the books by this author from ES.
    :param request:
    :param author_name:
    :return:
    """
    #print("author name = ",author_name)
    # author_name = " ".join(author_name.split("-"))
    author_name = " ".join(author_name.split("_"))
    #print(author_name)
    # TODO: explicitly define the index name
    search_field = "author_list"
    search_value = author_name
    kwargs = {
        search_field: search_value
    }

    # Query to elastic search in keywords field having the value of search_value
    # Return response object.

    #context = list_search_from_elastic(request, **kwargs)
    context = list_search_from_elastic_work(request,author_name)

    context["keyword"] = context
    context["author"] = author_name
    # Reuse the keyword template
    return render(request, "core/author_books.html", context)
