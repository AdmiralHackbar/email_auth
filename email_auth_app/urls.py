from django.conf.urls import patterns, url

from email_auth_app import views

urlpatterns = patterns('',
    url(r'^login/', views.login_view, name='login_view'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^create_user/', views.create_user, name='create_user'),
    url(r'^login_token/', views.login_token, name='login_token'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^$', views.index, name='index')
)
