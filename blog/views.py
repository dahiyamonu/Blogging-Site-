from django.shortcuts import render

from .models import Product
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .form import ProductForm, ContactForm

#imports of generic view that i used in my project
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy


# contact us form
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# generic views 

class ProductListView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'index2.html'
    context_object_name = 'product'

class EditProductView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit.html'

    def get_success_url(self):
        return reverse_lazy('product_list')
    
class DeleteProductView(DeleteView):
    model = Product
    template_name = 'delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('product_list')

class HomeView(TemplateView):
    template_name = 'home.html'
    def get(self, request, *args, **kwargs):
        return HttpResponse("hello world !")

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'




# function based views 

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'index.html', {'products': products})

# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(request, 'index2.html', {'product': product})

# def edit_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'edit.html', {'form': form})

# def delete_product(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method =="POST":
#         product.delete()
#         return redirect('product_list')
#     return render(request, 'delete.html', {'product': product})

# def home(request):
#     return HttpResponse("Hello World !")

# def about(request):
#     return render(request, 'about.html')  

# def contact(request):
#     return render(request, 'contact.html')




# contact us form

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            send_mail(
                f"New Contact Message from {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.ADMIN_EMAIL],  # Replace with your admin email
            )
            return render(request, 'contact.html', {'form': form, 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
