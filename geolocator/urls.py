from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
	# (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'geolocator.views.home', name='home'),
	url(r'^location/(?P<loc_id>.*)/$', 'locations.views.single_location', name='single_location'),
)


if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
