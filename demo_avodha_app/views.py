from django.http import HttpResponse
from django.shortcuts import render
from .models import  shop

# Create your views here.
def demo(request):
    product=shop.objects.all()
    return render(request,"home.html",{'products':product})
