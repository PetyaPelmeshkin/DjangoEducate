from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Ah shit here we go again...</h1>")
