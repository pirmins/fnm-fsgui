from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", include("fsgui.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    # path('', TemplateView.as_view(template_name="home.html"), name="home"),
    # Needs to stay at bottom for "login" override (there's a fix to do it right somehow/probably)
]
