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
The suggestion algorithms with memcache.
"""

from django.core.cache import cache
from suggestion.service import const
from suggestion.service.models import Service
from suggestion.utils.exceptions import ValidationError

class Node(object):
  children = None
  end = None

  def __init__(self):
    self.children = {}
    self.end = False


class Trie(object):
  root = None

  def __init__(self, word_list=None):
    self.root = Node()
    if word_list:
      self.build(word_list)

  def query(self, prefix, max_count=10):
    node = self.root
    for key in prefix:
      if key not in node.children:
        return []
      node = node.children[key]
    result = []
    self._search_words_in_subtree(node, max_count, list(prefix), result)
    return result

  def build(self, word_list):
    for word in word_list:
      self._insert(word)

  def _insert(self, word):
    node = self.root
    for key in word:
      if key not in node.children:
        node.children[key] = Node()
      node = node.children[key]
    node.end = True

  def _search_words_in_subtree(self, node, remain, char_list, result):
    if remain == 0:
      return
    found = 0
    if node.end:
      result.append(''.join(char_list))
      remain -= 1
      found += 1

    for key, child in node.children.iteritems():
      if remain == 0:
        break
      char_list.append(key)
      child_found = self._search_words_in_subtree(
          child, remain, char_list, result)
      found += child_found
      remain -= child_found
      char_list.pop()
    return found


def query(service_name, query, max_count):
  tree = cache.get(service_name)
  if not tree:
    service = Service.objects.prefetch_related().get(name=service_name)
    snippets = service.snippets.all().values_list('content', flat=True)
    tree = Trie(snippets)
    cache.set(service_name, tree, const.CACHE_EXPIRED_TIME_IN_SECONDS)
  return tree.query(query, max_count)


def create_tree(service_name):
  cache.set(service_name, Trie(), const.CACHE_EXPIRED_TIME_IN_SECONDS)
