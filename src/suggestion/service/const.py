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
Constants of the suggestion service.
"""

import string

from django.conf import settings

SERVICE_NAME_MAX_LENGTH = 64
SERVICE_NAME_CHARSET = string.lowercase + string.digits + '_#'
SERVICE_NAME_INVALID_MESSAGE = \
    'The service name must be between 1 and %d characters in [%s]' % (
        SERVICE_NAME_MAX_LENGTH, SERVICE_NAME_CHARSET)

TOKEN_MAX_LENGTH = 64
TOKEN_CHARSET = string.letters + string.digits

SNIPPET_MAX_LENGTH = 256

if settings.DEBUG:
  CACHE_EXPIRED_TIME_IN_SECONDS = 5
else:
  CACHE_EXPIRED_TIME_IN_SECONDS = 60
