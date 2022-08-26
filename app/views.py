from django.shortcuts import render,redirect
from django.http import Http404
# from .models import Pictures
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def departments(request):
    return render(request, 'departments.html')

def gallery(request):
    try:
        pictures = Pictures.objects.get(id = pictures_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'gallery.html',{"pictures":pictures})

def contact(request):
    return render(request, 'contact.html')