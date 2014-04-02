from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mesosphere.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls, app_name='admin')),
    url(r'^blog/', include('mesoblog.urls', app_name='mesoblog')),
) + static("media/", document_root="media/")


