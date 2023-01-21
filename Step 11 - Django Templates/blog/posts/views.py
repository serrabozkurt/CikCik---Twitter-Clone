from django.http import HttpResponse
from django.shortcuts import render


def hello(request, person="world"):
    # return HttpResponse("Hello " + person + "!")

    return render(request, "hello.html", {
        "isim": person
    })


def exchange(request, value):
    # return HttpResponse("{} USD'nin TL karşılığı: {}".format(value, 5.5 * value))

    return render(request, "kur.html", {
        "dolar": value,
        "tl": 18.76 * value,
    })


def form(request):
    return render(request, "form.html")


def hesap(request):
    s1 = int(request.POST.get("sayi1", 1))
    s2 = int(request.POST.get("sayi2", 1))

    isim = request.GET["selam"]

    return render(request, "hesap.html", {
        "sonuc": s1 * s2,
        "selam": isim
    })