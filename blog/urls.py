from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('<int:id>/edit/', views.edit_product, name='edit_product'),
    path('<int:id>/delete/', views.delete_product, name='delete_product'),
 

    path('about/', views.about, name='about'),          
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)