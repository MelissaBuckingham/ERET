from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.
def all_listings(request):
    """ A view to show all listings, including sorting and search queries """
    listings = Product.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('listings'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            listings = listings.filter(queries)

    context = {
        'listings': listings,
        'search_term': query,
    }
    return render(request, 'listings/listings.html', context)

def listing_detail(request, product_id):
    """ A view to show individual listing details """
    listing = get_object_or_404(Product, pk=product_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing_detail.html', context)