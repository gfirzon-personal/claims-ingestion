import requests
import json
import logging
from factories.SearchClientFactory import SearchClientFactory
from services.EmbeddingsService import EmbeddingsService
from utils import config
from models.PharmaRecord import PharmaRecord

class SearchingService:
    """Service to search data in the index"""
    
    #------------------------------------------------------------------------------------------------
    def __init__(self, index_name: str):
        self.embeddings_service = EmbeddingsService()
        self.search_client = SearchClientFactory().create(index_name)

        config_dict = config.load_env_as_dict('.env')
        self.search_service_endpoint = config_dict['SEARCH_SERVICE_ENDPOINT']
        self.search_service_api_version = config_dict['SEARCH_SERVICE_API_VERSION']
        self.search_service_key = config_dict['SEARCH_SERVICE_KEY']

    #------------------------------------------------------------------------------------------------
    def search(self, query: str):
        #query_filter = f"email eq '{record['email']}' and name eq '{record['name']}'"
        query_filter = f"content eq '{query}'"
        results = self.search_client.search(search_text="", filter=query_filter)

        # Perform a full-text search on the 'content' field
        #results = search_client.search(search_text=query, search_fields=["content"])

        for result in results:
            print("Found:", result)

        return query
    
    #------------------------------------------------------------------------------------------------
    def record_search(self, record: PharmaRecord):
        """Search for a record in the index (which has been setup in ctor)"""

        #query_filter = f"PrescriptionRefNo eq 'I86K4NBSAHHF' and PatientFirstName eq ''"
        query_filter = self.build_query_filter(record)
        #print(query_filter)
        results = self.search_client.search(search_text="", filter=query_filter)

        # Perform a full-text search on the 'content' field
        #results = search_client.search(search_text=query, search_fields=["content"])

        result_count = 0
        service_results = []
        for result in results:
            #print("Found:", result)
            result_count += 1
            service_results.append(result)

        return {
            "query_filter": query_filter,
            "result_count": result_count,
            "results": service_results
        }   
    
    #------------------------------------------------------------------------------------------------
    def build_query_filter(self, record: PharmaRecord):
        query_filter = " and ".join([
            f"{field} eq '{getattr(record, field)}'" if getattr(record, field) is not None else f"{field} eq null"
            for field in record.model_fields
        ])

        return query_filter

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
                    "exhaustive": False,
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
    # https://stackoverflow.com/questions/79328696/azure-cognitive-vector-search-query-and-index-creation

    def hybrid_search(self, query_text: str):
        """Perform a hybrid search using both keyword search and vector search"""
        logging.info(f"Performing hybrid search for: {query_text}")

        # Generate a query vector using the EmbeddingsService
        # Note! The number of dimensions must match the vector field definition in Azure AI Search.
        vector_embedding = self.embeddings_service.get_embeddings(query_text).tolist()

        #logging.info(f"query_vector: {query_vector}")
        if not vector_embedding or not isinstance(vector_embedding, list):
            raise ValueError("Vector embedding is missing or not a valid list")

        # The k parameter specifies the number of nearest neighbors to return
        search_results = self.search_client.search(
            search_text=query_text, # Keyword search
            vector_queries=[{
                #"value": vector_embedding,
                "vector": vector_embedding,
                "kind": "vector",  # Required for vector queries
                #"exhaustive": False,  # If true, Return all results, sorted by similarity
                #"similarity": "cosine",  # Similarity measure to use
                "k": 5,  # Number of vector search results
                "fields": "content_vector"  # The field where the vector embeddings are stored
            }],
            select=["id", "content"],  # Fields to return
            top=10,  # Total results including both keyword and vector search
        )    

        # Display results
        # for result in search_results:
        #     print(f"ID: {result['id']}, Content: {result['content']}, Score: {result['@search.score']}")
        results_list = []
        for result in search_results:
            results_list.append({
                "ID": result['id'],
                "Content": result['content'],
                "Score": result['@search.score']
            })

        return {
            "query_text": query_text,
            "results": results_list
        }
