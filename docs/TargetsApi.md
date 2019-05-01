# swagger_client.TargetsApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**targets_create**](TargetsApi.md#targets_create) | **POST** /api/targets/ | 
[**targets_delete**](TargetsApi.md#targets_delete) | **DELETE** /api/targets/{id}/ | 
[**targets_list**](TargetsApi.md#targets_list) | **GET** /api/targets/ | 
[**targets_partial_update**](TargetsApi.md#targets_partial_update) | **PATCH** /api/targets/{id}/ | 
[**targets_read**](TargetsApi.md#targets_read) | **GET** /api/targets/{id}/ | 
[**targets_update**](TargetsApi.md#targets_update) | **PUT** /api/targets/{id}/ | 


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
api_instance = swagger_client.TargetsApi()
data = swagger_client.Data3() # Data3 |  (optional)

try:
    api_instance.targets_create(data=data)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_create: %s\n" % e)
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
api_instance = swagger_client.TargetsApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)

try:
    api_instance.targets_delete(id, name=name)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_delete: %s\n" % e)
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
api_instance = swagger_client.TargetsApi()
name = 'name_example' # str |  (optional)

try:
    api_instance.targets_list(name=name)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_list: %s\n" % e)
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
api_instance = swagger_client.TargetsApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)
data = swagger_client.Data5() # Data5 |  (optional)

try:
    api_instance.targets_partial_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this target template. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data5**](Data5.md)|  | [optional] 

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
api_instance = swagger_client.TargetsApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)

try:
    api_instance.targets_read(id, name=name)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_read: %s\n" % e)
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
api_instance = swagger_client.TargetsApi()
id = 56 # int | A unique integer value identifying this target template.
name = 'name_example' # str |  (optional)
data = swagger_client.Data4() # Data4 |  (optional)

try:
    api_instance.targets_update(id, name=name, data=data)
except ApiException as e:
    print("Exception when calling TargetsApi->targets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this target template. | 
 **name** | **str**|  | [optional] 
 **data** | [**Data4**](Data4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

