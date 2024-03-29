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
# shellcheck source=scripts/ci/libraries/_script_init.sh
. "$( dirname "${BASH_SOURCE[0]}" )/../libraries/_script_init.sh"

# Pushes empty PROD images with tags to registry in GitHub to stop waiting. They will fail validation
# And whole job will fail
function push_prod_image_with_tag_to_github () {
    start_end::group_start "Prepare and push empty PROD images"
    docker_v build -t "${AIRFLOW_PROD_IMAGE}" - <<EOF
FROM scratch
EOF
    local airflow_prod_tagged_image="${AIRFLOW_PROD_IMAGE}:${GITHUB_REGISTRY_PUSH_IMAGE_TAG}"
    docker_v tag "${AIRFLOW_PROD_IMAGE}" "${airflow_prod_tagged_image}"
    push_pull_remove_images::push_image_with_retries "${airflow_prod_tagged_image}"
    start_end::group_end
}

build_images::prepare_prod_build

build_images::login_to_docker_registry

push_prod_image_with_tag_to_github
