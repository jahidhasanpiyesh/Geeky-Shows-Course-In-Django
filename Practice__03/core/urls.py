"""
URL configuration for core project.

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
from django.urls import path

# ----------------Multiple App inpurt in date or Functions ----------------
# --------------First Way -----------------
from homeapp import views as first
from homeapp2 import views as second

# ----------------Second way -----------------------
from homeapp.views import homeapp
from homeapp2.views import homeapp2


urlpatterns = [
    path('admin/', admin.site.urls),

    # Defiend First Way In Code
    path('first/', first.homeapp),
    path('second/', second.homeapp2),

    # second way in code
        path('f/',homeapp),
        path('ff/',homeapp2),



]
