"""
URL configuration for countrydelight project.

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
from atexit import register
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app1 import views

# from app1 import views

urlpatterns = [
    path('',include('app1.urls')),
    path('admin/', admin.site.urls),
    path('register.html/register', views.register, name='register'),
    #  path('register/', register.as_view(), name='register'),

    # path('register.html',views.register),
    # path('accounts/',include('accounts.urls')),
]
# urlpatterns = urlpatterns + static(settings.MEDIA_URL,docment_root=settings.MEDIA_ROOT)