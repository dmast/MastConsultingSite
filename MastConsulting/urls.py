from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo_project.views.home', name='home'),
    # url(r'^demo_project/', include('demo_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^$', direct_to_template, {'template': 'index.html'}, "home"),
    (r'^contact$', direct_to_template, {'template': 'contact.html'}, "contact"),
    (r'^form$', 'MastConsulting.views.demo_form'),
    (r'^form_template$', 'MastConsulting.views.demo_form_with_template'),
    (r'^form_inline$', 'MastConsulting.views.demo_form_inline'),
    (r'^tabs$', 'MastConsulting.views.demo_tabs', {}, "tabs"),
    (r'^pagination$', 'MastConsulting.views.demo_pagination', {}, "pagination"),
    (r'^widgets$', 'MastConsulting.views.demo_widgets', {}, "widgets"),
)
urlpatterns += staticfiles_urlpatterns()
