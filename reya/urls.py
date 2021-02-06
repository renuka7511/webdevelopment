"""reya URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from vidhyardi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',views.sample),
    path('center/',views.centerexample),
    path('paragraph/',views.paragraph),
    path('example/',views.example),
    path('stringvalue/<str:name>/',views.stringvalueex),
    path('inte/<int:num>/',views.inte),
    path('samplehtml/',views.samplehtmlex,name='samplehtmlex'),
    path('demo/',views.htmlcss,name='htmlcss'),
    path('rrr/',views.ex,name='ex'),
    path('bootex/',views.bootstrapex,name='boot'),
    path('loginpage/',views.login,name='login'),
    path('respage/',views.registration,name='res'),
    path('',include('CurdApp.urls')),
    path('forms/',include('app3.urls')),

]
