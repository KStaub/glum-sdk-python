# swagger_client.TasksApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tasks_create**](TasksApi.md#tasks_create) | **POST** /api/tasks/ | 
[**tasks_delete**](TasksApi.md#tasks_delete) | **DELETE** /api/tasks/{id}/ | 
[**tasks_list**](TasksApi.md#tasks_list) | **GET** /api/tasks/ | 
[**tasks_partial_update**](TasksApi.md#tasks_partial_update) | **PATCH** /api/tasks/{id}/ | 
[**tasks_read**](TasksApi.md#tasks_read) | **GET** /api/tasks/{id}/ | 
[**tasks_update**](TasksApi.md#tasks_update) | **PUT** /api/tasks/{id}/ | 


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
api_instance = swagger_client.TasksApi()
data = swagger_client.Data6() # Data6 |  (optional)

try:
    api_instance.tasks_create(data=data)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_create: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)

try:
    api_instance.tasks_delete(id, name=name, requires=requires, outputs=outputs)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_delete: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)

try:
    api_instance.tasks_list(name=name, requires=requires, outputs=outputs)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_list: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)
data = swagger_client.Data8() # Data8 |  (optional)

try:
    api_instance.tasks_partial_update(id, name=name, requires=requires, outputs=outputs, data=data)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task template. | 
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 
 **data** | [**Data8**](Data8.md)|  | [optional] 

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
api_instance = swagger_client.TasksApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)

try:
    api_instance.tasks_read(id, name=name, requires=requires, outputs=outputs)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_read: %s\n" % e)
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
api_instance = swagger_client.TasksApi()
id = 56 # int | A unique integer value identifying this task template.
name = 'name_example' # str |  (optional)
requires = 'requires_example' # str |  (optional)
outputs = 'outputs_example' # str |  (optional)
data = swagger_client.Data7() # Data7 |  (optional)

try:
    api_instance.tasks_update(id, name=name, requires=requires, outputs=outputs, data=data)
except ApiException as e:
    print("Exception when calling TasksApi->tasks_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this task template. | 
 **name** | **str**|  | [optional] 
 **requires** | **str**|  | [optional] 
 **outputs** | **str**|  | [optional] 
 **data** | [**Data7**](Data7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

