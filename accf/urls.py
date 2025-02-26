"""
URL configuration for accf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from website.media_admin import media_admin_site
from website.bible_study_admin import bible_study_admin_site
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('media-admin/', media_admin_site.urls),
    path('bible-study-admin/', bible_study_admin_site.urls),
    path('',include('website.urls')),
]