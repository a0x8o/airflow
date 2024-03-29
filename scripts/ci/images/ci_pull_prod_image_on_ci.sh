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

export VERBOSE="true"

# shellcheck source=scripts/ci/libraries/_script_init.sh
. "$( dirname "${BASH_SOURCE[0]}" )/../libraries/_script_init.sh"

# Pulls prepared  PROD image in the CI environment
function pull_prod_images_on_ci() {
    build_images::prepare_prod_build
    start_end::group_start "Pull PROD image ${AIRFLOW_PROD_IMAGE}"
    build_images::clean_build_cache
    local image_name_with_tag="${AIRFLOW_PROD_IMAGE}:${GITHUB_REGISTRY_PULL_IMAGE_TAG}"
    push_pull_remove_images::wait_for_image "${image_name_with_tag}"
    docker_v tag  "${image_name_with_tag}" "${AIRFLOW_PROD_IMAGE}"
    start_end::group_end
}

pull_prod_images_on_ci
