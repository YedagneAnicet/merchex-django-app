from django.http import HttpResponse
from django.shortcuts import render

from .models import Band
from .models import Listing


def hello(request):
    bands = Band.objects.all()
    listing = Listing.objects.all()
    return render(request, 'listings/hello.html',
                  context={'bands': bands})

def listing(request):
    listing = Listing.objects.all()
    return render(request, 'listings/listings.html',
                  context={'listings': listing})