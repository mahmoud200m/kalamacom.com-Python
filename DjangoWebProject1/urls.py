"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    url(r'^home', 'app.views.home', name='home'),
    url(r'^get_twittes', 'app.views.get_twittes', name='get_twittes'),
    url(r'^contact', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^login', 'app.views.login_user', name='login'),
    url(r'^register', 'app.views.register', name='register'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
