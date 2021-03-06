# coding: utf-8

"""
    Workflower API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class CreatorApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def results_create(self, **kwargs):  # noqa: E501
        """results_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_create(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.results_create_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.results_create_with_http_info(**kwargs)  # noqa: E501
            return data

    def results_create_with_http_info(self, **kwargs):  # noqa: E501
        """results_create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_create_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Data data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_create" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creator/results/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def results_delete(self, id, **kwargs):  # noqa: E501
        """results_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.results_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.results_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def results_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """results_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'workflow', 'salted_hash', 'successful', 'date_created']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `results_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'workflow' in params:
            query_params.append(('workflow', params['workflow']))  # noqa: E501
        if 'salted_hash' in params:
            query_params.append(('salted_hash', params['salted_hash']))  # noqa: E501
        if 'successful' in params:
            query_params.append(('successful', params['successful']))  # noqa: E501
        if 'date_created' in params:
            query_params.append(('date_created', params['date_created']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creator/results/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def results_list(self, **kwargs):  # noqa: E501
        """results_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.results_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.results_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def results_list_with_http_info(self, **kwargs):  # noqa: E501
        """results_list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workflow', 'salted_hash', 'successful', 'date_created']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'workflow' in params:
            query_params.append(('workflow', params['workflow']))  # noqa: E501
        if 'salted_hash' in params:
            query_params.append(('salted_hash', params['salted_hash']))  # noqa: E501
        if 'successful' in params:
            query_params.append(('successful', params['successful']))  # noqa: E501
        if 'date_created' in params:
            query_params.append(('date_created', params['date_created']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creator/results/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def results_partial_update(self, id, **kwargs):  # noqa: E501
        """results_partial_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_partial_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :param Data2 data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.results_partial_update_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.results_partial_update_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def results_partial_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """results_partial_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_partial_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :param Data2 data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'workflow', 'salted_hash', 'successful', 'date_created', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_partial_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `results_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'workflow' in params:
            query_params.append(('workflow', params['workflow']))  # noqa: E501
        if 'salted_hash' in params:
            query_params.append(('salted_hash', params['salted_hash']))  # noqa: E501
        if 'successful' in params:
            query_params.append(('successful', params['successful']))  # noqa: E501
        if 'date_created' in params:
            query_params.append(('date_created', params['date_created']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creator/results/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def results_read(self, id, **kwargs):  # noqa: E501
        """results_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.results_read_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.results_read_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def results_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """results_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'workflow', 'salted_hash', 'successful', 'date_created']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `results_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'workflow' in params:
            query_params.append(('workflow', params['workflow']))  # noqa: E501
        if 'salted_hash' in params:
            query_params.append(('salted_hash', params['salted_hash']))  # noqa: E501
        if 'successful' in params:
            query_params.append(('successful', params['successful']))  # noqa: E501
        if 'date_created' in params:
            query_params.append(('date_created', params['date_created']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creator/results/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def results_update(self, id, **kwargs):  # noqa: E501
        """results_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_update(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :param Data1 data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.results_update_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.results_update_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def results_update_with_http_info(self, id, **kwargs):  # noqa: E501
        """results_update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.results_update_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this successful workflow gen. (required)
        :param str workflow: 
        :param str salted_hash: 
        :param str successful: 
        :param str date_created: 
        :param Data1 data:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'workflow', 'salted_hash', 'successful', 'date_created', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method results_update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `results_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'workflow' in params:
            query_params.append(('workflow', params['workflow']))  # noqa: E501
        if 'salted_hash' in params:
            query_params.append(('salted_hash', params['salted_hash']))  # noqa: E501
        if 'successful' in params:
            query_params.append(('successful', params['successful']))  # noqa: E501
        if 'date_created' in params:
            query_params.append(('date_created', params['date_created']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/creator/results/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
