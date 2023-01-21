import datetime

from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post



def ekle(request):
    return render(request, "ekle.html", {
        "form": PostForm()
    })


def kaydet(request):
    form = PostForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return redirect('/ekle/')


def anasayfa(request):
    durum = request.GET.get("durum")
    # TODO: Tüm yazıları gösterin!
    if durum == "taslak":
        yazilar = Post.objects.filter(published=False).order_by("-created")
    else:
        yazilar = Post.objects.filter(published=True).order_by("-created")
    return render(request, "anasayfa.html", {
        "gonderiler": yazilar
    })


def filtre(request):
    # yazilar = Post.objects.exclude(category=2).order_by("-created")
    # yazilar = Post.objects.filter(category__in=[1,3]).order_by("-created")
    # yazilar = Post.objects.filter(published=True).exclude(category=1).order_by("-created")
    yazilar = Post.objects.filter(
        created__lt=datetime.datetime(2018, 11, 22, 15),
        created__gt=datetime.datetime(2018, 11, 22, 10)
    ).order_by("-created")
    return render(request, "anasayfa.html", {
        "gonderiler": yazilar
    })
