from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse("<h1>Hello Django!</h1>")
    return render(request, "hello.html")


def python(request):
    return render(request, "python.html")