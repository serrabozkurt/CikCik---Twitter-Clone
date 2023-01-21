from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator

from posts.forms import PostForm, LoginForm
from posts.models import Post


# RedirectView araştırma ödevi :)

# Bu fonksiyonu kullanmıyoruz. Yerine aşağıdaki yöntemi öğrendik!
def anasayfa(request):
    return render(request, "anasayfa.html")


class Homepage(TemplateView):
    template_name = "sablon.html"

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)
        # posts = Post.yayinlanmis.filter(category=1)
        posts = Post.yayinlanmis.all()
        paginator = Paginator(posts, 3)
        sayfa = self.request.GET.get("sayfa", 1)
        context["posts"] = paginator.get_page(sayfa)
        return context


class NewPost(FormView):
    template_name = "ekle.html"
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        send_mail("Blog'da yeni yazı!", "Yeni yazı yazıldı", "onur@ari24.com",
                  ["onur@ari24.com"])
        if form.cleaned_data["published"]:
            messages.add_message(self.request, messages.SUCCESS,
                                 "Yazı başarıyla yayınlandı.")
        else:
            messages.warning(self.request, "Yazı taslak olarak kaydedildi.")

        return super(NewPost, self).form_valid(form)


class Login(FormView):
    template_name = "giris.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            if "next" in self.request.GET:
                self.success_url = self.request.GET["next"]
            return super(Login, self).form_valid(form)
        else:
            return super(Login, self).form_invalid(form)


def cikis(request):
    logout(request)
    return redirect('/')
