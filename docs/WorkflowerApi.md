# swagger_client.WorkflowerApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parameters_create**](WorkflowerApi.md#parameters_create) | **POST** /api/workflower/parameters/ | 
[**parameters_delete**](WorkflowerApi.md#parameters_delete) | **DELETE** /api/workflower/parameters/{id}/ | 
[**parameters_list**](WorkflowerApi.md#parameters_list) | **GET** /api/workflower/parameters/ | 
[**parameters_partial_update**](WorkflowerApi.md#parameters_partial_update) | **PATCH** /api/workflower/parameters/{id}/ | 
[**parameters_read**](WorkflowerApi.md#parameters_read) | **GET** /api/workflower/parameters/{id}/ | 
[**parameters_update**](WorkflowerApi.md#parameters_update) | **PUT** /api/workflower/parameters/{id}/ | 
[**targets_create**](WorkflowerApi.md#targets_create) | **POST** /api/workflower/targets/ | 
[**targets_delete**](WorkflowerApi.md#targets_delete) | **DELETE** /api/workflower/targets/{id}/ | 
[**targets_list**](WorkflowerApi.md#targets_list) | **GET** /api/workflower/targets/ | 
[**targets_partial_update**](WorkflowerApi.md#targets_partial_update) | **PATCH** /api/workflower/targets/{id}/ | 
[**targets_read**](WorkflowerApi.md#targets_read) | **GET** /api/workflower/targets/{id}/ | 
[**targets_update**](WorkflowerApi.md#targets_update) | **PUT** /api/workflower/targets/{id}/ | 
[**tasks_create**](WorkflowerApi.md#tasks_create) | **POST** /api/workflower/tasks/ | 
[**tasks_delete**](WorkflowerApi.md#tasks_delete) | **DELETE** /api/workflower/tasks/{id}/ | 
[**tasks_list**](WorkflowerApi.md#tasks_list) | **GET** /api/workflower/tasks/ | 
[**tasks_partial_update**](WorkflowerApi.md#tasks_partial_update) | **PATCH** /api/workflower/tasks/{id}/ | 
[**tasks_read**](WorkflowerApi.md#tasks_read) | **GET** /api/workflower/tasks/{id}/ | 
[**tasks_update**](WorkflowerApi.md#tasks_update) | **PUT** /api/workflower/tasks/{id}/ | 
[**workflows_create**](WorkflowerApi.md#workflows_create) | **POST** /api/workflower/workflows/ | 
[**workflows_delete**](WorkflowerApi.md#workflows_delete) | **DELETE** /api/workflower/workflows/{id}/ | 
[**workflows_generate**](WorkflowerApi.md#workflows_generate) | **GET** /api/workflower/workflows/{id}/generate/ | 
[**workflows_list**](WorkflowerApi.md#workflows_list) | **GET** /api/workflower/workflows/ | 
[**workflows_partial_update**](WorkflowerApi.md#workflows_partial_update) | **PATCH** /api/workflower/workflows/{id}/ | 
[**workflows_read**](WorkflowerApi.md#workflows_read) | **GET** /api/workflower/workflows/{id}/ | 
[**workflows_update**](WorkflowerApi.md#workflows_update) | **PUT** /api/workflower/workflows/{id}/ | 


# **parameters_create**
> parameters_create(data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
data = swagger_client.Data3() # Data3 |  (optional)

try:
    api_instance.parameters_create(data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->parameters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data3**](Data3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_delete**
> parameters_delete(id, name=name, type=type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    api_instance.parameters_delete(id, name=name, type=type)
except ApiException as e:
    print("Exception when calling WorkflowerApi->parameters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this parameter template. | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_list**
> parameters_list(name=name, type=type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    api_instance.parameters_list(name=name, type=type)
except ApiException as e:
    print("Exception when calling WorkflowerApi->parameters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_partial_update**
> parameters_partial_update(id, name=name, type=type, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
data = swagger_client.Data5() # Data5 |  (optional)

try:
    api_instance.parameters_partial_update(id, name=name, type=type, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->parameters_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this parameter template. | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **data** | [**Data5**](Data5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_read**
> parameters_read(id, name=name, type=type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    api_instance.parameters_read(id, name=name, type=type)
except ApiException as e:
    print("Exception when calling WorkflowerApi->parameters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this parameter template. | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parameters_update**
> parameters_update(id, name=name, type=type, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
data = swagger_client.Data4() # Data4 |  (optional)

try:
    api_instance.parameters_update(id, name=name, type=type, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->parameters_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this parameter template. | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **data** | [**Data4**](Data4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_create**
> targets_create(data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
data = swagger_client.Data6() # Data6 |  (optional)

try:
    api_instance.targets_create(data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->targets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data6**](Data6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_delete**
> targets_delete(id, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)

try:
    api_instance.targets_delete(id, name=name)
except ApiException as e:
    print("Exception when calling WorkflowerApi->targets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this target template. | 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_list**
> targets_list(name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
name = 'name_example' # str |  (optional)

try:
    api_instance.targets_list(name=name)
except ApiException as e:
    print("Exception when calling WorkflowerApi->targets_list: %s\n" % e)
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

# **targets_partial_update**
> targets_partial_update(id, name=name, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)
data = swagger_client.Data8() # Data8 |  (optional)

try:
    api_instance.targets_partial_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->targets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this target template. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data8**](Data8.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_read**
> targets_read(id, name=name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)

try:
    api_instance.targets_read(id, name=name)
except ApiException as e:
    print("Exception when calling WorkflowerApi->targets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this target template. | 
 **name** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **targets_update**
> targets_update(id, name=name, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)
data = swagger_client.Data7() # Data7 |  (optional)

try:
    api_instance.targets_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->targets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this target template. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data7**](Data7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_create**
> tasks_create(data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
data = swagger_client.Data9() # Data9 |  (optional)

try:
    api_instance.tasks_create(data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->tasks_create: %s\n" % e)
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

# **tasks_delete**
> tasks_delete(id, name=name, requires=requires, outputs=outputs)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)

try:
    api_instance.tasks_delete(id, name=name, requires=requires, outputs=outputs)
except ApiException as e:
    print("Exception when calling WorkflowerApi->tasks_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task template. | 
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_list**
> tasks_list(name=name, requires=requires, outputs=outputs)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)

try:
    api_instance.tasks_list(name=name, requires=requires, outputs=outputs)
except ApiException as e:
    print("Exception when calling WorkflowerApi->tasks_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_partial_update**
> tasks_partial_update(id, name=name, requires=requires, outputs=outputs, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)
data = swagger_client.Data11() # Data11 |  (optional)

try:
    api_instance.tasks_partial_update(id, name=name, requires=requires, outputs=outputs, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->tasks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task template. | 
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 
 **data** | [**Data11**](Data11.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_read**
> tasks_read(id, name=name, requires=requires, outputs=outputs)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)

try:
    api_instance.tasks_read(id, name=name, requires=requires, outputs=outputs)
except ApiException as e:
    print("Exception when calling WorkflowerApi->tasks_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task template. | 
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tasks_update**
> tasks_update(id, name=name, requires=requires, outputs=outputs, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)
data = swagger_client.Data10() # Data10 |  (optional)

try:
    api_instance.tasks_update(id, name=name, requires=requires, outputs=outputs, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->tasks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task template. | 
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 
 **data** | [**Data10**](Data10.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.WorkflowerApi()
data = swagger_client.Data12() # Data12 |  (optional)

try:
    api_instance.workflows_create(data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data12**](Data12.md)|  | [optional] 

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
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)

try:
    api_instance.workflows_delete(id, name=name)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_delete: %s\n" % e)
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
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this workflow.

try:
    api_instance.workflows_generate(id)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_generate: %s\n" % e)
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
api_instance = swagger_client.WorkflowerApi()
name = 'name_example' # str |  (optional)

try:
    api_instance.workflows_list(name=name)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_list: %s\n" % e)
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
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)
data = swagger_client.Data14() # Data14 |  (optional)

try:
    api_instance.workflows_partial_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data14**](Data14.md)|  | [optional] 

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
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)

try:
    api_instance.workflows_read(id, name=name)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_read: %s\n" % e)
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
api_instance = swagger_client.WorkflowerApi()
id = 56 # int | A unique integer value identifying this workflow.
name = 'name_example' # str |  (optional)
data = swagger_client.Data13() # Data13 |  (optional)

try:
    api_instance.workflows_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling WorkflowerApi->workflows_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this workflow. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data13**](Data13.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

