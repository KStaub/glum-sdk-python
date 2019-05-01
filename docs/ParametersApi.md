# swagger_client.ParametersApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parameters_create**](ParametersApi.md#parameters_create) | **POST** /api/parameters/ | 
[**parameters_delete**](ParametersApi.md#parameters_delete) | **DELETE** /api/parameters/{id}/ | 
[**parameters_list**](ParametersApi.md#parameters_list) | **GET** /api/parameters/ | 
[**parameters_partial_update**](ParametersApi.md#parameters_partial_update) | **PATCH** /api/parameters/{id}/ | 
[**parameters_read**](ParametersApi.md#parameters_read) | **GET** /api/parameters/{id}/ | 
[**parameters_update**](ParametersApi.md#parameters_update) | **PUT** /api/parameters/{id}/ | 


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
api_instance = swagger_client.ParametersApi()
data = swagger_client.Data() # Data |  (optional)

try:
    api_instance.parameters_create(data=data)
except ApiException as e:
    print("Exception when calling ParametersApi->parameters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Data**](Data.md)|  | [optional] 

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
api_instance = swagger_client.ParametersApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    api_instance.parameters_delete(id, name=name, type=type)
except ApiException as e:
    print("Exception when calling ParametersApi->parameters_delete: %s\n" % e)
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
api_instance = swagger_client.ParametersApi()
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    api_instance.parameters_list(name=name, type=type)
except ApiException as e:
    print("Exception when calling ParametersApi->parameters_list: %s\n" % e)
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
api_instance = swagger_client.ParametersApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
data = swagger_client.Data2() # Data2 |  (optional)

try:
    api_instance.parameters_partial_update(id, name=name, type=type, data=data)
except ApiException as e:
    print("Exception when calling ParametersApi->parameters_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this parameter template. | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **data** | [**Data2**](Data2.md)|  | [optional] 

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
api_instance = swagger_client.ParametersApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    api_instance.parameters_read(id, name=name, type=type)
except ApiException as e:
    print("Exception when calling ParametersApi->parameters_read: %s\n" % e)
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
api_instance = swagger_client.ParametersApi()
id = 56 # int | A unique integer value identifying this parameter template.
name = 'name_example' # str |  (optional)
type = 'type_example' # str |  (optional)
data = swagger_client.Data1() # Data1 |  (optional)

try:
    api_instance.parameters_update(id, name=name, type=type, data=data)
except ApiException as e:
    print("Exception when calling ParametersApi->parameters_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this parameter template. | 
 **name** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

