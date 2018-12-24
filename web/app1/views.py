from django.shortcuts import render
from .models import retust
from django.http import HttpResponse
from django.template import loader

from django.http import Http404
# Create your views here.


def student(request):
    context = {
        "all_retust": retust.objects.all()
    }
    return render(request, "index.html", context=context)