import os
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .forms import FeedBackForm
from django.conf import settings
from pustakalaya_apps.document.tasks import send_feedback_email_task





def change_language(request):
    return HttpResponse("Change language")


def feedback(request):
    if request.method == 'GET':
        form = FeedBackForm()
    else:
        form = FeedBackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            country = form.cleaned_data['country']
            location = form.cleaned_data['address']
            suggestion = form.cleaned_data['suggestion']
            html_message = """
                <p>From: {0}</p>
                <p>Location: {1}</p>
                <p>Sender Email: {2}</p>
                <p>Country: {3}</p>
                <br><br>
                <b>
                {4}
                </b>

            """.format(name, location, email, country, suggestion)
            try:
                # Call the celery tasks to send email. 
                message =  'From: {}\n Email: {} \n Location: {} \n Country: {}\n Message: {}'.format(name, email, location, country, suggestion )

                send_feedback_email_task.delay(
                    "Feedback Email",
                    message
                )

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect("/")
    return render(request, "static_pages/feedback.html", {'form': form})


# Get the elastic search url
ES_HOST = settings.ES_HOST
ES_PORT  =settings.ES_PORT

elastic_search_endpoint = "http://{}:{}/pustakalaya/_search?pretty                                                                                                                                                                                                                                                                                                                                                                                                              ".format(ES_HOST, ES_PORT)

@api_view(['GET'])
def api_v1_root_view(request, format=None):
     return Response({
       'documents':reverse('api_v1:document_list', request=request, format=format),
       'documentfiles': reverse('api_v1:documentfileupload-list', request=request, format=format),
       'documentlinkinfos': reverse('api_v1:documentlinkinfo-list', request=request, format=format),
       'audios': reverse('api_v1:audio_list', request=request, format=format),
       'audiofiles': reverse('api_v1:audiofileupload-list', request=request, format=format),
       'audiolinkinfos': reverse('api_v1:audiolinkinfo-list', request=request, format=format),
       'videos': reverse('api_v1:video_list', request=request, format=format),
       'videofiles': reverse('api_v1:videofileupload-list', request=request, format=format),
       'videolinkinfos': reverse('api_v1:videolinkinfo-list', request=request, format=format),
       'collections': reverse('api_v1:collection-list', request=request, format=format),
       'search': elastic_search_endpoint,
       'suggestion': "{}?suggest_text=".format(reverse("search:completion", request=request, format=format)),
       
       # Author details.
       'documentauthors': reverse('api_v1:documentauthors_list', request=request, format=format),
       'documenteditors': reverse('api_v1:documenteditors_list', request=request, format=format),
       'documentillustrators': reverse('api_v1:documentillustrators_list', request=request, format=format),
       'audiovoiceartists': reverse('api_v1:audiovoiceartists_list', request=request, format=format),
       'videodirectors': reverse('api_v1:videodirectors_list', request=request, format=format),
       'videoproducers': reverse('api_v1:videoproducers_list', request=request, format=format),

       # keyword, EducationLevel, Publisher,
       'keywords': reverse('api_v1:keyword-list', request=request, format=format), 
       'languages': reverse('api_v1:language-list', request=request, format=format),
       'publishers': reverse('api_v1:publisher-list', request=request, format=format),
       'educationlevels': reverse('api_v1:educationlevel-list', request=request, format=format),
       'sponsors': reverse('api_v1:sponsor-list', request=request, format=format),
       'publisher': reverse('api_v1:licensetype-list', request=request, format=format),

       # Video series and genre viewsets
       'videoseries': reverse('api_v1:videoseries-list', request=request, format=format),
       'videogenres': reverse('api_v1:videogenre-list', request=request, format=format),

       # API endpoint to CRUD document series.
       'documentseries': reverse('api_v1:documentseries-list', request=request, format=format),
       'documentidentifiers': reverse('api_v1:documentidentifier-list', request=request, format=format),


    })
