import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Use processing functions from tools. as t TODO


# Create your views here.
def home(request):
    print("Welcome page")
    context = {}  # Nothing to send
    return render(request, 'cloudsearchbe/first.html', context)


@csrf_exempt
def find_keywords(request):
    tex = request.POST.get('tex')
    #kw = t.find_keywords(text) # TODO update? function to call
    kw = ["dummy1", "dummy2", tex]
    context = {"keywords": kw}
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def search_fetch(request):
    text = request.POST.get('keywords')
    #context = t.search_fetch(text) # TODO update? function to call
    context = {"keywords": ["dummy1", "dummy2"],
               "links": ["dummy1.com", "dummy2.com"]
    }
    return HttpResponse(json.dumps(context), content_type="application/json")


def get_engines(request):
    #engines = t.get_engines() # TODO update? function to call
    engines = ["dummy1", "dummy2"]
    context = {'engines': engines}
    return HttpResponse(json.dumps(context), content_type="application/json")


