# swagger_client.WorkflowsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workflows_create**](WorkflowsApi.md#workflows_create) | **POST** /api/workflows/ | 
[**workflows_delete**](WorkflowsApi.md#workflows_delete) | **DELETE** /api/workflows/{id}/ | 
[**workflows_generate**](WorkflowsApi.md#workflows_generate) | **GET** /api/workflows/{id}/generate/ | 
[**workflows_list**](WorkflowsApi.md#workflows_list) | **GET** /api/workflows/ | 
[**workflows_partial_update**](WorkflowsApi.md#workflows_partial_update) | **PATCH** /api/workflows/{id}/ | 
[**workflows_read**](WorkflowsApi.md#workflows_read) | **GET** /api/workflows/{id}/ | 
[**workflows_update**](WorkflowsApi.md#workflows_update) | **PUT** /api/workflows/{id}/ | 


# **workflows_create**
> workflows_create(data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
data = swagger_client.Data9() # Data9 |  (optional)

try:
    api_instance.workflows_create(data=data)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data9**](Data9.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_delete**
> workflows_delete(id, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)

try:
    api_instance.workflows_delete(id, name=name)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_generate**
> workflows_generate(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
id = 56 # int | A unique integer value identifying this workflow.

try:
    api_instance.workflows_generate(id)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_list**
> workflows_list(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
name = 'name_example' # str |  (optional)

try:
    api_instance.workflows_list(name=name)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_partial_update**
> workflows_partial_update(id, name=name, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)
data = swagger_client.Data11() # Data11 |  (optional)

try:
    api_instance.workflows_partial_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data11**](Data11.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_read**
> workflows_read(id, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)

try:
    api_instance.workflows_read(id, name=name)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows_update**
> workflows_update(id, name=name, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowsApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)
data = swagger_client.Data10() # Data10 |  (optional)

try:
    api_instance.workflows_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling WorkflowsApi->workflows_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data10**](Data10.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

