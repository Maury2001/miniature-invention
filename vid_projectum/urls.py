"""
URL configuration for vid_projectum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Vidz import views as vidz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', vidz_views.Home, name='home'),
    path('register/', vidz_views.userReg, name='register'),
    path('login/', vidz_views.userLog, name='login'),
    path('video/<str:pk>/', vidz_views.video, name='video'),
    path('video_form/', vidz_views.videoForm, name='video_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)