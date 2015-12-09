#!/bin/bash
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

DEFAULT_PORT=9216

ROOT_DIR=$(cd .. && pwd)
BASE_DIR=$ROOT_DIR/src/suggestion

RunServer() {
  python $BASE_DIR/manage.py runserver 0.0.0.0:$1
}

Main() {
  if (( $# > 0 )); then
    port=$1
  else
    port=$DEFAULT_PORT
  fi

  RunServer $port
}

Main $*
