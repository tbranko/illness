from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from illness.views import IllnessDetailView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'boljka_project.views.home', name='home'),
    url(r'i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += i18n_patterns('',
    url(r'^search/', include('haystack.urls')),
    url(r'^(?P<slug>[\w-]+)/$', IllnessDetailView.as_view(), name='illness_detail_view')
)
