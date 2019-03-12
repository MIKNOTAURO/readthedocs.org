# pylint: disable=missing-docstring
import debug_toolbar
from .urls import *
from readthedocs.overriding_behave import views
from allauth.account.views import login
# from django.contrib.auth import views as auth_views

if getattr(settings, 'DEBUG', False):
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^soporte/$', login, name='login-rtd'),
        url(r'^accounts/login/$', views.login_sso, name='login-sso'),

    ] + urlpatterns
