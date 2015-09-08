
from django.conf.urls import patterns, include, url
from django.contrib import admin

from api.views import manifest

urlpatterns = patterns(
    '',
    url(r'^api/manifests/(?P<manifest_id>[0-9]+)/$', manifest),
    url(r'^admin/', include(admin.site.urls)),

)
