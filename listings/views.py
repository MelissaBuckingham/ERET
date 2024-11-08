from django.shortcuts import render
from .models import Product

# Create your views here.
def all_listings(request):
    """ A view to show all listings, including sorting and search queries """
    listings = Product.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listings/listings.html', context)