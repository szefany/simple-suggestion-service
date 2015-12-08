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
Utils for validation.
"""

from suggestion.utils.exceptions import ValidationError

def require_fields(params, required_list):
  for item in required_list:
    if isinstance(item, tuple):
      key = item[0]
      Type = item[1]
    else:
      key = item
      Type = unicode
    if key not in params:
      raise ValidationError('The required key [%s] not found.' % key)
    try:
      Type(params[key])
    except ValueError:
      raise ValidationError('The required key [%s] must be %s.' % (key, Type))


def validator_with_message(function):
  def _decorated_validator(*args, **kwargs):
    if function(*args, **kwargs):
      return True
    if error:
      raise ValidationError(error)
    raise 'Invalid field: %s' % kwargs.get('field_name')
  return _decorated_validator


@validator_with_message
def validate_length(param, min_length, max_length, error=None, field_name=None):
  if not error:
    error = 'The %s must be between %d and %d characters.' % (
        field_name or 'param', min_length, max_length)
  length = len(param)
  return min_length <= length and length <= max_length


@validator_with_message
def validate_charset(param, charset, error=None, field_name=None):
  if not error:
    error = 'The %s must consist of [%s].' % (field_name or 'param', charset)
  for char in param:
    if char not in charset:
      return False
  return True
