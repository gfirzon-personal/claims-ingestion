Request to Create index in existing Azure AI Search service

Url: http://localhost:8000/importing/process
Method: POST

```json
{
    "index_name": "pharma-index",
    "index_type": "pharma",
    "container_name": "inbound-files",
    "blob_name": "generated_batch_sample.csv"
}
```