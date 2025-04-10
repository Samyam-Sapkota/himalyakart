"""
URL configuration for main project.

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
from django.urls import path,include
from .views import home,profile_views,about_project
from contact_us.views import contact_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home_view"),
    path('store/',include('store.urls')),
    path('cart/',include('cart_app.urls')),
    path('contact/',contact_views,name='contact'),
    path('auth/',include("all_auth.urls")),
    path('profile/',profile_views,name="profile_views"),
    path('about/',about_project,name="about_project"),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
