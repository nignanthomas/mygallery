from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Location,Category,Image


# Create your views here.


def landing(request):
    all_images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    title = 'Home'

    return render(request,'index.html', {'all_images':all_images,'locations':locations,'categories':categories, 'title':title})
