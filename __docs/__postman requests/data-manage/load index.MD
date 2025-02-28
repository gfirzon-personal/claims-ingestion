Request to load index from blob

Url: http://localhost:8000/index-data/
Method: POST

```json
{
    "index_name": "pharma-index",
    "index_type": "pharma",
    "container_name": "pharmatest",
    "blob_name": "generated_batch_sample.csv",
    "stream_mode": true
}
```