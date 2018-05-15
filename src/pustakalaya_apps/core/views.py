from itertools import chain 
from pustakalaya_apps.document.models import Document
from pustakalaya_apps.audio.models import Audio
from pustakalaya_apps.video.models import Video
from django.shortcuts import (
    render,
)
from django.conf import settings


def home(request):
    """view that serve homepage"""


    try:
        # Based on hit count so, need to capture Field error exception
        featured_books = Document.featured_objects.all() # Return top 4 views item.
        print("total book is", len(featured_books))
    except Exception as e: # Catch all error don't know what kind exist.
        pass 

    
    featured_audio = Audio.featured_objects.all() # Provide only top 2 items
    print("Total audio", len(featured_audio))
    featured_video = Video.featured_objects.all() # Provide only top 2 items
    print("Total video", len(featured_video))

    
    if not featured_books:
        featured_books = Document.objects.filter(featured="yes", published="yes").order_by('-updated_date')[:3]
        
    if not featured_audio:
        featured_audio =Audio.objects.filter(featured="yes", published="yes").order_by('-updated_date')[:3]

    if not featured_video:
        featured_video = Video.objects.filter(featured="yes", published="yes").order_by('-updated_date')[:2]

    items = list(chain(featured_audio, featured_books, featured_video))
    print("items is", len(items))

    context = {}
    context["featured_books"] = list(items)
    return render(request, "index.html", context)
