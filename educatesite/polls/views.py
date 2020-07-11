from django.http import HttpResponse
from django.shortcuts import render


def info(request):
    return render(request, "home.html")


def index(request):
    return HttpResponse("<h1>Ah shit here we go again....</h1>")

def myblog(request):
    return render(request, "myblog.html")