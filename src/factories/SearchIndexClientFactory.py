import os
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient

class SearchIndexClientFactory:
    @staticmethod
    def create_search_index_client() -> SearchIndexClient:
        load_dotenv()
        search_service_endpoint = os.getenv("SEARCH_SERVICE_ENDPOINT")
        search_service_key = os.getenv("SEARCH_SERVICE_KEY")   

        url = f"https://{search_service_endpoint}.search.windows.net"     
        return SearchIndexClient(endpoint=url, credential=AzureKeyCredential(search_service_key))