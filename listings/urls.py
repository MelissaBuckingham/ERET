from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<int:product_id>/', views.listing_detail, name='listing_detail'),
    path('add/', views.add_listing, name='add_listing'),
]