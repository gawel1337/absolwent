from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Dzien Dobry!</h1>")

def info(request):
    return HttpResponse("<h1>Info</h1>")
