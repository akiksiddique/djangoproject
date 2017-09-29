from django.conf.urls import include, url
from django.contrib import admin
from app.views import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^admin/', include(admin.site.urls)),
]
