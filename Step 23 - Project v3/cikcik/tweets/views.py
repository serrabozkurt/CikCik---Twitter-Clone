from django.views.generic import FormView, TemplateView, RedirectView
from django.contrib.auth import authenticate, login, logout

from tweets.forms import SignUpForm, SignInForm, TweetForm
from tweets.models import User, Tweet


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

    def get_context_data(self, **kwargs):
        context = super(Homepage, self).get_context_data(**kwargs)

        user = User.objects.get(id=self.request.user.id)
        context["timeline"] = Tweet.objects.filter(
            author__in=list(user.follows.all().values_list("id", flat=True)) + [user.id]
        ).order_by("-created")

        return context


class Profile(TemplateView):
    template_name = "profil.html"

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        user = User.objects.get(id=self.request.user.id)
        if "username" in kwargs:
            profile = User.objects.get(username=kwargs.get("username"))
            context["profile"] = profile
            context["follows"] = user.follows.filter(username=profile.username).exists()
        else:
            context["profile"] = user
        return context


class Follow(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user = User.objects.get(id=self.request.user.id)
        profile = User.objects.get(username=kwargs.get("username"))

        follows = user.follows.filter(username=profile.username).exists()

        if follows:
            user.follows.remove(profile)
        else:
            user.follows.add(profile)

        self.url = "/profil/" + profile.username

        return super(Follow, self).get_redirect_url(*args, *kwargs)


class SignOut(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        logout(self.request)
        return super(SignOut, self).get_redirect_url(*args, **kwargs)
