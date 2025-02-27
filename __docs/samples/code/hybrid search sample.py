from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

# Azure AI Search Configuration
SEARCH_SERVICE_NAME = "your-search-service-name"
SEARCH_INDEX_NAME = "your-index-name"
API_KEY = "your-api-key"
ENDPOINT = f"https://{SEARCH_SERVICE_NAME}.search.windows.net"

# Initialize Search Client
search_client = SearchClient(
    endpoint=ENDPOINT,
    index_name=SEARCH_INDEX_NAME,
    credential=AzureKeyCredential(API_KEY)
)

# Hybrid Search Query
def hybrid_search(query_text, vector_embedding):
    search_results = search_client.search(
        search_text=query_text,  # Keyword search
        vector_queries=[{
            "value": vector_embedding,
            "k": 5,  # Number of vector search results
            "fields": "embedding_field"  # The field where the vector embeddings are stored
        }],
        select=["id", "title", "content", "score"],  # Fields to return
        top=10,  # Total results including both keyword and vector search
    )

    # Display results
    for result in search_results:
        print(f"ID: {result['id']}, Title: {result['title']}, Score: {result['@search.score']}")

# Example Query
query_text = "best electric car for long range"
example_embedding = [0.1, 0.2, 0.3, ..., 0.768]  # Replace with a real embedding

hybrid_search(query_text, example_embedding)


"""
How It Works
Keyword Search (search_text): Matches relevant documents based on traditional text search.
Vector Search (vector_queries): Finds semantically similar documents using embeddings.
Ranking: Azure AI Search blends both results and sorts them using a relevance score.
"""

"""
Next Steps
Generate Embeddings: Use Azure OpenAI, Hugging Face, or OpenAI API (text-embedding-ada-002) to generate vector embeddings.
Indexing: Ensure your index has a vector field with an HNSW-enabled index.
Fine-Tuning: Adjust k, scoring weights, and ranking profiles for optimal results.
"""