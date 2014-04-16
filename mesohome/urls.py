from django.conf.urls import patterns, url

from mesohome import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

