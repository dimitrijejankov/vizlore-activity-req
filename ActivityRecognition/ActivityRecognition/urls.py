from django.conf.urls import patterns, url
from django.contrib import admin
from activity_server.views import HomeView
from activity_server.rest_view import RestView

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^ac/$', RestView.as_view()),
                       url(r'^$', HomeView.as_view()))
