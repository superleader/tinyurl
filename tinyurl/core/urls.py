from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from core.views import HomeView, URLDetailView, URLDetailByNameView, URLRedirectURLView


urlpatterns = patterns('',
   url(r'^$', HomeView.as_view(), name='home'),
   url(r'^!(?P<slug>[a-zA-Z0-9_\-]*)/$', URLDetailByNameView.as_view(),
       name='url-redirect'),
   url(r'^(?P<slug>[a-zA-Z0-9_\-]*)/$', URLRedirectURLView.as_view(),
       name='url-redirect'),
   url(r'^url/(?P<pk>\d+)/$', URLDetailView.as_view(), name='url-details'),
   #url(r'^mediabizbloggers/$', MediaBizBloggers.as_view(),
   #    name='mediabizbloggers'),

)
