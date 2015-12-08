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
Views (More specifically, the API methods) that handle http requests.
"""

from suggestion.service import algorithms
from suggestion.service import controllers as service_controllers
from suggestion.utils.decorators import api, get, post
from suggestion.utils.response import api_response, success_response
from suggestion.utils.validators import require_fields

@api
@post
def create_service(request):
  params = request.POST
  require_fields(params, ('service'))
  service = service_controllers.create_service(params['service'])
  return api_response(service.token)


@api
@post
def create_snippet(request):
  params = request.POST
  require_fields(params, ('service', 'snippet', 'token'))
  snippet = service_controllers.create_snippet(
      params['service'], params['snippet'], params['token'])
  return success_response()


@api
@post
def delete_service(request):
  params = request.POST
  require_fields(params, ('service', 'token'))
  service_controllers.delete_service(params['service'], params['token'])
  return success_response()


@api
@post
def delete_snippet(request):
  params = request.POST
  require_fields(params, ('service', 'snippet', 'token'))
  service_controllers.delete_snippet(
      params['service'], params['snippet'], params['token'])
  return success_response()


@api
@get
def query(request):
  params = request.GET
  require_fields(params, ('service', 'query', ('max_count', int)))
  result = algorithms.query(
      params['service'], params['query'], int(params['max_count']))
  return api_response(result)
