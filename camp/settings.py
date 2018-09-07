# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import ast
import os
from urlparse import urlparse, urlunparse
# Load more settings from a file called local_settings.py if it exists
try:
    from camp.local_settings import *
#    from geonode.local_settings import *
except ImportError:
    from geonode.settings import *

PROJECT_NAME = 'camp'
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)

# # Location of url mappings
ROOT_URLCONF = os.getenv('ROOT_URLCONF', '{}.urls'.format(PROJECT_NAME))
MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(LOCAL_ROOT, "uploaded"))
STATIC_ROOT = os.getenv('STATIC_ROOT',
                         os.path.join(LOCAL_ROOT, "static_root")
                         )

# Additional directories which hold static files
STATICFILES_DIRS.append(
     os.path.join(LOCAL_ROOT, "static"),
)

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
) + LOCALE_PATHS

TEMPLATES[0]['DIRS'].insert(0, os.path.join(LOCAL_ROOT, "templates"))
loaders = TEMPLATES[0]['OPTIONS'].get('loaders') or ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader']
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]['OPTIONS']['loaders'] = loaders
TEMPLATES[0].pop('APP_DIRS', None)

if PROJECT_NAME not in INSTALLED_APPS:
     INSTALLED_APPS += (
        PROJECT_NAME,
        # additional apps for worldmap
        # 'geonode.contrib.datastore_shards',
        # 'debug_toolbar',
     )

############################################
# other settings specific to WorldMap CAMP #
############################################

ACCOUNT_APPROVAL_REQUIRED = False

# add custom baselayers here
WM_BASELAYERS = [
    {
        "source": {"ptype": "gxp_stamensource"},
        "name": "watercolor",
        "visibility": False,
        "group": "background",
        "title": "Stamen Watercolor"
    },
    {
        "source": {"ptype": "gxp_stamensource"},
        "name": "toner",
        "visibility": False,
        "group": "background",
        "title": "Stamen Toner"
    },
]

MAP_BASELAYERS.extend(WM_BASELAYERS)

# disable for now csrf - we need to implement it when wfst
MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'dj_pagination.middleware.PaginationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)
