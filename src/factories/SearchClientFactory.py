import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

class SearchClientFactory:
    def __init__(self):
        pass

    def create(self, index_name: str) -> SearchClient:
        load_dotenv()
        search_service_endpoint = os.getenv("SEARCH_SERVICE_ENDPOINT")
        search_service_key = os.getenv("SEARCH_SERVICE_KEY")   

        url = f"https://{search_service_endpoint}.search.windows.net"  
        return SearchClient(endpoint=url, 
            index_name=index_name, credential=AzureKeyCredential(search_service_key))