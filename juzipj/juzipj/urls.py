"""juzipj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from juzipj1 import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/',views.ntime),
    url(r'year/(\d{4})$',views.year),    #匹配一个变动的url,用正则。
    url(r'year/(\d{4})/(\d{2})$',views.month),
    url(r'year/(?P<year>\d{4})/(?P<month>\d{2})$',views.days),
    url(r'^register/',views.register,name='reg'),
]
