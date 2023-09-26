"""
URL configuration for WorkshopApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from WorkshopApp import views_vuln
from WorkshopApp import views_main
from WorkshopApp import views_fixed

urlpatterns = [
    path('', views_main.hello_world),
    path('sqli', views_vuln.sqli),
    path('xss', views_vuln.xss),
    path('forgery', views_vuln.request_forgery),
    path('sqli/fixed', views_fixed.sqli),
    path('xss/fixed', views_fixed.xss),
    path('forgery/fixed', views_fixed.request_forgery)
]
