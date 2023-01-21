from django.shortcuts import render, redirect

from posts.models import Post

def form(request):
    return render(request, "form.html")


def kaydet(request):
    baslik = request.POST.get("baslik")
    icerik = request.POST.get("icerik")

    gonderi = Post.objects.create(title=baslik, content=icerik)
    return redirect('/')


def listele(request):
    gonderiler = Post.objects.all()
    return render(request, "listele.html", {
        "gonderiler": gonderiler
    })
