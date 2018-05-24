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
                send_mail(
                    'Feedback message',
                    """
                    From: {}\n Email: {} \n Location: {} \n Country: {}\n Message: {}
                    """.format(name, email, location, country, suggestion ),
                    settings.EMAIL_HOST_USER,
                    settings.FEEDBACK_MESSAGE_TO,
                    fail_silently=False
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
       'audios': reverse('api_v1:audio_list', request=request, format=format),
       'audiofiles': reverse('api_v1:audiofileupload-list', request=request, format=format),
       'videos': reverse('api_v1:video_list', request=request, format=format),
       'videofiles': reverse('api_v1:videofileupload-list', request=request, format=format),
       'collections': reverse('api_v1:collection-list', request=request, format=format),
       'search': elastic_search_endpoint,
       'suggestion': "{}?suggest_text=".format(reverse("search:completion", request=request, format=format)),
    })
