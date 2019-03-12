"""Production desk settings, including local_settings, if present."""
from __future__ import absolute_import
import os

from .base import CommunityBaseSettings


class CommunityProdSettings(CommunityBaseSettings):
    """Settings for desktop production"""
    PRODUCTION_DOMAIN = 'localhost:8000'
    WEBSOCKET_HOST = 'localhost:8088'

    ROOT_URLCONF = 'readthedocs.fork_urls'

    # @property
    # def DATABASES(self):  # noqa
    #     return {
    #         'default': {
    #             'ENGINE': 'django.db.backends.sqlite3',
    #             'NAME': os.path.join(self.SITE_ROOT, 'dev2.db'),
    #         }
    #     }

    @property
    def DATABASES(self):  # noqa
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'rtd_local',
                'USER': 'miknotauro',
                'PASSWORD': 'miksaing',
                'HOST': 'localhost',
                'PORT': ''
            }
        }

    @property
    def INSTALLED_APPS(self):
        apps = super(CommunityProdSettings, self).INSTALLED_APPS
        apps.append('debug_toolbar',)
        apps.append('readthedocs.overriding_behave',)
        return apps

    @property
    def MIDDLEWARE(self):
        middleware = super(CommunityProdSettings, self).MIDDLEWARE
        middleware += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
        return middleware

    @property
    def INTERNAL_IPS(self):
        internal_ips = super(CommunityProdSettings, self).INTERNAL_IPS
        internal_ips += ('localhost',)
        return internal_ips

    DONT_HIT_DB = False

    ACCOUNT_EMAIL_VERIFICATION = 'none'
    # SESSION_COOKIE_DOMAIN = None
    SESSION_COOKIE_DOMAIN = "localhost"
    CACHE_BACKEND = 'dummy://'

    SLUMBER_USERNAME = 'api_user'
    SLUMBER_PASSWORD = 'test'  # noqa: ignore dodgy check
    SLUMBER_API_HOST = 'http://127.0.0.1:8000'
    PUBLIC_API_URL = 'http://127.0.0.1:8000'
    # PUBLIC_API_URL = 'http://{0}'.format(PRODUCTION_DOMAIN)

    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ALWAYS_EAGER = True
    CELERY_TASK_IGNORE_RESULT = False

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    FILE_SYNCER = 'readthedocs.builds.syncers.LocalSyncer'

    # For testing locally. Put this in your /etc/hosts:
    # 127.0.0.1 test
    # and navigate to http://test:8000
    CORS_ORIGIN_WHITELIST = (
        'test:8000',
    )

    @property
    def LOGGING(self):  # noqa - avoid pep8 N802
        logging = super(CommunityProdSettings, self).LOGGING
        logging['formatters']['default']['format'] = '[%(asctime)s] ' + self.LOG_FORMAT
        # Allow Sphinx and other tools to create loggers
        logging['disable_existing_loggers'] = False
        return logging

    DOCKER_ENABLE = False
    DOCKER_IMAGE = 'readthedocs/build:3.0'

    ALLOW_PRIVATE_REPOS = True
    DEFAULT_PRIVACY_LEVEL = 'private'

    SERVE_DOCS = ['private']

    """
    Nunca se ocupa el backend de guardian por los otros 2 backends que se tienen configurados,
    por eso es irrelevante ponerlo en el settings.
    """
    # @property
    # def AUTHENTICATION_BACKENDS(self):
    #     authentication_backends = super(CommunityProdSettings, self).AUTHENTICATION_BACKENDS
    #     authentication_backends += ('guardian.backends.ObjectPermissionBackend',)
    #     return authentication_backends

    SECRET_KEY = '$uug$y086tj)(pa!4$jy!^w)hjfasb+)v9+u3an4-$)0g@a%55'

    TIME_ZONE = 'America/Mexico_City'
    LANGUAGE_CODE = 'es-MX'

    # Overriding Behave Settings
    # ADMIN_SERVER_BASE_URL = 'http://sso.atlas.ti:8000'
    ADMIN_SERVER_BASE_URL = 'http://localhost:8200'


CommunityProdSettings.load_settings(__name__)
