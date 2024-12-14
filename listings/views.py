from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm

# Create your views here.
def all_listings(request):
    """ A view to show all listings, including sorting and search queries """
    listings = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                listings = listings.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            listings = listings.order_by(sortkey)
            
        if 'listing' in request.GET:
            listings = request.GET['category'].split(',')
            listings = listings.filter(category__name__in=listings)
            listings = Category.objects.filter(name__in=listings)

        if 'product' in request.GET:
            products = request.GET['category'].split(',')
            products = products.filter(category__name__in=products)
            products = Category.objects.filter(name__in=products)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            listings = listings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('listings'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            listings = listings.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'listings': listings,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'listings/listings.html', context)

def listing_detail(request, product_id):
    """ A view to show individual listing details """
    listing = get_object_or_404(Product, pk=product_id)
    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing_detail.html', context)

def add_listing(request):
    """ Add a listing to the site """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added property!')
            return redirect(reverse('listing_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add property. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'listings/add_listing.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def edit_listing(request, product_id):
    """ Edit a listing on the website """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated property!')
            return redirect(reverse('listing_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update property. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')
    template = 'listings/edit_listing.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)

    
def delete_listing(request, product_id):
    """ Delete a listing from the website """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Property deleted!')
    return redirect(reverse('listings'))

def gallery_with_upload(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            for image in request.FILES.getlist('images'):
                Image.objects.create(image=image)
    else:
        form = UploadImageForm()

    gallery = Image.objects.all()
    return render(request, 'listings/gallery_with_upload.html', {'form': form, 'gallery': gallery})