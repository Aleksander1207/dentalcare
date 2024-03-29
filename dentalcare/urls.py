"""dentalcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from dentalcareapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/dentists/$', views.dentists_list),
    re_path(r'^api/dentists/([0-9])$', views.dentists_detail),
    re_path(r'^api/patients/$', views.patients_list),
    re_path(r'^api/patients/([0-9])$', views.patients_detail),
    re_path(r'^api/appointments/$', views.appointments_list),
    re_path(r'^api/appointments/([0-9])$', views.appointments_detail),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
