from django.conf.urls import patterns, include, url
from django.contrib import admin
from activity_server.views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', HomeView.as_view()))
