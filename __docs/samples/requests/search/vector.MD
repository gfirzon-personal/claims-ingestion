Request to vector search in existing Azure AI Search service index

Url: 
https://pharma-search-service.search.windows.net/indexes/test-index/docs/search?api-version=2023-11-01

Method: POST

```json
{
    "count": true,
    "select": "content",
    "filter": "content eq 'This is the second document.'",
    "vectorFilterMode": "preFilter",
    "vectorQueries": [
        {
            "kind": "vector",
            "vector": [
                -0.009154141,
                0.018708462,
                -0.02178128,
                -0.00086512347
            ],
            "exhaustive": true,
            "fields": "content_vector",
            "k": 5
        }
    ]
}
```