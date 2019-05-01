# coding: utf-8

"""
    Workflower API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Data11(object):
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
        'name': 'str',
        'task_filename': 'str'
    }

    attribute_map = {
        'name': 'name',
        'task_filename': 'task_filename'
    }

    def __init__(self, name=None, task_filename=None):  # noqa: E501
        """Data11 - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._task_filename = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if task_filename is not None:
            self.task_filename = task_filename

    @property
    def name(self):
        """Gets the name of this Data11.  # noqa: E501

          # noqa: E501

        :return: The name of this Data11.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data11.

          # noqa: E501

        :param name: The name of this Data11.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def task_filename(self):
        """Gets the task_filename of this Data11.  # noqa: E501

          # noqa: E501

        :return: The task_filename of this Data11.  # noqa: E501
        :rtype: str
        """
        return self._task_filename

    @task_filename.setter
    def task_filename(self, task_filename):
        """Sets the task_filename of this Data11.

          # noqa: E501

        :param task_filename: The task_filename of this Data11.  # noqa: E501
        :type: str
        """

        self._task_filename = task_filename

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
        if issubclass(Data11, dict):
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
        if not isinstance(other, Data11):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
