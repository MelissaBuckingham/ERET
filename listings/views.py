from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_listings(request):
    """ A view to show all listings, including sorting and search queries """
    listings = Product.objects.all()
    context = {
        'listings': listings,
    }
    return render(request, 'listings/listings.html', context)

def listing_detail(request, listing_id):
    """ A view to show individual listing details """
    listing = get_object_or_404(Product, pk=listing_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing_detail.html', context)