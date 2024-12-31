GitHub Copilot: In Azure Cognitive Search, fields in an index can have different attributes that define how they can be used. Two important attributes are `filterable` and `searchable`.

### Filterable Fields
- **Definition**: Fields that can be used in filter expressions to narrow down search results.
- **Usage**: These fields can be used in `$filter` expressions in search queries.
- **Example**: If a field is filterable, you can use it to filter results like `price gt 100` or `category eq 'electronics'`.
- **Note**: Filterable fields are not tokenized, meaning the entire field value is used for filtering.

### Searchable Fields
- **Definition**: Fields that are full-text searchable.
- **Usage**: These fields are tokenized and indexed for full-text search. You can search for keywords within these fields.
- **Example**: If a field is searchable, you can search for terms within the field like `description: "wireless mouse"`.
- **Note**: Searchable fields are analyzed and tokenized, which means they are broken down into individual terms or tokens.

### Example
Consider an index with the following fields:

```json
{
  "name": "products",
  "fields": [
    { "name": "id", "type": "Edm.String", "key": true, "filterable": true, "searchable": false },
    { "name": "name", "type": "Edm.String", "filterable": true, "searchable": true },
    { "name": "description", "type": "Edm.String", "filterable": false, "searchable": true },
    { "name": "price", "type": "Edm.Double", "filterable": true, "searchable": false }
  ]
}
```

- `id`: Filterable but not searchable. You can filter by `id`, but you cannot perform full-text search on it.
- `name`: Both filterable and searchable. You can filter by `name` and also perform full-text search on it.
- `description`: Searchable but not filterable. You can perform full-text search on `description`, but you cannot filter by it.
- `price`: Filterable but not searchable. You can filter by `price`, but you cannot perform full-text search on it.

### How to Define Fields
When defining an index, you specify these attributes for each field:

```json
{
  "name": "name",
  "type": "Edm.String",
  "filterable": true,
  "searchable": true
}
```

### Conclusion
- **Filterable**: Used for filtering results based on exact matches or ranges.
- **Searchable**: Used for full-text search within the field.

Make sure to set the appropriate attributes based on how you intend to use each field in your search queries.