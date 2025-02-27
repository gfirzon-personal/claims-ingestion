## To run: 
# pipenv run python src/test_embeddings.py

from factories.SearchClientFactory import SearchClientFactory

# Function to get embedding from a document by ID
def get_embedding_by_id(search_client, document_id):
    results = search_client.get_document(key=document_id)

    embedding_field_name = "content_vector"  
    embedding = results.get(embedding_field_name) 
    return embedding

## ensure that the example usage only runs when the script is executed directly.
if __name__ == "__main__":
    # Create a search client
    index_name = "pharma-index"
    search_client = SearchClientFactory().create(index_name)

    # Example usage
    document_id = "92e7be94-a85a-4971-a685-1e4b3b0de81d"  # Replace with the needed document ID
    embedding = get_embedding_by_id(search_client, document_id)
    print(f"Embedding for document ID {document_id}: {embedding}")