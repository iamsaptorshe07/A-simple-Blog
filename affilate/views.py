from django.shortcuts import render
from .models import *
# Create your views here.
def product(request):
    product = Product.objects.all()
    context = {
        'Products':product,
    }
    return render(request,'affilate.html',context=context)