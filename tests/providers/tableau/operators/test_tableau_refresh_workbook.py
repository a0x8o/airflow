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

import warnings
from unittest.mock import Mock, patch

import pytest

from airflow.exceptions import AirflowException
from airflow.providers.tableau.hooks.tableau import TableauJobFinishCode

with warnings.catch_warnings():
    warnings.simplefilter("ignore", DeprecationWarning)
    from airflow.providers.tableau.operators.tableau_refresh_workbook import TableauRefreshWorkbookOperator


class TestTableauRefreshWorkbookOperator:
    """
    Test class for TableauRefreshWorkbookOperator
    """

    def setup_method(self):
        self.mocked_workbooks = []
        for i in range(3):
            mock_workbook = Mock()
            mock_workbook.id = i
            mock_workbook.name = f"wb_{i}"
            self.mocked_workbooks.append(mock_workbook)
        self.kwargs = {"site_id": "test_site", "task_id": "task", "dag": None, "check_interval": 1}

    @patch("airflow.providers.tableau.operators.tableau.TableauHook")
    def test_execute(self, mock_tableau_hook):
        mock_tableau_hook.get_all = Mock(return_value=self.mocked_workbooks)
        mock_tableau_hook.return_value.__enter__ = Mock(return_value=mock_tableau_hook)
        operator = TableauRefreshWorkbookOperator(blocking=False, workbook_name="wb_2", **self.kwargs)

        job_id = operator.execute(context={})

        mock_tableau_hook.server.workbooks.refresh.assert_called_once_with(2)
        assert mock_tableau_hook.server.workbooks.refresh.return_value.id == job_id

    @patch("airflow.providers.tableau.operators.tableau.TableauHook")
    def test_execute_blocking(self, mock_tableau_hook):
        mock_tableau_hook.get_all = Mock(return_value=self.mocked_workbooks)
        mock_tableau_hook.return_value.__enter__ = Mock(return_value=mock_tableau_hook)
        mock_tableau_hook.server.jobs.get_by_id = Mock(
            return_value=Mock(finish_code=TableauJobFinishCode.SUCCESS.value)
        )
        operator = TableauRefreshWorkbookOperator(workbook_name="wb_2", **self.kwargs)

        job_id = operator.execute(context={})

        mock_tableau_hook.server.workbooks.refresh.assert_called_once_with(2)
        assert mock_tableau_hook.server.workbooks.refresh.return_value.id == job_id
        mock_tableau_hook.wait_for_state.assert_called_once_with(
            job_id=job_id, check_interval=1, target_state=TableauJobFinishCode.SUCCESS
        )

    @patch("airflow.providers.tableau.operators.tableau.TableauHook")
    def test_execute_missing_workbook(self, mock_tableau_hook):
        mock_tableau_hook.get_all = Mock(return_value=self.mocked_workbooks)
        mock_tableau_hook.return_value.__enter__ = Mock(return_value=mock_tableau_hook)
        operator = TableauRefreshWorkbookOperator(workbook_name="test", **self.kwargs)

        with pytest.raises(AirflowException):
            operator.execute({})
