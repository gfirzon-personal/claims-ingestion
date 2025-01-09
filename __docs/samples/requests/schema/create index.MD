Request to Create index in existing Azure AI Search service

Url: http://localhost:8000/index-schema/
Method: POST

```json
{
    "index_name": "test-index",
    "index_type": "pharma",
    "vector_search_profile_name": "pharma-vector-config",
    "algorithm_configuration_name": "pharma-algorithms-config"
}
```