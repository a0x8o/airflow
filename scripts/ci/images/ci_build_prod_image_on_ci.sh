#!/usr/bin/env bash
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

export INSTALL_FROM_PYPI="false"
export INSTALL_PROVIDERS_FROM_SOURCES="false"
export INSTALL_FROM_DOCKER_CONTEXT_FILES="true"
export AIRFLOW_PRE_CACHED_PIP_PACKAGES="false"
export VERBOSE="true"

# shellcheck source=scripts/ci/libraries/_script_init.sh
. "$( dirname "${BASH_SOURCE[0]}" )/../libraries/_script_init.sh"

# Builds or waits for the PROD image in the CI environment
function build_prod_images_on_ci() {
    build_images::prepare_prod_build
    start_end::group_start "Build PROD image ${AIRFLOW_CI_IMAGE}"
    build_images::clean_build_cache
    build_images::build_prod_images_from_locally_built_airflow_packages
    start_end::group_end
}

build_prod_images_on_ci
