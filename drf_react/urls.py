"""drf_react URL Configuration

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
from django.views.generic import TemplateView

import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^api/', include('api.urls')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    
    # for serve media file when debug false https://groups.google.com/forum/#!topic/django-oscar/CiujM572GuU
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
]

"""
if not settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
"""

"""
if settings.DEBUG:
    urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', TemplateView.as_view(template_name='index.html')),
        url(r'^api/', include('api.urls')),
        url(r'^auth/', include('rest_framework_social_oauth2.urls')),
        url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    ]
"""