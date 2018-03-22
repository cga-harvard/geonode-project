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
import os
from geonode.settings import *

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = '%s/{{ project_name }}/uploaded/' % PROJECT_ROOT
STATIC_ROOT = '%s/{{ project_name }}/static_root' % PROJECT_ROOT

# SECRET_KEY = '************************'
# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', "{{ secret_key }}")

# per-deployment settings should go here
SITE_HOST_NAME = os.getenv('SITE_HOST_NAME', "localhost")
SITE_HOST_PORT = os.getenv('SITE_HOST_PORT', "8000")
SITEURL = os.getenv('SITEURL', "http://%s:%s/" % (SITE_HOST_NAME, SITE_HOST_PORT))

#
# General Django development settings
#

#Define email service on GeoNode
EMAIL_ENABLE = True

if EMAIL_ENABLE:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.zju.edu.cn'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'camp2018@zju.edu.cn'
    EMAIL_HOST_PASSWORD = ''
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'camp2018@zju.edu.cn'


POSTGIS_VERSION = (2, 0, 7)

PG_USERNAME = os.getenv('PG_USERNAME', "worldmap")
PG_PASSWORD = os.getenv('PG_PASSWORD', "worldmap")
PG_WORLDMAP_DJANGO_DB = os.getenv('PG_WORLDMAP_DJANGO_DB', "worldmap")
PG_WORLDMAP_UPLOADS_DB = os.getenv('PG_WORLDMAP_UPLOADS_DB', "wmdata")

DATABASES = {
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'worldmap',
         'USER': 'worldmap',
         'PASSWORD': 'worldmap',
         'HOST' : 'localhost',
         'PORT' : '5432',
         'CONN_TOUT': 900,
     },
    # vector datastore for uploads
    'wmdata' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'wmdata',
        'USER' : 'worldmap',
        'PASSWORD' : 'worldmap',
        'HOST' : 'localhost',
        'PORT' : '5432',
        'CONN_TOUT': 900,
    }
}

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
)

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://localhost:8080/geoserver/'
)

GEOSERVER_PUBLIC_HOST = os.getenv(
    'GEOSERVER_PUBLIC_HOST', SITE_HOST_NAME
)

GEOSERVER_PUBLIC_PORT = os.getenv(
    'GEOSERVER_PUBLIC_PORT', 8080
)

GEOSERVER_PUBLIC_LOCATION = os.getenv(
    'GEOSERVER_PUBLIC_LOCATION', 'http://{}:{}/geoserver/'.format(GEOSERVER_PUBLIC_HOST, GEOSERVER_PUBLIC_PORT)
)

OGC_SERVER_DEFAULT_USER = os.getenv(
    'GEOSERVER_ADMIN_USER', 'admin'
)

OGC_SERVER_DEFAULT_PASSWORD = os.getenv(
    'GEOSERVER_ADMIN_PASSWORD', 'geoserver'
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER': OGC_SERVER_DEFAULT_USER,
        'PASSWORD': OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOFENCE_SECURITY_ENABLED': True,
        'GEOGIG_ENABLED': False,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        'LOG_FILE': '/home/geosolutions/work/logs/geoserver.log',
        # Set to dictionary identifier of database containing spatial data in
        # DATABASES dictionary to enable
        'DATASTORE': 'wmdata',
        'PG_GEOGIG': False,
        'TIMEOUT': 30  # number of seconds to allow for HTTP requests
    }
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%s/catalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
        'ALTERNATES_ONLY': True,
    }
}

# pycsw settings
PYCSW = {
    # pycsw configuration
    'CONFIGURATION': {
        # uncomment / adjust to override server config system defaults
        # 'server': {
        #    'maxrecords': '10',
        #    'pretty_print': 'true',
        #    'federatedcatalogues': 'http://catalog.data.gov/csw'
        # },
        'metadata:main': {
            'identification_title': 'GeoNode Catalogue',
            'identification_abstract': 'GeoNode is an open source platform' \
            ' that facilitates the creation, sharing, and collaborative use' \
            ' of geospatial data',
            'identification_keywords': 'sdi, catalogue, discovery, metadata,' \
            ' GeoNode',
            'identification_keywords_type': 'theme',
            'identification_fees': 'None',
            'identification_accessconstraints': 'None',
            'provider_name': 'Organization Name',
            'provider_url': SITEURL,
            'contact_name': 'Lastname, Firstname',
            'contact_position': 'Position Title',
            'contact_address': 'Mailing Address',
            'contact_city': 'City',
            'contact_stateorprovince': 'Administrative Area',
            'contact_postalcode': 'Zip or Postal Code',
            'contact_country': 'Country',
            'contact_phone': '+xx-xxx-xxx-xxxx',
            'contact_fax': '+xx-xxx-xxx-xxxx',
            'contact_email': 'Email Address',
            'contact_url': 'Contact URL',
            'contact_hours': 'Hours of Service',
            'contact_instructions': 'During hours of service. Off on ' \
            'weekends.',
            'contact_role': 'pointOfContact',
        },
        'metadata:inspire': {
            'enabled': 'true',
            'languages_supported': 'eng,gre',
            'default_language': 'eng',
            'date': 'YYYY-MM-DD',
            'gemet_keywords': 'Utility and governmental services',
            'conformity_service': 'notEvaluated',
            'contact_name': 'Organization Name',
            'contact_email': 'Email Address',
            'temp_extent': 'YYYY-MM-DD/YYYY-MM-DD',
        }
    }
}

# If you want to enable Mosaics use the following configuration
UPLOADER = {
    'BACKEND': 'geonode.rest',
    # 'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': True,
        'MOSAIC_ENABLED': False,
        'GEOGIG_ENABLED': False,
    },
    'SUPPORTED_CRS': [
        'EPSG:4326',
        'EPSG:3785',
        'EPSG:3857',
        'EPSG:900913',
        'EPSG:32647',
        'EPSG:32736'
    ]
}


### WorldMap Settings ###
USE_WORLDMAP = strtobool(os.getenv('USE_WORLDMAP', 'True'))
# USE_WORLDMAP = False
if USE_WORLDMAP:
    # for now we remove CsrfViewMiddleware, which creates failures on x-csrftoken
    # We need to fix this
    # TODO Niran: do not remove csrf considering of that choosing language in base.html need use csrfs    
    MIDDLEWARE_CLASSES = (
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'pagination.middleware.PaginationMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'oauth2_provider.middleware.OAuth2TokenMiddleware',
    )

    INSTALLED_APPS += (
            'geonode.contrib.worldmap.gazetteer',
            'geonode.contrib.worldmap.queue',
            'geonode.contrib.worldmap.wm_extra',
            'geonode.contrib.createlayer',
        )

    HYPERMAP_REGISTRY_URL = os.getenv('HYPERMAP_REGISTRY_URL', 'http://localhost:8001')
    SOLR_URL = os.getenv('SOLR_URL', 'http://localhost:8983/solr/hypermap/select/')
    MAPPROXY_URL = os.getenv('MAPPROXY_URL', 'http://localhost:8001')

    # Other settings
    GEONODE_CLIENT_LOCATION = '/static/worldmap/worldmap_client/'
    USE_GAZETTEER = True
    GAZETTEER_DB_ALIAS = 'wmdata'
    GAZETTEER_FULLTEXTSEARCH = False
    USE_CUSTOM_ORG_AUTHORIZATION = True
    CUSTOM_ORG_AUTH_TEXT = 'Are you affiliated with Harvard University?'
    # Uncomment following line if debugging GeoExplorer static files
    # GEONODE_CLIENT_LOCATION = 'http://localhost:9090/'
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')


ALLOWED_HOSTS = ['localhost', 'amap.zju.edu.cn', ]
