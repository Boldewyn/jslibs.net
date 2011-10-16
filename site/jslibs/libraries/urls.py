from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('libraries.views',
    url(r'^$', 'detail'),
)

