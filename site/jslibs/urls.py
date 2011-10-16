from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jslibs.views.home', name='home'),
    # url(r'^jslibs/', include('jslibs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^(?:' + '|'.join(settings.NON_LIBRARY_PATHS) + ')(?:/.*)?$', 'django.views.defaults.page_not_found'),
    url(r'^~(?P<name>[a-zA-Z0-9$_][a-zA-Z0-9_!$%&()*+,\-.:;=^_`{|}]*)', include('jsuser.urls')),
    url(r'^(?P<name>[a-zA-Z0-9$_][a-zA-Z0-9_!$%&()*+,\-.:;=^_`{|}]*)', include('libraries.urls')),
)
