import requests
import json
from factories.SearchClientFactory import SearchClientFactory
from services.EmbeddingsService import EmbeddingsService
from utils import config

class SearchingService:
    def __init__(self):
        self.embeddings_service = EmbeddingsService()

        config_dict = config.load_env_as_dict('.env')
        self.search_service_endpoint = config_dict['SEARCH_SERVICE_ENDPOINT']
        self.search_service_api_version = config_dict['SEARCH_SERVICE_API_VERSION']
        self.search_service_key = config_dict['SEARCH_SERVICE_KEY']

    def search(self, index_name: str, query: str):
        search_client = SearchClientFactory().create(index_name)

        #query_filter = f"email eq '{record['email']}' and name eq '{record['name']}'"
        query_filter = f"content eq '{query}'"
        results = search_client.search(search_text="", filter=query_filter)

        # Perform a full-text search on the 'content' field
        #results = search_client.search(search_text=query, search_fields=["content"])

        for result in results:
            print("Found:", result)

        return query

    #---------------------------------------------------------------------------------------
    def search_vectorized(self, index_name: str, query: str):
        print(query)

        # Replace these with your Azure Search service details
        endpoint = f"https://{self.search_service_endpoint}.search.windows.net"
        api_key = self.search_service_key

        # Query vector and parameters
        # Generate a query vector using the EmbeddingsService
        query_vector = self.embeddings_service.get_embeddings(query).tolist()
        top_k = 5  # Number of nearest neighbors

        # URL for the Azure Search REST API
        url = f"{endpoint}/indexes/{index_name}/docs/search?api-version={self.search_service_api_version}"

        # Request payload for vector search
        payload = {
            "count": True,
            "select": "content",
            "filter": f"content eq '{query}'",
            #"filter": f"content eq 'This is the second document.'",
            "vectorFilterMode": "preFilter",
            "vectorQueries": [
                {
                    "kind": "vector",
                    "vector": query_vector,
                    "exhaustive": True,
                    "fields": "content_vector",
                    "k": top_k
                }
            ]
        }

        # HTTP headers
        headers = {
            "Content-Type": "application/json",
            "api-key": api_key
        }

        # Perform the search request
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Handle response
        if response.status_code == 200:
            service_result = []
            results = response.json()
            for result in results.get("value", []):
                print(f"Document ID: {result.get('@search.documentId')}")
                print(f"Score: {result.get('@search.score')}")
                print(f"Content: {result.get('content', 'N/A')}")
                print("-" * 40)

                service_result.append({
                    "Document ID": result.get('@search.documentId'),
                    "Score": result.get('@search.score'),
                    "content": result.get('content', 'N/A')
                })
        else:
            print(f"Error: {response.status_code} - {response.text}")

        return service_result
    
    #---------------------------------------------------------------------------------------
    def foo(self, index_name: str, query: str):
        search_client = SearchClientFactory().create(index_name)

        # Generate a query vector using the EmbeddingsService
        query_vector = self.embeddings_service.get_embeddings(query).tolist()

        # Perform vector search using the 'content_vector' field
        # The k parameter specifies the number of nearest neighbors to return
        results = search_client.search(
            search_text="",
            #vectors=[{"fieldName": "content_vector", "vector": query_vector, "k": 10}]
            vector={"fieldName": "content_vector", "value": query_vector, "k": 10}
        )    

        for result in results:
            print("Found:", result)

        return query
