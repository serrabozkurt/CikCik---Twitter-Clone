from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth import authenticate, login, logout

from posts.forms import PostForm, LoginForm
from posts.models import Post


# RedirectView araştırma ödevi :)

# Bu fonksiyonu kullanmıyoruz. Yerine aşağıdaki yöntemi öğrendik!
def anasayfa(request):
    return render(request, "anasayfa.html")


class Homepage(TemplateView):
    template_name = "anasayfa.html"


class NewPost(FormView):
    template_name = "ekle.html"
    form_class = PostForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
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
