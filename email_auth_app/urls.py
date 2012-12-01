from django.conf.urls import patterns, url

from email_auth_app import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
