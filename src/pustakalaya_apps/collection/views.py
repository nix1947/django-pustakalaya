from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Collection
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections


def collection_detail(request, name, pk):
    """
    Render collection detail
    :param request:
    :param name: collection_name
    :param pk: primary key of a collection
    :return: Response Obj
    """
    # Context holder
    context = {}
    sort_order_type = "asc", "desc"
    sort_by_type = "title.keyword", "updated_date"

    if request.method == "GET":
        # Default sort options
        sort_by = request.GET.get("sort_by") or "title.keyword"
        sort_order = request.GET.get("sort_order") or "asc"

        if sort_order not in sort_order_type:
            sort_order = "asc"

        if sort_by not in sort_by_type:
            sort_by = "title.keyword"

    # Query to elastic search to grab all the items related to this collection name
    # And sort the result based on the sorting options.
    client = connections.get_connection()
    name = " ".join(name.split("-"))
    s = Search(index="pustakalaya").using(client).query("match", collections_ids=pk).sort({
        sort_by: {"order": sort_order}
    })

    # Pagination configuration before executing a query.
    number_per_page= 25
    paginator = Paginator(s, number_per_page)

    page_no = request.GET.get('page')
    try:
        page = paginator.page(page_no)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    start_item_count = 0

    if page_no is not None:

        if page_no.isdigit():
            if page_no==1:
                start_item_count = 1
            elif int(page_no) > 1 :
                start_item_count = (int(page_no) - 1) * number_per_page
        else:
            start_item_count = 0


    response = page.object_list.execute()
    splitted_name = name.split()
    collection_name = "-".join(splitted_name)
    collection = Collection.objects.get(pk=pk)

    context["response"] = response
    context["collection_name"] = collection_name
    context["collection_pk"] = pk
    context["community_name"] = collection.community_name
    context["sort_order"] = sort_order
    context["sort_by"] = sort_by

    context["page_obj"] = page
    context["page_number_count"]= start_item_count


    return render(request, "collection/collection_detail.html", context)
