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

# A fast deployment script which install the packages in default locations.
# Super privilege might be required.

ROOT_DIR=$(cd .. && pwd)
BASE_DIR=$ROOT_DIR/src/suggestion

InstallRequirements() {
  apt-get install python-pip memcached
  pip install -r $ROOT_DIR/deploy/requirements
}

GenSecret() {
  secret="$(< /dev/urandom tr -dc A-Z-a-z-0-9\!\@\#\$\%\^\& | head -c${1:-64})"
  echo "SECRET_KEY = \""$secret"\"" > $BASE_DIR/common/secret.py
}

MigrateData() {
  python $BASE_DIR/manage.py migrate
}

Main() {
  InstallRequirements
  GenSecret
  MigrateData
}

Main
