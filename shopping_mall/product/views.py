from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from .models import Product
from .forms import RegisterForm
from order.forms import OrderForm

# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"

class ProductRegister(FormView):
    template_name = "product/register.html"
    form_class = RegisterForm
    success_url = '/product/'

class ProductDetail(DetailView):
    template_name = "product/detail.html"
    #queryset = Product.objects.all()
    model = Product
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form']=OrderForm()
        return context