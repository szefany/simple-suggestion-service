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
Models and some handler related to validation.
"""

import random
import string

from django.db import models
from django.db.models import signals
from suggestion.service import const
from suggestion.utils import gen_random_string, validators

class Snippet(models.Model):
  content = models.CharField(unique=True, max_length=const.SNIPPET_MAX_LENGTH)

  class Meta:
    db_table = 'snippet'


class Service(models.Model):
  name = models.CharField(unique=True, max_length=const.SERVICE_NAME_MAX_LENGTH)
  token = models.CharField(
    unique=True,
    blank=True,
    null=True,
    max_length=const.TOKEN_MAX_LENGTH)
  snippets = models.ManyToManyField(Snippet, db_table='service_snippet')

  class Meta:
    db_table = 'service'


def _add_token(sender, instance, created, **kwargs):
  if created:
    instance.token = gen_random_string(
        const.TOKEN_CHARSET, const.TOKEN_MAX_LENGTH)
    instance.save()
signals.post_save.connect(_add_token, sender=Service)


def _validate_service_before_save(sender, instance, **kwargs):
  validators.validate_length(
      instance.name, 1, const.SERVICE_NAME_MAX_LENGTH,
      error=const.SERVICE_NAME_INVALID_MESSAGE)
  validators.validate_charset(
      instance.name, const.SERVICE_NAME_CHARSET,
      error=const.SERVICE_NAME_INVALID_MESSAGE)
signals.pre_save.connect(_validate_service_before_save, sender=Service)


def _validate_snippet_before_save(sender, instance, **kwargs):
  validators.validate_length(
      instance.content, 1, const.SNIPPET_MAX_LENGTH, field_name='Snippet')
signals.pre_save.connect(_validate_snippet_before_save, sender=Snippet)
