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

import io
import unittest

import boto3
from moto import mock_s3

from airflow.exceptions import AirflowException
from airflow.providers.amazon.aws.operators.s3 import S3DeleteObjectsOperator


class TestS3DeleteObjectsOperator(unittest.TestCase):
    @mock_s3
    def test_s3_delete_single_object(self):
        bucket = "testbucket"
        key = "path/data.txt"

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        conn.upload_fileobj(Bucket=bucket, Key=key, Fileobj=io.BytesIO(b"input"))

        # The object should be detected before the DELETE action is taken
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=key)
        assert len(objects_in_dest_bucket['Contents']) == 1
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key

        op = S3DeleteObjectsOperator(task_id="test_task_s3_delete_single_object", bucket=bucket, keys=key)
        op.execute(None)

        # There should be no object found in the bucket created earlier
        assert 'Contents' not in conn.list_objects(Bucket=bucket, Prefix=key)

    @mock_s3
    def test_s3_delete_multiple_objects(self):
        bucket = "testbucket"
        key_pattern = "path/data"
        n_keys = 3
        keys = [key_pattern + str(i) for i in range(n_keys)]

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        for k in keys:
            conn.upload_fileobj(Bucket=bucket, Key=k, Fileobj=io.BytesIO(b"input"))

        # The objects should be detected before the DELETE action is taken
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=key_pattern)
        assert len(objects_in_dest_bucket['Contents']) == n_keys
        assert sorted(x['Key'] for x in objects_in_dest_bucket['Contents']) == sorted(keys)

        op = S3DeleteObjectsOperator(task_id="test_task_s3_delete_multiple_objects", bucket=bucket, keys=keys)
        op.execute(None)

        # There should be no object found in the bucket created earlier
        assert 'Contents' not in conn.list_objects(Bucket=bucket, Prefix=key_pattern)

    @mock_s3
    def test_s3_delete_prefix(self):
        bucket = "testbucket"
        key_pattern = "path/data"
        n_keys = 3
        keys = [key_pattern + str(i) for i in range(n_keys)]

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        for k in keys:
            conn.upload_fileobj(Bucket=bucket, Key=k, Fileobj=io.BytesIO(b"input"))

        # The objects should be detected before the DELETE action is taken
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=key_pattern)
        assert len(objects_in_dest_bucket['Contents']) == n_keys
        assert sorted(x['Key'] for x in objects_in_dest_bucket['Contents']) == sorted(keys)

        op = S3DeleteObjectsOperator(task_id="test_task_s3_delete_prefix", bucket=bucket, prefix=key_pattern)
        op.execute(None)

        # There should be no object found in the bucket created earlier
        assert 'Contents' not in conn.list_objects(Bucket=bucket, Prefix=key_pattern)

    @mock_s3
    def test_s3_delete_empty_list(self):
        bucket = "testbucket"
        key_of_test = "path/data.txt"
        keys = []

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        conn.upload_fileobj(Bucket=bucket, Key=key_of_test, Fileobj=io.BytesIO(b"input"))

        # The object should be detected before the DELETE action is tested
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=key_of_test)
        assert len(objects_in_dest_bucket['Contents']) == 1
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key_of_test

        op = S3DeleteObjectsOperator(task_id="test_s3_delete_empty_list", bucket=bucket, keys=keys)
        op.execute(None)

        # The object found in the bucket created earlier should still be there
        assert len(objects_in_dest_bucket['Contents']) == 1
        # the object found should be consistent with dest_key specified earlier
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key_of_test

    @mock_s3
    def test_s3_delete_empty_string(self):
        bucket = "testbucket"
        key_of_test = "path/data.txt"
        keys = ""

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        conn.upload_fileobj(Bucket=bucket, Key=key_of_test, Fileobj=io.BytesIO(b"input"))

        # The object should be detected before the DELETE action is tested
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=key_of_test)
        assert len(objects_in_dest_bucket['Contents']) == 1
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key_of_test

        op = S3DeleteObjectsOperator(task_id="test_s3_delete_empty_string", bucket=bucket, keys=keys)
        op.execute(None)

        # The object found in the bucket created earlier should still be there
        assert len(objects_in_dest_bucket['Contents']) == 1
        # the object found should be consistent with dest_key specified earlier
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key_of_test

    @mock_s3
    def test_assert_s3_both_keys_and_prifix_given(self):
        bucket = "testbucket"
        keys = "path/data.txt"
        key_pattern = "path/data"

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        conn.upload_fileobj(Bucket=bucket, Key=keys, Fileobj=io.BytesIO(b"input"))

        # The object should be detected before the DELETE action is tested
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=keys)
        assert len(objects_in_dest_bucket['Contents']) == 1
        assert objects_in_dest_bucket['Contents'][0]['Key'] == keys
        with self.assertRaises(AirflowException):
            op = S3DeleteObjectsOperator(
                task_id="test_assert_s3_both_keys_and_prifix_given",
                bucket=bucket,
                keys=keys,
                prefix=key_pattern,
            )
            op.execute(None)

        # The object found in the bucket created earlier should still be there
        assert len(objects_in_dest_bucket['Contents']) == 1
        # the object found should be consistent with dest_key specified earlier
        assert objects_in_dest_bucket['Contents'][0]['Key'] == keys

    @mock_s3
    def test_assert_s3_no_keys_or_prifix_given(self):
        bucket = "testbucket"
        key_of_test = "path/data.txt"

        conn = boto3.client('s3')
        conn.create_bucket(Bucket=bucket)
        conn.upload_fileobj(Bucket=bucket, Key=key_of_test, Fileobj=io.BytesIO(b"input"))

        # The object should be detected before the DELETE action is tested
        objects_in_dest_bucket = conn.list_objects(Bucket=bucket, Prefix=key_of_test)
        assert len(objects_in_dest_bucket['Contents']) == 1
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key_of_test
        with self.assertRaises(AirflowException):
            op = S3DeleteObjectsOperator(task_id="test_assert_s3_no_keys_or_prifix_given", bucket=bucket)
            op.execute(None)
        # The object found in the bucket created earlier should still be there
        assert len(objects_in_dest_bucket['Contents']) == 1
        # the object found should be consistent with dest_key specified earlier
        assert objects_in_dest_bucket['Contents'][0]['Key'] == key_of_test
