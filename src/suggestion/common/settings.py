#!/usr/bin/env python2.7
# coding: utf-8
#
# Copyright 2015 Sifan Weng (szefany@gmail.com). All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The main settings of the django project.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_DIR = os.path.dirname(BASE_DIR)
ROOT_DIR = os.path.dirname(SRC_DIR)
RUN_DIR = os.path.join(ROOT_DIR, 'run')

sys.path.append(SRC_DIR)

from secret import SECRET_KEY

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'suggestion.service',
)
MIDDLEWARE_CLASSES = ()

ROOT_URLCONF = 'common.urls'
WSGI_APPLICATION = 'common.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(RUN_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

LANGUAGE_CODE = 'en-us'
