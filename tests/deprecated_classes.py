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
HOOKS = [
    (
        "airflow.hooks.base.BaseHook",
        "airflow.hooks.base_hook.BaseHook",
    ),
    (
        'airflow.providers.apache.druid.hooks.druid.DruidHook',
        'airflow.hooks.druid_hook.DruidHook',
    ),
    (
        'airflow.providers.apache.druid.hooks.druid.DruidDbApiHook',
        'airflow.hooks.druid_hook.DruidDbApiHook',
    ),
    (
        'airflow.providers.apache.hdfs.hooks.hdfs.HDFSHookException',
        'airflow.hooks.hdfs_hook.HDFSHookException',
    ),
    (
        'airflow.providers.apache.hdfs.hooks.hdfs.HDFSHook',
        'airflow.hooks.hdfs_hook.HDFSHook',
    ),
    (
        'airflow.providers.apache.hive.hooks.hive.HiveMetastoreHook',
        'airflow.hooks.hive_hooks.HiveMetastoreHook',
    ),
    (
        'airflow.providers.apache.hive.hooks.hive.HiveCliHook',
        'airflow.hooks.hive_hooks.HiveCliHook',
    ),
    (
        'airflow.providers.apache.hive.hooks.hive.HiveServer2Hook',
        'airflow.hooks.hive_hooks.HiveServer2Hook',
    ),
    (
        'airflow.providers.apache.pig.hooks.pig.PigCliHook',
        'airflow.hooks.pig_hook.PigCliHook',
    ),
    (
        'airflow.providers.apache.hdfs.hooks.webhdfs.WebHDFSHook',
        'airflow.hooks.webhdfs_hook.WebHDFSHook',
    ),
    (
        'airflow.providers.docker.hooks.docker.DockerHook',
        'airflow.hooks.docker_hook.DockerHook',
    ),
    (
        'airflow.providers.microsoft.mssql.hooks.mssql.MsSqlHook',
        'airflow.hooks.mssql_hook.MsSqlHook',
    ),
    (
        'airflow.providers.mysql.hooks.mysql.MySqlHook',
        'airflow.hooks.mysql_hook.MySqlHook',
    ),
    (
        'airflow.providers.oracle.hooks.oracle.OracleHook',
        'airflow.hooks.oracle_hook.OracleHook',
    ),
    (
        'airflow.providers.postgres.hooks.postgres.PostgresHook',
        'airflow.hooks.postgres_hook.PostgresHook',
    ),
    (
        'airflow.providers.presto.hooks.presto.PrestoHook',
        'airflow.hooks.presto_hook.PrestoHook',
    ),
    (
        'airflow.providers.samba.hooks.samba.SambaHook',
        'airflow.hooks.samba_hook.SambaHook',
    ),
    (
        'airflow.providers.sqlite.hooks.sqlite.SqliteHook',
        'airflow.hooks.sqlite_hook.SqliteHook',
    ),
    (
        'airflow.providers.slack.hooks.slack.SlackHook',
        'airflow.hooks.slack_hook.SlackHook',
    ),
    (
        'airflow.providers.zendesk.hooks.zendesk.ZendeskHook',
        'airflow.hooks.zendesk_hook.ZendeskHook',
    ),
    (
        'airflow.providers.http.hooks.http.HttpHook',
        'airflow.hooks.http_hook.HttpHook',
    ),
    (
        'airflow.providers.jdbc.hooks.jdbc.JdbcHook',
        'airflow.hooks.jdbc_hook.JdbcHook',
    ),
    (
        "airflow.providers.atlassian.jira.hooks.jira.JiraHook",
        "airflow.providers.jira.hooks.jira.JiraHook",
    ),
]

OPERATORS = [
    (
        'airflow.providers.common.sql.operators.sql.SQLCheckOperator',
        'airflow.operators.druid_check_operator.DruidCheckOperator',
    ),
    (
        'airflow.providers.apache.hive.operators.hive.HiveOperator',
        'airflow.operators.hive_operator.HiveOperator',
    ),
    (
        'airflow.providers.apache.hive.operators.hive_stats.HiveStatsCollectionOperator',
        'airflow.operators.hive_stats_operator.HiveStatsCollectionOperator',
    ),
    (
        'airflow.providers.apache.pig.operators.pig.PigOperator',
        'airflow.operators.pig_operator.PigOperator',
    ),
    (
        'airflow.operators.branch.BaseBranchOperator',
        'airflow.operators.branch_operator.BaseBranchOperator',
    ),
    (
        'airflow.operators.bash.BashOperator',
        'airflow.operators.bash_operator.BashOperator',
    ),
    (
        'airflow.providers.docker.operators.docker.DockerOperator',
        'airflow.operators.docker_operator.DockerOperator',
    ),
    (
        'airflow.providers.microsoft.mssql.operators.mssql.MsSqlOperator',
        'airflow.operators.mssql_operator.MsSqlOperator',
    ),
    (
        'airflow.providers.mysql.operators.mysql.MySqlOperator',
        'airflow.operators.mysql_operator.MySqlOperator',
    ),
    (
        'airflow.providers.oracle.operators.oracle.OracleOperator',
        'airflow.operators.oracle_operator.OracleOperator',
    ),
    (
        'airflow.providers.papermill.operators.papermill.PapermillOperator',
        'airflow.operators.papermill_operator.PapermillOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLCheckOperator',
        'airflow.operators.presto_check_operator.PrestoCheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLIntervalCheckOperator',
        'airflow.operators.presto_check_operator.PrestoIntervalCheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLValueCheckOperator',
        'airflow.operators.presto_check_operator.PrestoValueCheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLCheckOperator',
        'airflow.operators.check_operator.CheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLIntervalCheckOperator',
        'airflow.operators.check_operator.IntervalCheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLValueCheckOperator',
        'airflow.operators.check_operator.ValueCheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.SQLThresholdCheckOperator',
        'airflow.operators.check_operator.ThresholdCheckOperator',
    ),
    (
        'airflow.providers.common.sql.operators.sql.BranchSQLOperator',
        'airflow.operators.sql_branch_operator.BranchSqlOperator',
    ),
    (
        'airflow.operators.python.BranchPythonOperator',
        'airflow.operators.python_operator.BranchPythonOperator',
    ),
    (
        'airflow.operators.python.PythonOperator',
        'airflow.operators.python_operator.PythonOperator',
    ),
    (
        'airflow.operators.python.ShortCircuitOperator',
        'airflow.operators.python_operator.ShortCircuitOperator',
    ),
    (
        'airflow.operators.python.PythonVirtualenvOperator',
        'airflow.operators.python_operator.PythonVirtualenvOperator',
    ),
    (
        'airflow.providers.sqlite.operators.sqlite.SqliteOperator',
        'airflow.operators.sqlite_operator.SqliteOperator',
    ),
    (
        'airflow.providers.slack.operators.slack.SlackAPIPostOperator',
        'airflow.operators.slack_operator.SlackAPIPostOperator',
    ),
    (
        'airflow.providers.slack.operators.slack.SlackAPIOperator',
        'airflow.operators.slack_operator.SlackAPIOperator',
    ),
    (
        'airflow.operators.email.EmailOperator',
        'airflow.operators.email_operator.EmailOperator',
    ),
    (
        'airflow.providers.http.operators.http.SimpleHttpOperator',
        'airflow.operators.http_operator.SimpleHttpOperator',
    ),
    (
        'airflow.providers.jdbc.operators.jdbc.JdbcOperator',
        'airflow.operators.jdbc_operator.JdbcOperator',
    ),
    (
        'airflow.providers.postgres.operators.postgres.PostgresOperator',
        'airflow.operators.postgres_operator.PostgresOperator',
    ),
    (
        "airflow.operators.latest_only.LatestOnlyOperator",
        "airflow.operators.latest_only_operator.LatestOnlyOperator",
    ),
    (
        "airflow.operators.trigger_dagrun.TriggerDagRunOperator",
        "airflow.operators.dagrun_operator.TriggerDagRunOperator",
    ),
    (
        "airflow.operators.subdag.SubDagOperator",
        "airflow.operators.subdag_operator.SubDagOperator",
    ),
    (
        "airflow.operators.empty.EmptyOperator",
        "airflow.operators.dummy_operator.DummyOperator",
    ),
    (
        "airflow.operators.empty.EmptyOperator",
        "airflow.operators.dummy.DummyOperator",
    ),
    (
        "airflow.providers.atlassian.jira.operators.jira.JiraOperator",
        "airflow.providers.jira.operators.jira.JiraOperator",
    ),
]

SENSORS = [
    (
        "airflow.sensors.base.BaseSensorOperator",
        "airflow.sensors.base_sensor_operator.BaseSensorOperator",
    ),
    (
        "airflow.sensors.date_time.DateTimeSensor",
        "airflow.sensors.date_time_sensor.DateTimeSensor",
    ),
    (
        "airflow.sensors.time_delta.TimeDeltaSensor",
        "airflow.sensors.time_delta_sensor.TimeDeltaSensor",
    ),
    (
        'airflow.providers.apache.hive.sensors.hive_partition.HivePartitionSensor',
        'airflow.sensors.hive_partition_sensor.HivePartitionSensor',
    ),
    (
        'airflow.providers.apache.hive.sensors.metastore_partition.MetastorePartitionSensor',
        'airflow.sensors.metastore_partition_sensor.MetastorePartitionSensor',
    ),
    (
        'airflow.providers.apache.hive.sensors.named_hive_partition.NamedHivePartitionSensor',
        'airflow.sensors.named_hive_partition_sensor.NamedHivePartitionSensor',
    ),
    (
        'airflow.providers.apache.hdfs.sensors.web_hdfs.WebHdfsSensor',
        'airflow.sensors.web_hdfs_sensor.WebHdfsSensor',
    ),
    (
        'airflow.providers.apache.hdfs.sensors.hdfs.HdfsSensor',
        'airflow.sensors.hdfs_sensor.HdfsSensor',
    ),
    (
        'airflow.providers.amazon.aws.sensors.s3.S3KeySensor',
        'airflow.sensors.s3_key_sensor.S3KeySensor',
    ),
    (
        'airflow.providers.http.sensors.http.HttpSensor',
        'airflow.sensors.http_sensor.HttpSensor',
    ),
    (
        "airflow.providers.atlassian.jira.sensors.jira.JiraSensor",
        "airflow.providers.jira.sensors.jira.JiraSensor",
    ),
    (
        "airflow.providers.atlassian.jira.sensors.jira.JiraTicketSensor",
        "airflow.providers.jira.sensors.jira.JiraTicketSensor",
    ),
]

TRANSFERS = [
    (
        'airflow.providers.amazon.aws.transfers.gcs_to_s3.GCSToS3Operator',
        'airflow.operators.gcs_to_s3.GCSToS3Operator',
    ),
    (
        'airflow.providers.amazon.aws.transfers.google_api_to_s3.GoogleApiToS3Operator',
        'airflow.operators.google_api_to_s3_transfer.GoogleApiToS3Transfer',
    ),
    (
        'airflow.providers.amazon.aws.transfers.redshift_to_s3.RedshiftToS3Operator',
        'airflow.operators.redshift_to_s3_operator.RedshiftToS3Transfer',
    ),
    (
        'airflow.providers.amazon.aws.transfers.s3_to_redshift.S3ToRedshiftOperator',
        'airflow.operators.s3_to_redshift_operator.S3ToRedshiftTransfer',
    ),
    (
        'airflow.providers.apache.druid.transfers.hive_to_druid.HiveToDruidOperator',
        'airflow.operators.hive_to_druid.HiveToDruidTransfer',
    ),
    (
        'airflow.providers.apache.hive.transfers.hive_to_mysql.HiveToMySqlOperator',
        'airflow.operators.hive_to_mysql.HiveToMySqlTransfer',
    ),
    (
        'airflow.providers.apache.hive.transfers.mysql_to_hive.MySqlToHiveOperator',
        'airflow.operators.mysql_to_hive.MySqlToHiveTransfer',
    ),
    (
        'airflow.providers.apache.hive.transfers.s3_to_hive.S3ToHiveOperator',
        'airflow.operators.s3_to_hive_operator.S3ToHiveTransfer',
    ),
    (
        'airflow.providers.apache.hive.transfers.hive_to_samba.HiveToSambaOperator',
        'airflow.operators.hive_to_samba_operator.HiveToSambaOperator',
    ),
    (
        'airflow.providers.apache.hive.transfers.mssql_to_hive.MsSqlToHiveOperator',
        'airflow.operators.mssql_to_hive.MsSqlToHiveTransfer',
    ),
    (
        'airflow.providers.mysql.transfers.presto_to_mysql.PrestoToMySqlOperator',
        'airflow.operators.presto_to_mysql.PrestoToMySqlTransfer',
    ),
]

LOGS = [
    (
        "airflow.providers.amazon.aws.log.s3_task_handler.S3TaskHandler",
        "airflow.utils.log.s3_task_handler.S3TaskHandler",
    ),
    (
        'airflow.providers.amazon.aws.log.cloudwatch_task_handler.CloudwatchTaskHandler',
        'airflow.utils.log.cloudwatch_task_handler.CloudwatchTaskHandler',
    ),
    (
        'airflow.providers.elasticsearch.log.es_task_handler.ElasticsearchTaskHandler',
        'airflow.utils.log.es_task_handler.ElasticsearchTaskHandler',
    ),
    (
        "airflow.providers.google.cloud.log.stackdriver_task_handler.StackdriverTaskHandler",
        "airflow.utils.log.stackdriver_task_handler.StackdriverTaskHandler",
    ),
    (
        "airflow.providers.google.cloud.log.gcs_task_handler.GCSTaskHandler",
        "airflow.utils.log.gcs_task_handler.GCSTaskHandler",
    ),
    (
        "airflow.providers.microsoft.azure.log.wasb_task_handler.WasbTaskHandler",
        "airflow.utils.log.wasb_task_handler.WasbTaskHandler",
    ),
]

ALL = HOOKS + OPERATORS + SENSORS + TRANSFERS + LOGS

RENAMED_ALL = [
    (old_class, new_class)
    for old_class, new_class in HOOKS + OPERATORS + SENSORS
    if old_class.rpartition(".")[2] != new_class.rpartition(".")[2]
]
