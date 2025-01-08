from django.urls import path
# from . import views

from .views import (
    ProductListView,
    ProductDetailView,
    EditProductView,
    DeleteProductView,
    HomeView,
    AboutView,
    ContactView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/edit/<int:pk>/', EditProductView.as_view(), name='edit_product'),
    path('products/delete/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
    
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]


# function based urls

# urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('', views.product_list, name='product_list'),
#     path('product/<int:id>/', views.product_detail, name='product_detail'),
#     path('<int:id>/edit/', views.edit_product, name='edit_product'),
#     path('<int:id>/delete/', views.delete_product, name='delete_product'),
 

#     path('about/', views.about, name='about'),          
#     path('contact/', views.contact, name='contact'),
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)