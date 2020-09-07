"""fusionmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from django.urls import path, include

apis = [
    path("accounts/", include("accounts.api.urls")),
    path("appointments/", include("appointments.api.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(apis)),
    path('', TemplateView.as_view(template_name="langing_page.html")),
    path('prontuario/', TemplateView.as_view(template_name="prontuario.html")),
    path("api-auth/", include("rest_framework.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
