"""cikcik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from tweets.views import SignUp, SignIn, SignOut, Homepage, Profile, Follow

urlpatterns = [
    path('', Homepage.as_view()),
    path('profil/', Profile.as_view()),
    path('profil/<str:username>', Profile.as_view(), name="profil"),
    path('takip/<str:username>', Follow.as_view(), name="takip"),
    path('kayit/', SignUp.as_view(), name="kayit"),
    path('giris/', SignIn.as_view(), name="giris"),
    path('cikis/', SignOut.as_view(), name="cikis"),
    path('admin/', admin.site.urls),
] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
