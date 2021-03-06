"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^$", views.HomePage.as_view(), name="home"),
    url(r"^start/$", views.LoginPage.as_view(), name="start"),
    url(r"^end/$", views.LogoutPage.as_view(), name="end"),
    url(r"^accounts/", include(("accounts.urls","accounts"), namespace="accounts")),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    #url(r"^blog/", include(("blog.urls","blog"), namespace="blog")),
    #url(r"^blog/", include("django.contrib.auth.urls")),
    url(r"^projects/", include(("my_projects.urls", "my_projects"), namespace="my_projects")),
    url(r"^projects/", include("django.contrib.auth.urls")),
    url(r"^me/", include(("whoami.urls", "whoami"), namespace="whoami")),
    url(r"^me/", include("django.contrib.auth.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)