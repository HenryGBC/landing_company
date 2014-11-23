from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from landing.views import home, crear, PostsView, PostDetailView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'landing_company.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home, name="home"),
    url(r'^crear/', crear, name="crear"),
    url(r'^posts/', PostsView.as_view(), name='posts'),
    url(r'^post/(?P<slug>[-_\w]+)/$', PostDetailView.as_view(), name='post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
