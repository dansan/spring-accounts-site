from django.conf.urls import patterns, include, url
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^openid/login/$', 'django_openid_auth.views.login_begin', name='openid-login', kwargs={"template_name": "openid_login.html"}),
    url(r'^openid/complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^openid/logo.gif$', 'django_openid_auth.views.logo', name='openid-logo'),
    url(r'^logout/$', views.logout_view),
    url(r'^ajax_modal_add_player/$', views.ajax_modal_add_player, name="ajax_modal_add_player"),
)
