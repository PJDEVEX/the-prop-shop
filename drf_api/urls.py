from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from accounts import urls as accounts_urls

urlpatterns = [
    # Admin panel
    path("admin/", admin.site.urls),
    # Django Rest Framework auth
    path("api-auth/", include("rest_framework.urls")),
    # Uncomment the line below if you want to include a custom HTML template
    # path("", TemplateView.as_view(template_name="index.html")),
    # Social auth - drf_social_oauth2
    re_path("api-auth/", include('drf_social_oauth2.urls', namespace='drf')),
    # Accounts views
    path("api-auth/", include("accounts.urls")),
]
