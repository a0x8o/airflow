#
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
from __future__ import annotations

import pytest

from airflow.providers.google.cloud.example_dags.example_datafusion import BUCKET_1, BUCKET_2
from tests.providers.google.cloud.utils.gcp_authenticator import GCP_DATAFUSION_KEY
from tests.test_utils.gcp_system_helpers import CLOUD_DAG_FOLDER, GoogleSystemTest, provide_gcp_context


@pytest.mark.backend("mysql", "postgres")
@pytest.mark.credential_file(GCP_DATAFUSION_KEY)
class TestCloudDataFusionExampleDagsSystem(GoogleSystemTest):
    def setup_method(self) -> None:
        self.create_gcs_bucket(name=BUCKET_1)
        self.create_gcs_bucket(name=BUCKET_2)

    def teardown_method(self) -> None:
        self.delete_gcs_bucket(name=BUCKET_1)
        self.delete_gcs_bucket(name=BUCKET_2)

    @provide_gcp_context(GCP_DATAFUSION_KEY)
    def test_run_example_dag_function(self):
        self.run_dag("example_data_fusion", CLOUD_DAG_FOLDER)
