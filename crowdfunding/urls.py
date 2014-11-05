from django.conf.urls import patterns, include, url
from django.contrib import admin

from .main.views import IndexView, ProjectDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^project/(?P<pk>\d+)/$', ProjectDetailView.as_view(), name="project-detail"),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
