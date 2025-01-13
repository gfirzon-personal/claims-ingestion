Request to Create index in existing Azure AI Search service

Url: http://localhost:8000/importing/process
Method: POST

```json
{
    "index_name": "pharma-index",
    "index_type": "pharma",
    "container_name": "inbound-files",
    "blob_name": "Inbound-mix001.csv",
    "out_container_name": "result-files"
}
```