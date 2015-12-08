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
Decorators related to the request handlers.
"""

import traceback

from suggestion.utils.exceptions import get_error_code, BadRequest
from suggestion.utils.response import api_response

def api(function):
  def _decorated_view(request, *args, **kwargs):
    try:
      return function(request, *args, **kwargs)
    except Exception as e:
      message = unicode(e)
      code = get_error_code(e)
      if code / 100 == 5:
        print traceback.format_exc()
      return api_response(message, code)
  return _decorated_view


def get(function):
  def _decorated_view(request, *args, **kwargs):
    if request.method != 'GET':
      raise BadRequest('The request method must be GET.')
    return function(request, *args, **kwargs)
  return _decorated_view


def post(function):
  def _decorated_view(request, *args, **kwargs):
    if request.method != 'POST':
      raise BadRequest('The request method must be POST.')
    return function(request, *args, **kwargs)
  return _decorated_view
