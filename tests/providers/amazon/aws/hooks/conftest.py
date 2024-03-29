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

import boto3
import pytest
from moto import mock_s3


@pytest.fixture
def mocked_s3_res():
    with mock_s3():
        yield boto3.resource("s3")


@pytest.fixture
def s3_bucket(mocked_s3_res):
    bucket = "airflow-test-s3-bucket"
    mocked_s3_res.create_bucket(Bucket=bucket)
    return bucket
