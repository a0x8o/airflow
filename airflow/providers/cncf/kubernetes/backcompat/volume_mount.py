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
"""Classes for interacting with Kubernetes API"""
from __future__ import annotations

import warnings

from kubernetes.client import models as k8s

warnings.warn(
    "This module is deprecated. Please use `kubernetes.client.models.V1VolumeMount`.",
    DeprecationWarning,
    stacklevel=2,
)


class VolumeMount:
    """Backward compatible VolumeMount"""

    __slots__ = ("name", "mount_path", "sub_path", "read_only")

    def __init__(self, name, mount_path, sub_path, read_only):
        """
        Initialize a Kubernetes Volume Mount. Used to mount pod level volumes to
        running container.

        :param name: the name of the volume mount
        :param mount_path:
        :param sub_path: subpath within the volume mount
        :param read_only: whether to access pod with read-only mode
        """
        self.name = name
        self.mount_path = mount_path
        self.sub_path = sub_path
        self.read_only = read_only

    def to_k8s_client_obj(self) -> k8s.V1VolumeMount:
        """
        Converts to k8s object.

        :return: Volume Mount k8s object
        """
        return k8s.V1VolumeMount(
            name=self.name, mount_path=self.mount_path, sub_path=self.sub_path, read_only=self.read_only
        )
