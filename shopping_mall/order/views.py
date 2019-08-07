from django.shortcuts import render
from django.views.generic import FormView
from .forms import OrderForm
# Create your views here.
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = "/product/"
    
    