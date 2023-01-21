from django.views.generic import FormView

from tweets.forms import SignUpForm
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
