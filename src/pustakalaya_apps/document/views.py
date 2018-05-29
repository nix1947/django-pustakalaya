import json
from django.shortcuts import render
from .models import Document
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView
from .models import DocumentFileUpload
from django.core.exceptions import ValidationError
from pustakalaya_apps.review_system.models import Review
from pustakalaya_apps.favourite_collection.models import Favourite
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.http import Http404, HttpResponse
from star_ratings.models import Rating
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

# from .forms import BaseDocumentFormSet

def documents(request):
    documents = 1 or Document.objects.all()
    return render(request, 'document/documents.html', {'documents': documents})

def flipBook(request, pk):

    return render(request, 'document/flip_book.html', {
        "book_id":pk
    })


class DocumentDetailView(HitCountDetailView):  # Detail view is inherited from HitCountDetailView
    model = Document
    count_hit = True

    def get(self, request, **kwargs):
        self.object = self.get_object()
        if self.object.published == "no":
            # return HttpResponseRedirect("/")
            # return Http404()
            # msg = "Page not found"
            # return HttpResponse(msg, status=404)
            raise Http404

        hit_count = HitCount.objects.get_for_object(self.object)


        # next, you can attempt to count a hit and get the response
        # you need to pass it the request object as well
        hit_count_response = HitCountMixin.hit_count(request, hit_count)
        context = self.get_context_data(object=self.object)



        data_review = Review.objects.filter(content_id=self.object.pk, content_type='document')

        #************Review pagination add************#

        length = len(data_review)
        print("len=",length)
        number_per_page =15
        if length > number_per_page:
            #print("inside pagination")
            #   for pagination we have following code
            paginator = Paginator(data_review, number_per_page)
            page = request.GET.get('page')
            try:
                users = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                users = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 7777), deliver last page of results.
                users = paginator.page(paginator.num_pages)

            context["paginated_data"] = users

        ########################Review Pagination end########################

        favourite_data=""
        # favourite item data extractions
        if request.user.is_authenticated:
            favourite_data = Favourite.objects.filter(favourite_item_id=self.object.pk, favourite_item_type='document', user=request.user);

        if length > 0 and length <= number_per_page:
            context["data_review"]= data_review



        context["favourite_data"]= favourite_data
        context["total_review_count"]=length

        # Rating average,total,and user_rating
        # Get the rating of current object
        # Get content type
        try:
            content_type = ContentType.objects.get(model="document")
            rating_obj = Rating.objects.get(content_type=content_type, object_id=self.object.pk)

            # Average rating
            context["rating_average"] = round(rating_obj.average, 1)

            # Total ratings
            context["rating_total"]=rating_obj.total
        except ObjectDoesNotExist:
            pass



        return self.render_to_response(context)

    template_name = "document/document_detail_new.html"


def document_page_view(request, pk):
    json_response = {}
    if request.method == "GET":
        try:
            document = DocumentFileUpload.objects.get(pk=pk)
            if document:
                json_response["file_name"] = document.file_name
                json_response["title"] = document.document.title
                json_response["total_page"] = document.total_pages
                json_response["page_urls"] = document.get_files()
        except (DocumentFileUpload.DoesNotExist, ValidationError):
            pass

    # Create json response
    #print(json_response)
    json_response = json.dumps(json_response)
    return HttpResponse(json_response, content_type="application/json")
