# swagger_client.CreatorApi

All URIs are relative to *http://localhost:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**results_create**](CreatorApi.md#results_create) | **POST** /api/creator/results/ | 
[**results_delete**](CreatorApi.md#results_delete) | **DELETE** /api/creator/results/{id}/ | 
[**results_list**](CreatorApi.md#results_list) | **GET** /api/creator/results/ | 
[**results_partial_update**](CreatorApi.md#results_partial_update) | **PATCH** /api/creator/results/{id}/ | 
[**results_read**](CreatorApi.md#results_read) | **GET** /api/creator/results/{id}/ | 
[**results_update**](CreatorApi.md#results_update) | **PUT** /api/creator/results/{id}/ | 


# **results_create**
> results_create(data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreatorApi()
data = swagger_client.Data() # Data |  (optional)

try:
    api_instance.results_create(data=data)
except ApiException as e:
    print("Exception when calling CreatorApi->results_create: %s\n" % e)
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

# **results_delete**
> results_delete(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreatorApi()
id = 56 # int | A unique integer value identifying this successful workflow gen.
workflow = 'workflow_example' # str |  (optional)
salted_hash = 'salted_hash_example' # str |  (optional)
successful = 'successful_example' # str |  (optional)
date_created = 'date_created_example' # str |  (optional)

try:
    api_instance.results_delete(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created)
except ApiException as e:
    print("Exception when calling CreatorApi->results_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this successful workflow gen. | 
 **workflow** | **str**|  | [optional] 
 **salted_hash** | **str**|  | [optional] 
 **successful** | **str**|  | [optional] 
 **date_created** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_list**
> results_list(workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreatorApi()
workflow = 'workflow_example' # str |  (optional)
salted_hash = 'salted_hash_example' # str |  (optional)
successful = 'successful_example' # str |  (optional)
date_created = 'date_created_example' # str |  (optional)

try:
    api_instance.results_list(workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created)
except ApiException as e:
    print("Exception when calling CreatorApi->results_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow** | **str**|  | [optional] 
 **salted_hash** | **str**|  | [optional] 
 **successful** | **str**|  | [optional] 
 **date_created** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_partial_update**
> results_partial_update(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreatorApi()
id = 56 # int | A unique integer value identifying this successful workflow gen.
workflow = 'workflow_example' # str |  (optional)
salted_hash = 'salted_hash_example' # str |  (optional)
successful = 'successful_example' # str |  (optional)
date_created = 'date_created_example' # str |  (optional)
data = swagger_client.Data2() # Data2 |  (optional)

try:
    api_instance.results_partial_update(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created, data=data)
except ApiException as e:
    print("Exception when calling CreatorApi->results_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this successful workflow gen. | 
 **workflow** | **str**|  | [optional] 
 **salted_hash** | **str**|  | [optional] 
 **successful** | **str**|  | [optional] 
 **date_created** | **str**|  | [optional] 
 **data** | [**Data2**](Data2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_read**
> results_read(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreatorApi()
id = 56 # int | A unique integer value identifying this successful workflow gen.
workflow = 'workflow_example' # str |  (optional)
salted_hash = 'salted_hash_example' # str |  (optional)
successful = 'successful_example' # str |  (optional)
date_created = 'date_created_example' # str |  (optional)

try:
    api_instance.results_read(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created)
except ApiException as e:
    print("Exception when calling CreatorApi->results_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this successful workflow gen. | 
 **workflow** | **str**|  | [optional] 
 **salted_hash** | **str**|  | [optional] 
 **successful** | **str**|  | [optional] 
 **date_created** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **results_update**
> results_update(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created, data=data)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CreatorApi()
id = 56 # int | A unique integer value identifying this successful workflow gen.
workflow = 'workflow_example' # str |  (optional)
salted_hash = 'salted_hash_example' # str |  (optional)
successful = 'successful_example' # str |  (optional)
date_created = 'date_created_example' # str |  (optional)
data = swagger_client.Data1() # Data1 |  (optional)

try:
    api_instance.results_update(id, workflow=workflow, salted_hash=salted_hash, successful=successful, date_created=date_created, data=data)
except ApiException as e:
    print("Exception when calling CreatorApi->results_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this successful workflow gen. | 
 **workflow** | **str**|  | [optional] 
 **salted_hash** | **str**|  | [optional] 
 **successful** | **str**|  | [optional] 
 **date_created** | **str**|  | [optional] 
 **data** | [**Data1**](Data1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

