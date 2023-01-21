from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate, login

from tweets.forms import SignUpForm, SignInForm, TweetForm
from tweets.models import User


class SignUp(FormView):
    template_name = "kayit.html"
    form_class = SignUpForm
    success_url = "/"

    def form_valid(self, form):
        kullanici = User.objects.create(
            username=form.cleaned_data.get("username"),
            first_name=form.cleaned_data.get("first_name"),
            last_name=form.cleaned_data.get("last_name"),
            email=form.cleaned_data.get("email")
        )
        kullanici.set_password(form.cleaned_data.get("password"))
        kullanici.save()
        return super(SignUp, self).form_valid(form)


class SignIn(FormView):
    template_name = "giris.html"
    form_class = SignInForm
    success_url = "/"

    def form_valid(self, form):
        user = authenticate(
            self.request,
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password")
        )
        if user is not None:
            login(self.request, user)
            return super(SignIn, self).form_valid(form)
        else:
            return super(SignIn, self).form_invalid(form)


class Homepage(FormView):
    template_name = "anasayfa.html"
    form_class = TweetForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = User.objects.get(id=self.request.user.id)
        form.save()
        return super(Homepage, self).form_valid(form)


class Profile(TemplateView):
    template_name = "profil.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        if "username" in kwargs:
            context["profile"] = User.objects.get(username=kwargs.get("username"))
        else:
            context["profile"] = User.objects.get(id=self.request.user.id)
        return context
