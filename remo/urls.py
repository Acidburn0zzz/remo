from django.conf import settings
from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from funfactory.monkeypatches import patch
patch()

handler404 = 'remo.base.views.custom_404'
handler500 = 'remo.base.views.custom_500'
robots_txt = 'remo.base.views.robots_txt'

admin.autodiscover()

urlpatterns = patterns('',
    # 'me' urls
    url(r'^me/$', 'remo.profiles.views.view_my_profile',
        name='profiles_view_my_profile'),
    url(r'^me/currentreport/$', 'remo.reports.views.current_report',
        name='reports_view_current_report'),
    url(r'^me/currentreport/edit/$', 'remo.reports.views.current_report',
        dict({'edit': True}), name='reports_edit_current_report'),

    # profiles
    url(r'^u/', include('remo.profiles.user_urls')),
    url(r'^people/', include('remo.profiles.people_urls')),

    # events
    url(r'^e/', include('remo.events.e_urls')),
    url(r'^events/', include('remo.events.event_urls')),

    # reports
    url(r'^reports/', include('remo.reports.report_urls')),

    # featuredrep
    url(r'^featured/', include('remo.featuredrep.urls')),

    # custom browserid
    url(r'', include('remo.base.urls')),

    # API
    url(r'^api/', include('remo.api.urls')),

    url(r'^', include('remo.base.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # Voting
    url(r'^voting/', include('remo.voting.voting_urls')),
    url(r'^v/', include('remo.voting.v_urls')),

    # Generate a robots.txt
    (r'^robots\.txt$', robots_txt),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^404/$', handler404, name='404'),
        url(r'^500/$', handler500, name='500'))
    urlpatterns += staticfiles_urlpatterns()
