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
Controllers of the suggestion models.
"""

from django.db.utils import IntegrityError
from suggestion.service.models import Service, Snippet
from suggestion.utils.exceptions import ValidationError, PermissionDenied

def get_service(service_name):
  try:
    return Service.objects.get(name=service_name)
  except Service.DoesNotExist:
    raise ValidationError('Service not found: %s' % service_name)


def get_service_and_validate_permission(service_name, token):
  service = get_service(service_name)
  if service.token != token:
    raise PermissionDenied('Invalid token.')
  return service


def get_snippet(content):
  try:
    return Snippet.objects.get(content=content)
  except Snippet.DoesNotExist:
    raise ValidationError('Snippet not found: %s' % content)


def create_service(service_name):
  try:
    return Service.objects.create(name=service_name)
  except IntegrityError:
    raise ValidationError('Service has been registered: %s' % service_name)


def create_snippet(service_name, snippet_content, token):
  service = get_service_and_validate_permission(service_name, token)
  snippet = Snippet.objects.get_or_create(content=snippet_content)[0]
  service.snippets.add(snippet)
  return snippet


def delete_service(service_name, token):
  service = get_service_and_validate_permission(service_name, token)
  service.snippets.clear()
  service.delete()


def delete_snippet(service_name, snippet_content, token):
  service = get_service_and_validate_permission(service_name, token)
  snippet = get_snippet(content=snippet_content)
  service.snippets.remove(snippet)
