/*!
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import axios from 'axios';
import { useQuery } from 'react-query';
import { getMetaValue } from '../../utils';

const extraLinksUrl = getMetaValue('extra_links_url');

export default function useExtraLinks({
  dagId, taskId, executionDate, extraLinks,
}) {
  return useQuery(
    ['extraLinks', dagId, taskId, executionDate],
    async () => {
      const data = await Promise.all(extraLinks.map(async (link) => {
        const url = `${extraLinksUrl
        }?task_id=${encodeURIComponent(taskId)
        }&dag_id=${encodeURIComponent(dagId)
        }&execution_date=${encodeURIComponent(executionDate)
        }&link_name=${encodeURIComponent(link)}`;
        try {
          const datum = await axios.get(url);
          return {
            name: link,
            url: datum.url,
          };
        } catch (e) {
          console.error(e);
          return {
            name: link,
            url: '',
          };
        }
      }));
      return data;
    },
  );
}
