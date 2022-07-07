from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def route(request, short_code):
    return render(request, 'route.html')