from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('<h1> Hello</h1>')
