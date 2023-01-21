from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post


def ekle(request):
    return render(request, "ekle.html", {
        "form": PostForm()
    })


def kaydet(request):
    Post.objects.create(
        title=request.POST["title"],
        content=request.POST["content"]
    )
    return redirect('/')


def anasayfa(request):
    return render(request, "anasayfa.html", {
        "gonderiler": Post.objects.all().order_by('title')
    })
