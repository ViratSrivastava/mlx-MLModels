# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# coding: utf-8

"""
    MLX API

    MLX API Extension for Kubeflow Pipelines  # noqa: E501

    OpenAPI spec version: 0.1.25-related-assets
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.models.api_parameter import ApiParameter  # noqa: F401,E501


class ApiPipeline(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'created_at': 'datetime',
        'name': 'str',
        'description': 'str',
        'parameters': 'list[ApiParameter]',
        'status': 'str',
        'default_version_id': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'name': 'name',
        'description': 'description',
        'parameters': 'parameters',
        'status': 'status',
        'default_version_id': 'default_version_id',
        'namespace': 'namespace'
    }

    def __init__(self, id=None, created_at=None, name=None, description=None, parameters=None, status=None, default_version_id=None, namespace=None):  # noqa: E501
        """ApiPipeline - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created_at = None
        self._name = None
        self._description = None
        self._parameters = None
        self._status = None
        self._default_version_id = None
        self._namespace = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if parameters is not None:
            self.parameters = parameters
        if status is not None:
            self.status = status
        if default_version_id is not None:
            self.default_version_id = default_version_id
        if namespace is not None:
            self.namespace = namespace

    @property
    def id(self):
        """Gets the id of this ApiPipeline.  # noqa: E501


        :return: The id of this ApiPipeline.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiPipeline.


        :param id: The id of this ApiPipeline.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this ApiPipeline.  # noqa: E501


        :return: The created_at of this ApiPipeline.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiPipeline.


        :param created_at: The created_at of this ApiPipeline.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this ApiPipeline.  # noqa: E501


        :return: The name of this ApiPipeline.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiPipeline.


        :param name: The name of this ApiPipeline.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ApiPipeline.  # noqa: E501


        :return: The description of this ApiPipeline.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApiPipeline.


        :param description: The description of this ApiPipeline.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def parameters(self):
        """Gets the parameters of this ApiPipeline.  # noqa: E501


        :return: The parameters of this ApiPipeline.  # noqa: E501
        :rtype: list[ApiParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ApiPipeline.


        :param parameters: The parameters of this ApiPipeline.  # noqa: E501
        :type: list[ApiParameter]
        """

        self._parameters = parameters

    @property
    def status(self):
        """Gets the status of this ApiPipeline.  # noqa: E501

        In case any error happens retrieving a pipeline field, only pipeline ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501

        :return: The status of this ApiPipeline.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ApiPipeline.

        In case any error happens retrieving a pipeline field, only pipeline ID and the error message is returned. Client has the flexibility of choosing how to handle error. This is especially useful during listing call.  # noqa: E501

        :param status: The status of this ApiPipeline.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def default_version_id(self):
        """Gets the default_version_id of this ApiPipeline.  # noqa: E501

        The default version of the pipeline. As of now, the latest version is used as default. (In the future, if desired by customers, we can allow them to set default version.)  # noqa: E501

        :return: The default_version_id of this ApiPipeline.  # noqa: E501
        :rtype: str
        """
        return self._default_version_id

    @default_version_id.setter
    def default_version_id(self, default_version_id):
        """Sets the default_version_id of this ApiPipeline.

        The default version of the pipeline. As of now, the latest version is used as default. (In the future, if desired by customers, we can allow them to set default version.)  # noqa: E501

        :param default_version_id: The default_version_id of this ApiPipeline.  # noqa: E501
        :type: str
        """

        self._default_version_id = default_version_id

    @property
    def namespace(self):
        """Gets the namespace of this ApiPipeline.  # noqa: E501


        :return: The namespace of this ApiPipeline.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ApiPipeline.


        :param namespace: The namespace of this ApiPipeline.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApiPipeline, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiPipeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
