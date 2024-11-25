from django.urls import path
from . import views
urlpatterns = [
    path('', views.all_listings, name='listings'),
    path('<int:product_id>/', views.listing_detail, name='listing_detail'),
    path('add/', views.add_listing, name='add_listing'),
    path('edit/<int:product_id>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:product_id>/', views.delete_listing, name='delete_listing'),
]